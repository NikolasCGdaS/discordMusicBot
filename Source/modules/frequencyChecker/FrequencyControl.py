import discord
from discord.ext import commands
from .FrequencyService import FrequencyService


# Define a classe Cog de comandos básicos
class FrequencyControl(commands.Cog):

    # Instância do bot e da classe de serviço
    def __init__(self, bot):
        self.bot = bot
        self.service = FrequencyService()

    # Verifica entrada de usuário em canal
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):


        # Entrou em um canal sem estar em nenhum antes
        if before.channel is None and after.channel is not None:
            timestamp = self.service.eventRegister(
                member, 
                "ENTRADA", 
                after.channel.name, 
                "N/A"
            )
            mensagem = f"{member.name} de id {member.id} entrou em {after.channel.name} às {timestamp}."
            print(mensagem)

        # Saiu de um canal para nenhum
        elif before.channel is not None and after.channel is None:
            timestamp = self.service.eventRegister(
                member, 
                "SAIDA", 
                "N/A",
                before.channel.name
            )
            mensagem = f"{member.name} de id {member.id} saiu de {before.channel.name} às {timestamp}."
            print(mensagem)

        # Saiu e um canal para entrar em outro
        elif before.channel is not None and after.channel != before.channel:
            timestamp = self.service.eventRegister(
                member, 
                "TROCA", 
                after.channel.name, 
                before.channel.name
            )
            mensagem = f"{member.name} de id {member.id} saiu de {before.channel.name} para {after.channel.name} {timestamp}."
            print(mensagem)

    @commands.command(name='upJs')
    async def uploadJson_command(self, ctx):
        self.service.jsonConvert()
        await ctx.send(f"Log de voz salvo em {self.service.outputFile}.")


# Função de configuração para carregar o Cog
async def setup(bot):
    await bot.add_cog(FrequencyControl(bot))
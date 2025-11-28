import discord
from discord.ext import commands
import datetime

# Define a classe Cog de comandos básicos
class frequencyChecker(commands.Cog):
    # Instância do bot
    def __init__(self, bot):
        self.bot = bot

    # Verifica entrada de usuário em canal
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        #user_id = member.id
        now = datetime.datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S") # Formata como DD/MM/AAAA HH:MM:SS

        if before.channel is None and after.channel is not None:
            mensagem = f"{member.name} entrou em {after.channel.name} às {timestamp}."
            print(mensagem)
        
        if before.channel is not None and after.channel is None:
            mensagem = f"{member.name} saiu de {before.channel.name} às {timestamp}."
            print(mensagem)

        if before.channel is not None and after.channel != before.channel:
            mensagem = f"{member.name} saiu de {before.channel.name} para {after.channel.name} {timestamp}."
            print(mensagem)

# Função de configuração para carregar o Cog
async def setup(bot):
    await bot.add_cog(frequencyChecker(bot))
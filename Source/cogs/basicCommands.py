import discord
from discord.ext import commands

# Define a classe Cog de comandos básicos
class BasicCommands(commands.Cog):
    # Instância do bot
    def __init__(self, bot):
        self.bot = bot

    # Comando básico de ping: cb/ping
    @commands.command(name='ping')
    async def ping_command(self, ctx):
        await ctx.send('Pong!')

    # Comando de Teste: Responde com "Olá!" ao usar o comando cb/ola
    @commands.command(name='ola')
    async def ola_command(self, ctx):
        await ctx.send(f'Olá, {ctx.author.display_name}! Fico feliz em te ver.')

# Função de configuração para carregar o Cog
async def setup(bot):
    await bot.add_cog(BasicCommands(bot))
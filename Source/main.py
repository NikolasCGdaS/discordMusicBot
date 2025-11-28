import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

# Carrega o arquivo .env e lê o token inserido nele
load_dotenv()
botToken = os.getenv('DISCORD_TOKEN')

# Verifica a existencia da pasta cogs
if not os.path.isdir('cogs'):
    os.mkdir('cogs')

# Definição de arquivo de logs
logDeExecucao = logging.FileHandler(filename='discordBot.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Define as Cogs a serem carregadas
cogsToLoad = [
    'cogs.basicCommands'
]

# Define o prefixo do bot e seus intents
bot = commands.Bot(command_prefix='cb/', intents=intents)

async def loadCogs():
    for cogName in cogsToLoad:
        try:
            await bot.load_extension(cogName)
            print(f"Cog '{cogName}' loaded")
        except commands.ExtensionNotFound:
            print(f"Erro: Cog '{cogName}' não foi encontrado.")
        except Exception as e:
            print(f"Falha ao carregar Cog '{cogName}': {type(e).__name__}: {e}")
            logging.error(f"Falha ao carregar Cog '{cogName}': {e}")

@bot.event
async def on_ready():
    print(f'Bot {bot.user} Funcionando')
    await loadCogs()
    print('Chola bot preparado e operante!')

bot.run(botToken, log_handler=logDeExecucao, log_level=logging.DEBUG)
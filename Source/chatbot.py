import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

class CholaBot(commands.Bot):
    def __init__(self, log_handler):

        # Define as funcionalidades a serem carregadas
        self.cogsToLoad = [
            'modules.basicCommands.basicService',
            'modules.frequencyChecker.FrequencyControl',
            'modules.music.musiccontroller'
        ]

        # Carrega o arquivo .env e lê o token do bot dentro dele
        load_dotenv()
        self.botToken = os.getenv('DISCORD_TOKEN')

        # Declara os intents
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(
            command_prefix='cb/',
            intents=intents,
            log_handler=log_handler,
            log_level=logging.DEBUG
        )

    # Carrega as Cogs especificadas anteriormente
    async def setup_hook(self):
        for cogName in self.cogsToLoad:
            try:
                await self.load_extension(cogName)
                print(f"Cog '{cogName}' loaded")
            except commands.ExtensionNotFound:
                print(f"Erro: Cog '{cogName}' não foi encontrado.")
            except Exception as e:
                print(f"Falha ao carregar Cog '{cogName}': {type(e).__name__}: {e}")
                logger.error(f"Falha ao carregar Cog '{cogName}': {e}", exc_info=True)

    async def on_ready(self):
        print(f"{self.user.name} ativo e operante!")
        canal = self.get_channel(962854221244411964)
        if canal:
            await canal.send("Estou ativo")

    def iniciar(self):
        self.run(self.botToken)
        
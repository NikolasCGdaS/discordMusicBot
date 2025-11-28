import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv

class CholaBot(commands.Bot):
    def __init__(self):
        load_dotenv()
        self.botToken = os.getenv('DISCORD_TOKEN')

        logDeExecucao = logging.FileHandler(
            filename='discordBot.log', encoding='utf-8', mode='w'
        )

        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(
            command_prefix='cb/',
            intents=intents,
            log_handler=logDeExecucao,
            log_level=logging.DEBUG
        )

    async def setup_hook(self):
        # Carrega o módulo musiccontroller
        await self.load_extension("module.music.musiccontroller")
        print("Setup concluído.")

    async def on_ready(self):
        print(f"{self.user.name} ativo e operante!")
        canal = self.get_channel(962854221244411964)
        if canal:
            await canal.send("Estou ativo")

    async def on_member_join(self, member):
        await member.send(f"Bem vindo {member.name}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if "cholabot" in message.content.lower() and "ola" in message.content.lower():
            await message.channel.send(f"Ola {message.author.mention} !!!")

        await self.process_commands(message)

    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            canal = self.get_channel(962854221244411964)
            if canal:
                await canal.send(
                    f"{member.name} entrou em {after.channel}"
                )

    def iniciar(self):
        self.run(self.botToken)

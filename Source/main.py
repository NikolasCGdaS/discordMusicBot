import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
botToken = os.getenv('DISCORD_TOKEN')

logDeExecucao = logging.FileHandler(filename='discordBot.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='cb/', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} ativo e operante!")
    await bot.get_channel(962854221244411964).send("Estou ativo")

@bot.event
async def on_member_join(member):
    await member.send(f"Bem vindo {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "cholabot" in message.content.lower() and "ola" in message.content.lower():
        await message.channel.send(f"Ola {message.author.mention} !!!")

    await bot.process_commands(message)

@bot.event
async def on_voice_state_update(member, before, after):
    user_id = member.id

    if before.channel is None and after.channel is not None:
        await bot.get_channel(962854221244411964).send(f"{member.name} entrou em {after.channel}")

bot.run(botToken, log_handler=logDeExecucao, log_level=logging.DEBUG)
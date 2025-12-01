import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

class CholaBot:
    # Carrega o arquivo .env e lê o token inserido nele
    def __init__(self):
        load_dotenv()
        botToken = os.getenv('DISCORD_TOKEN')

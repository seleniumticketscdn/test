import discord
from discord.ext import commands
import os
import dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix = "?",intents = discord.Intents.all(),strip_after_prefix = True , case_insensitive= True)

bot.run(os.getenv("TOKEN"))

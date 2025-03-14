import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import glob

load_dotenv()
TOKEN = os.getenv('discord')

client = discord.Client()
bot = commands.Bot(command_prefix=';')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    for filename in glob.glob('./commands/*.py'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{os.path.basename(filename)[:-3]}')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(TOKEN)

import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

<@&1454990254703378531>.event
async def on_ready():
    print(f'Bot online como {bot.user}')

bot.run(os.getenv("TOKEN"))

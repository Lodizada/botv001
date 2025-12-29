import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

<@&1454990254703378531>.event
async def on_ready():
    print(f'Bot online como {bot.user}')

bot.run(os.getenv("MTQyNzUwMTc5MzAyMTAwNTg1NA.GdCDxF.j32Ci_UR2Lqh3xafRcUL49gmc-Y64XjiOjxW-0"))

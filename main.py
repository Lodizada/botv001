import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

<@&1418729105796628597>.event
async def on_ready():
    print(f'Bot online como {bot.user}')

<@&1418729105796628597>.command()
async def teste(ctx):
    await ctx.send("✅ Comando de teste funcionando!")

bot.run(os.getenv("TOKEN"))

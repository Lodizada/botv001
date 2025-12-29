import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot online como {bot.user}')

@bot.command()
async def teste(ctx):
    await ctx.send("✅ Comando de teste funcionando!")
    
@bot.command()
async def say(ctx, *, mensagem):
    await ctx.send(mensagem)
    
bot.run(os.getenv("TOKEN"))

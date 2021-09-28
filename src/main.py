import os
import nextcord
from nextcord.ext import commands

PREFIX = os.environ['PREFIX']
intents = nextcord.Intents.default() 
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} is online!')


@bot.command()
async def ping(ctx):
    await ctx.reply('Pong!')


bot.run(os.environ['TOKEN'])

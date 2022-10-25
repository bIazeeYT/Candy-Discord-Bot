from discord.ext import commands #pip install discord.py==2.0.1
from discord.ext.commands import CommandNotFound
import discord
import asyncio
import os

prefix = "$"  # your prefix here
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix,case_insensitive=True,strip_after_prefix=True,intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    while True:
        members = 0
        for guild in bot.guilds:
            members += guild.member_count - 1
        await bot.change_presence(status=discord.Status.idle,
	activity=discord.Activity(type=discord.ActivityType.listening,name=f"{prefix}help | {members} Members"))   
        await asyncio.sleep(5)

@bot.command()
async def command(ctx):
    await ctx.send("This Is A Simple Command")

@bot.event
async def on_message(message):
    if message.content.startswith(prefix):
        await bot.process_commands(message)



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


bot.run('your Token here')

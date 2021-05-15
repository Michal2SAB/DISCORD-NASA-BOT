# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *

@commands.command(aliases=['commands', 'command', 'help'])
async def cmds(ctx):
    embed=discord.Embed(title="Bot Commands", description="!apod - Get the Astronomy Picture of The Day\n\n!mars - Get random latest pictures of Mars, taken either by the Curiosity or the Perseverance Rover.\n\n!marsweather - Get the latest mars weather update from the Perseverance Rover.", color=0x24262B)
    embed.set_author(name="Michal2SAB", url="https://github.com/Michal2SAB")
    await ctx.send(embed=embed)

# Make the command load & work
def setup(bot):
    bot.add_command(cmds)

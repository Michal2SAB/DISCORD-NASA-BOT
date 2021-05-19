# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import *
from calculator.simple import SimpleCalculator

c = SimpleCalculator()

@commands.command(aliases=['calculate', 'calculator'])
async def calc(ctx, *, calculation):
    try:
        c.run(calculation)
        
        result = c.log[-1]
        first = result.split(".")[0]
        second = result.split(".")[1]

        if second == '0':
            result = first

        await ctx.send(result.capitalize())
    except Exception as e:
        print(e)

# Make the command load & work
def setup(bot):
    bot.add_command(calc)
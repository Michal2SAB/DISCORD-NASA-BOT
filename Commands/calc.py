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
            
        if 'result' not in result:
            result = "Math symbol not supported."

        await ctx.send(result.capitalize())
    except IndexError:
        await ctx.send("Wrong arguments passed! Use numbers and math symbols only! Example: !calc 2 + 2")
    except Exception as e:
        print(e)

# Make the command load & work
def setup(bot):
    bot.add_command(calc)

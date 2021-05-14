# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import requests
import json
import random

@commands.command(aliases=['mpic', 'marspic'])
async def mars(ctx):
    api_key = ""
    pers_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos?api_key={api_key}"
    curio_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key={api_key}"

    rovers = [pers_url, curio_url]

    useAPI = random.choice(rovers)

    whatRover = "Perseverance"

    if "curiosity" in useAPI:
        whatRover = "Curiosity"

    r = requests.get(useAPI)

    mars_dict = json.loads(r.content)
    latestDict = random.choice(mars_dict['latest_photos'])

    marsDay = latestDict['sol']
    cameraName = latestDict['camera']['full_name']
    theImg = latestDict['img_src']
    earthDate = latestDict['earth_date']

    embed=discord.Embed(title=whatRover + "'s Recent Mars Pic", url=theImg, description="A recent picture of Mars taken by the " + whatRover + " Rover.", color=0xfc0303)
    embed.set_author(name="NASA")
    embed.set_image(url=theImg)
    embed.add_field(name="Mars Day (Sol)", value=marsDay, inline=True)
    embed.add_field(name="Earth Date", value=earthDate, inline=True)

    await ctx.send(embed=embed)


# Make the command load & work
def setup(bot):
    bot.add_command(mars)

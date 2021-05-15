# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import requests
import json
import datetime
from datetime import datetime
import radar

@commands.command(aliases=['picture', 'pic', 'astropic'])
async def apod(ctx, date=''):
    if date == 'random':
        date = radar.random_datetime(start='1995-06-16', stop=datetime.today().strftime('%Y-%m-%d'))
        
    api_key = ""
    api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}&hd=True"

    r = requests.get(api_url)
    nasa_dict = json.loads(r.content)

    theDate = nasa_dict['date']
    theDesc = nasa_dict['explanation']
    theTitle = nasa_dict['title']
    hdUrl = nasa_dict['hdurl']
    copyrightn = ''
    if 'copyright' in nasa_dict:
        copyrightn = nasa_dict['copyright']

    embed=discord.Embed(title=theTitle, url=hdUrl, description=theDesc, color=0xfc0303)
    embed.set_author(name="Copyright: " + copyrightn)
    embed.set_image(url=hdUrl)
    embed.set_footer(text="Astronomy Picture of The Day | " + theDate)

    await ctx.send(embed=embed)

# Make the command load & work
def setup(bot):
    bot.add_command(apod)

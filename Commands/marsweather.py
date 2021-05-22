# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import sys,twitter
import json

# You need to create application on twitter developer portal to get these values (it's free)
c_key = ''
c_secret = ''
a_token_key = ''
a_token_secret = ''

api = twitter.Api(
    consumer_key=c_key,
    consumer_secret=c_secret,
    access_token_key=a_token_key,
    access_token_secret=a_token_secret,
    tweet_mode='extended'
)

def get_tweet(user):
	statuses = api.GetUserTimeline(screen_name=user)
	return statuses[0].full_text

@commands.command(aliases=['mweather', 'mw'])
async def marsweather(ctx):
    try:
        latest_tweet = get_tweet("marswxreport")
        parts = latest_tweet.split(",")

        if 'high' in parts:
            title = parts[0] + "," + parts[1]
            hTemp = parts[2][5:]
            lTemp = parts[3][5:]
            pressure = parts[4][9:]
            daylight = parts[5][:-24]
            daylight1 = daylight[9:].split("-")[0]
            daylight2 = daylight[9:].split("-")[1]
            imgLink = parts[5][27:]

            embed=discord.Embed(title="Latest Weather Report From The Perseverance Rover", url=imgLink, description=title)
            embed.set_author(name="MarsWxReport", url="https://twitter.com/MarsWxReport", icon_url="https://pbs.twimg.com/profile_images/2552209293/220px-Mars_atmosphere_400x400.jpg")
            embed.add_field(name="Highest Temperature", value=hTemp, inline=True)
            embed.add_field(name="Lowest Temperature", value=lTemp, inline=True)
            embed.add_field(name="Pressure", value=pressure, inline=False)
            embed.add_field(name="Daylight Time", value=daylight1 + " - " + daylight2, inline=False)
        
            await ctx.send(embed=embed)
        else:
            await ctx.send("No recent Mars weather updates")
    except Exception as e:
        print(e)

# Make the command load & work
def setup(bot):
    bot.add_command(marsweather)

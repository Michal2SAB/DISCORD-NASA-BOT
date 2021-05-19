# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import urllib.request as urllib
import json

@commands.command(aliases=['sn', 'anton', 'news'])
async def spacenews(ctx):
    try:
        apikey = "" # your api key for youtube data api v3
        chnl = "UCciQ8wFcVoIIMi-lfu8-cjQ"

        video_url = 'https://www.youtube.com/watch?v='
        search_url = 'https://www.googleapis.com/youtube/v3/search?'

        url = search_url+f'key={apikey}&channelId={chnl}&part=snippet,id&order=date&maxResults=1'
        visit = urllib.urlopen(url)
        resp = json.load(visit)
        video_link = ""

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_link = video_url + i['id']['videoId']

        await ctx.send(video_link)

    except Exception as e:
        print(e)

# Make the command load & work
def setup(bot):
    bot.add_command(spacenews)

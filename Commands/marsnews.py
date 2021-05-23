# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from splinter import Browser
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession

@commands.command(aliases=['mn', 'mnews'])
async def marsnews(ctx):
    try:
        session = AsyncHTMLSession()
        url = 'https://mars.nasa.gov/news/'

        r = await session.get(url)

        await ctx.send("Loading javascript content on NASA website, this may take a few seconds...")

        await r.html.arender()

        getNews = r.html.find('ul.item_list li.slide', first=True)
        news = getNews.text.split("\n")

        desc = news[0]
        title = news[1]
        date = news[2]
        nasaLogo = "https://github.com/Michal2SAB/DISCORD-NASA-BOT/blob/main/nlogo.png?raw=true"
        
        embed=discord.Embed(title=title, description=desc)
        embed.set_author(name="NASA", url="https://mars.nasa.gov/news/", icon_url=nasaLogo)
        embed.set_thumbnail(url=nasaLogo)
        embed.add_field(name="Date", value=date, inline=False)
        await ctx.send(embed=embed)
        await r.session.close()

    except Exception as e:
        print(e)

# Make the command load & work
def setup(bot):
    bot.add_command(marsnews)

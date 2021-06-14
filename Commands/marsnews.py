# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
from requests_html import AsyncHTMLSession

@commands.command(aliases=['mn', 'mnews'])
async def marsnews(ctx):
    try:
        # Open nasa mars news website
        session = AsyncHTMLSession()
        url = 'https://mars.nasa.gov/news/'

        r = await session.get(url)
        
        # Enable javascript so that all the content from website is loaded
        await ctx.send("Loading javascript content on NASA website, this may take a few seconds...")
        await r.html.arender()
        
        # Find our news section and get the latest post
        getNews = r.html.find('ul.item_list li.slide', first=True)
        news = getNews.text.split("\n")
        
        # Specify elements
        desc = news[0]
        title = news[1]
        date = news[2]
        link = next(iter(getNews.absolute_links))
        nasaLogo = "https://github.com/Michal2SAB/DISCORD-NASA-BOT/blob/main/nlogo.png?raw=true"
        
        # Set parameters for our embed discord message
        embed=discord.Embed(title=title, description=desc, url=link)
        embed.set_author(name="NASA", url=url, icon_url=nasaLogo)
        embed.set_thumbnail(url=nasaLogo)
        embed.add_field(name="Date", value=date, inline=False)
        
        # Send our mars news update message and close our session
        await ctx.send(embed=embed)
        await r.session.close()

    except Exception as e:
        print(e)

# Make the command load & work
def setup(bot):
    bot.add_command(marsnews)

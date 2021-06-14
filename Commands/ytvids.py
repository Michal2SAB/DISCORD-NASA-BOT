# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
import Tools.yt_handler as yt

class YTvids(commands.Cog):
    def __init__(self, bot):
        # Specify yt channel ids for different commands
        self.mars = "UChE5mIr9I1sHPHjSQeRp3FQ"
        self.space = "UCciQ8wFcVoIIMi-lfu8-cjQ"
        self.ufo = "UC4F3j3ed_To-M3H2YLLD5vw"
    
    # Get the latest mars video
    @commands.command(aliases=['mvid'])
    async def marsvid(self, ctx):
        await ctx.send(yt.getVid(self.mars))
    
    # Get the latest space news video
    @commands.command(aliases=['sn', 'anton', 'news'])
    async def spacenews(self, ctx):
        await ctx.send(yt.getVid(self.space))
    
    # Get the latest conspiracy theory video about ufo or alien
    @commands.command(aliases=['ufovid', 'ufonews'])
    async def ufo(self, ctx):
        await ctx.send(yt.getVid(self.ufo))

# Load the commands & make it work
def setup(bot):
    bot.add_cog(YTvids(bot))

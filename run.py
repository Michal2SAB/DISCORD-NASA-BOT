# Importing some necessary modules
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext import *
import os
from configparser import ConfigParser

# Extracting variables from config file
config_object = ConfigParser()
config_object.read("config.ini")
botinfo = config_object["BOT INFO"]

# Defining some important things
Client = discord.Client()
prefix = botinfo['bot_prefix']
botActivity = botinfo['bot_activity']
botText = botinfo['bot_status_text']
botStatus = botinfo['bot_status']

client = commands.Bot(command_prefix=prefix)

# Remove default 'help' command
client.remove_command('help')

# Set presence on discord & print bot info in console
@client.event
async def on_ready():
  activityKeys = {"watching": discord.ActivityType.watching, "playing": discord.ActivityType.playing,
  "listening": discord.ActivityType.listening}

  statusKeys = {"online": discord.Status.online, "offline": discord.Status.offline, 
  "away": discord.Status.idle, "afk": discord.Status.idle, "busy": discord.Status.do_not_disturb, 
  "dnd": discord.Status.do_not_disturb}
  
  # Set bot presence
  await client.change_presence(status=statusKeys[botStatus], activity=discord.Activity(type=activityKeys[botActivity], name=botText))
  
  # Print bot info (name & id)
  print(f"Name: {client.user.name}")
  print(f"ID: {client.user.id}")
  count = 1
  
  # Print all servers that the bot is located in
  for server in client.guilds:
    print(f"Server {str(count)}: {server.name} <ID: {str(server.id)}>")
    count += 1

# Handle common 'command not found' error
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, CommandNotFound):
    if str(error)[9:][:1] == botinfo['bot_prefix']:
      pass
    else:
      return await ctx.send(str(error))

# Load commands
for file in os.listdir('./Commands'):
  if file.endswith('.py'):
    client.load_extension(f'Commands.{file[:-3]}')

# Run our bot    
client.run(botinfo['bot_token'])

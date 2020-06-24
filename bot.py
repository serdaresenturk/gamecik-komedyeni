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
    elif context.message.author.id == ("339488733789290496"):
        await bot.say("Bakın! " + context.message.author.mention + " tam bir şüpheli! Polisi kim arıyor?")
    elif context.message.author.id == ("370266360850284555"):
        await bot.say("Hadi ama! " + context.message.author.mention + " kimseye zarar vermez.")
    elif context.message.author.id == ("393150554320273408"):
        await bot.say(context.message.author.mention + " ile ilgili derin söylentiler var. Kayıp kargolarla ilgili bir şuçtan aranıyor!")
    elif context.message.author.id == ("370266360850284555"):
        await bot.say("Hadi ama! " + context.message.author.mention + " kimseye zarar vermez.")
    else:
        await bot.say("Rahatla " + context.message.author.mention + " şüpheli değilsin.")
        
@bot.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick= "Test")
    await ctx.send(f'Nickname was changed for {member.mention} ')

bot.run(os.environ['BOT_TOKEN'])

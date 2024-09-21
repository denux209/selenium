import discord 
from discord.ext import commands
from datetime import datetime
import Don_Tüpütak
import locale
intents = discord.Intents.default()
intents.message_content = True
now = datetime.now()
locale.setlocale(locale.LC_ALL, '')
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def don(ctx,SEHIR,ILCE,BITKI,SAFHA=""):
    date=datetime.strftime(now,"%d %B")
    span_data=Don_Tüpütak.func(SEHIR,ILCE,BITKI,SAFHA)
    await ctx.send(span_data)
    # for j in span_data:
    #     x=j
    #     print(x)
    #     for i in x[date]:
    #         await ctx.send(i)

bot.run("MTIxMzQwMzk2ODY0Njk0MjcyMQ.G-yUPt.FKS7ue3je_8M-WhJM1VpOyWX3BpUJctZDWZDYw")
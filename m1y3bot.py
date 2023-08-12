import discord
from passchecker import *
from discord.ext import commands


# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix = '$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(cxt):
    await cxt.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def password(cxt, count_password = 8):
    await cxt.send(gen_pas(count_password))

@bot.command()

    

    


bot.run("MTEzNzMxNTEzOTE1OTMzNDk3Mg.GxM-fu.K1OgfTjo-I0MkEiQ6E3RBMLdMq8q880u6LaEyY")
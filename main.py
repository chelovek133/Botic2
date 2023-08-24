import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Наш бот {bot.user} запущен!')

@bot.command()
async def fact(ctx):
    IMG
    with open('images/IMG_2289.png', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

bot.run('MTEzNDE1MTc5Mjk4MTE5MjgzNQ.GW50Rt.kX8bUTc6Rg6XqqkYnc4tatDABRXoJAJR5l9nh0')
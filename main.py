import discord
from discord.ext import commands
import asyncio



token = ''
with open('token.txt') as f:
    token = f.read()

target_user_id = 269964731706507274

intents = discord.Intents.default()
intents.messages = True  # To listen to message content

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    
    if message.author.id == target_user_id:
        if not message.author.bot:
            await message.channel.send("who asked?")

    await bot.process_commands(message)


bot.run(token)

import discord
from discord.ext import commands, tasks
from itertools import cycle 
import os
import asyncio 
from dotenv import load_dotenv

load_dotenv()

DISCORD_API_KEY = os.environ.get("DISCORD_API_KEY")
client = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None)

bot_status = cycle(["'!help' for help", "'!help'", "Try: '!help' to get started"])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event 
async def on_ready():
    print('Bot has connected to Discord')
    change_status.start()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start(DISCORD_API_KEY)

asyncio.run(main())



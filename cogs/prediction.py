import discord 
from discord.ext import commands
import sys 
import asyncio
sys.path.insert(1, 'C:/Users/matth/NBA Discord API Bot/nba_api')
import GetPrediction

class Prediction(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print("prediction.py is ready!")

    @commands.command()
    async def predict(self, ctx):
        await ctx.send(f"Enter the season (ex: '2025' for 2024-2025 season):")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            msg = await self.client.wait_for("message", check=check, timeout=30) # 30 seconds to reply

            bot_prediction = GetPrediction.getPrediction(msg.content)
            
            if bot_prediction is None:
                await ctx.send('No teams from the past season match the model used to predict future NBA Finals winners.')
            else:
                await ctx.send(bot_prediction)
                
        except asyncio.TimeoutError:
            await ctx.send("Sorry, you didn't reply in time!")



async def setup(client):
    await client.add_cog(Prediction(client))

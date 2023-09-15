import discord 
from discord.ext import commands
import sys 
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
        bot_prediction = GetPrediction.getPrediction()
        
        if bot_prediction is None:
            await ctx.send('No teams from the past season match the model used to predict future NBA Finals winners.')
        else:
            await ctx.send(bot_prediction)


async def setup(client):
    await client.add_cog(Prediction(client))

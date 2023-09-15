import discord 
from discord.ext import commands
import asyncio # To get the exception
import sys 
sys.path.insert(1, 'C:/Users/matth/NBA Discord API Bot/nba_api')
import FindPlayerByName
import GetAdvancedStats


class FindAdvancedStats(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print("FindAdvancedStats.py is ready!")

    @commands.command()
    async def advanced(self, ctx):
        await ctx.send("Enter player's full name:")

        # This will make sure that the response will only be registered if the following
        # conditions are met:
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            msg = await self.client.wait_for("message", check=check, timeout=30) # 30 seconds to reply
            player_name = str(msg.content)
            player = FindPlayerByName.getPlayer(player_name)
            
            if player is None:
                await ctx.send("You did not enter a valid NBA player name.")
            else:
                player_stats = GetAdvancedStats.getAdvancedStats(player['id'])
                if player_stats is None:
                    await ctx.send("Advanced stats do not start until the 1996-97 season. Also, be sure to enter the player's full name")
                else:
                    await ctx.send(player_stats)

        except asyncio.TimeoutError:
            await ctx.send("Sorry, you didn't reply in time!")


async def setup(client):
    await client.add_cog(FindAdvancedStats(client))
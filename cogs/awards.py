import discord 
from discord.ext import commands
import asyncio
import sys 
sys.path.insert(1, 'C:/Users/matth/NBA Discord API Bot/nba_api')
import FindPlayerAwards
import FindPlayerByName


class Awards(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print("awards.py is ready!")

    @commands.command()
    async def awards(self, ctx):
        await ctx.send(f"Enter player's full name:")

        # This will make sure that the response will only be registered if the following
        # conditions are met:
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        
        try:
            msg = await self.client.wait_for("message", check=check, timeout=30)     # 30 seconds to reply
            player_name = str(msg.content)
            player = FindPlayerByName.getPlayer(player_name)

            if player is None:
                await ctx.send("You did not enter a valid NBA player name.")
            else:
                player_awards = FindPlayerAwards.getPlayerAwards(player['id'], False)
            
                if player_awards is None:
                    await ctx.send('No awards.')
                else:
                    await ctx.send(player_awards)                

        except asyncio.TimeoutError:
            await ctx.send("Sorry, you didn't reply in time!")


async def setup(client):
    await client.add_cog(Awards(client))

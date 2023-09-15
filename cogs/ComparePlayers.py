import discord 
from discord.ext import commands
import asyncio # To get the exception
import sys
sys.path.insert(1, 'C:/Users/matth/NBA Discord API Bot/nba_api')
import FindPlayerByName
import GetPlayerComparison


class Compare(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print("ComparePlayers.py is ready!")

    @commands.command()
    async def compare(self, ctx):
        await ctx.send("Enter the two players, separated by a comma (',')\n (Example: Stephen Curry, Magic Johnson)")

        # This will make sure that the response will only be registered if the following
        # conditions are met:
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        
        try:
            msg = await self.client.wait_for("message", check=check, timeout=30) # 30 seconds to reply
            user_input = str(msg.content)
            first_player_name = ''
            second_player_name = ''
            input_len = len(user_input)
            i = 0

            # Grab first player until ',' is reached or end of string
            while user_input[i] != ',' and i < input_len-1:
                first_player_name += user_input[i]
                i += 1
            
            # End of string reached indicates user forgot to add a comma, or only entered one player
            if i == input_len-1:
                await ctx.send("Error! You forgot to add a comma to separate the two players!")
                
            else:
                # Move pointer to start of second player
                while user_input[i] == ',' or user_input[i] == ' ' and i < input_len:
                    i += 1

                # Grab second player with remainder of input 
                while i < input_len:
                    second_player_name += user_input[i]
                    i += 1 
                    
                first_player = FindPlayerByName.getPlayer(first_player_name)
                second_player = FindPlayerByName.getPlayer(second_player_name)

                if first_player is None:
                    await ctx.send("Error! The first player you entered is invalid!")
                if second_player is None:
                    await ctx.send("Error! The second player you entered is invalid!")
                else:
                    compare_stats = GetPlayerComparison.getPlayerComparison(first_player, second_player)
                    await ctx.send(compare_stats)

        except asyncio.TimeoutError:
            await ctx.send("Sorry, you didn't reply in time!")


async def setup(client):
    await client.add_cog(Compare(client))

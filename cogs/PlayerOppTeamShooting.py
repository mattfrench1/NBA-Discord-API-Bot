import discord 
from discord.ext import commands
import asyncio # To get the exception
import sys
sys.path.insert(1, 'C:/Users/matth/NBA Discord API Bot/nba_api')
import FindPlayerByName
import FindTeamByName
import FindPlayerVsOppTeamShooting


class PlayerOppShooting(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print("PlayerOppTeamShooting.py is ready!")

    @commands.command()
    async def oppshot(self, ctx):
        await ctx.send("Enter player's full name, followed by a comma (',') and a team:")
        await ctx.send("(Example: Lebron James, Celtics)")

        # This will make sure that the response will only be registered if the following
        # conditions are met:
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        
        try:
            msg = await self.client.wait_for("message", check=check, timeout=30) # 30 seconds to reply
            user_input = str(msg.content)
            player_name = ''
            team_name = ''
            input_len = len(user_input)
            i = 0

            # Grab player name until comma is reached or end of string
            while user_input[i] != ',' and i < input_len-1:
                player_name += user_input[i]
                i += 1
            
            # End of string indicates user forgot to add a comma
            if i == input_len-1:
                await ctx.send("Error! You forgot to add a comma to separate the player and team!")

            else:
                # Move pointer to start of team name
                while user_input[i] == ',' or user_input[i] == ' ' and i < input_len:
                    i += 1

                # Grab team name with remainder of input 
                while i < input_len:
                    team_name += user_input[i]
                    i += 1 
                    
                player = FindPlayerByName.getPlayer(player_name)
                team = FindTeamByName.getTeam(team_name)
                
                if player is None:
                    await ctx.send("You did not enter a valid NBA player name.")
                elif team is None:
                    await ctx.send("You did not enter a valid NBA team name.")
                else:
                    shooting_stats = FindPlayerVsOppTeamShooting.getPlayerShootingVsOpp(player['id'], team['id'])
                    if shooting_stats is None:
                        await ctx.send("The player you entered does not currently play in the NBA. Only enter active NBA players.")
                    else:
                        await ctx.send(shooting_stats)

        except asyncio.TimeoutError:
            await ctx.send("Sorry, you didn't reply in time!")


async def setup(client):
    await client.add_cog(PlayerOppShooting(client))

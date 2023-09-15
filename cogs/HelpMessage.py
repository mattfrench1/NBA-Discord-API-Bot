import discord 
from discord.ext import commands


class HelpMessage(commands.Cog):
    def __init__(self, client):
        self.client = client 
        self.find_message = "Type in player's name to find their stats from the current NBA season, after prompted to by bot"
        self.awards_message = "Type in a player's name to get their awards, after prompted to by bot"
        self.advanced_message = "Type in a player's name to get their advanced stats for their most recent season"
        self.prediction_message = "Predicts the NBA finals favorites, and choses a winner based on the advanced team stats from the previous season."
        self.oppshooting_message = "Type in a player's name and a team's name to find out the player's recent shooting performance against said team. Percentages are the differences between league average against said team."
        self.compare_message = "Type in two NBA players to get a comparison of their awards and career stats."
        self.career_message = "Type in a player's name to get their career stats totals and per game averages."

    @commands.Cog.listener()
    async def on_ready(self):
        print("HelpMessage.py is ready!")

    @commands.command()
    async def help(self, ctx):
        embed_message = discord.Embed(title="List of Commands:", description="", color=discord.Color.dark_purple())
        embed_message.add_field(name="!find", value=self.find_message, inline=False)
        embed_message.add_field(name="!awards", value=self.awards_message, inline=False)
        embed_message.add_field(name="!advanced", value=self.advanced_message, inline=False)
        embed_message.add_field(name="!predict", value=self.prediction_message, inline=False)
        embed_message.add_field(name="!oppshot", value=self.oppshooting_message, inline=False)
        embed_message.add_field(name="!compare", value=self.compare_message, inline=False)
        embed_message.add_field(name="!career", value=self.career_message, inline=False)

        await ctx.send(embed = embed_message)


async def setup(client):
    await client.add_cog(HelpMessage(client))

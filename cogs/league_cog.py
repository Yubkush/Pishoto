import discord
from discord.ext import commands
import random

class League(commands.Cog):
    """
    League realted commands
    """
    def __init__(self, bot):
        self.bot = bot


    @commands.command(help="Send mika's 0/19 game")
    async def oops(self, ctx):
        await ctx.send(file=discord.File("oops.png"))


    @commands.command(help="Send Yasuo syndrome")
    async def nadav(self, ctx):
        await ctx.send(file=discord.File("yasuo.png"))


    @commands.command(help="Distribute roles for 5v5")
    async def minyan(self, ctx):
        voice_channel = discord.utils.get(ctx.guild.channels, name="General")
        members = [member.name for member in voice_channel.members]
        team_0 = []
        team_1 = []
        if len(members) == 10:
            for player in members:
                team_token = random.randint(0, 1)
                if (team_token == 0 and len(team_0) < 5) or len(team_1) >= 5:
                    team_0.append(player)
                elif (team_token == 1 and len(team_1) < 5) or len(team_0) >= 5:
                    team_1.append(player)

            def assign_roles(team):
                roles = {
                    "Top": "None",
                    "Jungle": "None",
                    "Mid": "None",
                    "ADC": "None",
                    "Support": "None",
                }
                for role in roles:
                    roles[role] = team.pop(team.index(random.choice(team)))
                return roles

            team_0_dict = assign_roles(team_0)
            team_1_dict = assign_roles(team_1)

            await ctx.send(f"{team_0_dict}\n{team_1_dict}")

        else:
            await ctx.send("Not the right amount of people for a 5v5")


    @commands.command(help="Returns link to champion's popular build at a given role")
    async def build(self, ctx, champ, role=""):
        await ctx.send(f"https://eune.op.gg/champion/{champ}/statistics/{role}")
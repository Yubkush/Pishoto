import random
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix=".")

# informs the bot has connected to Discord
@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord!")


# Delete default help command
client.remove_command("help")

# Embeded help with list and details of commands
@client.command()
async def help(ctx):
    embed = discord.Embed(color=discord.Colour.green())
    embed.set_author(name="Help : list of commands available")
    embed.add_field(
        name=".ping", value="Returns bot respond time in milliseconds", inline=True
    )
    embed.add_field(
        name=".minyan",
        value="Arrange teams for a 5v5, assuming everyone has a number from 1 to 10",
        inline=False,
    )
    embed.add_field(
        name=".nadav", value="The essence of Nadav", inline=False,
    )
    embed.add_field(name=".oops", value="Send an embarrassing image", inline=False)
    await ctx.send(embed=embed)


# answers with the ms latency
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


# Send mika's 0/19 game
@client.command()
async def oops(ctx):
    await ctx.send(file=discord.File("oops.png"))


# Send Yasuo syndrome
@client.command()
async def nadav(ctx):
    await ctx.send(file=discord.File("yasuo.png"))


# Distribute roles for 5v5
@client.command()
async def minyan(ctx):
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


@client.command()
async def build(ctx, champ, role=""):
    await ctx.send(f"https://eune.op.gg/champion/{champ}/statistics/{role}")


# alert the user of a command syntax error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error! Try .help ({error})")


client.run(TOKEN)

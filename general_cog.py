import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # informs the bot has connected to Discord
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user.name} has connected to Discord!")
        # Delete default help command
        self.bot.remove_command("help")

    # Embeded help with list and details of commands
    # @commands.command()
    # async def help(ctx):
    #     embed = discord.Embed(color=discord.Colour.green())
    #     embed.set_author(name="Help : list of commands available")
    #     embed.add_field(
    #         name=".ping", value="Returns bot respond time in milliseconds", inline=True
    #     )
    #     embed.add_field(
    #         name=".minyan",
    #         value="Arrange teams for a 5v5, assuming everyone has a number from 1 to 10",
    #         inline=False,
    #     )
    #     embed.add_field(
    #         name=".nadav", value="The essence of Nadav", inline=False,
    #     )
    #     embed.add_field(name=".oops", value="Send an embarrassing image", inline=False)
    #     await ctx.send(embed=embed)


    # answers with the ms latency
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")


    # alert the user of a command syntax error
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(f"Error! Try .help ({error})")
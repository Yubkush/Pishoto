import discord
import os

import league_cog
import general_cog

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents=discord.Intents.default()

bot = commands.Bot(command_prefix=commands.when_mentioned_or("."),
                    description="Private Discord Bot for LOLBros Server",
                    intents=intents)

bot.remove_command('help')
bot.add_cog(league_cog.League(bot))
bot.add_cog(general_cog.General(bot))
bot.run(TOKEN)

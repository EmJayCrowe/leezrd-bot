import discord
from discord.ext import commands

import slashCommands

from config import TOKEN

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="l!")

bot.run(TOKEN)
exec("slashCommands.py")
import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='>')

if __name__ == "__main__":
  # Same as obtaining 'cd ../.bot_token' path
  token_file_path = open(os.path.join(os.path.split(os.path.dirname(__file__))[0], '.bot_token')).name
  token = open(token_file_path, "r").read()
  bot.run(token)

import discord
from discord.ext import commands

import os

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
  print('{0.user} is online'.format(bot))

@bot.event
async def on_message(message):
  # Ignore bot messages including self
  user_message = message.author
  if user_message == bot.user or user_message.bot == True:
    return
  print(user_message.name + '#' + user_message.discriminator + ": " + message.content)


if __name__ == "__main__":
  # Same as obtaining 'cd ../.bot_token' path
  token_file_path = open(os.path.join(os.path.split(os.path.dirname(__file__))[0], '.bot_token')).name
  token = open(token_file_path, "r").read()
  bot.run(token)

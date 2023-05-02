import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
 # Add this line


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')

@bot.command(name='ping')
async def _ping(ctx):
    await ctx.send('Pong!')

def load_modules():
    for filename in os.listdir('./modules'):
        if filename.endswith('.py'):
            print(f'Loading module: {filename[:-3]}')  # Add this line to print the module name
            bot.load_extension(f'modules.{filename[:-3]}')


if __name__ == '__main__':
    load_modules()
    bot.run(TOKEN)

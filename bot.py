import os, random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command(name='help')
async def nine_nine(ctx):
    response = (
        'WaitressBot can bring you a cold one, just ask for it.\n'
        'Created by Henrick'
    )
    await ctx.send(response)

bot.run(TOKEN)
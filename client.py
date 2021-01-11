# bot.py
import os, discord, random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(
        f'{client.user.name} is connected to the following guild:'
    )
    for guild in client.guilds:
        print(
            f'{guild.name}(id: {guild.id})\n'
        )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {guild.name}!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    reply_list = {
        'beer': {
            'receive': ('beer', 'cerveja', 'uma gelada'),
            'send': (
                'Here it is.',
                (
                    'Here it is.\n'
                    'Anything else?'
                ),
                'Have you asked for a beer? I will get it for you.\n',
                (
                    'Have you asked for a beer? I will get it for you.\n'
                    'Here it is.'
                ),
                'Your beer...',
                (
                    'Your beer...\n'
                    'Anything else?'
                ),
                (
                    'I heard you wanted beer.\n'
                    'Brought you some.'
                ),
                (
                    'I heard you wanted beer.\n'
                    'Brought you some, on the house.'
                ),
            )
        }
    }

    if any(reply in message.content for reply in reply_list['beer']['receive']):
        response = random.choice(reply_list['beer']['send'])
        await message.channel.send(response)

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)
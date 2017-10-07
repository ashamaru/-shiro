import discord
import asyncio

client = discord.Client()
bot_name = '•shiro'
help_text = 'To use ' + bot_name + ', type < followed by a command.\n'  \
            'Available commands are:\n'                                 \
            '\t- test: no clue\n'                                       \
            '\t- sleep: sleeps for 5 seconds\n'                         \
            '\t- help: prints out this help\n'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('<test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('<sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('<help'):
        await client.send_message(message.channel, help_text)

# replace with the token for your discord app/ dc bot
client.run('token')
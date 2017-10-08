import discord
import asyncio
from xml.etree import ElementTree
from random import randint

client = discord.Client()
bot_name = '• kurisu •'
help_text = 'To use ' + bot_name + ', type - followed by a command.\n'  \
            'Available commands are:\n'                                 \
            '\t- test: no clue\n'                                       \
            '\t- sleep: sleeps for 5 seconds\n'                         \
            '\t- help: prints out this help\n'                          \
            '\nor type @kurisu followed by a message.\n'                \
            'Available messages are:\n'                                 \
            '\t- smile\n'                                               \

dir_root = '/Users/tak7tsuki/PycharmProjects/shiro'
path_to_db = dir_root + '/kurisu/db.xml'


# db.xml database wrapper

class KurisuDatabaseWrapper:
    path_to_xml_db = None

    def __init__(self, path_to_xml_db):
        if path_to_xml_db is None:
            raise Exception
        # *
        # todo validate path
        # *
        self.path_to_xml_db = path_to_xml_db

    def get_random_reply(self, mood):
        tree = ElementTree.parse(self.path_to_xml_db)
        root = tree.getroot()
        for categorie in list(root):
            if mood == categorie.tag:
                noe = int(categorie.get('count'))
                specific = randint(0, noe-1)
                return list(categorie)[specific].text
        return None

db_wrapper = KurisuDatabaseWrapper(path_to_db)


# Future message pipeline

def eval_mood(message):
    if randint(0 ,1) == 0:
        return 'angry'
    return 'bored'


# common discord api

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('-test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('-sleep'):
        await client.send_message(message.channel, 'Zzzz...')
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Huh?! I... I did not sleep because you wanted me to do so! '
                                                   'In fact I was just tired. Yeah tired, '
                                                   'because you bore ma that much! Baka...')
    elif message.content.startswith('-help'):
        await client.send_message(message.channel, help_text)

    elif message.content.lower().startswith('@kurisu'):
        index = message.content.find('@')
        command = message.content[index + 7:].strip()

        if command == 'smile':
            await client.send_message(message.channel, '\*smiles\*')
        else:
            await client.send_message(message.channel, '\*sight\* what?')

    # reacts to kuriso in msg
    elif 'kurisu' in message.content:
        mood = eval_mood(message.content)
        reply = db_wrapper.get_random_reply(mood)
        await client.send_message(message.channel, reply)


# replace with the token for your discord app/ dc bot
client.run('MzY2NTkyNTAyMTYzMzA4NTQ2.DLvz0g.o7z41XU91zfO5oD7JGUvnhnRjFI')
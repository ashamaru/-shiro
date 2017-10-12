import asyncio
import os
import sys
from random import randint

import discord

# Init the python path - will be changed later
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
print(SCRIPT_DIR)
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
print(sys.path)

from kurisudb.kurisudb import DBHandel

dir_root = '/Users/tak7tsuki/PycharmProjects/shiro'
path_to_db = dir_root + '/kurisu/kurisudb.xml'


class KurisuDatabaseWrapper:
    path_to_xml_db = None
    # kurisudb.xml database wrapper
    db_handel = DBHandel()

    def __init__(self, path_to_xml_db):
        if path_to_xml_db is None:
            raise Exception
        self.path_to_xml_db = path_to_xml_db

    def get_random_reply(self, mood):
        noe = self.db_handel.getlength(mood)
        specific = randint(0, noe - 1)
        return self.db_handel.selectReply(mood, specific)

db_wrapper = KurisuDatabaseWrapper(path_to_db)


# Future message pipeline

def prime_coroutines():
    eval_mood_coro().__next__()


def msg_pipeline_source(msg):
    eval_mood_coro().send(msg)


def eval_mood(message):
    if randint(0 ,1) == 0:
        return 'angry'
    return 'bored'


def eval_mood_coro():
    print("Init coroutine eval_mood")
    while True:
        msg = (yield)
        #
        # todo: code to evaluate the mood
        #
        return eval_mood(msg)
    return None

# common discord api

client = discord.Client()
bot_name = '• kurisu •'
help_text = 'To use ' + bot_name + ', type - followed by a command.\n'  \
            'Available commands are:\n'                                 \
            '\t- test: no clue\n'                                       \
            '\t- sleep: sleeps for 5 seconds\n'                         \
            '\t- help: prints out this help\n'                          \
            '\nor type @kurisu followed by a message.\n'                \
            'Available messages are:\n'                                 \
            '\t- smile\n'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    # -test
    if message.content.startswith('-test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    # -sleep
    elif message.content.startswith('-sleep'):
        await client.send_message(message.channel, 'Zzzz...')
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Huh?! I... I did not sleep because you wanted me to do so! '
                                                   'In fact I was just tired. Yeah tired, '
                                                   'because you bore ma that much! Baka...')    # <- weird...

    # -help
    elif message.content.startswith('-help'):
        await client.send_message(message.channel, help_text)

    # @kurisu
    elif message.content.lower().startswith('@kurisu'):
        index = message.content.find('@')
        command = message.content[index + 7:].strip()

        if command == 'smile':
            await client.send_message(message.channel, '\*smiles\*')
        else:
            await client.send_message(message.channel, '\*sight\* what?')

    # kurisu reaction - todo: remove
    elif '#kurisu' in message.content:
        mood = eval_mood(message.content)
        reply = db_wrapper.get_random_reply(mood)
        if reply is not None:
            await client.send_message(message.channel, reply)
        else:
            await client.send_message(message.channel, 'bugs...')

# init the msg pipeline
prime_coroutines()

# replace with the token for your discord app/ dc bot
client.run('MzY2NTkyNTAyMTYzMzA4NTQ2.DLvz0g.o7z41XU91zfO5oD7JGUvnhnRjFI')
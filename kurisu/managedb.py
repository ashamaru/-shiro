# Script to modify the database in use
# Available commands
# - addcategory
# - rmcategory
# - registercategory


import sys
from kurisu.kurisudb import DBHandel
from kurisu import settings

# name containing a reference for available subcommands
DB_COMMANDS = [
    'addcategory',
    'rmcategory',
    'registercategory'
]

class BaseCommand(object):
    args = None
    db_handle = None

    def __init__(self, args):
        """
            Initializes the Object

        """
        self.args = args

    def parse_commandline_options(self, argv):
        """
            Expects The part of the sys.argv after the subcommand
            Needs to be overriden in subclasses

        """

    def execute(self):
        """
        Attempts to execute the command.

        """
class AddCategoryCommand(BaseCommand):

    def parse_commandline_options(self, argv):
        return None

    def execute(self):
        return None


def create_command_handler(subcommand, args):
    if subcommand == 'addcategory':
        return AddCategoryCommand(args)
    return None

def parse_commandline_options(argv):
    subcommand = argv[1]
    print('subcommand: ' + subcommand)
    if subcommand in DB_COMMANDS:
        return create_command_handler(subcommand, argv[2:])
    return None


if __name__ == '__main__':
    command = parse_commandline_options(sys.argv)
    exit_satus = command.execute()
    exit(exit_satus)

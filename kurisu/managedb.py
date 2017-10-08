# script to modify db.xml
# available commands
# - add_catg
# - rm_catg
# - register_domain
# - insert_domain
# - delete_domain
# - drop_domain

import sys

# A setting name determining the underlying storage stategy
STORAGE_DB = 'db.xml'

class BaseCommand(object):
    args = None

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



def parse_commandline_options(argv):
    subcommand = argv[1]
    print('subcommand: ' + subcommand)
    args = argv[2:]
    command = BaseCommand(args)
    return None;

if __name__ == '__main__':
    parse_commandline_options(sys.argv)


# module for supported commands of managedb

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#   NOTE:
#   This modul is currently unsupported and needs to be revoked
#
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# name containing a reference for available subcommands
DB_COMMANDS = [
    'adddomain',
    'rmdomain',
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
        Needs to be overridden in subclasses

        """
        pass

    def execute(self):
        """
        Attempts to execute the command.

        """
        pass


class AddCategoryCommand(BaseCommand):

    def parse_commandline_options(self, argv):
        raise Exception

    def execute(self):
        raise Exception


def create_command_handler(subcommand, args):
    """
    Creates the coresponding instance for the specified subcommand
    :param subcommand: subcommand
    :param args: the args after the subcommand
    :return: the subcommand or none
    """
    if subcommand == 'adddomain':
        return AddCategoryCommand(args)
    return None


def parse_commandline_options(argv):
    """
    parses the argv to retrieve the subcommand and pass the rest to the handler
    :param argv: the sys.argv after the commandname
    :return: command instance with execute function or none
    """
    subcommand = argv[1]
    print('subcommand: ' + subcommand)
    if subcommand in DB_COMMANDS:
        return create_command_handler(subcommand, argv[2:])
    return None
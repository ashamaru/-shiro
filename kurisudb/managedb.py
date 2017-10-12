# Script to modify the database in use

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
#   NOTE:
#   This script is currently unsupported and needs to be revoked
#
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

import sys

from kurisudb import mdbcommands

if __name__ == '__main__':
    command = mdbcommands.parse_commandline_options(sys.argv)
    exit_satus = command.execute()
    exit(exit_satus)

"""
simple-password

Usage:
  simple-password login
  simple-password logout
  simple-password ls
  simple-password new
  simple-password update <id>
  simple-password unlock <id>
  simple-password delete <id>
  simple-password change
  simple-password -h | --help
  simple-password --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  simple-password ls

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/erjantj/simple-password-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import simple_password.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items(): 
        if hasattr(simple_password.commands, k) and v:
            module = getattr(simple_password.commands, k)
            simple_password.commands = getmembers(module, isclass)
            command = [command[1] for command in simple_password.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()

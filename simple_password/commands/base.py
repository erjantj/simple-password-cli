"""The base command."""

import getpass

class Base(object):
    """A base command."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')

    def require(self, label):
        field = ''
        while not field:
            field = input(label+': ').strip()
            if not field:
                print('The {label} field is required'.format(label=label))

        return field

    def requirePassword(self, label):
        field = ''
        while not field:
            field = getpass.getpass(label+': ')
            if not field:
                print('The {label} field is required'.format(label=label))

        return field
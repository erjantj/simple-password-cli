"""The login command."""

from json import dumps
from .base import Base
from . import user_service
import getpass
import sys

class Login(Base):
    """Login to system"""

    def run(self):
        print('Login to Simple Password')
        username = input('Username: ')
        password = getpass.getpass('Password: ')

        if user_service.login(username, password):
            print('Success!')
        else:
            print('Problem occurred while login')
            sys.exit(1)

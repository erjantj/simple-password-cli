"""New password command."""

from .base import Base
from . import password_service
import getpass
import sys

class New(Base):
    """New password"""

    def run(self):
        name = self.require('Name')
        account_name = self.require('Account name')
        password = self.requirePassword('Password')
        master_password = self.requirePassword('Master password')

        password_record = password_service.create(name, account_name, password, master_password)

        print('Created new password', '{name}({account_name}):'.format(name=password_record['name'], account_name=password_record['account_name']))
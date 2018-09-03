"""New password command."""

from .base import Base
from . import password_service
from .api import authorized
import getpass

class New(Base):
    """New password"""

    @authorized
    def run(self):
        name = input('Name: ').strip()
        account_name = input('Account name: ').strip()
        password = getpass.getpass('Password: ')
        password_record = password_service.create(name, account_name, password)
        print('Created new password', '{name}({account_name}):'.format(name=password_record['name'], account_name=password_record['account_name']))
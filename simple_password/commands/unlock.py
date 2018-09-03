"""Unlock passwords command."""

from .base import Base
from . import password_service
from .api import authorized
import getpass

class Unlock(Base):
    """Unlock passwords"""

    @authorized
    def run(self):
        password = password_service.get(self.options['<id>'])
        print('Unlocking', '{name}({account_name}):'.format(name=password['name'], account_name=password['account_name']))
        master_password = getpass.getpass('Master password: ')
        password = password_service.unlock(self.options['<id>'], master_password)
        print('Password:',password)

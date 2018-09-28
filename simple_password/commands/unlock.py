"""Unlock passwords command."""

from .base import Base
from . import password_service
import getpass

class Unlock(Base):
    """Unlock passwords"""

    def run(self):
        id = self.options['<id>']
        password = password_service.get(id)
        print('Unlocking', '{name}({account_name}):'.format(name=password['name'], account_name=password['account_name']))
        master_password = self.requirePassword('Master password')
        password = password_service.unlock(id, master_password)
        print('Password:',password)

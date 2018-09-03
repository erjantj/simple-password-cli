"""Delete passwords command."""

from .base import Base
from . import password_service
from .api import authorized
import getpass

class Delete(Base):
    """Delete passwords"""

    @authorized
    def run(self):
        password_record = password_service.get(self.options['<id>'])
        answer = input('Do you want to delete {name}({account_name})? (y/n): '.format(name=password_record['name'], account_name=password_record['account_name']))
        if answer == 'y':
            master_password = getpass.getpass('Master password: ')
            password_service.delete(self.options['<id>'], master_password)
            print('Password deleted!')

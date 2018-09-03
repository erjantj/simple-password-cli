"""Update passwords command."""

from .base import Base
from . import password_service
from .api import authorized
import getpass

class Update(Base):
    """Update passwords"""

    @authorized
    def run(self):
        password_record = password_service.get(self.options['<id>'])
        print('Updating', '{name}({account_name}):'.format(name=password_record['name'], account_name=password_record['account_name']))
        name = input('Name ({name}): '.format(name=password_record['name'])) or password_record['name']
        account_name = input('Account name ({account_name}): '.format(account_name=password_record['account_name'])) or password_record['account_name']
        password = getpass.getpass('New Password: ')
        
        master_password = getpass.getpass('Master password: ')
        password_record = password_service.update(self.options['<id>'], name, account_name, password, master_password)
        print('Success!')

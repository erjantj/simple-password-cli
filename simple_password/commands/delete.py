"""Delete passwords command."""

from .base import Base
from . import password_service

class Delete(Base):
    """Delete passwords"""

    def run(self):
        id = self.options['<id>']
        password_record = password_service.get(id)
        answer = input('Do you want to delete {name}({account_name})? (y/n): '.format(name=password_record['name'], account_name=password_record['account_name']))
        if answer == 'y':
            master_password = self.requirePassword('Master password')
            password_service.delete(id, master_password)
            print('Password deleted!')

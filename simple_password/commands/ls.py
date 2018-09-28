"""List passwords command."""

from .base import Base
from . import password_service

class Ls(Base):
    """List passwords"""

    def run(self):
        passwords_data = password_service.all()
        if not passwords_data['passwords']:
            print('You have no stored passwords. Go on and create one.')
        else:
            for i in range(len(passwords_data['passwords'])):
                password = passwords_data['passwords'][i]
                print('{id}\t{name}({account_name})'.format(
                    id=(i+1), 
                    name=password['name'],
                    account_name=password['account_name']
                ))
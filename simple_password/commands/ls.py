"""List passwords command."""

from .base import Base
from . import password_service
from .api import authorized

class Ls(Base):
    """List passwords"""

    @authorized
    def run(self):
        passwords = password_service.all()
        for password in passwords:
            print('{id}\t{name}({account_name})'.format(
                id=password['id'], 
                name=password['name'],
                account_name=password['account_name']
            ))
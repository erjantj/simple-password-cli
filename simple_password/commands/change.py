"""Change master password command."""

from .base import Base
from . import password_service
from .api import authorized
import getpass

class Change(Base):
    """Change master password"""

    @authorized
    def run(self):
        print('Updating master password:')
        old_password = getpass.getpass('Old Password: ')
        new_password = getpass.getpass('New Password: ')
        new_password_confirmation = getpass.getpass('New password confirmation: ')
        
        password_service.change(old_password, new_password, new_password_confirmation)
        print('Success!')

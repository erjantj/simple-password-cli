"""Change master password command."""

from .base import Base
from . import password_service

class Change(Base):
    """Change master password"""

    def run(self):
        print('Updating master password:')
        old_password = self.requirePassword('Old password')
        new_password = self.requirePassword('New password')
        
        password_service.change(old_password, new_password)
        print('Success!')

"""The logout command."""

from json import dumps
from .base import Base
from . import user_service
import getpass
import sys

class Logout(Base):
    """Logout to system"""

    def run(self):
        user_service.logout()
        print('Logged out')
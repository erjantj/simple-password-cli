"""Tests for our main simple password CLI module."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase

from simple_password import __version__ as VERSION


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['simple-password', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['simple-password', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['simple-password', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), VERSION)

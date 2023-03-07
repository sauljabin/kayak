from unittest import TestCase

from kayak import __version__


class TestKayak(TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.2.1")

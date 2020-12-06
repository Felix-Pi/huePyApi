from unittest import TestCase

from Hue import *


class TestHue(TestCase):
    def setUp(self):
        self.hue = Hue(ip=ip, api_key=api_key)


from unittest import TestCase
from Alert import *


class TestAlert(TestCase):
    def test_enum(self):
        print(Alert.LSELECT.value)

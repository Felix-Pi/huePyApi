from unittest import TestCase
from huePyApi.enums.Alert import *


class TestAlert(TestCase):
    def test_enum(self):
        print(Alert.LSELECT.value)

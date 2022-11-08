import unittest
from unittest.mock import patch
from service_module import inp_string


class TestClass_1_Functions(unittest.TestCase):
    @patch('builtins.input', return_value='()')
    def test_inp_string(self, mock_input):
        result = inp_string()
        self.assertEqual('()', result)

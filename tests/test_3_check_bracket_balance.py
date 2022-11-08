import unittest
from parameterized import parameterized
from service_module import check_bracket_balance

FIXTURES = [
    ('[([])((([[[]]])))]{()}',
     'Скобки сбалансированы'),
    ('(())(',
     'Скобки не сбалансированы')
]


class TestClass_3_Functions(unittest.TestCase):
    @parameterized.expand(FIXTURES)
    def test_check_bracket_balance(self, bracket_string, expected_result):
        result = check_bracket_balance(bracket_string)
        self.assertEqual(result, expected_result)

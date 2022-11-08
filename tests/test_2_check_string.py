import unittest
from parameterized import parameterized
from service_module import check_string

FIXTURES = [
    ('((f))',
     'Строка содержит одну или более скобок'),
    ('123456789',
     'Строка не содержит скобок')
]


class TestClass_2_Functions(unittest.TestCase):
    @parameterized.expand(FIXTURES)
    def test_check_string(self, bracket_string, expected_result):
        result = check_string(bracket_string)
        self.assertEqual(result, expected_result)

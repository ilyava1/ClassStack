from test_1_inp_string import TestClass_1_Functions
from test_2_check_string import TestClass_2_Functions
from test_3_check_bracket_balance import TestClass_3_Functions

import unittest
from unittest import TestSuite


def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in (TestClass_1_Functions, TestClass_2_Functions,
                       TestClass_3_Functions):
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite


unittest.main(verbosity=2)

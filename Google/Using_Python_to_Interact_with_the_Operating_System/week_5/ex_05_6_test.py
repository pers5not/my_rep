import unittest
from ex_05_6 import validate_user_name


class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user_name('validuser', 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user_name('inv', 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user_name('invalid_user', 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user_name, 'user', 0)


unittest.main()

#!/usr/bin/env python3

from ex_05_1 import rerange_name
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = 'Lovelace, Ada'
        expected = 'Ada Lovelace'
        self.assertEqual(rerange_name(testcase), expected)

    def test_empty(self):
        testcase = ''
        expected = ''
        self.assertEqual(rerange_name(testcase), expected)

    def test_double_name(self):
        testcase = 'Hopper, Grace M.'
        expected = 'Grace M. Hopper'
        self.assertEqual(rerange_name(testcase), expected)

    def test_one_name(self):
        testcase = 'Volteir'
        expected = 'Volteir'
        self.assertEqual(rerange_name(testcase), expected)


unittest.main()

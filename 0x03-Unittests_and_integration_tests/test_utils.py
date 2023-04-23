#!/usr/bin/env python3
"""
Implement the TestAccessNestedMap.test_access_nested_map method to test
that the method returns what it is supposed to.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """
    write the unit test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(
        self, nested_map: Mapping,
        path: Sequence,
        expected: Any
    ):
        """
        Test access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b')),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence
    ):
        """
        Test access_nested_map exception
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(e.exception, KeyError(path[-1]))


if __name__ == "__main__":
    unittest.main()

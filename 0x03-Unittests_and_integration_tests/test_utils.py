#!/usr/bin/env python3
"""
Implement the TestAccessNestedMap.test_access_nested_map method to test
that the method returns what it is supposed to.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """
    Test the get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(
        self,
        test_url: str,
        test_payload: Mapping,
        mock_get: Mock
    ):
        """
        Test the get_json method
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test the memoize function
    """
    def test_memoize(self):
        """
        Test that when calling a_property twice, the correct result
        is returned but a_method is only called once using
        assert_called_once
        """
        class TestClass:
            """ Test Class """
            def a_method(self):
                """ a method """
                return 42
            
            @memoize
            def a_property(self):
                """ a property """
                return self.a_method()
        
        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()

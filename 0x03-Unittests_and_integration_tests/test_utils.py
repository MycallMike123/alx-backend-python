#!/usr/bin/env python3

"""Unittests for utils.py to ensure that the 
access_nested_map function works as expected
"""

import unittest
from unittest import mock
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class to test the access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access of nested_map
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, 'a'),
        ({"a": 1}, ("a", "b"), KeyError, 'b')
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, expected_message, expected_key):
        with self.assertRaises(expected_message):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Class to test the get_json function
    """
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json function returns the expected result
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Class to test the memoize function"""
    def test_memoize(self):
        """To mock a_method and test the memoize property"""
        # Define a test class with a method and a memoized property
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Patch the a_method of TestClass
        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42

            test_instance = TestClass()
            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert that a_method is only called once
            mock_method.assert_called_once()
            # Assert that the result is correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

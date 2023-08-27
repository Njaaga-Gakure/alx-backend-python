#!/usr/bin/env python3
"""Test functions module."""


from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict


class TestAccessNestedMap(unittest.TestCase):
    """A class to test the access_nested_map function."""

    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2]
    ])
    def test_access_nested_map(self, a: Mapping,
                               b: Sequence,
                               expected_result: Any):
        """Check if a function returns the expected results."""
        self.assertEqual(access_nested_map(a, b), expected_result)

    @parameterized.expand([
        [{}, ("a",), KeyError('a')],
        [{"a": 1}, ("a", "b"), KeyError('b')]
    ])
    def test_access_nested_map_exception(self,
                                         a: Mapping,
                                         b: Sequence,
                                         expected_result: Any):
        """Check if function raises the correct exeptions."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(a, b)
            self.assertEqual(str(context.exception), str(expected_result))


class TestGetJson(unittest.TestCase):
    """A class that tests the get_json function."""

    @parameterized.expand([
        ["http://example.com", {"payload": True}, {"payload": True}],
        ["http://holberton.io", {"payload": False}, {"payload": False}]
    ])
    @patch('requests.get')
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict[str, bool],
                      expected_output: Dict[str, bool],
                      mock_get: Mock):
        """Test that the get_json function return the expected output."""
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        mock_get.return_value = mock_resp
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, expected_output)


class TestMemoize(unittest.TestCase):
    """A class that tests the memoize function."""

    def test_memoize(self):
        """Test the memoize function."""

        class TestClass:
            """A test class."""

            def a_method(self):
                """Return an int."""
                return 42

            @memoize
            def a_property(self):
                """Call a method inside a class."""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as m:
            test_obj = TestClass()
            test_obj.a_property
            test_obj.a_property
            m.assert_called_once()

#!/usr/bin/env python3
"""Test access_nested_map function."""


from utils import access_nested_map
from unittest import TestCase
from parameterized import parameterized
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(TestCase):
    """A class to test the method access_nested_map."""

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

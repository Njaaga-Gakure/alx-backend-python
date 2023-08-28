#!/usr/bin/env python3
"""Test GithubOrgClient class."""


from client import GithubOrgClient
import unittest
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """A class that test the GithubOrgClient class."""

    @parameterized.expand([
        ["google"],
        ["abc"]
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock):
        """Test the org method of the GithubOrgClient class."""
        org_client = GithubOrgClient(org_name)
        org_client.org()
        org_client.org()
        mock.assert_called_once_with(org_client.ORG_URL.format(org=org_name))

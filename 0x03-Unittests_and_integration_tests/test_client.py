#!/usr/bin/env python3
"""Test GithubOrgClient class."""


from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        with patch.object(GithubOrgClient,
                          'org',
                          new_callable=PropertyMock) as mock:
            mock.return_value = {
                     "login": "google",
                     "id": 1342004,
                     "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
                     "url": "https://api.github.com/orgs/google",
                     "repos_url": "https://api.github.com/orgs/google/repos"
                    }
            client_org = GithubOrgClient('google')
            expected_repos_url = "https://api.github.com/orgs/google/repos"
            self.assertEqual(client_org._public_repos_url, expected_repos_url)

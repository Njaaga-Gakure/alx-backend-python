#!/usr/bin/env python3
"""Test GithubOrgClient class."""


from typing import Dict
from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock, MagicMock
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock):
        """Test public_repos method of the GithubOrgClient class."""
        mock_get_json.return_value = [
                                      {"name": "alx-backend-js"},
                                      {"name": "alx-backend-py"}
                                     ]
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = "https://api.github.com/orgs/alx"
            client_org = GithubOrgClient('alx')
            self.assertEqual(client_org.public_repos(),
                             ['alx-backend-js', 'alx-backend-py'])
            mock_get_json.assert_called_once()
            mock_repos_url.assert_called_once()

    @parameterized.expand([
        [{"license": {"key": "my_license"}}, "my_license", True],
        [{"license": {"key": "other_license"}}, "my_license", False],
    ])
    def test_has_license(self,
                         repo: Dict,
                         license: str,
                         expected_result: bool):
        """Test has_license method of the GithubOrgClient class."""
        client_org = GithubOrgClient('google')
        self.assertEqual(client_org.has_license(repo, license),
                         expected_result)

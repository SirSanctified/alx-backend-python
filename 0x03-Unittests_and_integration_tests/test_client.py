#!/usr/bin/env python3
"""
Test client
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError
from utils import access_nested_map, get_json, memoize


class TestGithubOrgClient(unittest.TestCase):
    """
    Test the GithubOrgClient
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock):
        """
        Test that GithubOrgClient.org returns the correct value
        """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient._public_repos_url returns the correct value
        """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "test"}
            test_class = GithubOrgClient("google")
            self.assertEqual(test_class._public_repos_url, "test")
            mock_org.assert_called_once()


if __name__ == '__main__':
    unittest.main()

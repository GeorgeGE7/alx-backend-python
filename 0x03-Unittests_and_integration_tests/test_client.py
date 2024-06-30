#!/usr/bin/env python3
""" Unittest Test client

    This is a unittest for GithubOrgClient
"""
import unittest
import json
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data, mock):
        """Test the org method of GithubOrgClient"""
        endpoint = 'https://api.github.com/orgs/{}'.format(data)
        spec = GithubOrgClient(data)
        spec.org()
        mock.assert_called_once_with(endpoint)

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, rest):
        """Test the _public_repos_url property of GithubOrgClient"""
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=rest)):
            res = GithubOrgClient(name)._public_repos_url
            self.assertEqual(res, rest.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        """Test the public_repos method of GithubOrgClient"""
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as pub_mocke:

            pub_mocke.return_value = "world"
            res = GithubOrgClient('test').public_repos()

            self.assertEqual(res, ["Google", "TT"])

            pub_mocke.assert_called_once()
            mocked_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expectation):
        """Test the has_license method of GithubOrgClient"""
        rest = GithubOrgClient.has_license(repo, key)
        self.assertEqual(rest, expectation)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test the GithubOrgClient class in integration test"""

    @classmethod
    def setUpClass(classess):
        classess.get_patcher = patch('requests.get', side_effect=[
            classess.org_payload, classess.repos_payload
        ])
        classess.mocked_get = classess.get_patcher.start()

    @classmethod
    def tearDownClass(classess):
        classess.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method in integration test"""

    def test_public_repos_with_license(self):
        """Test the public_repos method with license in integration test"""


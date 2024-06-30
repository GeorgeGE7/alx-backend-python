#!/usr/bin/env python3
""" Unittest Test
"""


class TestAccessNestedMap(unittest.TestCase):
    def test_access_nested_map(self, nested_map, path, expected):
        ''' Test access nested map '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self, nested_map, path):
        ''' Test exception'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    def test_get_json(self, test_url, test_payload):
        ''' Test get json '''
        class Mocked(Mock):
            def json(self):
                return test_payload

        with patch('requests.get') as MockClass:
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        ''' Test memoize '''

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()


import os.path
import unittest
from collections import OrderedDict

from json_database.database_api import DatabaseAPI


class DatabaseAPITest(unittest.TestCase):
    def setUp(self):
        self.path = 'database.json'

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_api_with_not_existing_database_file_creates_it(self):
        api = DatabaseAPI(self.path)
        self.assertTrue(os.path.isfile(self.path))
        self.assertEqual(api.data, OrderedDict())

    def test_api_with_existing_empty_database_file_sets_data_to_none(self):
        with open(self.path, 'a'):
            self.assertTrue(os.path.isfile(self.path))
            api = DatabaseAPI(self.path)
            self.assertEqual(api.data, OrderedDict())

    def test_api_with_existing_not_empty_database_file_reads_it(self):
        with open(self.path, 'w+')as data_file:
            data_file.write('{}')

        self.assertTrue(os.path.isfile(self.path))
        api = DatabaseAPI(self.path)
        self.assertEqual(api.data, {})

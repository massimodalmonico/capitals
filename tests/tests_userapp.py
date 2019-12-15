#! /usr/bin/env python3


import unittest
from capitalspackage import checks
import tempfile  # for creating temp files


class TestMain(unittest.TestCase):

    # setup by creating 3 temp files
    def setUp(self):
        self.right_file = tempfile.NamedTemporaryFile(mode='w+', delete=True)
        self.right_file.write('ITALY;ROME')
        self.wrong_format = tempfile.NamedTemporaryFile(mode='w+', delete=True)
        self.right_file.write('ITALY,ROME')
        self.empty_file = tempfile.NamedTemporaryFile(mode='w+', delete=True)

# smoke test with right file
    def test_right_datafile(self):
        self.right_file.seek(0)
        u = checks.load_csv(filename=self.right_file.name)
        self.assertTrue(u)

# test with a file with wrong format
    def test_wrong_format_datafile(self):
        self.wrong_format.seek(0)
        u = checks.load_csv(filename=self.wrong_format.name)
        self.assertFalse(u)

# test with an empty file
    def test_empty_datafile(self):
        self.empty_file.seek(0)
        u = checks.load_csv(filename=self.empty_file.name)
        self.assertFalse(u)

    def tearDown(self):
        self.right_file.close()
        self.wrong_format.close()
        self.empty_file.close()

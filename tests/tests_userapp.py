#! /usr/bin/env python3


import unittest
from capitalspackage import checks
import tempfile
import os


class TestMain(unittest.TestCase):

    def setUp(self):
        self.right_file = tempfile.NamedTemporaryFile(mode='w+', delete=True)
        self.right_file.write('ITALY;ROME')
        self.wrong_format = tempfile.NamedTemporaryFile(mode='w+', delete=True)
        self.right_file.write('ITALY,ROME')
        self.empty_file = tempfile.NamedTemporaryFile(mode='w+', delete=True)

    def test_right_datafile(self):
        self.right_file.seek(0)
        u = checks.load_csv(filename=self.right_file.name)
        self.assertTrue(u)

    def test_wrong_format_datafile(self):
        self.wrong_format.seek(0)
        u = checks.load_csv(filename=self.wrong_format.name)
        self.assertFalse(u)

    def test_empty_datafile(self):
        self.empty_file.seek(0)
        u = checks.load_csv(filename=self.empty_file.name)
        self.assertFalse(u)

    def tearDown(self):
        self.right_file.close()
        self.wrong_format.close()
        self.empty_file.close()

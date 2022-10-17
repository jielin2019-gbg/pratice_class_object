import unittest

from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover('../cases', 'testcase_01.py')
runner = TestRunner(suite)
runner.run()
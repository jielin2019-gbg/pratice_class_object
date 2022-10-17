#1. 最原始方法加载测试用例
# suite = unittest.TestSuite()
# suite.addTest(Test("test_01"))
# suite.addTest(Test("test_02"))
# suite.addTest(Test("test_03"))
# suite.addTest(Test("test__change_password"))
# suite.addTest(Test("test_account_left_money_01"))
#
# runner = unittest.TextTestRunner()
# runner.run(suite)

#2. 使用testloader加载测试用例,没有测试报告

import unittest

suite = unittest.TestLoader().discover('../cases', 'testcase_01.py')   #或者直接用testcase_01
unittest.TextTestRunner().run(suite)
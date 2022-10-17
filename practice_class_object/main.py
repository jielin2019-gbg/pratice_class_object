# from bank_manager.BankDatas import AccountDatas
# from bank_manager.account_manager import AccountManager
# from tools.file_tool import FileTool
#
# file_tool = FileTool("cases.xls")
# file_tool.write_json_to_excel(AccountDatas, "cases.xls")
# #
# # AccountManager().update_acount_passwd("橘园子", "123456")
# # AccountManager().update_acount_left_money("橘园子", 200)
# # FileTool().write_json_to_excel(AccountDatas, "cases.xls")
# #
# AccountManager().update_acount_passwd("huahua亲", "123456", file_tool)
# AccountManager().update_acount_left_money("huahua亲", -200, file_tool)
import os.path
import unittest

from unittestreport import TestRunner
file = os.path.join((os.path.dirname(os.path.abspath(__file__))),"cases")
suite = unittest.defaultTestLoader.discover(file, 'test*.py')
runner = TestRunner(suite)
runner.run()
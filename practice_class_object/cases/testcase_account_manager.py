"""
======================
Author: 柠檬班-小简
Time: 2022/1/24 15:36
Project: py47-编码技术
Company: 湖南零檬信息技术有限公司
======================
"""
import unittest

from unittestreport import ddt, list_data

from bank_manager.BankDatas import AccountDatas
from bank_manager.account_manager import AccountManager
from tools.file_tool import FileTool
from tools.read_test_data_tool import ReadTestDataTool

"""
请在此文件当中，实现3个人的取钱、存钱、打印余额的操作。
3个人的帐号密码分别是：
第1个人： 嗯   753351
第2个人： 昌   362254
第3个人： 早睡早起     362254

当然，你可以添加更多。不限制。
最好是把异常场景、正常场景的用例都设计出来。全部测试一遍你写的类是不是有bug
"""

# cases_money = [{"user": "huahua亲", "money": -200, "left_money": 2752},
#                {"user": "船长", "money": 500, "left_money": 10094}, {"user": "阿辰", "money": -1500, "left_money": 1476},
#                {"user": "云自无心水空流", "money": 200.23, "left_money": 9056.23}]
# cases_password = [("huahua亲", "123456"), ("船长", "321654"), ("阿辰", "111111")]
# cases_user = [("huahua亲", "the user is exist"), ("船长", "the user is exist"), ("阿", "the user does not exist")]


@ddt
class Test(unittest.TestCase):
    tool = ReadTestDataTool("test_data.xlsx")
    users = tool.read_test_data("test_user_exist")
    money = tool.read_test_data("test_left_money")
    passwords = tool.read_test_data("test_password")

    def setUp(self) -> None:
        self.file_tool = FileTool("cases.xls")

    @list_data(money)
    def test_left_money(self, case):
        print(case)
        for item in AccountDatas:
            if item["user"] == case["user"]:
                AccountManager().update_acount_left_money(case["user"], case["money"], self.file_tool)
                assert case["left_money"] == item["left_money"]

    @list_data(passwords)
    def test_change_password(self,case):
        # MyAtm().login("4628858585535730", "362254")
        for item in AccountDatas:
            if item["user"] == case["user"]:
                #测试密码有写入数据中
                AccountManager().update_acount_passwd(case["user"], case["password"], self.file_tool)
                print(case["password"])
                assert case["password"] == item["passwd"]

    @list_data(users)
    def test_user_is_exists(self,case):
        actual_result = AccountManager().check_user_is_exists(case["user"])
        print(actual_result)
        assert actual_result == case["result"]

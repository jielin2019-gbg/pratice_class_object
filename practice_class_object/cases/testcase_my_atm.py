from parameterized import parameterized
from unittestreport import ddt, list_data

from bank_manager.my_atm import MyAtm
from tools.file_tool import FileTool
import unittest

from tools.read_test_data_tool import ReadTestDataTool

cases = [(5100, "the save money is more then 5000."), (100, 6600), (360, "钱不是100的倍数.请重新存入100的倍数")]
get_save_cases = [(1000, 2000, 7600), (100, 500, 8000)]


# save_money = [{"money": 5100, "result": "the save money is more then 5000."}, {"money": 100, "result": 10100},
#               {"money": 360, "result": "钱不是100的倍数.请重新存入100的倍数"}]
#

@ddt
class TestMyAtm(unittest.TestCase):
    tool = ReadTestDataTool("test_data.xlsx")
    save_money_data = tool.read_test_data("test_save_money")
    get_money_data = tool.read_test_data("test_get_money")
    get_money_data2 = tool.read_test_data("test_save_money2")
    print(save_money_data)

    def setUp(self):
        self.file_tool = FileTool("cases.xls")
        self.my_atm = MyAtm()
        self.my_atm.login("6585359869774900", "753351")
        print(self.my_atm)
        print(self.my_atm.ATM_MONEY)

    @list_data(get_money_data)
    def test_get_money(self, case):
        get_result = self.my_atm.get_money(case["money"])
        assert get_result == case["result"]

    @parameterized.expand(cases)  # 练习使用parameterized.expand
    def test_save_money(self, save_money, result):
        safe_result = self.my_atm.save_money(save_money)
        print(safe_result)
        print(result)
        assert safe_result == result

    @list_data(get_money_data2)
    def test_save_money_together(self, case):   #使用合适的名称保证用例执行的顺序，因为这样会影响到用例执行的结果
        self.my_atm.get_money(case["deposit_money"])
        result = self.my_atm.save_money(case["save_money"])
        # 断言判断atm操作后的余额是否等于atm机中余额
        print("this is the result:", result)
        assert result == case["expected_money"]

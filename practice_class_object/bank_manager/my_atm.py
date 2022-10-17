"""
======================
Author: 柠檬班-小简
Time: 2022/1/11 21:02
Project: py47-编码技术
Company: 湖南零檬信息技术有限公司
======================
"""
from bank_manager.BankDatas import AccountDatas
from bank_manager.account_manager import AccountManager
from tools.file_tool import FileTool


class MyAtm:
    ATM_MONEY = 10000

    def __init__(self):
        self.CURRENT_USER = None    #难点：注意CURRENT_USER的用法
        self.file_tool = FileTool("cases.xlsx")
        self.file_tool.write_json_to_excel(AccountDatas, "cases.xlsx")

    def login(self, accout, passwd):
        """
        用户插卡登录帐号。要确保帐号和密码在银行数据当中存在。否则提示帐号不存在。
        :param account:
        :param passwd:
        :return:
        """
        for case in self.file_tool.read_excel_all_data():
            if case['accout'] == accout and case['passwd'] == passwd:
                print("login success.")
                # global CURRENT_USER
                self.CURRENT_USER = case
                print(self.CURRENT_USER)
                return True
            else:
                # print("the account does not exsit.")
                pass

    def get_money(self, money):
        """
        用户登陆成功之后，进行的取钱操作。
        需要判断3件事：一是atm中的钱是否够。二是用户的余额是否够。三是要取的钱是否为100的整数倍。
        同时满足的条件，才可以取出钱。
        在取出钱之后，需要再做2件事：一是更新atm中的钱。二是更新用户余额的钱。
        :param money: 要取出的金额。
        :return:
        """
        if self.CURRENT_USER:
            if MyAtm.ATM_MONEY >= money:
                # case = self.login(self.accout, self.passwd)
                if self.CURRENT_USER["left_money"] >= money:
                    if money % 100 == 0:
                        # CURRENT_USER["left_money"] -= money
                        AccountManager().update_acount_left_money(self.CURRENT_USER["user"], -money, self.file_tool)
                        MyAtm.ATM_MONEY -= money
                        return MyAtm.ATM_MONEY
                    else:
                        return "the money 不是100的整数倍."
                else:
                    return "accout money is not enough."
            else:
                return "ATM money is not enough"

    def save_money(self, money):
        """
        用户登陆成功之后，进行的存钱操作。
         需要判断2件事：一是要存的钱是否为100的整数倍。最高不能超过5000
        同时满足的条件，才可以存钱。
        在存钱之后，需要再做2件事：一是更新atm中的钱。二是更新用户余额的钱。
        :param money:
        :return:
        """
        # if self.login(self.accout, self.passwd) != False:
        # case = self.login(self.accout, self.passwd)
        if self.CURRENT_USER:
            if money <= 5000:
                if money % 100 == 0:
                    AccountManager().update_acount_left_money(self.CURRENT_USER["user"], money, self.file_tool)
                    # CURRENT_USER["left_money"] += money
                    MyAtm.ATM_MONEY += money
                    return MyAtm.ATM_MONEY
                else:
                    return "钱不是100的倍数.请重新存入100的倍数"
            else:
                return "the save money is more then 5000."

    def print_info(self):
        """
        显示用户当前的余额是多少即可。
        :return:
        """
        # if self.login(self.accout, self.passwd)!= False:
        #     case = self.login(self.accout, self.passwd)
        if self.CURRENT_USER:
            print(self.CURRENT_USER['left_money'])
            return self.CURRENT_USER['left_money']

    def get_atm_money(self):
        return self.ATM_MONEY


if __name__ == '__main__':
    x = MyAtm()
    file_tool = FileTool("cases.xls")

    print(x.login('4283396949201070000', '869342'))
    print(x.get_money(1000))
    print(x.print_info())
    print(x.save_money(2000))
    print(x.print_info())
    print(x.get_atm_money())
    print(x.ATM_MONEY)

"""
======================
Author: 柠檬班-小简
Time: 2022/1/24 15:04
Project: py47-编码技术
Company: 湖南零檬信息技术有限公司
======================
"""
import json

from bank_manager.BankDatas import AccountDatas
from config import column
from tools.file_tool import FileTool


class AccountManager:

    def update_acount_passwd(self, user, passwd, file_tool):
        """
        1、判断帐号是否存在。如果不存在，则直接提示帐号不存在。
        2、如果帐号存在，更新密码时，密码长度必须为6位。而且不能与之前的一样。
        :param user: 用户名。
        :param passwd: 更新后的密码。
        :return:
        """
        i = 0
        for case in AccountDatas:
            i += 1
            if user == case["user"] and len(str(passwd)) == 6 and passwd != self.get_passwd(user):
                # AccountDatas.index(case)           #可以取到一个元素的index
                self.set_passwd(user, passwd)
                list = [i, column["password"]]
                file_tool.write_data(list, passwd)

    def update_acount_left_money(self, user, money, file_tool):
        """
        1、判断帐号是否存在。如果不存在，则直接提示帐号不存在。
        2、如果用户存在。更新后的用户余额，不得低于0。
        :param user: 用户名。
        :param money: money可正可负。要减少/增加的钱。用当前余额加上money这个值。
        :return:
        """
        i = 0
        for case in AccountDatas:
            i += 1
            msg = ""
            if user == case["user"]:
                if money + case["left_money"] >= 0:
                    self.set_money(user, money)
                    # 在密码栏更新为新的密码
                    my_list = [i, column["left_money"]]
                    account_money = case["left_money"]
                    file_tool.write_data(my_list, account_money)
                    return account_money
                else:
                    return "余额不足"

    def check_user_is_exists(self, user):
        """
        判断用户是否在银行数据库中存在。如果存在，则返回用户的所有信息。如果不存在，则返回False
        :param user:用户名
        :return:
        """
        msg = ""
        for case in AccountDatas:
            if user == case["user"]:
                msg = "the user is exist"
                return msg
            else:
                msg = "the user does not exist"
        return msg

    def get_passwd(self, user):
        for case in AccountDatas:
            if user == case["user"]:
                passwd = case["passwd"]
                return passwd

    def set_passwd(self, user, passwd):
        for case in AccountDatas:
            if user == case["user"]:
                case["passwd"] = passwd
                print(case["passwd"])

    def set_money(self, user, money):
        for case in AccountDatas:
            if user == case["user"]:
                if case["left_money"] + money >= 0:
                    # if case["left_money"] > money:
                    case["left_money"] += money
                    # 在此处写入excel最后一列写入存取钱的数据money，
                    # 并更新left_money

                else:
                    return "存取不成功，请查看金额。"


if __name__ == '__main__':
    file_tool = FileTool("cases.xls")
    AccountManager().update_acount_passwd("橘园子", "11111", file_tool)
    print(AccountDatas)
    AccountManager().update_acount_left_money("橘园子", 200, file_tool)
    print(AccountDatas)
    print(AccountManager().check_user_is_exists("橘园"))

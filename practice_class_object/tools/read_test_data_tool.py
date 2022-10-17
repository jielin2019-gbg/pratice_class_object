import os

import openpyxl


class ReadTestDataTool:
    def __init__(self, file_name):
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dir = os.path.join(file_path, "data", file_name)
        self.workbook = openpyxl.load_workbook(dir)

    def read_test_data(self, sheet_name):
        self.worksheet = self.workbook[sheet_name]
        case_list = []
        datas = list(self.worksheet.values)
        for value in datas[1:]:
            dict_data = dict(zip(datas[0], value))
            case_list.append(dict_data)
        return case_list


if __name__ == '__main__':
    # tool = ReadTestDataTool("test_data.xlsx")
    # print(tool.read_test_data("test_user_exist"))
    tool = ReadTestDataTool("test_data.xlsx")
    users = tool.read_test_data("test_user_exist")
    print(users)

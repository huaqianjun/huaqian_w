from selenium import webdriver
from common.login_page import LoginPage
from common.read_excel import ExcelUtil
import unittest
import ddt
import os
login_url = "http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"
# '''测试的数据'''
# testdates = [
#     {"user": "admin", "psw": "123456", "expect": "admin"},
#     {"user": "admin", "psw": "", "expect": ""},
#     {"user": "admin11", "psw": "123456", "expect": ""},
# ]
propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 工程路径
filepath = os.path.join(propath, "common", "datas.xlsx")
data = ExcelUtil(filepath)
testdates = data.dict_data()
print(filepath)
print(testdates)

# filepath = "D:\\web_d\\common\\datas.xlsx"


@ddt.ddt
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)
        cls.driver.get(login_url)

    def setUp(self):
        self.driver.get(login_url)
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()  # 退出登陆
        self.driver.refresh()
        self.driver.get(login_url)

    def login_case(self, user, psw, expect):
        self.loginp.login(user, psw)
        # self.loginp.input_user(user)
        # self.loginp.input_psw(psw)
        # self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        print("测试结果：%s" % result)
        self.assertTrue(result == expect)
    @ddt.data(*testdates)
    def test_01(self, data):
        '''输入账号admin，输入密码123456 点登陆'''
        print("-------开始测试-------")
        # data1 = testdates[0]
        print("测试数据“%s" % data)
        self.login_case(data["user"], data["psw"], data["expect"])
        print("-------结束：pass-------")


    def tearDown(self):
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()  # 退出登陆
        self.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == "__main__":
    unittest.main()

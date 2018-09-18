import time
import unittest

from selenium import webdriver

from case.add_bug import ZenTaoBug


class Test_Add_Bug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.bug = ZenTaoBug(cls.driver)
        cls.bug.login()

    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d %H:%M:%S")
        title = "测试标题bug"+timestr
        self.bug.add_bug(title)
        result = self.bug.is_login_success(title)
        print(result)
        self.assertTrue(result)
if __name__ == "__main__":
    unittest.main()

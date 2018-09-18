# coding:utf-8
from selenium import webdriver
from common.Base import Base
import time
login_url = ("http://127.0.0.1:81/zentao/bug-create-1-0-moduleID=0.html")

class ZenTaoBug(Base):  # 继承
    # 定位登陆
    loc1 = ("id", "account")
    loc2 = ("css selector", "[name='password']")
    loc3 = ("xpath", "//*[@id='submit']")
    # 添加bug
    loc_test = ("link text", "测试")
    loc_bug = ("link text", "Bug")
    loc_addbug = ("xpath", ".//*[@id='createActionMenu']/a")
    loc_trunk = ("xpath", ".//*[@id='openedBuild_chosen']/ul")
    loc_trunk_add = ("xpath", ".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_input_title = ("id", "title")
    # 需要先切换frame
    loc_inputbody = ("class name", "article-content")
    # 切换回来
    loc_keep_login = ("id", "submit")
    loc_new = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    def login(self, user="admin", psw="123456", keep_login=False):
        self.driver.get(login_url)
        self.sendKeys(self.loc1, user)
        self.sendKeys(self.loc2, psw)
        if keep_login: self.click(self.loc_keep_login)
        self.click(self.loc3)

    def add_bug(self, title="测试标题bug"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_trunk)
        self.click(self.loc_trunk_add)
        self.sendKeys(self.loc_input_title, title)
        # 输入正文
        frame = self.driver.find_element("class name", "ke-edit-iframe")
        self.driver.switch_to.frame(frame)
        # 富文本不能清空
        body = '''[测试步骤]xxx
        [结果]xxx
        [期望结果]xxx
        '''
        self.sendKeys(self.loc_inputbody, body)
        self.driver.switch_to_default_content()
        self.click(self.loc_keep_login)
    def is_login_success(self, _text):
        return self.is_text_in_element(self.loc_new, _text)
if __name__ == "__main__":
    driver = webdriver.Firefox()
    bug = ZenTaoBug(driver)
    bug.login()
    timestr = time.strftime("%Y_%m_%d %H:%M:%S")
    title = "测试标题bug"+timestr
    bug.add_bug(title)
    result = bug.is_login_success(title)
    print(result)





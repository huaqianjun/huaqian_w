# coding:utf-8
import time

from selenium import webdriver

from common import Base


class AddBugPage(Base):  # 继承
    # 添加BUG
    loc_test = ("link text", "测试")
    loc_bug = ("link text", "Bug")
    loc_addbug = ("xpath", ".//*[@id='createActionMenu']/a")
    loc_truck = ("xpath", ".//*[@id='openedBuild_chosen']/ul")
    loc_truck_add = ("xpath", ".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_input_title = ("id", "title")
    # 需要先切换iframe
    loc_input_body = ("class name", "article-content")
    loc_avse = ("css selector", "#submit")

    # 新增的列表
    loc_new = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    def add_bug(self, title="测试提交BUG"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)

        self.sendKeys(self.loc_input_title, title)
        # 输入body
        frame = self.findElement(("class name", "ke-edit-iframe"))
        self.driver.switch_to.frame(frame)
        # 富文本不能clear
        body = '''[测试步骤]xxx
        [结果]xxx
        [期望结果]xxx
        '''
        self.sendKeys(self.loc_input_body, body)
        self.driver.switch_to.default_content()

        self.click(self.loc_avse)

    def is_add_bug_sucess(self,_text):
        return self.is_text_in_element(self.loc_new, _text)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    bug = AddBugPage(driver)

    from pages.login_page import LoginPage
    a = LoginPage(driver)
    a.login()

    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    title = "测试提交BUG"+timestr
    bug.add_bug(title)
    result = bug.is_add_bug_sucess(title)
    print(result)








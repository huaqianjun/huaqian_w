from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# from selenium.webdriver.common.by import By
class Base():
    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 5
        self.t = 0.5
    def finElementNew(self, locator):
        '''定位到元素，返回元素对象，没定位到返回timeout异常'''
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        return ele

    def findElement(self, locator):
        if not isinstance(locator, tuple):
            print('locator参数类型错误，必须传元组类型：loc=（"id", "value")')
        else:
            print("正在定位的元素信息：定位的方式->%s, value值-_%s"% (locator[0], locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    def sendKeys(self, locator, text):
        ele = self.findElement(locator)
        ele.send_keys(text)
    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()
    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()
    def isSelected(self,locator):
        '''判断元素是否存在'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r
    def is_title(self, _title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title):
        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False
    def is_text_in_element(self, locator, _text):

        '''返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False
    def is_alert(self):
        '''判断alert在不在'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False
    def move_to_element(self, locator):
        '''鼠标悬停操作'''
        element = self.findElement(locator)
        ActionChains(self.driver).move_to_element(element).perform()
    def select_by_index(self, locator, index=0):
        '''通过索引，index是索引第几个，从0开始，默认选第一个'''
        element = self.findElement(locator)  # 定位select这一栏
        Select(element).select_by_index(index)
    def select_by_value(self,locator, value):
        '''通过value值属性'''
        element = self.findElement(locator)  # 定位select这一栏
        Select(element).select_by_value(value)
    def select_by_text(self, locator, text):
        '''通过文本值定位'''
        element = self.findElement(locator)  # 定位select这一栏
        Select(element).select_by_visible_text(text)
    def js_scroll_end(self,):
        '''鼠标滚动到底部'''
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)
    def js_scroll_top(self):
        '''鼠标滚动到顶部'''
        js = "window.scrollto(0,0）"
        self.driver.execute_script(js)
    def js_focus_element(self, locator):
        '''聚焦元素'''
        target = self.findElement(locator)
        self.driver.execute_script("argument[0].scrollIntoView();", target)




if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
    zentao = Base(driver)
    # loc1 = (By.ID, "account")
    # loc2 = (By.NAME, "password")
    # loc3 = (By.ID, "submit")
    loc1 = ("id", "account")
    loc2 = ("css selector", "[name='password']")
    loc3 = ("xpath", "//*[@id='submit']")
    zentao.sendKeys(loc1, "admin")
    zentao.sendKeys(loc2, "123456")
    zentao.click(loc3)



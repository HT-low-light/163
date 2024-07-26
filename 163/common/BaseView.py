import os
import csv
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class BaseView:

    def __init__(self, driver):
        self.driver = driver

    # 打开页面
    def open_url(self, url):
        self.driver.get(url)

    # 获取元素
    def find_element(self, *loc):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda x: x.find_element(*loc))
        return element

    # 获取多个元素
    def find_elements(self, *loc):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(lambda x: x.find_elements(*loc))
        return element

    # 获取屏幕的大小
    def get_window_size(self):
        return self.get_window_size()

    # 点击
    def click(self, *loc):
        el = self.find_element(*loc)
        el.click()

    # 输入文本
    def input_text(self, text, *loc):
        el = self.find_element(*loc)
        el.clear()
        el.send_keys(text)

    # 清空文本
    def clear(self, *loc):
        el = self.find_element(*loc)
        el.clear()

    # 打印文本
    def print_text(self, *loc):
        el = self.find_element(*loc).text
        return el

    # 获取文本框的值
    def get_input_value(self, *loc):
        el = self.find_element(*loc).get_attribute('value')
        return el

    # 退出
    def quit(self):
        sleep(3)
        self.driver.quit()

    # 刷新页面
    def refresh(self):
        self.driver.refresh()

    # 操作js的
    def execute_script(self, script):
        self.driver.execute_script(script)

    # 进入frame框架
    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    # 退出frame框架
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    # 截图
    def screenshot_save(self, file):
        self.driver.save_screenshot(file)

    def get_csv_data(self, row):
        file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), '..') + '/data/account.csv')
        with open(file_name, encoding='utf-8') as f:
            datas = csv.reader(f)
            for index, data in enumerate(datas):
                if index == row:
                    return data


if __name__ == '__main__':
    pass

import pytest
from time import sleep
from selenium import webdriver

from config import BASE_DIR
from common.get_data import get_json_data
from pageobjects.login_page import LoginPage
from pageobjects.index_163_page import IndexPage


class TestLogin:
    #打开浏览器
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://mail.163.com/")
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)
        sleep(2)

    def teardown(self):
        sleep(2)
        self.driver.close()

    @pytest.mark.parametrize("param", get_json_data(BASE_DIR + '/testdatas/login_data.json'))
    def test_01_login_success(self, param):
        # 进入登录的iframe框架
        self.login_page.switch_to_frame_login()
        # 登录，输入账号，密码
        self.login_page.login(param['username'], param['password'])
        sleep(3)
        self.driver.switch_to.default_content()
        text = self.index_page.get_index_text()
        assert text == '首页'


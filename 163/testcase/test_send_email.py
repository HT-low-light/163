import time
import pytest
from selenium import webdriver
from time import sleep
from config import BASE_DIR
from common.get_data import get_json_data
from pageobjects.login_page import LoginPage
from pageobjects.index_163_page import IndexPage


class TestEmail:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://mail.163.com/")
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)
        # 进入登录的iframe框架
        self.login_page.switch_to_frame_login()
        # 登录，输入账号密码
        self.login_page.login("15703070836", "Hm12012326")
        # 跳出login框架
        self.driver.switch_to.default_content()

    def teardown(self):
        time.sleep(3)
        # 退出页面
        self.driver.quit()

    def test_01_receive_mail(self):
        self.index_page.click_index()
        self.index_page.click_receive_email()
        self.index_page.click_first_email()
        sleep(2)
        text = self.index_page.get_sender_text()
        sleep(2)
        assert text == "发件人："

    def test_02_delete_email(self):
        self.index_page.click_receive_email()
        self.index_page.click_email_checkbox()
        sleep(2)
        self.index_page.click_delete_email()
        sleep(2)
        text = self.index_page.get_not_email_text()
        assert text == "收件箱没有邮件哦"

    @pytest.mark.parametrize("param", get_json_data(BASE_DIR + '/testdatas/send_email_data.json'))
    def test_03_send_email(self, param):
        self.index_page.click_send_mail()
        # 收件人
        self.index_page.input_addressee(param["address"])
        self.index_page.input_theme(param["theme"])
        self.index_page.switch_to_frame_body()
        self.index_page.input_body(param["body"])
        sleep(2)
        # 跳出body框架
        self.driver.switch_to.default_content()
        sleep(2)
        # 点击发送邮件
        self.index_page.send_email()
        sleep(2)
        text = self.index_page.get_send_email_success_text().strip()
        assert text == '邮件发送成功'

from time import sleep

import pytest
from common.BaseView import BaseView
from selenium.webdriver.common.by import By

"""
登录页面
"""


class LoginPage(BaseView):
    '''定位页面元素'''

    # 账号
    email_loc = (By.NAME, 'email')
    # 密码
    password_loc = (By.NAME, 'password')
    # 登录
    login_loc = (By.ID, 'dologin')
    login_iframe = (By.XPATH, '//*[@id="loginDiv"]/iframe')

    def switch_to_frame_login(self):
        el_frame = self.find_element(*self.login_iframe)
        self.switch_to_frame(el_frame)

    def login(self, email, password):
        self.input_text(email, *self.email_loc)
        self.input_text(password, *self.password_loc)
        self.click(*self.login_loc)







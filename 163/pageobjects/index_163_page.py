from selenium.webdriver.common.by import By

from common.BaseView import BaseView


# 163邮箱首页
class IndexPage(BaseView):

    # 首页
    index_loc = (By.XPATH, '//nav[@id="dvMultiTabWrapper"]/div[1]/ul/li[1]/div[3]')
    # 写信
    write_email_loc = (By.XPATH, '//*[@id="dvNavContainer"]/nav/div[1]/ul/li[2]')
    # 收信
    receive_email_loc = (By.ID, "_mail_component_92_92")
    # 收件人
    addressee_loc = (By.XPATH, '//*[@id="dvContainer"]/div[2]/div[1]/section/header/div[1]/div[1]/div/div[2]/div/input')
    # 主题
    theme_loc = (By.XPATH, '//*[@id="dvContainer"]/div[2]/div[1]/section/header/div[2]/div[1]/div/div/input')
    body_frame = (By.XPATH, '//*[@class="APP-editor-edtr"]/iframe')
    body_loc = (By.XPATH, '/html/body')
    # 发送
    send_email_loc = (By.XPATH, '//footer[@class="jp0"]/div[1]')
    # 点击邮件
    email_loc = (By.XPATH, '//*[@sign="start"]')
    # 发件人text
    sender_loc = (By.XPATH, '//*[@role="list"]/div[1]/div[2]/ul[2]/li[2]/div[1]')
    # 第一封邮件的复选框
    email_checkbox = (By.XPATH, '//*[@sign="start"]/label/span/b')
    # 删除按钮
    delete_button_loc = (By.XPATH, '/html/body/div[2]/div[1]/div[2]/header/div/div[2]/div/span')
    # 没有邮件的text
    not_email_text_loc = (By.XPATH, '//div[@id="dvContainer"]/div/div/div/div/div[6]/div/div/div[1]')
    # 发送邮件成功的text
    send_email_success_text_loc = (By.XPATH, '//div[@id="dvContainer"]/div[2]/div[2]/section/h1')

    # 点击首页
    def click_index(self):
        self.click(*self.index_loc)

    # 点击写信
    def click_send_mail(self):
        self.click(*self.write_email_loc)

    # 输入收件人
    def input_addressee(self, text):
        self.input_text(text, *self.addressee_loc)

    # 输入主题
    def input_theme(self, text):
        self.input_text(text, *self.theme_loc)

    # 进入body frame框架
    def switch_to_frame_body(self):
        el_frame = self.find_element(*self.body_frame)
        self.switch_to_frame(el_frame)

    # 输入内容
    def input_body(self, text):
        self.input_text(text, *self.body_loc)

    # 发送email
    def send_email(self):
        self.click(*self.send_email_loc)

    # 点击收信
    def click_receive_email(self):
        self.click(*self.receive_email_loc)

    # 点击第一封邮件
    def click_first_email(self):
        self.click(*self.email_loc)

    # 点击邮件的复选框
    def click_email_checkbox(self):
        self.click(*self.email_checkbox)

    # 点击删除按钮
    def click_delete_email(self):
        self.click(*self.delete_button_loc)

    # 获取首页文本，用于断言
    def get_index_text(self):
        text = self.print_text(*self.index_loc)
        return text

    # 获取发件人文本，用于断言用
    def get_sender_text(self):
        text = self.print_text(*self.sender_loc)
        return text

    # 获取没有邮件的文本，用于断言
    def get_not_email_text(self):
        text = self.print_text(*self.not_email_text_loc)
        return text

    # 获取发送邮件成功的文本，用于断言
    def get_send_email_success_text(self):
        text = self.print_text(*self.send_email_success_text_loc)
        return text










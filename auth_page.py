from test.base_page import BasePageLocators
from test.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators_LiveJournal_LOGIN(BasePageLocators, BasePage):
    LOCATOR_LOGIN = (By.XPATH, '//*[@id="js"]/body/div[2]/header/div/nav[2]/ul/li[2]/a')
    LOCATOR_USERNAME = (By.ID, 'user')
    LOCATOR_PASSWORD = (By.XPATH, '//*[@id="lj_loginwidget_password"]')
    LOCATOR_LOGIN_TO_SITE = (By.XPATH, '//*[@id="js"]/body/div[2]/div[3]/div/div[2]/form[1]/button')

    def open(self):
        self.browser.get(self.url)

    def click_login_page(self):
        enter_button = self.browser.find_element(*Locators_LiveJournal_LOGIN.LOCATOR_LOGIN)
        enter_button.click()

    def enter_login(self, login):
        username_input = self.browser.find_element(*Locators_LiveJournal_LOGIN.LOCATOR_USERNAME)
        username_input.send_keys(login)

    def click_to_password(self):
        enter_button = self.browser.find_element(*Locators_LiveJournal_LOGIN.LOCATOR_PASSWORD)
        enter_button.click()

    def enter_password(self, password):
        password_input = self.browser.find_element(*Locators_LiveJournal_LOGIN.LOCATOR_PASSWORD)
        password_input.send_keys(password)

    def click_login_button(self):
        enter_button = self.browser.find_element(*Locators_LiveJournal_LOGIN.LOCATOR_LOGIN_TO_SITE)
        enter_button.click()







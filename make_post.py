from test.base_page import BasePageLocators
from test.base_page import BasePage
from selenium.webdriver.common.by import By
import time


class Locators_LiveJournal_NEW_POST(BasePageLocators, BasePage):
    LOCATOR_WRITE_BLOG = (By.XPATH, '//*[@id="js"]/body/div[2]/header/div[1]/nav[2]/ul/li[4]/a')
    LOCATOR_TITLE = (By.XPATH, '//*[@id="content"]/div/div/div[2]/textarea')
    LOCATOR_TEXT = (By.XPATH, '//*[@id="editorWrapper"]/div[1]/div[2]/div/div/div[2]/div')
    LOCATOR_CONFIGURE_AND_PUBLISH = (By.CSS_SELECTOR, 'body > div:nth-child(13) > footer > div > div > '
                                                      'div.primSxn-0-2-237 > div:nth-child(2) > button')
    LOCATOR_PUBLISH = (By.CSS_SELECTOR, 'body > div:nth-child(13) > footer > div > div > div.primSxn-0-2-237 > '
                                        'div:nth-child(2) > div > footer > div > button')



    def click_create_post(self):
        create_button = self.browser.find_element(*Locators_LiveJournal_NEW_POST.LOCATOR_WRITE_BLOG)
        create_button.click()

    def click_write_title(self):
        write_title_field = self.browser.find_element(*Locators_LiveJournal_NEW_POST.LOCATOR_TITLE)
        write_title_field.click()

    def click_write_text(self):
        write_text_field = self.browser.find_element(*Locators_LiveJournal_NEW_POST.LOCATOR_TEXT)
        write_text_field.click()

    def enter_title(self, title):
        title_input = self.browser.find_element(*Locators_LiveJournal_NEW_POST.LOCATOR_TITLE)
        title_input.send_keys(title)

    def enter_text(self, text):
        text_input = self.browser.find_element(*Locators_LiveJournal_NEW_POST.LOCATOR_TEXT)
        text_input.send_keys(text)

    def click_configure_and_publish(self):
        conf_and_publ_button = self.browser.find_element(*Locators_LiveJournal_NEW_POST.LOCATOR_CONFIGURE_AND_PUBLISH)
        conf_and_publ_button.click()

    def click_publish(self):
        publish_button = self.browser.find_element(*Locators_LiveJournal_NEW_POST.LOCATOR_PUBLISH)
        publish_button.click()
        time.sleep(10)




from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasePage:
    def __init__(self, browser, url,timeout=20):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # открывает страницу переданную в url
    def open(self):
        self.browser.get(self.url)

    def open_site(self):
        return self.browser.get(self.url)

    def find_element(self, locator, time=10):
        element = WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))
        return element


    def find_elements(self, *locator):
        return self.browser.find_elements(*locator)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK),
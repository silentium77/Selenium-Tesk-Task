import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome('C:/Users/zimin/PycharmProjects/LiveJournalProject/chromedriver.exe')
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
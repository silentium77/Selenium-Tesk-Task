import pytest
from pages.make_post import Locators_LiveJournal_NEW_POST
from pages.auth_page import Locators_LiveJournal_LOGIN

@pytest.mark.autorization
def test_login_and_publish_new_post(browser):
    link = "https://www.livejournal.com/media/"
    page = Locators_LiveJournal_LOGIN(browser, link)

    page.open()

    page.click_login_page()

    username = "Julia_S91"
    password = "Silentium345"

    page.enter_login(username)

    page.click_to_password()

    page.enter_password(password)

    page.click_login_button()

    page2 = Locators_LiveJournal_NEW_POST(browser, browser.current_url)
    title = "Hello Everybody!"
    text = "New post about greetings"

    page2.click_create_post()

    page2.click_write_title()

    page2.enter_title(title)

    page2.click_write_text()

    page2.enter_text(text)

    page2.click_configure_and_publish()

    page2.click_publish()









import time

from pages.data_login_password import url
from pages.news_history_page import CheckNewsHistoryPage


class TestNewsHistory:

    class TestCheckNewsHistory:

        def test_person1(self, driver):
            news_history_page = CheckNewsHistoryPage(driver, url)
            news_history_page.open()
            news_history_page.create_change_del_restored_article()
            news_history_page.open()
            # news_history_page.person1_auth()

        def test_create_person(self, driver):
            news_history_page = CheckNewsHistoryPage(driver, url)
            news_history_page.open()
            # news_history_page.add_role_content()
            # news_history_page.add_role_no_content()
            news_history_page.open()
            login1, password_person1 = news_history_page.create_person1()
            news_history_page.open()
            news_history_page.person1_auth(login=login1, password=password_person1)
            time.sleep(6)





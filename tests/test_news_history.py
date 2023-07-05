import time

from pages.data_login_password import url
from pages.news_history_page import CheckNewsHistoryPage


class TestNewsHistory:

    class TestCheckNewsHistory:

        # def test_person1(self, driver):
        #     news_history_page = CheckNewsHistoryPage(driver, url)
        #     news_history_page.open()
        #     news_history_page.create_change_del_restored_article()
        #     news_history_page.open()
        #     # news_history_page.person1_auth()

        def test_create_person(self, driver):
            news_history_page = CheckNewsHistoryPage(driver, url)
            news_history_page.open()
            # news_history_page.add_role_content()
            # news_history_page.add_role_no_content()
            login1, password_person1 = news_history_page.create_person1()
            login2, password_person2 = news_history_page.create_person2()
            news_history_page.open()
            first_name_1, changed_name_1 = news_history_page.create_change_del_restored_article()
            news_history_page.open()
            first_name_2, changed_name_2 = news_history_page.create_change_del_article()
            news_history_page.open()
            news_history_page.persons_auth(login=login1, password=password_person1)
            news_history_page.check_restored_1()
            news_history_page.check_del_article_2()
            news_history_page.open()
            news_history_page.persons_auth(login=login2, password=password_person2)
            news_history_page.check_restored_1_person2()
            news_history_page.check_del_article_2_person2()


            time.sleep(16)





            # time.sleep(1600)





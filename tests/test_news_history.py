import time
import allure
import pytest
from pages.news_history_page import CheckNewsHistoryPage
from pages.users import fry, person2, person1

user_for_test = fry


@pytest.mark.order(6)
@allure.suite("Проверка новостей о статье и новостей о комментариях в История")
class TestNewsHistory:

    class TestCheckNewsHistory:

        @allure.title("Проверка новостей о статье и новостей о комментариях в История")
        def test_check_persons_article_news(self, driver):
            news_history_page = CheckNewsHistoryPage(driver)
            news_history_page.get_authorisation_in_selen(user_for_test)
            # login1, password_person1 = news_history_page.create_person1(driver)
            # login2, password_person2 = news_history_page.create_person2(driver)
            # news_history_page.open()
            first_name, changed_name_1, deleted_name_1 = news_history_page.create_change_del_restored_article()
            first_name_2, changed_name_2, deleted_name_2 = news_history_page.create_change_del_article()
            """check person1"""
            # news_history_page.persons_auth(login=login1, password=password_person1)
            news_history_page.get_authorisation_in_selen(person2)
            news_history_page.check_restored_1()
            news_history_page.check_del_article_2(deleted_name_2)
            news_history_page.check_comment_1(deleted_name_2)
            # news_history_page.open()
            """check person2"""
            time.sleep(2)
            # news_history_page.persons_auth(login=login2, password=password_person2)
            news_history_page.get_authorisation_in_selen(person1)
            news_history_page.check_restored_1_person2()
            news_history_page.check_del_article_2_person2(deleted_name_1)
            news_history_page.check_comment_1_person2(deleted_name_1)
            # time.sleep(6)












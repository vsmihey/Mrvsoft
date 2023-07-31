import time
import allure
import pytest
from pages.create_article_and_comments import Comments, DataParser
from pages.person_validation import Person1, Person2, Person3, Person4, PersonValidation


@allure.suite(
    'Тесты по созданию, редактированию, удалению, восстановлению обычной статьи и отслеживание изменений в истории и '
    'колокольчике')
@pytest.mark.order(7)
class TestCheckNewArticleStatus:
    # TODO: решить проблему с проверкой комментариев в истории и колокольчике

    @allure.feature('Создание новой статьи, наполнение тестовыми комментами, проверка в истории и колокольчике')
    class TestNewArticle:
        @allure.title('Создание новой статьи')
        def test_article_create_base(self, driver):
            page_article_base = PersonValidation(driver)
            page_article_base.creating_base_article()

        @allure.title('Создание тестового набора комментов')
        def test_create_comments(self, driver):
            Comments.create_comments(driver, DataParser.get_url_from_data_file())

        @allure.title('Закрытие первого тестового комментария')
        def test_close_first_comment(self, driver):
            Comments.close_first_comment(driver, DataParser.get_url_from_data_file())

        @allure.title('Проверка истории пользователем без доступа к статье')
        def test_new_article_history_person1(self, driver):
            person = Person1(driver)
            person.get_check_history()

        @allure.title('Проверка колокольчика пользователем без доступа к статье')
        def test_new_article_bell_person1(self, driver):
            person = Person1(driver)
            person.get_check_bell()

        @allure.title('Проверка истории пользователем с полным доступа к статье')
        def test_new_article_history_person2(self, driver):
            person = Person2(driver)
            person.get_check_history()
            # person.history_gray_comment_check()
            # person.history_four_no_solve_comment_check()
            # person.history_third_no_solve_comment_check()
            # person.history_second_no_solve_comment_check()
            # person.history_first_solve_comment_check()
            person.go_to_new_article_from_history_or_bell()
            person.check_open_valid_article()

        @allure.title('Проверка колокольчика пользователем с полным доступа к статье')
        def test_new_article_bell_person2(self, driver):
            person = Person2(driver)
            person.get_check_bell()
            # person.bell_gray_comment_check()
            # person.bell_four_comment_check()
            # person.bell_third_comment_check()
            # person.bell_second_comment_check()
            # person.bell_first_comment_check()
            person.go_to_new_article_from_history_or_bell()
            person.check_open_valid_article()

        @allure.title('Проверка колокольчика пользователем с подтверждением прочтения')
        def test_new_article_bell_person3(self, driver):
            person = Person3(driver)
            person.get_check_bell()
            person.go_to_new_article_from_history_or_bell()
            person.check_open_valid_article()
            person.check_article_bottom_banner()
            person.bottom_banner_button_click()

        @allure.title('Проверка колокольчика пользователем с доступом к статье но с выключенными уведомлениями')
        def test_new_article_bell_person4(self, driver):
            person = Person4(driver)
            person.get_check_bell()
            person.check_no_article_notifications()

    class TestMinorArticle:

        def test_article_minor_edit_base(self, driver):
            page_article_base = PersonValidation(driver)
            page_article_base.minor_edit_base_article(DataParser.get_url_from_data_file())

        def test_close_second_comment(self, driver):
            Comments.close_second_comment(driver, DataParser.get_url_from_data_file())

        def test_minor_edit_article_history_person1(self, driver):
            person = Person1(driver)
            person.get_check_history()

        def test_minor_edit_article_bell_person1(self, driver):
            person = Person1(driver)
            person.get_check_bell()

        # def test_minor_edit_article_history_person2(self, driver):
        #     person = Person2(driver)
        #     person.get_check_history()
        #     person.history_second_solve_comment_check()
        #
        # def test_minor_edit_article_bell_person2(self, driver):
        #     person = Person2(driver)
        #     person.get_check_bell()
        #
        # def test_minor_edit_article_bell_person3(self, driver):
        #     person = Person3(driver)
        #     person.get_check_bell()

        def test_minor_edit_article_bell_person4(self, driver):
            person = Person4(driver)
            person.get_check_bell()
            person.check_no_article_notifications()

    class TestMajorArticle:

        def test_article_major_edit_base(self, driver):
            page_article_base = PersonValidation(driver)
            page_article_base.major_edit_base_article(DataParser.get_url_from_data_file())

        def test_close_third_comment(self, driver):
            Comments.close_third_comment(driver, DataParser.get_url_from_data_file())

        def test_major_edit_article_history_person1(self, driver):
            person = Person1(driver)
            person.get_check_history()

        def test_major_edit_article_bell_person1(self, driver):
            person = Person1(driver)
            person.get_check_bell()

        def test_major_edit_article_history_person2(self, driver):
            person = Person2(driver)
            person.get_check_history()
            # person.history_third_solve_comment_check()
            person.go_to_major_edit_article_from_history()
            person.check_open_valid_article()

        def test_major_edit_article_bell_person2(self, driver):
            person = Person2(driver)
            person.get_check_bell()
            person.go_to_major_edit_article_from_history()
            person.check_open_valid_article()

        def test_major_edit_article_bell_person3(self, driver):
            person = Person3(driver)
            person.get_check_bell()
            person.go_to_major_edit_article_from_history()
            person.check_open_valid_article()
            person.check_article_bottom_banner()
            person.bottom_banner_button_click()

        def test_new_article_article_bell_person4(self, driver):
            person = Person4(driver)
            person.get_check_bell()
            person.check_no_article_notifications()

    class TestDeleteArticle:
        def test_article_delete_base(self, driver):
            page_article_base = PersonValidation(driver)
            page_article_base.delete_base_article(DataParser.get_url_from_data_file())

        def test_delete_article_history_person1(self, driver):
            person = Person1(driver)
            person.get_check_history()

        def test_delete_article_bell_person1(self, driver):
            person = Person1(driver)
            person.get_check_bell()

        def test_delete_article_history_person2(self, driver):
            person = Person2(driver)
            person.get_check_history()
            person.go_to_deleted_article_from_history()
            person.check_open_valid_article()
            person.check_article_bottom_banner()
            person.check_restore_button()

        def test_delete_article_bell_person2(self, driver):
            person = Person2(driver)
            person.get_check_bell()
            person.go_to_deleted_article_from_history()
            person.check_open_valid_article()
            person.check_article_bottom_banner()
            person.check_restore_button()

        def test_delete_article_bell_person3(self, driver):
            person = Person3(driver)
            person.get_check_bell()
            person.go_to_deleted_article_from_history()
            person.check_open_valid_article()
            person.check_article_bottom_banner()
            person.check_restore_button()

        def test_delete_article_bell_person4(self, driver):
            person = Person4(driver)
            person.get_check_bell()
            person.check_no_article_notifications()

    # class TestRestoreArticle:
    #     def test_article_delete_base(self, driver):
    #         page_article_base = PersonValidation(driver)
    #         page_article_base.delete_base_article(DataParser.get_url_from_data_file())
    #
    #     def test_delete_article_history_person2(self, driver):
    #         person = Person2(driver)
    #         person.get_check_history()
    #         person.go_to_deleted_article_from_history()
    #         person.check_open_valid_article()
    #         person.check_article_bottom_banner()
    #         person.check_restore_button()

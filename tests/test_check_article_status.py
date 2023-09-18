import allure
import pytest
import random
from pages.create_article_and_comments import Comments
from pages.person_validation import Person1, Person2, Person3, Person4, PersonValidation
from pages.users import morty

user_for_test = morty


@allure.suite(
    'Тесты по созданию, редактированию, удалению, восстановлению обычной статьи и отслеживание изменений в истории и '
    'колокольчике')
@pytest.mark.order(7)
class TestCheckNewArticleStatus:
    # TODO: решить проблему с проверкой комментариев в истории и колокольчике
    LINK = ''

    @allure.feature('Создание новой статьи, наполнение тестовыми комментами, проверка в истории и колокольчике')
    class TestNewArticle:
        @allure.title('Создание новой статьи')
        def test_article_create_base(self, driver):
            page_article_base = PersonValidation(driver)
            page_article_base.creating_base_article(user_for_test)
            TestCheckNewArticleStatus.LINK = page_article_base.LINK

        @allure.title('Создание тестового набора комментов')
        def test_create_comments(self, driver):
            page = Comments(driver)
            page.get_authorisation_in_url(TestCheckNewArticleStatus.LINK, user_for_test)
            page.create_comments()

        @allure.title('Закрытие первого тестового комментария')
        def test_close_first_comment(self, driver):
            page = Comments(driver)
            page.get_authorisation_in_url(TestCheckNewArticleStatus.LINK, user_for_test)
            page.close_first_comment()

        @allure.title('Новая статья. Проверка истории пользователем без доступом к статье')
        def test_new_article_history_person1(self, driver):
            person = Person1(driver)
            person.get_check_history()
            person.check_no_article_notifications_and_history_1()

        @allure.title('Новая статья. Проверка колокольчика пользователем без доступом к статье')
        def test_new_article_bell_person1(self, driver):
            person = Person1(driver)
            person.get_check_bell()
            person.check_no_article_notifications_and_history_2()

        @allure.title('Новая статья. Проверка истории пользователем с полным доступом к статье')
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

        @allure.title('Новая статья. Проверка колокольчика пользователем с полным доступом к статье')
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

        @allure.title('Новая статья. Проверка колокольчика пользователем с подтверждением прочтения')
        def test_new_article_bell_person3(self, driver):
            person = Person3(driver)
            person.get_check_bell()
            # person.bell_gray_comment_check()
            # person.bell_first_comment_check()
            person.go_to_new_article_from_history_or_bell()
            person.check_open_valid_article()
            person.check_article_bottom_banner()
            person.bottom_banner_button_click()

        @allure.title(
            'Новая статья. Проверка колокольчика пользователем с доступом к статье но с выключенными уведомлениями')
        def test_new_article_bell_person4(self, driver):
            person = Person4(driver)
            person.get_check_bell()
            person.check_no_article_notifications_and_history_1()
            # person.bell_gray_comment_check()
            # person.bell_first_comment_check()

    @allure.feature('Минорное редактирование статьи, проверка в истории и колокольчике')
    class TestMinorArticle:
        @allure.title('Минорное редактирование статьи')
        def test_article_minor_edit_base(self, driver):
            page_article_base = PersonValidation(driver)
            page_article_base.minor_edit_base_article(TestCheckNewArticleStatus.LINK, user_for_test)

        @allure.title('Закрытие второго тестового комментария')
        def test_close_second_comment(self, driver):
            page = Comments(driver)
            page.get_authorisation_in_url(TestCheckNewArticleStatus.LINK, user_for_test)
            page.close_second_comment()

        @allure.title('Минорное редактирование. Проверка истории пользователем без доступом к статье')
        def test_minor_edit_article_history_person1(self, driver):
            person = Person1(driver)
            person.get_check_history()
            person.check_no_article_notifications_and_history_2()

        @allure.title('Минорное редактирование. Проверка колокольчика пользователем без доступом к статье')
        def test_minor_edit_article_bell_person1(self, driver):
            person = Person1(driver)
            person.get_check_bell()
            person.check_no_article_notifications_and_history_2()

        @allure.title('Минорное редактирование. Проверка истории пользователем с полным доступом к статье')
        def test_minor_edit_article_history_person2(self, driver):
            person = Person2(driver)
            person.get_check_history()
            # person.history_second_solve_comment_check()
            person.check_no_article_notifications_and_history_2()

        @allure.title('Минорное редактирование. Проверка колокольчика пользователем с полным доступом к статье')
        def test_minor_edit_article_bell_person2(self, driver):
            person = Person2(driver)
            person.get_check_bell()
            # person.bell_second_comment_check()
            person.check_no_article_notifications_and_history_2()

        @allure.title('Минорное редактирование. Проверка колокольчика пользователем с подтверждением прочтения')
        def test_minor_edit_article_bell_person3(self, driver):
            person = Person3(driver)
            person.get_check_bell()
            # person.bell_second_comment_check()
            person.check_no_article_notifications_and_history_2()

        @allure.title(
            'Минорное редактирование. Проверка колокольчика пользователем с доступом к статье но с выключенными '
            'уведомлениями')
        def test_minor_edit_article_bell_person4(self, driver):
            person = Person4(driver)
            person.get_check_bell()
            # person.bell_second_comment_check()
            person.check_no_article_notifications_and_history_2()

    #
    @allure.feature('Мажорное редактирование статьи, проверка в истории и колокольчике')
    class TestMajorArticle:

        @allure.title('Мажорное редактирование статьи')
        def test_article_major_edit_base(self, driver):
            page_article_base = PersonValidation(driver)
            page_article_base.major_edit_base_article(TestCheckNewArticleStatus.LINK, user_for_test)

        @allure.title('Закрытие третьего тестового комментария')
        def test_close_third_comment(self, driver):
            page = Comments(driver)
            page.get_authorisation_in_url(TestCheckNewArticleStatus.LINK, user_for_test)
            page.close_third_comment()

        @allure.title('Мажорное редактирование. Проверка истории пользователем без доступом к статье')
        def test_major_edit_article_history_person1(self, driver):
            person = Person1(driver)
            person.get_check_history()
            person.check_no_article_notifications_and_history_2()

        @allure.title('Мажорное редактирование. Проверка колокольчика пользователем без доступом к статье')
        def test_major_edit_article_bell_person1(self, driver):
            person = Person1(driver)
            person.get_check_bell()
            person.check_no_article_notifications_and_history_2()

        @allure.title('Мажорное редактирование. Проверка истории пользователем с полным доступом к статье')
        def test_major_edit_article_history_person2(self, driver):
            person = Person2(driver)
            person.get_check_history()
            # person.history_third_solve_comment_check()
            person.go_to_major_edit_article_from_history_or_bell()
            person.check_open_valid_article()

        @allure.title('Мажорное редактирование. Проверка колокольчика пользователем с полным доступом к статье')
        def test_major_edit_article_bell_person2(self, driver):
            person = Person2(driver)
            person.get_check_bell()
            # person.bell_third_comment_check()
            person.go_to_major_edit_article_from_history_or_bell()
            person.check_open_valid_article()

        @allure.title('Мажорное редактирование. Проверка колокольчика пользователем с подтверждением прочтения')
        def test_major_edit_article_bell_person3(self, driver):
            person = Person3(driver)
            person.get_check_bell()
            # person.bell_third_comment_check()
            person.go_to_major_edit_article_from_history_or_bell()
            person.check_open_valid_article()
            person.check_article_bottom_banner()
            person.bottom_banner_button_click()

        @allure.title(
            'Мажорное редактирование. Проверка колокольчика пользователем с доступом к статье но с выключенными '
            'уведомлениями')
        def test_major_article_article_bell_person4(self, driver):
            person = Person4(driver)
            person.get_check_bell()
            # person.bell_third_comment_check()
            person.check_no_article_notifications_and_history_2()

    @allure.feature('Удаление статьи, проверка в истории и колокольчике')
    class TestDeleteArticle:
        @allure.title('Удаление статьи')
        def test_article_delete_base(self, driver):
            page_article_base = PersonValidation(driver)
            page_article_base.delete_base_article(TestCheckNewArticleStatus.LINK, user_for_test)

        @allure.title('Удаление. Проверка истории пользователем без доступом к статье')
        def test_delete_article_history_person1(self, driver):
            person = Person1(driver)
            person.get_check_history()
            person.check_no_article_notifications_and_history_3()

        @allure.title('Удаление. Проверка колокольчика пользователем без доступом к статье')
        def test_delete_article_bell_person1(self, driver):
            person = Person1(driver)
            person.get_check_bell()
            person.check_no_article_notifications_and_history_3()

        @allure.title('Удаление. Проверка истории пользователем с полным доступом к статье')
        def test_delete_article_history_person2(self, driver):
            person = Person2(driver)
            person.get_check_history()
            person.go_to_deleted_article_from_history_or_bell()
            person.check_open_valid_article()
            person.check_article_bottom_banner()
            person.check_restore_button()

        @allure.title('Удаление. Проверка колокольчика пользователем с полным доступом к статье')
        def test_delete_article_bell_person2(self, driver):
            person = Person2(driver)
            person.get_check_bell()
            person.go_to_deleted_article_from_history_or_bell()
            person.check_open_valid_article()
            person.check_article_bottom_banner()
            person.check_restore_button()

        @allure.title('Удаление. Проверка колокольчика пользователем с подтверждением прочтения')
        def test_delete_article_bell_person3(self, driver):
            person = Person3(driver)
            person.get_check_bell()
            person.go_to_deleted_article_from_history_or_bell()
            person.check_open_valid_article()
            person.check_article_bottom_banner()
            person.check_restore_button()

        @allure.title(
            'Удаление. Проверка колокольчика пользователем с доступом к статье но с выключенными уведомлениями')
        def test_delete_article_bell_person4(self, driver):
            person = Person4(driver)
            person.get_check_bell()
            person.check_no_article_notifications_and_history_3()

    @allure.feature('Восстановление статьи, проверка в истории и колокольчике')
    class TestRestoreArticle:
        @allure.title('Восстановление статьи')
        def test_article_restore_base(self, driver):
            page_article_base = PersonValidation(driver)
            page_article_base.restore_base_article(TestCheckNewArticleStatus.LINK, user_for_test)

        @allure.title('Восстановление. Проверка истории пользователем без доступом к статье')
        def test_restore_article_history_person1(self, driver):
            person = Person1(driver)
            person.get_check_history()
            person.check_no_article_notifications_and_history_4()

        @allure.title('Восстановление. Проверка колокольчика пользователем без доступом к статье')
        def test_restore_article_bell_person1(self, driver):
            person = Person1(driver)
            person.get_check_bell()
            person.check_no_article_notifications_and_history_4()

        @allure.title('Восстановление. Проверка истории пользователем с полным доступом к статье')
        def test_restore_article_history_person2(self, driver):
            person = Person2(driver)
            person.get_check_history()
            person.go_to_restored_article_from_history_or_bell()
            person.check_open_valid_article()

        @allure.title('Восстановление. Проверка истории колокольчика с полным доступом к статье')
        def test_restore_article_bell_person2(self, driver):
            person = Person2(driver)
            person.get_check_bell()
            person.go_to_restored_article_from_history_or_bell()
            person.check_open_valid_article()

        @allure.title('Восстановление. Проверка колокольчика пользователем с подтверждением прочтения')
        def test_restore_article_bell_person3(self, driver):
            person = Person3(driver)
            person.get_check_bell()
            person.go_to_restored_article_from_history_or_bell()
            person.check_open_valid_article()
            person.check_article_bottom_banner()
            person.bottom_banner_button_click()

        @allure.title(
            'Восстановление. Проверка колокольчика пользователем с доступом к статье но с выключенными уведомлениями')
        def test_restore_article_bell_person4(self, driver):
            person = Person4(driver)
            person.get_check_bell()
            person.check_no_article_notifications_and_history_4()

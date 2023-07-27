import time

import pytest
from pages.create_article_and_comments import BaseArticleEditor, Comments, DataParser
from pages.person_validation import Person1, Person2, Person3, Person4


@pytest.mark.order(7)
class TestCheckNewArticleStatus:

    class TestNewArticle:
        def test_article_create_base(self, driver):
            page_article_base = BaseArticleEditor(driver)
            page_article_base.creating_base_article()

        def test_create_comments(self, driver):
            Comments.create_comments(driver, DataParser.get_url_from_data_file())

        def test_close_first_comment(self, driver):
            Comments.close_first_comment(driver, DataParser.get_url_from_data_file())

        # def test_new_article_history_person1(self, driver):
        #     person = Person1(driver)
        #     person.get_check_history()
        #
        # def test_new_article_bell_person1(self, driver):
        #     person = Person1(driver)
        #     person.get_check_bell()

        # def test_new_article_history_person2(self, driver):
        #     person = Person2(driver)
        #     person.get_check_history()
        #     person.new_article_history_check()
        #     person.go_to_new_article_from_history()
        #     person.check_open_valid_article()

        # def test_new_article_bell_person2(self, driver):
        #     person = Person2(driver)
        #     person.get_check_bell()
        #
        # def test_new_article_bell_person3(self, driver):
        #     person = Person3(driver)
        #     person.get_check_bell()
        #
        # def test_new_article_bell_person4(self, driver):
        #     person = Person4(driver)
        #     person.get_check_bell()

    #не влияет на историю и колокольчик
    class TestMinorArticle:

        def test_article_minor_edit_base(self, driver):
            page_article_base = BaseArticleEditor(driver)
            page_article_base.minor_edit_base_article(DataParser.get_url_from_data_file())

        def test_close_second_comment(self, driver):
            Comments.close_second_comment(driver, DataParser.get_url_from_data_file())

        # def test_new_article_history_person1(self, driver):
        #     person = Person1(driver)
        #     person.get_check_history()
        #
        # def test_new_article_bell_person1(self, driver):
        #     person = Person1(driver)
        #     person.get_check_bell()

        # def test_minor_edit_article_history_person2(self, driver):
        #     person = Person2(driver)
        #     person.get_check_history()
        #     person.minor_edit_article_history_check()
        #
        #
        #
        # def test_new_article_bell_person2(self, driver):
        #     person = Person2(driver)
        #     person.get_check_bell()
        #
        # def test_new_article_bell_person3(self, driver):
        #     person = Person3(driver)
        #     person.get_check_bell()

        # def test_new_article_bell_person4(self, driver):
        #     person = Person4(driver)
        #     person.get_check_bell()

    class TestMajorArticle:

        def test_article_major_edit_base(self, driver):
            page_article_base = BaseArticleEditor(driver)
            page_article_base.major_edit_base_article(DataParser.get_url_from_data_file())

        def test_close_third_comment(self, driver):
            Comments.close_third_comment(driver, DataParser.get_url_from_data_file())

        # def test_new_article_history_person1(self, driver):
        #     person = Person1(driver)
        #     person.get_check_history()
        #
        # def test_new_article_bell_person1(self, driver):
        #     person = Person1(driver)
        #     person.get_check_bell()

        # def test_major_edit_article_history_person2(self, driver):
        #     person = Person2(driver)
        #     person.get_check_history()
        #     # person.major_edit_article_history_check()

        # def test_new_article_bell_person2(self, driver):
        #     person = Person2(driver)
        #     person.get_check_bell()
        #
        # def test_new_article_bell_person3(self, driver):
        #     person = Person3(driver)
        #     person.get_check_bell()
        #
        # def test_new_article_bell_person4(self, driver):
        #     person = Person4(driver)
        #     person.get_check_bell()

    class TestDeleteArticle:
        def test_article_delete_base(self, driver):
            page_article_base = BaseArticleEditor(driver)
            page_article_base.delete_base_article(DataParser.get_url_from_data_file())

        # def test_delete_article_history_person2(self, driver):
        #     person = Person2(driver)
        #     person.get_check_history()
        #     # person.major_edit_article_history_check()
        #     person.go_to_delete_article_from_history()
        #     person.check_open_valid_article()

import time

import pytest
from pages.create_article_and_comments import BaseArticleEditor, Comments, DataParser
from pages.person_validation import Person1, Person2, Person3, Person4
from pages.users import admin


@pytest.mark.order(7)
class TestCheckArticleStatus:

    # def test_article_create_base(self, driver):
    #     page_article_base = BaseArticleEditor(driver)
    #     page_article_base.creating_base_article(admin)
    #
    # def test_create_comments(self, driver):
    #     Comments.create_comments(driver, DataParser.get_url_from_data_file(), admin)
    #
    # def test_close_comment(self, driver):
    #     Comments.close_first_comment(driver, DataParser.get_url_from_data_file(), admin)

    # def test_new_article_history_person1(self, driver):
    #     person = Person1(driver)
    #     person.get_check_history()

    # def test_new_article_bell_person1(self, driver):
    #     person = Person1(driver)
    #     person.get_check_bell()

    def test_new_article_history_person2(self, driver):
        person = Person2(driver)
        person.get_check_history()
        person.new_article_history_check()
        person.go_to_article_from_history()
        person.check_open_valid_article()

    # def test_new_article_bell_person2(self, driver):
    #     person = Person2(driver)
    #     person.get_check_bell()

    def test_new_article_history_person3(self, driver):
        person = Person3(driver)
        person.get_check_history()
        person.new_article_history_check()
        person.go_to_article_from_history()
        person.check_open_valid_article()

    # def test_new_article_bell_person3(self, driver):
    #     person = Person3(driver)
    #     person.get_check_bell()

    def test_new_article_history_person4(self, driver):
        person = Person4(driver)
        person.get_check_history()
        person.new_article_history_check()
        person.go_to_article_from_history()
        person.check_open_valid_article()

    # def test_new_article_bell_person4(self, driver):
    #     person = Person4(driver)
    #     person.get_check_bell()

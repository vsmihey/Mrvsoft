import pytest
from pages.create_article_and_comments import BaseArticleEditor, Comments, DataParser
from pages.person_validation import Person1, Person2

@pytest.mark.order(7)
class TestCheckArticleStatus:

    def test_article_create_base(self, driver):
        page_article_base = BaseArticleEditor(driver)
        page_article_base.creating_base_article()

    def test_create_comments(self, driver):
        Comments.create_comments(driver, DataParser.get_url_from_data_file())

    def test_close_comment(self, driver):
        Comments.close_first_comment(driver, DataParser.get_url_from_data_file())

    def test_new_article_history_person1(self, driver):
        person = Person1(driver)
        person.get_check_history()

    def test_new_article_bell_person1(self, driver):
        person = Person1(driver)
        person.get_check_bell()

    def test_new_article_history_person2(self, driver):
        person = Person2(driver)
        person.get_check_history()

    def test_new_article_bell_person2(self, driver):
        person = Person2(driver)
        person.get_check_bell()














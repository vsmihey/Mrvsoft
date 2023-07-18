import pytest
from pages.create_article_and_comments import BaseArticleEditor, Comments


@pytest.mark.order(7)
class TestCheckArticleStatus:

    def test_article_create_base(self, driver):
        page_article_base = BaseArticleEditor(driver)
        page_article_base.creating_base_article()

    def test_create_comments(self, driver):
        Comments.create_comments(driver, BaseArticleEditor.get_url_from_data_file())

    def test_close_comment(self, driver):
        Comments.close_first_comment(driver, BaseArticleEditor.get_url_from_data_file())












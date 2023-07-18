import pytest
from pages.create_article_and_comments import BaseArticleEditor, Comments


@pytest.mark.order(7)
class TestCheckArticleStatus:

    def test_article_create_base(self, driver):
        page_article_base = BaseArticleEditor(driver)
        page_article_base.creating_base_article()











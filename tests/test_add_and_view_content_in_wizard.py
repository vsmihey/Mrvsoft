import pytest
from conftest import driver
from pages.add_and_view_content_in_wizard_page import AddViewContentWizard
from pages.checking_filter_changes_page import AddFilterChanges
from pages.data_login_password import url
from pages.repeat_function import RepeatFunction


@pytest.mark.order(5)
class TestAddViewContentWizard:

    def test_add_view_article(self, driver):
        add_view_content_page = AddViewContentWizard(driver, url)
        add_view_content_page.open()
        add_view_content_page.check_article()





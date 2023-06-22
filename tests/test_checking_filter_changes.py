import pytest
from pages.data_login_password import *
from pages.checking_filter_changes_page import AddFilterChanges


@pytest.mark.order(4)
class TestCheckingFilterChanges:

    class TestAddFilterChanges:

        def test_add_filters_changes(self, driver):
            checking_filters_changes_page = AddFilterChanges(driver, url)
            checking_filters_changes_page.open()
            checking_filters_changes_page.add_filters_mass_change()

        def test_check_mass_change_filters(self, driver):
            checking_filters_changes_page = AddFilterChanges(driver, url)
            checking_filters_changes_page.open()
            checking_filters_changes_page.check_mass_change_filters_article()





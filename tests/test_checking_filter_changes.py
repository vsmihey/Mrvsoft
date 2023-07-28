import allure
import pytest
from pages.data_login_password import *
from pages.checking_filter_changes_page import AddFilterChanges


@pytest.mark.order(4)
class TestCheckingFilterChanges:

    class TestAddFilterChanges:

        # @allure.title("Проверка изменения фильтров через массовые изменения")
        def test_add_filters_changes(self, driver):
            checking_filters_changes_page = AddFilterChanges(driver)
            # checking_filters_changes_page.open()
            checking_filters_changes_page.get_authorisation_in_selen()
            checking_filters_changes_page.add_filters_mass_change()

        def test_check_mass_change_filters_article(self, driver):
            checking_filters_changes_page = AddFilterChanges(driver)
            # checking_filters_changes_page.open()
            checking_filters_changes_page.get_authorisation_in_selen()
            checking_filters_changes_page.check_mass_change_filters_article(driver)
            # checking_filters_changes_page.open()
            # checking_filters_changes_page.delete_all_filters(driver)

        def test_check_mass_change_filters_template(self, driver):
            checking_filters_changes_page = AddFilterChanges(driver)
            # checking_filters_changes_page.open()
            checking_filters_changes_page.get_authorisation_in_selen()
            checking_filters_changes_page.check_mass_change_filters_template(driver)

        def test_check_mass_change_filters_script(self, driver):
            checking_filters_changes_page = AddFilterChanges(driver)
            # checking_filters_changes_page.open()
            checking_filters_changes_page.get_authorisation_in_selen()
            checking_filters_changes_page.check_mass_change_filters_script(driver)
            checking_filters_changes_page.open()
            # checking_filters_changes_page.delete_all_filters(driver)













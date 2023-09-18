import allure
import pytest
from conftest import driver
from pages.reports_page import ReportsPage
from pages.users import ricksanchez

user_for_test = ricksanchez


@allure.suite("Получение писем на почту об отчетах")
@pytest.mark.order(10)
class TestReports:

    @pytest.mark.skip('Скачивание отчетов')
    @allure.suite("Скачивание отчетов")
    def test_reports(self, driver):
        report_page = ReportsPage(driver)
        report_page.get_authorisation_in_selen(user_for_test)
        report_page.reports_click()
        report_page.shadow_element(driver)
        # report_page.check_iframe_ticket(driver)
        # report_page.check_iframe_search(driver)

    # @allure.suite("Скачивание отчетов в обучении")
    # def test_reports_learning(self):
    #     pass
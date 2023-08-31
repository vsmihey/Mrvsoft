import time

from pages.authorisation_page import Authorisation
import locators.all_locators as locators
from pages.base_page import BasePage
from pages.menu_navigation import MenuNavigation


class ReportsPage(Authorisation, MenuNavigation, BasePage):

    def download_reports(self, driver):
        """Клик по кнопке Отчеты"""
        self.reports_click()
        reports_by_content_list = self.element_is_visible(locators.Reports.REPORTS_BY_CONTENT_LIST)
        ddwn_rep_btn = self.elements_is_present(locators.Reports.DOWNLOAD_REPORTS_BUTTON_1)
        time.sleep(10)
        agree_button = self.expand_shadow_element(ddwn_rep_btn)
        # time.sleep(10)
        # agree_button = self.browser.execute_script('return arguments[0].shadowRoot.querySelector("button")', ddwn_rep_btn)
        # shadow_root = driver.execute_script("return document.querySelector('ddwn_rep_btn').shadowRoot")
        agree_button.click()



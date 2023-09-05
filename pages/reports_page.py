import time

from pages.authorisation_page import Authorisation
import locators.all_locators as locators
from pages.base_page import BasePage
from pages.menu_navigation import MenuNavigation


class ReportsPage(Authorisation, MenuNavigation, BasePage):

    def download_reports(self, driver):
        """Клик по кнопке Отчеты"""
        self.reports_click()
        root1 = self.element_is_visible(locators.Reports.SHADOW_1)
        self.expand_shadow_element(root1)

        root2 = self.element_is_visible(locators.Reports.SHADOW_2)
        self.expand_shadow_element(root2)

        root3 = self.element_is_visible(locators.Reports.SHADOW_3)
        self.expand_shadow_element(root3)

        root4 = self.element_is_visible(locators.Reports.SHADOW_4)
        self.expand_shadow_element(root4)

        self.click_to_element(locators.Reports.TARGET_ELEMENT_SHADOW)



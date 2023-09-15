import time
from pages.base_class import *
from pages.authorisation_page import Authorisation
import locators.all_locators as locators
from pages.base_page import BasePage
from pages.menu_navigation import MenuNavigation


class ReportsPage(Authorisation, MenuNavigation, BasePage):

    # def list_report_by_content(self, driver):
    #     i = 0
    #     list_reports = self.elements_are_visible(locators.Reports.REPORTS_BY_CONTENT_LIST)
    #     iframe_ticket = self.element_is_visible_all(locators.Reports.IFRAME_TICKET)
    #     iframe_search = self.element_is_visible_all(locators.Reports.IFRAME_SEARCH)
    #     iframe_useful = self.element_is_visible_all(locators.Reports.IFRAME_USEFUL)
    #     iframe_article_view = self.element_is_visible_all(locators.Reports.IFRAME_ARTICLE_VIEW)
    #     iframe_notification = self.element_is_visible_all(locators.Reports.IFRAME_NOTIFICATION)
    #     iframe_integration = self.element_is_visible_all(locators.Reports.IFRAME_INTEGRATION)
    #     # for n in list_reports:
    #     #     if i == 5:
    #     #         break
    #     #     else:
    #     #         n.click()
    #     #         time.sleep(3)
    #     #         for iframe_locator in iframe_locators:
    #     #             # if i == 5:
    #     #             #     break
    #     #             # else:
    #     #             #     n.click()
    #     #             time.sleep(3)
    #     #             self.download_reports(driver, iframe_locator)
    #     #             i += 1
    #
    # # list_reports = locators.Reports.REPORTS_BY_CONTENT_LIST

    # iframe_ticket = locators.Reports.IFRAME_TICKET
    # iframe_search = locators.Reports.IFRAME_SEARCH
    iframe_useful = locators.Reports.IFRAME_USEFUL
    iframe_article_view = locators.Reports.IFRAME_ARTICLE_VIEW
    iframe_notification = locators.Reports.IFRAME_NOTIFICATION
    iframe_integration = locators.Reports.IFRAME_INTEGRATION

    def download_reports(self, driver, iframe_locator):
        """Клик по кнопке Скачать отчеты"""
        # self.reports_click()
        time.sleep(2)
        # iframe = iframe_locator
        iframe = self.element_is_visible_all(iframe_locator)
        self.switch_to_frame(iframe)
        actions = ActionChains(driver)
        time.sleep(1)
        actions.move_by_offset(1692, 92).click().perform()
        self.switch_out_frame()
        send_report = self.element_is_visible_all(locators.Reports.CHECK_TEXT_SEND_REPORT).text
        assert send_report == "Отправка отчёта"
        assert self.element_is_visible(locators.Reports.CHECK_TEXT_SEND_EMAIL).text == "Ссылка на скачивание отчёта будет отправлена на email"
        assert self.element_is_visible(locators.Reports.BUTTON_ACCEPT).text == "понятно"
        self.click_to_element(locators.Reports.BUTTON_ACCEPT)
        time.sleep(1)

    def check_iframe_ticket(self, driver):
        iframe_ticket = locators.Reports.IFRAME_TICKET
        self.click_to_element(locators.Reports.IFRAME_TICKET)
        time.sleep(5)
        self.download_reports(driver, iframe_locator=iframe_ticket)
        self.browser.refresh()

    def check_iframe_search(self, driver):
        # self.browser.refresh()
        iframe_search = locators.Reports.IFRAME_SEARCH
        self.click_to_element(locators.Reports.BUTTON_SEARCH)
        time.sleep(5)
        self.download_reports(driver, iframe_locator=iframe_search)

    def shadow_element(self):
        iframe_ticket = locators.Reports.IFRAME_TICKET
        iframe = self.element_is_visible_all(iframe_ticket)
        self.switch_to_frame(iframe)
        self.click_to_element(locators.Reports.BUTTON_DOWNLOAD_REPORT)

    def dom_element(self):   # Находим элементы, которые содержат Shadow DOM на каждом уровне
        iframe_ticket = locators.Reports.IFRAME_TICKET
        iframe = self.element_is_visible_all(iframe_ticket)
        self.switch_to_frame(iframe)
        outer_element_level1 = self.element_is_visible(locators.Reports.SHADOW_1)
        outer_element_level2 = self.browser.execute_script("return arguments[0].shadowRoot;", outer_element_level1)
        # outer_element_level3 = self.browser.execute_script("return arguments[0].shadowRoot;", outer_element_level2)

        # Теперь мы можем получить доступ к элементу Shadow DOM на уровне 4
        # inner_button = driver.execute_script("return arguments[0].shadowRoot.querySelector('#inner-button');", outer_element_level3)

        # Нажимаем на кнопку внутри Shadow DOM на уровне 4
        outer_element_level2.click()

import time
from undetected_chromedriver import WebElement
from pages.base_class import *
from pages.authorisation_page import Authorisation
import locators.all_locators as locators
from pages.base_page import BasePage
from pages.menu_navigation import MenuNavigation


class ReportsPage(Authorisation, MenuNavigation, BasePage):

    def list_report_by_content(self, driver):
        i = 0
        list_reports = self.elements_are_visible(locators.Reports.REPORTS_BY_CONTENT_LIST)
        for n in list_reports:
            if i == 5:
                break
            else:
                n.click()
                time.sleep(3)
                self.download_reports(driver)
                i += 1

    def download_reports(self, driver):
        """Клик по кнопке Отчеты"""
        # self.reports_click()
        time.sleep(2)
        iframe = self.element_is_visible_all(locators.Reports.IFRAME_FOR_SHADOW)
        self.switch_to_frame(iframe)
        actions = ActionChains(driver)
        actions.move_by_offset(1692, 92).click().perform()
        self.switch_out_frame()
        send_report = self.element_is_visible_all(locators.Reports.CHECK_TEXT_SEND_REPORT).text
        assert send_report == "Отправка отчёта"
        assert self.element_is_visible(locators.Reports.CHECK_TEXT_SEND_EMAIL).text == "Ссылка на скачивание отчёта будет отправлена на email"
        assert self.element_is_visible(locators.Reports.BUTTON_ACCEPT).text == "понятно"
        self.click_to_element(locators.Reports.BUTTON_ACCEPT)





        time.sleep(10)

        # search_button = driver.execute_script(
        #     'return document.querySelector(".around-padding").shadowRoot.querySelector("ticket-filters").shadowRoot.querySelector("vaadin-vertical-layout").shadowRoot.querySelector("div")')
        # search_button.click()
        # shadow_host = driver.find_element(By.CSS_SELECTOR, '#shadow_host')
        # shadow_root = shadow_host.shadow_root
        # shadow_content = shadow_root.find_element(By.CSS_SELECTOR, '#shadow_content')
        #
        # assert shadow_content.text == 'some text'

        # root1 = self.elements_is_present(locators.Reports.SHADOW_1)
        # shadow_root1 = self.expand_shadow_element(root1)
        #
        # root2 = self.elements_is_present(locators.Reports.SHADOW_2)
        # shadow_root2 = self.expand_shadow_element(root2)
        #
        # root3 = self.elements_is_present(locators.Reports.SHADOW_3)
        # shadow_root3 = self.expand_shadow_element(root3)
        #


        # shadow_root_dict = driver.execute_script('return arguments[0].shadowRoot', root3)
        # shadow_root_id = shadow_root_dict['shadow-6066-11e4-a52e-4f735466cecf']
        # shadow_root = WebElement(driver, shadow_root_id, w3c=True)

        # root4 = self.elements_is_present(locators.Reports.SHADOW_4)
        # self.expand_shadow_element(root4)

        # shadow_root = root3.shadow_root
        #
        # search_button = shadow_root.find_element(locators.Reports.SHADOW_BUTTON_EXPORT)
        # search_button.click()
        #
        # # self.click_to_element(locators.Reports.SHADOW_BUTTON_EXPORT)
        #
        # time.sleep(3)

        # self.click_to_element(locators.Reports.TARGET_ELEMENT_SHADOW)

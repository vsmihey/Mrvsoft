import pathlib
import random
import time
from pathlib import Path

from selenium.common import StaleElementReferenceException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys

from conftest import driver
from generator.generator import generated_person
from locators.locator_add_and_view_content_in_wizard import AddViewContentWizardLocators
from locators.locators_topic_database import CreateTopicDatabaseLocators
from pages import checking_filter_changes_page
from pages.base_page import BasePage
from pages.checking_filter_changes_page import AddFilterChanges
from pages.data_login_password import url
from pages.repeat_function import RepeatFunction


class AddViewContentWizard(BasePage):

    Locators = AddViewContentWizardLocators()

    # def create_article(self):
    #     # self.input_in_my_project(self.driver)
    #     first_name, name_request = self.create_article_base()

    def create_templates(self, driver):
        self.input_in_my_project(driver)
        name, name_content, name_of_templates, name_request = self.create_article_by_template_base(driver)

    def create_script(self):
        self.input_in_my_project(driver)
        name_request_script, name_script = self.create_script_base()

    def create_files(self):
        self.input_in_my_project(driver)
        path = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        self.add_files_base(path)



    def check_article(self):
        self.input_in_my_project(self.driver)
        actions = ActionChains(self.driver)
        first_name, name_request, text_alert = self.create_article_base()
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request)
        svg_tooltip_request_field = self.element_is_visible(self.Locators.SVG_TOOLTIP_REQUEST_FIELD)
        svg_tooltip_request_field_value = svg_tooltip_request_field.get_attribute("data-tip")
        # print(svg_tooltip_request_field_value)
        assert svg_tooltip_request_field_value == "Запросы позволяют закрепить контент вверху поисковой выдачи с пометкой “Закрепленный контент”"
        self.element_is_visible(self.Locators.BUTTON_ADD).click()
        """check radio request folder name article"""
        self.element_is_visible(self.Locators.RADIO_LINK_TO_CONTENT).is_displayed()
        check_request = self.element_is_visible(self.Locators.CHECK_REQUEST).text
        assert check_request == name_request
        self.element_is_visible(self.Locators.FOLDER_CONTENT).is_displayed()
        name_article = self.element_is_visible(self.Locators.NAME_ARTICLE).text
        assert name_article == first_name
        self.element_is_visible(self.Locators.BUTTON_FINISH_1).click()
        text_link_to_content = self.element_is_visible(self.Locators.TEXT_LINK_TO_CONTENT).text
        assert text_link_to_content == "Ссылка на контент"
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys(text_alert)
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        """search"""
        # try:
        #     self.element_is_visible(self.Locators.SEARCH).click()
        # except StaleElementReferenceException:
        #     time.sleep(3)
        #     self.element_is_visible(self.Locators.SEARCH).click()
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(name_request)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)
        check_search_result = self.element_is_visible(self.Locators.CHECK_SEARCH_RESULT).text
        print(check_search_result)
        assert check_search_result == first_name
        text_fixing_by_expert = self.element_is_visible(self.Locators.TEXT_FIXING_BY_EXPERT).text
        assert text_fixing_by_expert == "Закреплено экспертом"
        """check fixing content"""
        self.element_is_visible(self.Locators.CHANGE_FIXING_CONTENT).click()
        get_request_name = self.element_is_visible(self.Locators.INPUT_FIELD_NAME_REQUEST).get_attribute('value')
        assert get_request_name == name_request









        time.sleep(10)







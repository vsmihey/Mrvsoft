import pathlib
import random
import time
from pathlib import Path

from selenium.common import StaleElementReferenceException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from conftest import driver
from generator.generator import generated_person
from locators.locator_wizard_and_search_ru_en import AddViewContentWizardLocators, SearchRuEnLocators
from locators.locators_topic_database import CreateTopicDatabaseLocators
from pages import checking_filter_changes_page
from pages.base_page import BasePage
from pages.checking_filter_changes_page import AddFilterChanges
from pages.data_login_password import url, text_ru, text_en
from pages.repeat_function import RepeatFunction


class AddViewContentWizard(BasePage):

    Locators = AddViewContentWizardLocators()

    def create_files(self):
        self.input_in_my_project(driver)
        path = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        self.add_files_base(path)

    def add_more_requests(self):
        """CREATE REQUEST , insert range count of requests"""
        data_request = []
        to_get_name_request = self.element_is_visible(self.Locators.TO_GET_NAME_REQUEST).text
        for i in range(20):
            self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(
                "request " + str(random.randint(999, 9999)))
            self.element_is_visible(self.Locators.BUTTON_ADD_REQUEST).click()
            try:
                to_get_name_added_request = self.element_is_visible(self.Locators.TO_GET_NAME_ADDED_REQUEST).text
            except TimeoutException:
                time.sleep(3)
                to_get_name_added_request = self.element_is_visible(self.Locators.TO_GET_NAME_ADDED_REQUEST).text
            self.element_is_visible(self.Locators.BUTTON_FINISH_1).click()
            data_request.append(to_get_name_added_request)
        data_request.append(to_get_name_request)
        return data_request

    def check_article(self, driver):
        self.input_in_my_project(self.driver)
        first_name, name_request, text_alert = self.create_article_base()
        # self.implicitly_wait()
        # actions = ActionChains(self.driver)
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request)
        svg_tooltip_request_field = self.element_is_visible(self.Locators.SVG_TOOLTIP_REQUEST_FIELD)
        svg_tooltip_request_field_value = svg_tooltip_request_field.get_attribute("data-tip")
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
        time.sleep(3)
        actions = ActionChains(self.driver)
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(name_request)
        actions.send_keys(Keys.RETURN).perform()
        # actions.perform()
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
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOWS_CHECK).click()
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        """add more question"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{first_name}"]')
        search_by_name.click()
        self.element_is_visible(self.Locators.CHANGE_ARTICLE).click()
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        data_request = self.add_more_requests()
        # print(data_request)
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXT_ALERT_NAME).send_keys("alert")
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        try:
            self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        """check added request"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{first_name}"]')
        search_by_name.click()
        self.element_is_visible(self.Locators.CHANGE_ARTICLE).click()
        try:
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY, timeout=3).click()
        except TimeoutException:
            self.element_is_visible(self.Locators.BUTTON_CONTINUE_DRAFT).click()
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        list_added_request = self.elements_are_present(self.Locators.LIST_ADDED_REQUEST)
        data_added_requests = []
        for n in list_added_request:
            request_text = n.text
            data_added_requests.append(request_text)
        # data_added_requests.reverse()
        data_request_sort = sorted(data_request)
        data_added_requests_sort = sorted(data_added_requests)
        # print(data_request_sort, data_added_requests_sort)
        assert data_request_sort == data_added_requests_sort
        """check new search"""
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_REQUEST).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_ARTICLE).click()
        self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        i = random.randint(0, 20)
        name_request = data_request_sort[i]
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

    def check_template(self, driver):
        self.input_in_my_project(driver)
        name, name_content, name_of_templates, name_request = self.create_article_by_template_base(driver)
        print(name, name_content, name_of_templates, name_request)
        actions = ActionChains(self.driver)
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request)
        svg_tooltip_request_field = self.element_is_visible(self.Locators.SVG_TOOLTIP_REQUEST_FIELD)
        svg_tooltip_request_field_value = svg_tooltip_request_field.get_attribute("data-tip")
        assert svg_tooltip_request_field_value == "Запросы позволяют закрепить контент вверху поисковой выдачи с пометкой “Закрепленный контент”"
        self.element_is_visible(self.Locators.BUTTON_ADD).click()
        """check radio request folder name article"""
        self.element_is_visible(self.Locators.RADIO_LINK_TO_CONTENT).is_displayed()
        check_request = self.element_is_visible(self.Locators.CHECK_REQUEST).text
        assert check_request == name_request
        self.element_is_visible(self.Locators.FOLDER_CONTENT).is_displayed()
        name_article = self.element_is_visible(self.Locators.NAME_ARTICLE).text
        assert name_article == name_content
        self.element_is_visible(self.Locators.BUTTON_FINISH_1).click()
        text_link_to_content = self.element_is_visible(self.Locators.TEXT_LINK_TO_CONTENT).text
        assert text_link_to_content == "Ссылка на контент"
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("text_alert")
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        """search"""
        time.sleep(3)
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(name_request)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)
        check_search_result = self.element_is_visible(self.Locators.CHECK_SEARCH_RESULT).text
        print(check_search_result)
        assert check_search_result == name_content
        text_fixing_by_expert = self.element_is_visible(self.Locators.TEXT_FIXING_BY_EXPERT).text
        assert text_fixing_by_expert == "Закреплено экспертом"
        """check fixing content"""
        self.element_is_visible(self.Locators.CHANGE_FIXING_CONTENT).click()
        get_request_name = self.element_is_visible(self.Locators.INPUT_FIELD_NAME_REQUEST).get_attribute('value')
        assert get_request_name == name_request
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOWS_CHECK).click()
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        """add more question"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_content}"]')
        search_by_name.click()
        self.element_is_visible(self.Locators.CHANGE_ARTICLE).click()
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        try:
            data_request = self.add_more_requests()
        except TimeoutException:
            time.sleep(3)
            data_request = self.add_more_requests()
        # print(data_request)
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXT_ALERT_NAME).send_keys("alert")
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        try:
            self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        """check added request"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_content}"]')
        search_by_name.click()
        self.element_is_visible(self.Locators.CHANGE_ARTICLE).click()
        try:
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY, timeout=3).click()
        except TimeoutException:
            self.element_is_visible(self.Locators.BUTTON_CONTINUE_DRAFT).click()
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        list_added_request = self.elements_are_present(self.Locators.LIST_ADDED_REQUEST)
        data_added_requests = []
        for n in list_added_request:
            request_text = n.text
            data_added_requests.append(request_text)
        data_request_sort = sorted(data_request)
        data_added_requests_sort = sorted(data_added_requests)
        assert data_request_sort == data_added_requests_sort
        """check new search"""
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_REQUEST).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_ARTICLE_BY_TEMPLATE).click()
        self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        i = random.randint(0, 20)
        name_request = data_request_sort[i]
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(name_request)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)
        check_search_result = self.element_is_visible(self.Locators.CHECK_SEARCH_RESULT).text
        print(check_search_result)
        assert check_search_result == name_content
        text_fixing_by_expert = self.element_is_visible(self.Locators.TEXT_FIXING_BY_EXPERT).text
        assert text_fixing_by_expert == "Закреплено экспертом"

    def check_script(self, driver):
        self.input_in_my_project(driver)
        name_request_script, name_script = self.create_script_base()
        actions = ActionChains(self.driver)
        button_typography = self.elements_is_present(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        actions.click(button_typography).perform()
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request_script)
        svg_tooltip_request_field = self.element_is_visible(self.Locators.SVG_TOOLTIP_REQUEST_FIELD)
        svg_tooltip_request_field_value = svg_tooltip_request_field.get_attribute("data-tip")
        assert svg_tooltip_request_field_value == "Запросы позволяют закрепить контент вверху поисковой выдачи с пометкой “Закрепленный контент”"
        self.element_is_visible(self.Locators.BUTTON_ADD).click()
        """check radio request folder name article"""
        self.element_is_visible(self.Locators.RADIO_LINK_TO_CONTENT).is_displayed()
        check_request = self.element_is_visible(self.Locators.CHECK_REQUEST).text
        assert check_request == name_request_script
        self.element_is_visible(self.Locators.FOLDER_CONTENT).is_displayed()
        name_article = self.element_is_visible(self.Locators.NAME_ARTICLE).text
        assert name_article == name_script
        self.element_is_visible(self.Locators.BUTTON_FINISH_1).click()
        text_link_to_content = self.element_is_visible(self.Locators.TEXT_LINK_TO_CONTENT).text
        assert text_link_to_content == "Ссылка на контент"
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("text_alert")
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        """search"""
        time.sleep(3)
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(name_request_script)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)
        check_search_result = self.element_is_visible(self.Locators.CHECK_SEARCH_RESULT).text
        print(check_search_result)
        assert check_search_result == name_script
        text_fixing_by_expert = self.element_is_visible(self.Locators.TEXT_FIXING_BY_EXPERT).text
        assert text_fixing_by_expert == "Закреплено экспертом"
        """check fixing content"""
        self.element_is_visible(self.Locators.CHANGE_FIXING_CONTENT).click()
        get_request_name = self.element_is_visible(self.Locators.INPUT_FIELD_NAME_REQUEST).get_attribute('value')
        assert get_request_name == name_request_script
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOWS_CHECK).click()
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        """add more question"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_script}"]')
        search_by_name.click()
        self.element_is_visible(self.Locators.CHANGE_ARTICLE).click()
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        data_request = self.add_more_requests()
        # print(data_request)
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXT_ALERT_NAME).send_keys("alert")
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        try:
            self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        """check added request"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_script}"]')
        search_by_name.click()
        self.element_is_visible(self.Locators.CHANGE_ARTICLE).click()
        try:
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT, timeout=3).click()
        except TimeoutException:
            self.element_is_visible(self.Locators.BUTTON_CONTINUE_DRAFT).click()
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        list_added_request = self.elements_are_present(self.Locators.LIST_ADDED_REQUEST)
        data_added_requests = []
        for n in list_added_request:
            request_text = n.text
            data_added_requests.append(request_text)
        data_request_sort = sorted(data_request)
        data_added_requests_sort = sorted(data_added_requests)
        assert data_request_sort == data_added_requests_sort
        """check new search"""
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_REQUEST).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_EDIT_SCRIPT).click()
        self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        i = random.randint(0, 20)
        name_request = data_request_sort[i]
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(name_request)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)
        check_search_result = self.element_is_visible(self.Locators.CHECK_SEARCH_RESULT).text
        print(check_search_result)
        assert check_search_result == name_script
        text_fixing_by_expert = self.element_is_visible(self.Locators.TEXT_FIXING_BY_EXPERT).text
        assert text_fixing_by_expert == "Закреплено экспертом"

    def check_files(self, driver):
        self.input_in_my_project(driver)
        actions = ActionChains(driver)
        path = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        # name_script = "media.jpg"
        name_request_script = "reuest " + str(random.randint(999, 9999))
        name_script = self.add_files_base(path)
        self.element_is_visible(self.Locators.TYPOGRAPHY_TEMPLATE).click()
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request_script)
        svg_tooltip_request_field = self.element_is_visible(self.Locators.SVG_TOOLTIP_REQUEST_FIELD)
        svg_tooltip_request_field_value = svg_tooltip_request_field.get_attribute("data-tip")
        assert svg_tooltip_request_field_value == "Запросы позволяют закрепить контент вверху поисковой выдачи с пометкой “Закрепленный контент”"
        self.element_is_visible(self.Locators.BUTTON_ADD).click()
        """check radio request folder name article"""
        self.element_is_visible(self.Locators.RADIO_LINK_TO_CONTENT).is_displayed()
        check_request = self.element_is_visible(self.Locators.CHECK_REQUEST).text
        assert check_request == name_request_script
        self.element_is_visible(self.Locators.FOLDER_CONTENT).is_displayed()
        name_article = self.element_is_visible(self.Locators.FILES_NAME).text
        assert name_article == name_script
        self.element_is_visible(self.Locators.BUTTON_FINISH_1).click()
        text_link_to_content = self.element_is_visible(self.Locators.TEXT_LINK_TO_CONTENT).text
        assert text_link_to_content == "Ссылка на контент"
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("text_alert")
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        """search"""
        time.sleep(3)
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(name_request_script)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)
        check_search_result = self.element_is_visible(self.Locators.CHECK_SEARCH_RESULT).text
        print(check_search_result)
        assert check_search_result == name_script
        text_fixing_by_expert = self.element_is_visible(self.Locators.TEXT_FIXING_BY_EXPERT).text
        assert text_fixing_by_expert == "Закреплено экспертом"
        """check fixing content"""
        self.element_is_visible(self.Locators.CHANGE_FIXING_CONTENT).click()
        get_request_name = self.element_is_visible(self.Locators.INPUT_FIELD_NAME_REQUEST).get_attribute('value')
        assert get_request_name == name_request_script
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOWS_CHECK).click()
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        """add more question"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_script}"]')
        search_by_name.click()
        self.element_is_visible(self.Locators.CHANGE_ARTICLE).click()
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        data_request = self.add_more_requests()
        # print(data_request)
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXT_ALERT_NAME).send_keys("alert")
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        try:
            self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        """check added request"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_script}"]')
        search_by_name.click()
        self.element_is_visible(self.Locators.CHANGE_ARTICLE).click()
        try:
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT, timeout=3).click()
        except TimeoutException:
            self.element_is_visible(self.Locators.BUTTON_CONTINUE_DRAFT).click()
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        self.element_is_visible(self.Locators.BUTTON_BACK).click()
        list_added_request = self.elements_are_present(self.Locators.LIST_ADDED_REQUEST)
        data_added_requests = []
        for n in list_added_request:
            request_text = n.text
            data_added_requests.append(request_text)
        data_request_sort = sorted(data_request)
        data_added_requests_sort = sorted(data_added_requests)
        assert data_request_sort == data_added_requests_sort
        """check new search"""
        # time.sleep(1)
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_REQUEST).click()
        self.element_is_visible(self.Locators.CLOSE_WINDOW_FILES).click()
        self.element_is_visible(self.Locators.GO_TO_CONTENT).click()
        i = random.randint(0, 20)
        name_request = data_request_sort[i]
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(name_request)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)
        check_search_result = self.element_is_visible(self.Locators.CHECK_SEARCH_RESULT).text
        print(check_search_result)
        assert check_search_result == name_script
        text_fixing_by_expert = self.element_is_visible(self.Locators.TEXT_FIXING_BY_EXPERT).text
        assert text_fixing_by_expert == "Закреплено экспертом"


class SearchRuEn(BasePage):

    Locators = SearchRuEnLocators()

    def create_article_ru(self):
        self.input_in_my_project(self.driver)
        Locators = CreateTopicDatabaseLocators
        # person = generated_person()
        first_name_ru = "Статья " + str(random.randint(999, 9999))
        text_article_ru = text_ru
        """upload media"""
        try:
            self.element_is_visible(Locators.CREATE_BUTTON, timeout=5).click()
        except (StaleElementReferenceException, TimeoutException):
            time.sleep(3)
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        self.element_is_visible(Locators.CREATE_ARTICLE).click()
        """input name and text an folder direct"""
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys(first_name_ru)
        try:
            self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE, timeout=2).send_keys("Контент 1")
        except ElementNotInteractableException:
            time.sleep(2)
            self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")
        try:
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE, timeout=3).send_keys(text_article_ru)
        except TimeoutException:
            time.sleep(3)
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE).send_keys(text_article_ru)
        list_split_ru = text_article_ru.split()
        self.element_is_visible(Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(Locators.INPUT_TEXTAREA_FIELD).send_keys("text_alert")
        self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_ARTICLE_RU_EN).click()
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        return first_name_ru, text_article_ru, list_split_ru

    def create_article_en(self):
        self.input_in_my_project(self.driver)
        Locators = CreateTopicDatabaseLocators
        # person = generated_person()
        first_name_en = "Article " + str(random.randint(999, 9999))
        text_article_en = text_en
        """upload media"""
        try:
            self.element_is_visible(Locators.CREATE_BUTTON, timeout=5).click()
        except (StaleElementReferenceException, TimeoutException):
            time.sleep(3)
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        self.element_is_visible(Locators.CREATE_ARTICLE).click()
        """input name and text an folder direct"""
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys(first_name_en)
        try:
            self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE, timeout=2).send_keys("Контент 1")
        except ElementNotInteractableException:
            time.sleep(2)
            self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")
        try:
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE, timeout=3).send_keys(text_article_en)
        except TimeoutException:
            time.sleep(3)
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE).send_keys(text_article_en)
        list_split_en = text_article_en.split()
        self.element_is_visible(Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(Locators.INPUT_TEXTAREA_FIELD).send_keys("text_alert")
        self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_ARTICLE_RU_EN).click()
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        return first_name_en, text_article_en, list_split_en

    # def del_article_ru_en(self, driver):
    #     """del articles ru and en"""
    #     driver.implicitly_wait(3)
    #     self.input_in_my_project(driver)
    #     self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
    #     list_article_for_del = self.elements_are_present(self.Locators.LIST_ARTICLE_FOR_DEL)
    #     for n in list_article_for_del:
    #         try:
    #             n.click()
    #         except StaleElementReferenceException:
    #             time.sleep(2)
    #             n.click()
    #         self.element_is_visible(self.Locators.MEATBALL_ARTICLE).click()
    #         self.element_is_visible(self.Locators.SVG_DEL).click()
    #         self.element_is_visible(self.Locators.INPUT_ALERT_FOR_DEL).send_keys("Alert - delete")
    #         self.element_is_visible(self.Locators.BUTTON_EXECUTE).click()

    # def ddd(self, driver):
    #     first_name_ru = self.create_article_ru()
    #     self.del_article_ru_en(driver, name=first_name_ru)

















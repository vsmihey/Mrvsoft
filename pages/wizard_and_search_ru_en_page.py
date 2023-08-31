import pathlib
import random
import time
from pathlib import Path
from selenium.common import StaleElementReferenceException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from conftest import driver
from locators.locator_wizard_and_search_ru_en import AddViewContentWizardLocators, SearchRuEnLocators
from locators.locators_topic_database import CreateTopicDatabaseLocators
from pages.authorisation_page import Authorisation
from pages.base_page import BasePage
from pages.users import text_ru, text_en


class AddViewContentWizard(Authorisation, BasePage):

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
                "request " + str(random.randint(1111, 99999)))
            self.click_to_element(self.Locators.BUTTON_ADD_REQUEST)
            try:
                to_get_name_added_request = self.element_is_visible(self.Locators.TO_GET_NAME_ADDED_REQUEST).text
            except TimeoutException:
                time.sleep(3)
                to_get_name_added_request = self.element_is_visible(self.Locators.TO_GET_NAME_ADDED_REQUEST).text
            self.click_to_element(self.Locators.BUTTON_FINISH_1)
            data_request.append(to_get_name_added_request)
        data_request.append(to_get_name_request)
        return data_request

    def check_article(self, driver):
        # self.input_in_my_project(self.driver)
        first_name, name_request, text_alert = self.create_article_base()
        # self.implicitly_wait()
        # actions = ActionChains(self.driver)
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request)
        svg_tooltip_request_field = self.element_is_visible(self.Locators.SVG_TOOLTIP_REQUEST_FIELD)
        svg_tooltip_request_field_value = svg_tooltip_request_field.get_attribute("data-tip")
        assert svg_tooltip_request_field_value == "Запросы позволяют закрепить контент вверху поисковой выдачи с пометкой “Закрепленный контент”"
        self.click_to_element(self.Locators.BUTTON_ADD)
        """check radio request folder name article"""
        self.element_is_visible(self.Locators.RADIO_LINK_TO_CONTENT).is_displayed()
        check_request = self.element_is_visible(self.Locators.CHECK_REQUEST).text
        assert check_request == name_request
        self.element_is_visible(self.Locators.FOLDER_CONTENT).is_displayed()
        name_article = self.element_is_visible(self.Locators.NAME_ARTICLE).text
        assert name_article == first_name
        self.click_to_element(self.Locators.BUTTON_FINISH_1)
        text_link_to_content = self.element_is_visible(self.Locators.TEXT_LINK_TO_CONTENT).text
        assert text_link_to_content == "Ссылка на контент"
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys(text_alert)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
        """search"""
        time.sleep(3)
        actions = ActionChains(driver)
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(name_request)
        actions.send_keys(Keys.RETURN).perform()
        # actions.perform()
        time.sleep(1)
        try:
            check_search_result = self.element_is_visible(self.Locators.CHECK_SEARCH_RESULT).text
        except (TimeoutException, StaleElementReferenceException):
            time.sleep(3)
            check_search_result = self.element_is_visible(self.Locators.CHECK_SEARCH_RESULT).text
        print(check_search_result)
        assert check_search_result == first_name
        text_fixing_by_expert = self.element_is_visible(self.Locators.TEXT_FIXING_BY_EXPERT).text
        assert text_fixing_by_expert == "Закреплено экспертом"
        """check fixing content"""
        self.click_to_element(self.Locators.CHANGE_FIXING_CONTENT)
        get_request_name = self.element_is_visible(self.Locators.INPUT_FIELD_NAME_REQUEST).get_attribute('value')
        assert get_request_name == name_request
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOWS_CHECK)
        time.sleep(1)
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        """add more question"""
        time.sleep(2)
        try:
            search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{first_name}"]')
        except (NoSuchElementException, TimeoutException):
            time.sleep(5)
            search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{first_name}"]')
        search_by_name.click()
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        time.sleep(3)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        except TimeoutException:
            time.sleep(1)
            self.click_to_element(self.Locators.BUTTON_DELETE_DRAFT_WIZARD_SEARCH)
            try:
                self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
            except (TimeoutException, ElementClickInterceptedException, StaleElementReferenceException):
                time.sleep(5)
                self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_BACK)
        self.click_to_element(self.Locators.BUTTON_BACK)
        data_request = self.add_more_requests()
        # print(data_request)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXT_ALERT_NAME).send_keys("alert")
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        """check added request"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{first_name}"]')
        search_by_name.click()
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY, timeout=3)
        except TimeoutException:
            # self.click_to_element(self.Locators.BUTTON_CONTINUE_DRAFT)
            self.delete_draft()
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_BACK)
        self.click_to_element(self.Locators.BUTTON_BACK)
        time.sleep(1)
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
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_REQUEST)
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_ARTICLE)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
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
        # self.input_in_my_project(driver)
        name, name_content, name_request = self.create_article_by_template_base(driver)
        print(name, name_content, name_request)
        actions = ActionChains(driver)
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request)
        svg_tooltip_request_field = self.element_is_visible(self.Locators.SVG_TOOLTIP_REQUEST_FIELD)
        svg_tooltip_request_field_value = svg_tooltip_request_field.get_attribute("data-tip")
        assert svg_tooltip_request_field_value == "Запросы позволяют закрепить контент вверху поисковой выдачи с пометкой “Закрепленный контент”"
        self.click_to_element(self.Locators.BUTTON_ADD)
        """check radio request folder name article"""
        self.element_is_visible(self.Locators.RADIO_LINK_TO_CONTENT).is_displayed()
        check_request = self.element_is_visible(self.Locators.CHECK_REQUEST).text
        assert check_request == name_request
        self.element_is_visible(self.Locators.FOLDER_CONTENT).is_displayed()
        name_article = self.element_is_visible(self.Locators.NAME_ARTICLE).text
        assert name_article == name_content
        self.click_to_element(self.Locators.BUTTON_FINISH_1)
        text_link_to_content = self.element_is_visible(self.Locators.TEXT_LINK_TO_CONTENT).text
        assert text_link_to_content == "Ссылка на контент"
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("text_alert")
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
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
        self.click_to_element(self.Locators.CHANGE_FIXING_CONTENT)
        get_request_name = self.element_is_visible(self.Locators.INPUT_FIELD_NAME_REQUEST).get_attribute('value')
        assert get_request_name == name_request
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOWS_CHECK)
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        """add more question"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_content}"]')
        search_by_name.click()
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_BACK)
        try:
            data_request = self.add_more_requests()
        except TimeoutException:
            time.sleep(3)
            data_request = self.add_more_requests()
        # print(data_request)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXT_ALERT_NAME).send_keys("alert")
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        """check added request"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_content}"]')
        search_by_name.click()
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY, timeout=3)
        except TimeoutException:
            self.delete_draft()
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_BACK)
        list_added_request = self.elements_are_present(self.Locators.LIST_ADDED_REQUEST)
        data_added_requests = []
        for n in list_added_request:
            request_text = n.text
            data_added_requests.append(request_text)
        data_request_sort = sorted(data_request)
        data_added_requests_sort = sorted(data_added_requests)
        assert data_request_sort == data_added_requests_sort
        """check new search"""
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_REQUEST)
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_ARTICLE_BY_TEMPLATE)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
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
        # self.input_in_my_project(driver)
        name_request_script, name_script = self.create_script_base(driver)
        actions = ActionChains(driver)
        button_typography = self.elements_is_present(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        actions.click(button_typography).perform()
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request_script)
        svg_tooltip_request_field = self.element_is_visible(self.Locators.SVG_TOOLTIP_REQUEST_FIELD)
        svg_tooltip_request_field_value = svg_tooltip_request_field.get_attribute("data-tip")
        assert svg_tooltip_request_field_value == "Запросы позволяют закрепить контент вверху поисковой выдачи с пометкой “Закрепленный контент”"
        self.click_to_element(self.Locators.BUTTON_ADD)
        """check radio request folder name article"""
        self.element_is_visible(self.Locators.RADIO_LINK_TO_CONTENT).is_displayed()
        check_request = self.element_is_visible(self.Locators.CHECK_REQUEST).text
        assert check_request == name_request_script
        self.element_is_visible(self.Locators.FOLDER_CONTENT).is_displayed()
        name_article = self.element_is_visible(self.Locators.NAME_ARTICLE).text
        assert name_article == name_script
        self.click_to_element(self.Locators.BUTTON_FINISH_1)
        text_link_to_content = self.element_is_visible(self.Locators.TEXT_LINK_TO_CONTENT).text
        assert text_link_to_content == "Ссылка на контент"
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("text_alert")
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
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
        self.click_to_element(self.Locators.CHANGE_FIXING_CONTENT)
        get_request_name = self.element_is_visible(self.Locators.INPUT_FIELD_NAME_REQUEST).get_attribute('value')
        assert get_request_name == name_request_script
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOWS_CHECK)
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        """add more question"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_script}"]')
        search_by_name.click()
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        self.click_to_element(self.Locators.BUTTON_BACK)
        self.click_to_element(self.Locators.BUTTON_BACK)
        data_request = self.add_more_requests()
        # print(data_request)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXT_ALERT_NAME).send_keys("alert")
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        """check added request"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_script}"]')
        search_by_name.click()
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT, timeout=3)
        except TimeoutException:
            self.delete_draft()
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        self.click_to_element(self.Locators.BUTTON_BACK)
        self.click_to_element(self.Locators.BUTTON_BACK)
        list_added_request = self.elements_are_present(self.Locators.LIST_ADDED_REQUEST)
        data_added_requests = []
        for n in list_added_request:
            request_text = n.text
            data_added_requests.append(request_text)
        data_request_sort = sorted(data_request)
        data_added_requests_sort = sorted(data_added_requests)
        assert data_request_sort == data_added_requests_sort
        """check new search"""
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_REQUEST)
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_EDIT_SCRIPT)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
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
        try:
            text_fixing_by_expert = self.element_is_visible(self.Locators.TEXT_FIXING_BY_EXPERT).text
        except TimeoutException:
            time.sleep(3)
            text_fixing_by_expert = self.element_is_visible(self.Locators.TEXT_FIXING_BY_EXPERT).text
        assert text_fixing_by_expert == "Закреплено экспертом"


    def check_files(self, driver):
        # self.input_in_my_project(driver)
        actions = ActionChains(driver)
        path = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        # name_script = "media.jpg"
        name_request_script = "reuest " + str(random.randint(999, 9999))
        name_script = self.add_files_base(path)
        try:
            self.click_to_element(self.Locators.TYPOGRAPHY_TEMPLATE)
        except (TimeoutException, ElementClickInterceptedException):
            time.sleep(3)
            self.click_to_element(self.Locators.TYPOGRAPHY_TEMPLATE)
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request_script)
        svg_tooltip_request_field = self.element_is_visible(self.Locators.SVG_TOOLTIP_REQUEST_FIELD)
        svg_tooltip_request_field_value = svg_tooltip_request_field.get_attribute("data-tip")
        assert svg_tooltip_request_field_value == "Запросы позволяют закрепить контент вверху поисковой выдачи с пометкой “Закрепленный контент”"
        self.click_to_element(self.Locators.BUTTON_ADD)
        """check radio request folder name article"""
        self.element_is_visible(self.Locators.RADIO_LINK_TO_CONTENT).is_displayed()
        check_request = self.element_is_visible(self.Locators.CHECK_REQUEST).text
        assert check_request == name_request_script
        self.element_is_visible(self.Locators.FOLDER_CONTENT).is_displayed()
        name_article = self.element_is_visible(self.Locators.FILES_NAME).text
        assert name_article == name_script
        self.click_to_element(self.Locators.BUTTON_FINISH_1)
        text_link_to_content = self.element_is_visible(self.Locators.TEXT_LINK_TO_CONTENT).text
        assert text_link_to_content == "Ссылка на контент"
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("text_alert")
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
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
        self.click_to_element(self.Locators.CHANGE_FIXING_CONTENT)
        get_request_name = self.element_is_visible(self.Locators.INPUT_FIELD_NAME_REQUEST).get_attribute('value')
        assert get_request_name == name_request_script
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOWS_CHECK)
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        """add more question"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_script}"]')
        search_by_name.click()
        time.sleep(1)
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT, timeout=2)
        except TimeoutException:
            self.delete_draft()
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        self.click_to_element(self.Locators.BUTTON_BACK)
        self.click_to_element(self.Locators.BUTTON_BACK)
        data_request = self.add_more_requests()
        # print(data_request)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXT_ALERT_NAME).send_keys("alert")
        self.click_to_element(self.Locators.BUTTON_FINISH)
        try:
            self.click_to_element(self.Locators.GO_TO_CONTENT)
        except TimeoutException:
            time.sleep(5)
            self.click_to_element(self.Locators.GO_TO_CONTENT)
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        """check added request"""
        time.sleep(3)
        search_by_name = driver.find_element(By.XPATH, f'//h3[normalize-space()="{name_script}"]')
        search_by_name.click()
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT, timeout=3)
        except TimeoutException:
            self.delete_draft()
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        self.click_to_element(self.Locators.BUTTON_BACK)
        self.click_to_element(self.Locators.BUTTON_BACK)
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
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_REQUEST)
        self.click_to_element(self.Locators.CLOSE_WINDOW_FILES)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
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


class SearchRuEn(Authorisation, BasePage):

    Locators = SearchRuEnLocators()

    def create_article_ru(self, driver):
        """CREATE ARTICLE RU"""
        # self.input_in_my_project(self.driver)
        actions = ActionChains(driver)
        Locators = CreateTopicDatabaseLocators
        # person = generated_person()
        first_name_ru = "Статья " + str(random.randint(999, 9999))
        text_article_ru = text_ru
        """upload media"""
        try:
            self.click_to_element(Locators.CREATE_BUTTON, timeout=5)
        except (StaleElementReferenceException, TimeoutException):
            time.sleep(3)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_ARTICLE)
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
        self.click_to_element(Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(Locators.BUTTON_SUBMIT)
        self.click_to_element(Locators.BUTTON_SUBMIT)
        self.click_to_element(Locators.BUTTON_SUBMIT)
        self.element_is_visible(Locators.INPUT_TEXTAREA_FIELD).send_keys("text_alert")
        self.click_to_element(Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_ARTICLE_RU_EN)
        # self.click_to_element(self.Locators.HISTORY_BUTTON)
        """check article ru"""
        # 1 test
        search_request = "Соображения dscituj"
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(search_request)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        list_article_ru = self.elements_are_visible(self.Locators.LIST_RESULT_SEARCH_RU_FIRST)
        for n in list_article_ru:
            # time.sleep(1)
            t = n.text
            # print(t)
            assert t == "Соображения"
        # 2 test
        search_request_new = "Cjj,hf;tybz высшего"
        self.click_to_element(self.Locators.SEARCH)
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(search_request_new)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        list_article_ru = self.elements_are_visible(self.Locators.LIST_RESULT_SEARCH_EN_SECOND)
        for n in list_article_ru:
            # time.sleep(1)
            t = n.text
            # print(t)
            assert t == "высшего"
        # 3 test check inversion
        search_request_new = "Cjj,hf;tybz dscituj"
        self.click_to_element(self.Locators.SEARCH)
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(search_request_new)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)
        try:
            list_article_ru = self.elements_are_visible(self.Locators.LIST_RESULT_SEARCH_INVERSION)
        except TimeoutException:
            time.sleep(3)
            list_article_ru = self.elements_are_visible(self.Locators.LIST_RESULT_SEARCH_INVERSION)
        for n in list_article_ru:
            # time.sleep(1)
            t = n.text
            # print(t)
            assert t == "Соображения высшего"
        # 4 test check search inversion -minus
        search_request_new = "Cjj,hf;tybz -высшего"
        self.click_to_element(self.Locators.SEARCH)
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(search_request_new)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        list_article_ru = self.elements_are_visible(self.Locators.LIST_RESULT_SEARCH_RU_FIRST)
        for n in list_article_ru:
            # time.sleep(1)
            t = n.text
            # print(t)
            assert t == "Соображения"
        return first_name_ru, text_article_ru, list_split_ru

    def create_article_en(self, driver):
        """CREATE ARTICLE EN"""
        # self.input_in_my_project(self.driver)
        actions = ActionChains(driver)
        Locators = CreateTopicDatabaseLocators
        # person = generated_person()
        first_name_en = "Article " + str(random.randint(999, 9999))
        text_article_en = text_en
        """upload media"""
        try:
            self.click_to_element(Locators.CREATE_BUTTON, timeout=5)
        except (StaleElementReferenceException, TimeoutException):
            time.sleep(3)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_ARTICLE)
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
        self.click_to_element(Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(Locators.BUTTON_SUBMIT)
        self.click_to_element(Locators.BUTTON_SUBMIT)
        self.click_to_element(Locators.BUTTON_SUBMIT)
        self.element_is_visible(Locators.INPUT_TEXTAREA_FIELD).send_keys("text_alert")
        self.click_to_element(Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_ARTICLE_RU_EN)
        # self.click_to_element(self.Locators.HISTORY_BUTTON)
        """check article en"""
        # 1 test
        search_request = "said вщмшыр"
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(search_request)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        list_article_en = self.elements_are_visible(self.Locators.LIST_RESULT_SEARCH_EN_FIRST_EN)
        for n in list_article_en:
            # time.sleep(1)
            t = n.text
            # print(t)
            assert t == "said"
        # 2 test
        search_request_new = "ыфшв dovish"
        self.click_to_element(self.Locators.SEARCH)
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(search_request_new)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        list_article_en = self.elements_are_visible(self.Locators.LIST_RESULT_SEARCH_EN_SECOND_EN)
        for n in list_article_en:
            # time.sleep(1)
            t = n.text
            # print(t)
            assert t == "dovish"
        # 3 test check inversion
        search_request_new = "ьщку вщмшыр"
        self.click_to_element(self.Locators.SEARCH)
        search = self.element_is_visible(self.Locators.SEARCH)
        actions.click(search)
        actions.send_keys(search_request_new)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        list_article_en = self.elements_are_visible(self.Locators.LIST_RESULT_SEARCH_EN_INVERSION_EN)
        for n in list_article_en:
            # time.sleep(1)
            t = n.text
            # print(t)
            assert t == "more dovish"
        return first_name_en, text_article_en, list_split_en




















import datetime
import os
import pathlib
import random
import time
from random import choice
from string import ascii_uppercase
from pathlib import Path
import allure
import selenium
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException, \
    WebDriverException, ElementNotInteractableException, StaleElementReferenceException, InvalidSelectorException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from generator.generator import generated_person, generated_file, generated_big_file
from pages import users
from pages.authorisation_page import Authorisation
from pages.base_page import BasePage
from locators.locators_form_pages import FormPagesLocators as Locators, StepByScriptLocators, CopyPastePageLocators, \
    CreateDraftLocators, FilesPagesLocators
# from locators.form_pages_locators import StepByScriptLocators as Locators
# from locators.form_pages_locators import FixingArticle as Locators
from pages.data_login_password import *
from selenium.webdriver.common.alert import Alert


class ArticlePage(Authorisation, BasePage):

    def input_in_my_project(self, driver):
        """INPUT IN MY PROJECT"""
        self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.click_to_element(Locators.INPUT_BUTTON)
        try:
            time.sleep(1)
            self.click_to_element(Locators.TEST_PROJECT, timeout=3)
        except TimeoutException:
            self.click_to_element(Locators.ADD)
            self.element_is_visible(Locators.ADD_NAMES_PROJECT).send_keys("selen")
            self.element_is_visible(Locators.ADD_DESCRIPTION_PROJECT).send_keys("test_selenium")
            self.click_to_element(Locators.ADD_PROJECT_BUTTON)
            self.click_to_element(Locators.TEST_PROJECT)
            self.click_to_element(Locators.CONTENT)
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
            self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys("Контент 1")
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        except ElementClickInterceptedException:
            self.click_to_element(Locators.ADD)
            self.element_is_visible(Locators.ADD_NAMES_PROJECT).send_keys("selen")
            self.element_is_visible(Locators.ADD_DESCRIPTION_PROJECT).send_keys("test_selenium")
            self.click_to_element(Locators.ADD_PROJECT_BUTTON)
            self.click_to_element(Locators.TEST_PROJECT)
            self.click_to_element(Locators.CONTENT)
            time.sleep(12)
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
            self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys("Контент 1")
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)

    def add_normal_article(self):
        # self.get_authorisation_in_selen(driver)
        person = generated_person()
        first_name = person.first_name+str(random.randint(99, 999))
        text = "Hello"
        text_long = first_name+"name_"+str(random.randint(99, 999))
        self.click_to_element(Locators.CONTENT)
        time.sleep(2)
        self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_ARTICLE)
        time.sleep(7)
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys(first_name)
        self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")
        """add media"""
        try:
            self.elements_is_present(Locators.UPLOAD_MEDIA, timeout=2).click()
        except TimeoutException:
            time.sleep(5)
            self.elements_is_present(Locators.UPLOAD_MEDIA).click()
        """input is visible for load files"""
        self.browser.execute_script(
            """document.querySelector(".popup__footer.file-manager__foot.file-manager--hidden").removeAttribute('class')""")
        self.browser.execute_script(
            """document.querySelector("form[enctype='multipart/form-data']").removeAttribute('style')""")
        path1 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        print(path2, path1)
        data_path = [path1, path2]
        for n in data_path:
            self.element_is_visible(Locators.INPUT_INVISIBLE).send_keys(n)
        time.sleep(5)
        checkbox_insert_files = self.elements_are_visible(Locators.CHECKBOX_INSERT_FILES)
        for n in checkbox_insert_files:
            time.sleep(0.5)
            n.click()
        try:
            self.click_to_element(Locators.INPUT_SELECTED, timeout=2)
        except ElementClickInterceptedException:
            time.sleep(2)
            self.click_to_element(Locators.INPUT_SELECTED)
        time.sleep(1)
        """add text and format"""
        self.element_is_visible(Locators.TEXT_AREA_ARTICLE).send_keys(text)
        time.sleep(1)
        self.element_is_visible(Locators.TEXT_AREA_ARTICLE).send_keys(Keys.LEFT_CONTROL + 'a')
        self.click_to_element(Locators.TEXT_BOLD_FORMAT)
        time.sleep(0.5)
        self.click_to_element(Locators.TEXT_ITALIC_FORMAT)
        time.sleep(0.5)
        self.click_to_element(Locators.TEXT_UNDERLINE_FORMAT)
        """typography and check"""
        self.click_to_element(Locators.TYPOGRAPHY_ARTICLE)
        navigation_text_check = self.element_is_visible(Locators.NAVIGATION)
        navigation_text_check_value = navigation_text_check.text
        assert navigation_text_check_value == "навигация"
        # print(navigation_text_check_value)
        """check text"""
        search_text_check = self.element_is_visible(Locators.SEARCH)
        search_text_check_value = search_text_check.text
        assert search_text_check_value == "поиск"
        # print(search_text_check_value)
        access_text_check = self.element_is_visible(Locators.ACCESS)
        access_text_check_value = access_text_check.text
        assert access_text_check_value == "доступ"
        # print(access_text_check_value)
        version_text_check = self.element_is_visible(Locators.VERSION)
        version_text_check_value = version_text_check.text
        assert version_text_check_value == "версионность"
        # print(version_text_check_value)
        self.click_to_element(Locators.SUBMIT_ARTICLE)
        self.element_is_visible(Locators.SEARCH_INPUT_REQUEST).send_keys(text_long)
        print(text_long)
        self.click_to_element(Locators.ADD_SEARCH_BUTTON)
        self.click_to_element(Locators.FINISH_BUTTON)
        self.click_to_element(Locators.SUBMIT_ARTICLE)
        """проверка чекбоксов"""
        self.element_is_visible(Locators.CHECKBOX_SETTINGS_COMMENTS).is_displayed()
        self.element_is_visible(Locators.CHECKBOX_SETTINGS_DOWNLOADS).is_displayed()
        self.element_is_visible(Locators.CHECKBOX_SETTINGS_PRINTING).is_displayed()
        self.click_to_element(Locators.SUBMIT_ARTICLE)
        check_text_role = self.element_is_visible(Locators.CHECK_TEXT_ROLE)
        check_text_role_value = check_text_role.text
        assert check_text_role_value == "роль"
        check_select_radio = self.element_is_visible(Locators.CHECK_RADIOBUTTON_TYPOGRAPHY_NOW)
        check_select_radio.is_selected()
        check_select_radio2 = self.element_is_visible(Locators.CHECK_RADIOBUTTON_NO_DELETE)
        check_select_radio2.is_selected()
        self.click_to_element(Locators.FINISH_BUTTON)
        check_text_filled = self.element_is_visible(Locators.CHECK_TEXT_FILLED_NEED)
        check_text_filled_value = check_text_filled.text
        assert check_text_filled_value == "Должно быть заполнено"
        time.sleep(1)
        self.element_is_visible(Locators.TEXT_AREA_ALERT).send_keys(first_name)
        self.click_to_element(Locators.FINISH_BUTTON)
        try:
            check_new_article = self.element_is_visible(Locators.CHECK_NEW_ARTICLE)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(Locators.FINISH_BUTTON)
            check_new_article = self.element_is_visible(Locators.CHECK_NEW_ARTICLE)
        check_new_article_value = check_new_article.text
        assert check_new_article_value == "Hello"
        # print(check_new_article_value, "статья отображается")

    def fixing_article(self, driver):
        """FIXING_ARTICLE"""
        driver.implicitly_wait(10)
        person = generated_person()
        alert_text = 'Alert '+ person.first_name+str(random.randint(1, 9))
        text_test = person.first_name+str(random.randint(99, 999))
        text_fixing = "как помыть крота"+str(random.randint(9999, 999999))
        self.click_to_element(Locators.CONTENT)
        """create test article"""
        text_area = "Hello"
        time.sleep(1)
        try:
            self.click_to_element(Locators.CREATE_BUTTON)
        except (WebDriverException, StaleElementReferenceException):
            time.sleep(3)
            self.click_to_element(Locators.CREATE_BUTTON)
        try:
            self.click_to_element(Locators.CREATE_ARTICLE)
        except TimeoutException:
            time.sleep(2)
            self.click_to_element(Locators.CREATE_ARTICLE)
        time.sleep(5)
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys(text_test)
        time.sleep(1)
        self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")
        try:
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE).send_keys(text_area)
        except TimeoutException:
            time.sleep(2)
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE).send_keys(text_area)
        self.click_to_element(Locators.TYPOGRAPHY_ARTICLE)
        self.click_to_element(Locators.SUBMIT_ARTICLE)
        self.click_to_element(Locators.SUBMIT_ARTICLE)
        self.click_to_element(Locators.SUBMIT_ARTICLE)
        self.element_is_visible(Locators.TEXT_AREA_ALERT).send_keys(alert_text)
        self.click_to_element(Locators.FINISH_BUTTON)
        time.sleep(3)
        try:
            self.click_to_element(Locators.CLOSE_CREATED_ARTICLE)
        except ElementNotInteractableException:
            time.sleep(2)
            self.click_to_element(Locators.CLOSE_CREATED_ARTICLE)
        # time.sleep(1)
        self.click_to_element(Locators.SEARCH_HEAD_PAGE)
        self.click_to_element(Locators.BUTTON_FIXING_CONTENT)
        time.sleep(1)
        self.element_is_visible(Locators.INPUT_REQUEST).send_keys(text_fixing)
        time.sleep(2)
        self.click_to_element(Locators.BUTTON_FIXING_CONTENT_CHANGE)
        check_add_fixing_content = self.element_is_visible(Locators.CHECK_ADD_FIXING_CONTENT)
        check_add_fixing_content_value = check_add_fixing_content.text
        assert check_add_fixing_content_value == "Добавление закрепленного контента"
        # print(check_add_fixing_content_value)
        time.sleep(1)
        self.element_is_visible(Locators.SEARCH_TEST_ARTICLE).send_keys(text_test)
        # time.sleep(10)
        time.sleep(1)
        self.click_to_element(Locators.TEST_ARTICLE_NAME)
        self.click_to_element(Locators.BUTTON_SUBMIT)
        # self.click_to_element(Locators.BUTTON_SUBMIT)
        check_link_of_content = self.element_is_visible(Locators.CHECK_LINK_OF_CONTENT_RADIO)
        check_link_of_content.is_selected()
        check_name_content = self.element_is_visible(Locators.CHECK_NAME_CONTENT)
        check_name_content_value = check_name_content.text
        assert check_name_content_value == "Контент 1"
        # print(check_name_content_value)
        time.sleep(1)
        check_name_article = driver.find_element(By.XPATH, f"//section[@class='m-content-fix-wizard__link']/./p[text()='{text_test}']")
        check_name_article_value = check_name_article.text
        assert check_name_article_value == text_test
        # print(check_name_article_value)
        self.click_to_element(Locators.INCLUDED_CONTENT_RADIO)
        included_content = self.element_is_visible(Locators.INCLUDED_CONTENT)
        included_content_value = included_content.text
        assert included_content_value == text_area
        # print(included_content_value)
        self.click_to_element(Locators.FIXING)
        time.sleep(1)
        try:
            check_number_1_of_list = self.element_is_visible(Locators.LIST_OF_ARTICLES)
        except TimeoutException:
            time.sleep(2)
            # self.click_to_element(Locators.FIXING)
            check_number_1_of_list = self.element_is_visible(Locators.LIST_OF_ARTICLES)
        check_number_1_of_list_value = check_number_1_of_list.text
        assert check_number_1_of_list_value == text_test
        # print(check_number_1_of_list_value)
        time.sleep(1)
        self.click_to_element(Locators.POPUP_CLOSE_SVG)
        time.sleep(1)
        search = self.element_is_visible(Locators.SEARCH_OF_CONTENTS)
        actions = ActionChains(driver)
        actions.click(search)
        actions.send_keys(text_fixing)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        print(text_fixing)
        # self.element_is_visible(Locators.SEARCH_OF_CONTENTS).send_keys(text_fixing)
        # print(text_fixing)
        # self.click_to_element(Locators.FIND_OF_CONTENT)
        time.sleep(1)
        # self.screenshot()
        try:
            check_text_hello = self.element_is_visible(Locators.CHECK_TEXT_HELLO, timeout=2)
        except TimeoutException:
            time.sleep(2)
            check_text_hello = self.element_is_visible(Locators.CHECK_TEXT_HELLO)
        check_text_hello_value = check_text_hello.text
        assert check_text_hello_value == "Hello"

        check_article = driver.find_element(By.XPATH, f"//p[normalize-space()='{text_test}']")
        check_article_value = check_article.text
        assert check_article_value == text_test
        # print(check_article_value)
        # print(text_fixing)

    def filling_all_fields(self, driver):
        person = generated_person()
        field_input = self.element_is_visible(Locators.EDIT_TEMPLATES)
        field_input_1 = self.element_is_visible(Locators.EDIT_TEMPLATES_1)
        field_input_2 = self.element_is_visible(Locators.EDIT_TEMPLATES_2)
        field_input_3 = self.element_is_visible(Locators.EDIT_TEMPLATES_3)
        field_input_4 = self.element_is_visible(Locators.EDIT_TEMPLATES_4)
        field_input_5 = self.element_is_visible(Locators.EDIT_TEMPLATES_5)
        field_can_not_del_2 = self.element_is_visible(Locators.FIELD_CAN_NOT_DEL_2)
        actions = ActionChains(driver)
        actions.click(field_input_1)
        actions.send_keys("some text")
        actions.click(field_input_2)
        # actions.click(field_input_2)
        actions.send_keys("one more some text")
        actions.click(field_input_3)
        # actions.click(field_input_3)
        actions.send_keys("777")
        actions.click(field_input_4)
        # actions.click(field_input_4)
        actions.send_keys("https://www.something.com")
        actions.click(field_input_5)
        # actions.click(field_input_5)
        mail = person.email
        actions.send_keys(mail)
        # actions.click(field_input)
        actions.click(field_can_not_del_2)
        actions.perform()


    def add_article_by_templates(self, driver):
        driver.implicitly_wait(10)
        person = generated_person()
        name = "1_Templates" + str(random.randint(1111, 99999))
        name_content = "Content" + str(random.randint(1111, 99999))
        try:
            self.click_to_element(Locators.CREATE_BUTTON_ON_HEAD_PAGE)
        except StaleElementReferenceException:
            time.sleep(2)
            self.click_to_element(Locators.CREATE_BUTTON_ON_HEAD_PAGE)
        self.click_to_element(Locators.CREATE_TEMPLATES)
        self.click_to_element(Locators.CREATE_TEMPLATES_NEW)
        for i in range(1, 6):
            time.sleep(1)
            self.click_to_element(Locators.ADD_FIELD_BUTTON)
            list_of_fields = driver.find_element(By.XPATH,
                                                 f"//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[{i}]")
            list_of_fields.click()
            self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys(
                "Name" + str(random.randint(1111, 99999)))
            self.click_to_element(Locators.SAVE_TEMPLATES)
        self.click_to_element(Locators.ADD_FIELD_BUTTON)
        list_of_fields = driver.find_element(By.XPATH,
                                             f"//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[6]")
        list_of_fields.click()
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(1111, 99999)))
        self.element_is_visible(Locators.ANSWER).send_keys("answer 1")
        self.click_to_element(Locators.ADD_ANSWER)
        self.click_to_element(Locators.SAVE_BUTTON)
        """step 5"""
        self.click_to_element(Locators.ADD_FIELD_BUTTON)
        self.click_to_element(Locators.LIST_OF_FIELDS_2)
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(1111, 99999)))
        self.click_to_element(Locators.CHECKBOX_VALUE)
        self.element_is_visible(Locators.INPUT_VALUE).send_keys("Name" + str(random.randint(1111, 99999)))
        self.click_to_element(Locators.SAVE_TEMPLATES)
        """step 6"""
        self.element_is_visible(Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name)
        print(name)
        self.click_to_element(Locators.SAVE_CREATED_TEMPLATES)
        self.click_to_element(Locators.SUBMIT_TEMPLATES)
        # скрол
        # locator_scroller = self.element_is_visible(Locators.MODAL_WINDOW_SCROLLER, timeout=3)
        # modal_scroller = self.element_is_visible(Locators.MODAL_WIZARD_SCROLLER_TEMPLATE, timeout=3)
        self.scroll_wizard_template(name, driver)
        time.sleep(1)
        self.element_is_visible(Locators.check_name_input).send_keys(name_content)
        # print(name_content)
        time.sleep(3)
        self.element_is_visible(Locators.FOLDER_SAVE).send_keys("Контент 1")
        # try:
        #     field_input = self.element_is_visible(Locators.EDIT_TEMPLATES)
        # except TimeoutException:
        time.sleep(1)
        #     field_input = self.element_is_visible(Locators.EDIT_TEMPLATES)
        field_input_1 = self.element_is_visible(Locators.EDIT_TEMPLATES_1)
        field_input_2 = self.element_is_visible(Locators.EDIT_TEMPLATES_2)
        field_input_3 = self.element_is_visible(Locators.EDIT_TEMPLATES_3)
        field_input_4 = self.element_is_visible(Locators.EDIT_TEMPLATES_4)
        field_input_5 = self.element_is_visible(Locators.EDIT_TEMPLATES_5)
        field_can_not_del_1 = self.element_is_visible(Locators.FIELD_CAN_NOT_DEL_1)
        # field_input_6 = self.element_is_visible(Locators.CHOSE_ANSWER)
        """add and check text correct link"""
        actions = ActionChains(driver)
        actions.click(field_input_1)
        actions.send_keys("some text")
        # actions.click(field_input_2)
        actions.click(field_input_2)
        actions.send_keys("one more some text")
        actions.click(field_input_3)
        # actions.click(field_input_3)
        actions.send_keys("777")
        actions.click(field_input_4)
        # actions.click(field_input_4)
        actions.send_keys("https://www.something.com")
        actions.click(field_input_5)
        # actions.click(field_input_5)
        mail = person.email
        actions.send_keys(mail)
        actions.click(field_can_not_del_1)
        actions.perform()
        time.sleep(1)
        check_name_of_templates = driver.find_element(By.XPATH, f"//h1[normalize-space()='{name}']")
        check_name_of_templates.is_displayed()
        check_name_of_templates.click()       # клик по названию, чтобы выйти из формы
        self.element_is_visible(Locators.CHANGE_TEMPLATES_BUTTON).is_displayed()
        # self.screenshot()
        self.click_to_element(Locators.TYPOGRAPHY_TEMPLATE)
        check_search_text = driver.find_element(By.XPATH, "//p[contains(text(),'поиск')]")
        check_search_text_value = check_search_text.text
        assert check_search_text_value == "поиск"
        check_version_text = driver.find_element(By.XPATH, "//p[contains(text(),'версионность')]")
        check_version_text_value = check_version_text.text
        assert check_version_text_value == "версионность"
        # print(check_version_text_value)
        self.click_to_element(Locators.SUBMIT_TEMPLATES)
        input_request = self.element_is_visible(Locators.INPUT_REQUEST)
        requests_name = "request " + str(random.randint(1111, 99999))
        input_request.send_keys(requests_name)
        self.click_to_element(Locators.ADD_SEARCH_BUTTON)
        self.click_to_element(Locators.FIELD_OF_CONTENT_RADIO)
        """fixing_all_fields"""
        select_field_for_fixing = self.element_is_visible(Locators.SELECT_FIELD_FOR_FIXING)
        for i in range(6):
            time.sleep(0.5)
            select_field_for_fixing.click()
            select_field_for_fixing.send_keys(Keys.DOWN)
            select_field_for_fixing.send_keys(Keys.RETURN)
        self.click_to_element(Locators.FINISH_BUTTON)
        self.click_to_element(Locators.SUBMIT_TEMPLATES)
        self.element_is_visible(Locators.TEXT_AREA_ALERT).send_keys("Name" + str(random.randint(1111, 99999)))
        self.click_to_element(Locators.SUBMIT_TEMPLATES)
        check_utility_text = self.element_is_visible(Locators.UTILITY_TEMPLATE)
        check_utility_text_value = check_utility_text.text
        assert check_utility_text_value == "полезен"
        check_utility_text = self.element_is_visible(Locators.NO_UTILITY_TEMPLATE)
        check_utility_text_value = check_utility_text.text
        assert check_utility_text_value == "не полезен"
        check_name_of_templates_text = driver.find_element(By.XPATH,
                                                           f"//header[@id='article-content-modal-header']//span[contains(text(),'{name_content}')]")
        check_name_of_templates_text_value = check_name_of_templates_text.text
        assert check_name_of_templates_text_value == name_content
        """CHECK_FIXING_TEMPLATES"""
        with allure.step("Проверка закрепления контента, при изменении шаблона"):
            self.click_to_element(Locators.CLOSE_CREATED_ARTICLE)
            # time.sleep(1)
            self.click_to_element(Locators.CHECK_TEXT_ALL_CONTENT_SORT_BY_POPULAR)
            # time.sleep(1)
            self.click_to_element(Locators.CHECK_TEXT_ALL_CONTENT_SORT_BY_DATA)
            # time.sleep(1)
            self.click_to_element(Locators.CHECK_TEXT_ALL_CONTENT_SORT_BY_POPULAR)
            time.sleep(1)
            name_of_templates_in_list = driver.find_element(By.XPATH, f"//p[normalize-space()='{name_content}']")
            name_of_templates_in_list.click()
            # time.sleep(1)
            self.click_to_element(Locators.EDIT_ARTICLE)
            actions = ActionChains(driver)
            field = self.element_is_visible(Locators.EDIT_TEMPLATES_1)
            field1 = self.element_is_visible(Locators.NUMBER_FIELD_FOR_CLEAR)
            field2 = self.element_is_visible(Locators.LINK_FIELD_FOR_CLEAR)
            field_can_not_del = self.elements_is_present(Locators.FIELD_CAN_NOT_DEL)
            actions.click(field)
            for n in range(1, 11):
                actions.send_keys(Keys.BACKSPACE)
            actions.click(field1)
            # actions.click(field1)
            time.sleep(1)
            actions.send_keys(Keys.BACKSPACE)
            actions.send_keys(Keys.BACKSPACE)
            actions.send_keys(Keys.BACKSPACE)
            # actions.click(field2)
            actions.click(field_can_not_del)  # клик по нередактируемому полю для выхода из поля редактирования
            actions.perform()
            self.click_to_element(Locators.TYPOGRAPHY_TEMPLATE)
            self.click_to_element(Locators.SUBMIT_TEMPLATES)
            self.click_to_element(Locators.SUBMIT_TEMPLATES)
            self.element_is_visible(Locators.TEXT_AREA_ALERT).send_keys("Name" + str(random.randint(1111, 99999)))
            self.click_to_element(Locators.SUBMIT_TEMPLATES)
            # print(requests_name)
            """search_by_request"""
            time.sleep(1)
            self.click_to_element(Locators.CLOSE_CREATED_ARTICLE)
            self.click_to_element(Locators.SEARCH_HEAD_PAGE)
            search_of_contents = self.element_is_visible(Locators.SEARCH_OF_CONTENTS)
            search_of_contents.send_keys(requests_name)
            search_of_contents.send_keys(Keys.RETURN)
            try:
                field.click()
                field1.click()
            except WebDriverException:
                print("очищенных полей в запросе нет")
            # check_name_of_content = self.element_is_visible(Locators.CHECK_NAME_OF_CONTENT)
            time.sleep(1)
            try:
                check_name_of_content = driver.find_element(By.XPATH, f"//p[text()='{name_content}']")
            except NoSuchElementException:
                time.sleep(2)
                check_name_of_content = driver.find_element(By.XPATH, f"//p[text()='{name_content}']")
            check_name_of_content_value = check_name_of_content.text
            assert check_name_of_content_value == name_content, "name content is not correct"
            time.sleep(1)
            name_of_content = driver.find_element(By.XPATH, f"//p[text()='{name_content}']")
            name_of_content.click()
            time.sleep(1)
            """step 7"""
            self.click_to_element(Locators.EDIT_ARTICLE)
            time.sleep(1)
            try:
                field4 = self.element_is_visible(Locators.TEXT_FIELD_ONE_MORE)
            except TimeoutException:
                time.sleep(3)
                self.click_to_element(Locators.BUTTON_DELETE_DRAFT)
                time.sleep(1)
                field4 = self.element_is_visible(Locators.TEXT_FIELD_ONE_MORE)
            field5 = self.element_is_visible(Locators.LINK_FIELD_FOR_CLEAR_1)
            field6 = driver.find_element(By.XPATH, f"//pre[text()='{mail}']")
            for_click = self.element_is_visible(Locators.FOR_CLICK)
            field_can_not_del_1 = self.elements_is_present(Locators.FIELD_CAN_NOT_DEL_1)
            actions.click(field4)
            for n in range(1, 20):
                actions.send_keys(Keys.BACKSPACE)
            actions.click(field5)
            # actions.click(field5)
            for n in range(1, 27):
                actions.send_keys(Keys.BACKSPACE)
            actions.click(field6)
            # actions.click(field6)
            for n in range(1, 35):
                actions.send_keys(Keys.BACKSPACE)
            # actions.click(for_click)
            actions.click(field_can_not_del_1)  # клик по нередактируемому полю для выхода из поля редактирования
            actions.perform()
            time.sleep(1)
            self.click_to_element(Locators.TYPOGRAPHY_TEMPLATE)
            self.click_to_element(Locators.SUBMIT_TEMPLATES)
            self.click_to_element(Locators.SUBMIT_TEMPLATES)
            self.element_is_visible(Locators.TEXT_AREA_ALERT).send_keys("Name" + str(random.randint(1111, 99999)))
            self.click_to_element(Locators.SUBMIT_TEMPLATES)
            time.sleep(1)
            try:
                field.click()
                field1.click()
            except WebDriverException:
                print("очищенных полей в запросе нет")
            self.click_to_element(Locators.CLOSE_CREATED_ARTICLE)
            self.click_to_element(Locators.SEARCH_HEAD_PAGE)
            search_of_contents = self.element_is_visible(Locators.SEARCH_OF_CONTENTS)
            search_of_contents.send_keys(requests_name)
            search_of_contents.send_keys(Keys.RETURN)
            time.sleep(1)
            check_name_of_content = driver.find_element(By.XPATH, f"//p[text()='{name_content}']")
            check_name_of_content_value = check_name_of_content.text
            assert check_name_of_content_value == name_content, "name content is not correct"
            time.sleep(1)
            name_of_content = driver.find_element(By.XPATH, "//section[@class='article-preview__header']")
            name_of_content.click()
            time.sleep(1)
            self.click_to_element(Locators.EDIT_ARTICLE)
            time.sleep(1)
            self.click_to_element(Locators.TYPOGRAPHY_TEMPLATE)
            time.sleep(1)
            self.click_to_element(Locators.BUTTON_BACK)
            time.sleep(1)
            text_check_link_of_content = self.element_is_visible(Locators.CHECK_LINK_OF_CONTENT)
            text_check_link_of_content_value = text_check_link_of_content.text
            assert text_check_link_of_content_value == 'Ссылка на контент', "не закреплена как ссылка на контент"
            self.click_to_element(Locators.SUBMIT_TEMPLATES)
            self.element_is_visible(Locators.TEXT_AREA_ALERT).send_keys("Name" + str(random.randint(1111, 99999)))
            self.click_to_element(Locators.SUBMIT_TEMPLATES)
            time.sleep(1)
            edit_article = self.element_is_visible(Locators.EDIT_ARTICLE)
            actions.click(edit_article).perform()
            self.filling_all_fields(driver)
            self.click_to_element(Locators.TYPOGRAPHY_TEMPLATE)
            self.click_to_element(Locators.BUTTON_BACK)
            self.click_to_element(Locators.BUTTON_BACK)
            self.click_to_element(Locators.BUTTON_SUBMIT)
            self.click_to_element(Locators.CLOSE_LINK_OF_CONTENT)
            self.click_to_element(Locators.INCLUDED_CONTENT_RADIO)
            select_field_for_fixing = self.element_is_visible(Locators.SELECT_FIELD_FOR_FIXING)
            for i in range(6):
                time.sleep(1)
                select_field_for_fixing.click()
                select_field_for_fixing.send_keys(Keys.DOWN)
                select_field_for_fixing.send_keys(Keys.RETURN)
            self.click_to_element(Locators.FINISH_BUTTON)
            self.click_to_element(Locators.SUBMIT_TEMPLATES)
            self.element_is_visible(Locators.TEXT_AREA_ALERT).send_keys("Name" + str(random.randint(1111, 99999)))
            self.click_to_element(Locators.SUBMIT_TEMPLATES)
            self.click_to_element(Locators.EDIT_ARTICLE)
            self.click_to_element(Locators.CHANGE_TEMPLATES)
            self.click_to_element(Locators.CHANGE_TEMPLATES_BUTTON_1)
            self.click_to_element(Locators.FIELD_FOR_DEL)
            self.click_to_element(Locators.CONFIRM_DEL)
            self.click_to_element(Locators.CONFIRM_DEL_ONE_MORE)
            # time.sleep(5)
            field_for_del_text = self.element_is_visible(Locators.FIELD_FOR_DEL_TEXT)
            field_for_del_text.click()
            self.click_to_element(Locators.CONFIRM_DEL)
            self.click_to_element(Locators.CONFIRM_DEL_ONE_MORE)
            self.click_to_element(Locators.CONFIRM_SAVE)
            self.click_to_element(Locators.FINISH_BUTTON)
            self.click_to_element(Locators.CLOSE_CREATED_ARTICLE)
            self.click_to_element(Locators.SEARCH_HEAD_PAGE)
            search_of_contents = self.element_is_visible(Locators.SEARCH_OF_CONTENTS)
            search_of_contents.send_keys(requests_name)
            time.sleep(1)
            search_of_contents.send_keys(Keys.RETURN)
            time.sleep(5)
            check_name_of_content = driver.find_element(By.XPATH, f"//p[text()='{name_content}']")
            try:
                check_name_of_content_value = check_name_of_content.text
            except StaleElementReferenceException:
                time.sleep(3)
                check_name_of_content_value = check_name_of_content.text
            assert check_name_of_content_value == name_content, "name content is not correct"
            try:
                field_text_check = driver.find_element(By.XPATH, "//section[text()='Текст']")
                field_text_check.click()
                field_any_content_check = driver.find_element(By.XPATH, "//section[text()='Любой контент']")
                field_any_content_check.click()
            except:
                print("поля удалены из шаблона")
                time.sleep(1)
                """delete all fields"""
            name_content = driver.find_element(By.XPATH, f"//p[text()='{name_content}']")
            name_content.click()
            self.click_to_element(Locators.EDIT_ARTICLE)
            self.click_to_element(Locators.CHANGE_TEMPLATES)
            self.click_to_element(Locators.CHANGE_TEMPLATES_BUTTON_1)
            self.click_to_element(Locators.LINK_FOR_DEL)
            self.click_to_element(Locators.CONFIRM_DEL)
            self.click_to_element(Locators.CONFIRM_DEL_ONE_MORE)
            self.click_to_element(Locators.EMAIL_FOR_DEL)
            self.click_to_element(Locators.CONFIRM_DEL)
            self.click_to_element(Locators.CONFIRM_DEL_ONE_MORE)
            self.click_to_element(Locators.ANSWER_FOR_DEL_1)
            self.click_to_element(Locators.CONFIRM_DEL)
            self.click_to_element(Locators.CONFIRM_DEL_ONE_MORE)
            self.click_to_element(Locators.NUMBER_FOR_DEL)
            self.click_to_element(Locators.CONFIRM_DEL)
            self.click_to_element(Locators.CONFIRM_DEL_ONE_MORE)
            self.click_to_element(Locators.SAVE_CREATED_TEMPLATES)
            self.click_to_element(Locators.FINISH_BUTTON)
            self.click_to_element(Locators.CLOSE_CREATED_ARTICLE)
            self.click_to_element(Locators.SEARCH_HEAD_PAGE)
            search_of_contents = self.element_is_visible(Locators.SEARCH_OF_CONTENTS)
            search_of_contents.send_keys(requests_name)
            search_of_contents.send_keys(Keys.RETURN)
            print(requests_name, name_content, name)
            time.sleep(2)
            try:
                check_fixing_content_text = self.element_is_visible(Locators.CHECK_FIXING_CONTENT_TEXT)
            except TimeoutException:
                time.sleep(3)
                check_fixing_content_text = self.element_is_visible(Locators.CHECK_FIXING_CONTENT_TEXT)
            check_fixing_content_text_value = check_fixing_content_text.text
            assert check_fixing_content_text_value == f'По запросу «{requests_name}» ничего не найдено'

    def check_text_link(self, driver):  # DISABLE
        driver.implicitly_wait(5)
        person = generated_person()
        name = "Templates" + str(random.randint(999, 99999))
        name_content = "Content" + str(random.randint(999, 99999))
        self.click_to_element(Locators.CREATE_BUTTON_ON_HEAD_PAGE)
        self.click_to_element(Locators.CREATE_TEMPLATES)
        self.click_to_element(Locators.CREATE_TEMPLATES_NEW)
        for i in range(1, 6):
            time.sleep(1)
            self.click_to_element(Locators.ADD_FIELD_BUTTON)
            list_of_fields = driver.find_element(By.XPATH, f"//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[{i}]")
            list_of_fields.click()
            self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name"+str(random.randint(999, 99999)))
            self.click_to_element(Locators.SAVE_TEMPLATES)
        self.click_to_element(Locators.ADD_FIELD_BUTTON)
        list_of_fields = driver.find_element(By.XPATH, f"//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[6]")
        list_of_fields.click()
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(Locators.ANSWER).send_keys("answer 1")
        self.click_to_element(Locators.ADD_ANSWER)
        self.click_to_element(Locators.SAVE_BUTTON)
        """step 5"""
        self.click_to_element(Locators.ADD_FIELD_BUTTON)
        self.click_to_element(Locators.LIST_OF_FIELDS_2)
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name"+str(random.randint(999, 99999)))
        self.click_to_element(Locators.CHECKBOX_VALUE)
        self.element_is_visible(Locators.INPUT_VALUE).send_keys("Name"+str(random.randint(999, 99999)))
        self.click_to_element(Locators.SAVE_TEMPLATES)
        """step 6"""
        self.element_is_visible(Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name)
        # print(name)
        self.click_to_element(Locators.SAVE_CREATED_TEMPLATES)
        self.click_to_element(Locators.SUBMIT_TEMPLATES)
        name_of_templates = driver.find_element(By.XPATH, f"//div[contains(text(),'{name}')]")
        name_of_templates.click()
        self.element_is_visible(Locators.check_name_input).send_keys(name_content)
        # print(name_content)
        time.sleep(3)
        self.element_is_visible(Locators.FOLDER_SAVE).send_keys("Контент 1")
        # field_input = self.element_is_visible(Locators.EDIT_TEMPLATES)
        field_input_1 = self.element_is_visible(Locators.EDIT_TEMPLATES_1)
        field_input_2 = self.element_is_visible(Locators.EDIT_TEMPLATES_2)
        # field_input_3 = self.element_is_visible(Locators.EDIT_TEMPLATES_3)
        # field_input_4 = self.element_is_visible(Locators.EDIT_TEMPLATES_4)
        # field_input_5 = self.element_is_visible(Locators.EDIT_TEMPLATES_5)
        # field_input_6 = self.element_is_visible(Locators.CHOSE_ANSWER)

        """add and check text correct link"""
        # text_content = " You can learn more about GPT-3 by visiting the https://openai.com/ and exploring their documentation and resources. " \
        #                "Feel free to click on the link to delve into the fascinating world of GPT-3 and discover its capabilities!"
        # self.click_to_element(Locators.EDIT_TEMPLATES_1)
        # # self.click_to_element(Locators.TEXT_AREA_ARTICLE)
        # self.element_is_visible(Locators.TEXT_AREA_ARTICLE).send_keys(text_content)
        # # actions = ActionChains(driver)
        # # actions.click(field_input_1)
        # # actions.send_keys(text_content)
        # # actions.click(field_input_2)
        # # actions.perform()
        # time.sleep(5)
        # text_check_link = self.element_is_visible(Locators.TEXT_CHECK_LINK).get_attribute('href')
        # assert text_check_link == 'https://openai.com/'


class StepByScriptPage(Authorisation, BasePage):
    Locators = StepByScriptLocators()

    def add_script(self):
        try:
            self.click_to_element(Locators.CREATE_BUTTON, timeout=2)
        except StaleElementReferenceException:
            time.sleep(3)
            self.click_to_element(Locators.CREATE_BUTTON)
        except TimeoutException:
            time.sleep(2)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(self.Locators.ADD_SCRIPT)
        time.sleep(1)

    def check_opened_added_script(self, driver):
        """check button text"""
        check_button_add_step = self.element_is_clickable(self.Locators.ADD_STEP_BUTTON)
        check_button_add_step_value = check_button_add_step.text
        assert check_button_add_step_value == "добавить шаг"
        """check typography button"""
        try:
            self.element_is_clickable(self.Locators.BUTTON_SCRIPT_TYPOGRAPHY).click()
            # button_script_typography = driver.find_element(By.XPATH, "//p[text()='Опубликовать']")
            # button_script_typography
        except ElementClickInterceptedException:
            print("Element is not clickable")
        """check name placeholder"""
        placeholder_check = self.element_is_visible(self.Locators.INPUT_NAME_PLACEHOLDER).get_attribute("placeholder")
        # print(type(placeholder_check), placeholder_check)
        assert placeholder_check == 'Введите название контента'
        """check name folder"""
        target_folder_name = self.element_is_visible(self.Locators.TARGET_FOLDER_NAME)
        target_folder_name_value = target_folder_name.text
        assert target_folder_name_value == "расположение контента:"
        """check plus button"""
        self.element_is_clickable(self.Locators.PLUS_BUTTON_ADD_STEP).is_displayed()

    def check_len_name_content(self, driver):
        # для цифр заменить ascii_uppercase на digits
        name_content = ''.join(choice(ascii_uppercase) for i in range(256)) + str(7)
        # print(name_content)
        self.element_is_visible(self.Locators.INPUT_NAME_PLACEHOLDER).send_keys(name_content)
        value_text = self.element_is_visible(self.Locators.INPUT_NAME_PLACEHOLDER).get_attribute("value")
        len_name_text = len(value_text)
        # print(value_text, len(value_text))
        assert len_name_text == 256
        self.element_is_clickable(self.Locators.INPUT_TARGET_FOLDER).send_keys('Контент 1')
        """check typography button"""
        try:
            self.element_is_clickable(self.Locators.BUTTON_SCRIPT_TYPOGRAPHY).click()
        except ElementClickInterceptedException:
            print("Element is not clickable")

    def add_new_step(self, driver):
        driver.implicitly_wait(10)
        # """check and push plus button"""
        # self.click_to_element(self.Locators.PLUS_BUTTON_ADD_STEP)
        # time.sleep(10)
        self.element_is_clickable(self.Locators.ADD_STEP_BUTTON).click()
        """check name fields"""
        check_text_begin = self.element_is_clickable(self.Locators.CHECK_TEXT_BEGIN).text
        assert check_text_begin == 'Начало'
        check_text_step1 = self.element_is_clickable(self.Locators.CHECK_TEXT_STEP1).text
        assert check_text_step1 == 'Шаг 1'
        edit_step_text_check = self.element_is_clickable(self.Locators.EDIT_STEP_TEXT_CHECK)
        edit_step_text_check_value = edit_step_text_check.text
        assert edit_step_text_check_value == 'Редактор шага'
        edit_name_text_check = self.element_is_clickable(self.Locators.EDIT_NAME_TEXT_CHECK)
        edit_name_text_check_value = edit_name_text_check.text
        assert edit_name_text_check_value == 'название:'
        edit_content_text_check = self.element_is_clickable(self.Locators.EDIT_CONTENT_TEXT_CHECK)
        edit_content_text_check_value = edit_content_text_check.text
        assert edit_content_text_check_value == 'контент шага:'
        self.element_is_clickable(self.Locators.DELETE_STEP)
        time.sleep(10)
        try:
            self.click_to_element(self.Locators.ADD_TRANSITION)
        except ElementClickInterceptedException:
            time.sleep(5)
            self.click_to_element(self.Locators.ADD_TRANSITION)
        self.element_is_visible(self.Locators.NEW_TRANSITION).is_displayed()
        placeholder_name = self.element_is_visible(self.Locators.NAME_TRANSACTION_FIELD).get_attribute("placeholder")
        assert placeholder_name == "Введите название", 'name placeholder is not'
        text_transaction_to_step = self.element_is_visible(self.Locators.TEXT_TRANSACTION_TO_STEP)
        text_transaction_to_step_value = text_transaction_to_step.text
        assert text_transaction_to_step_value == 'переход к шагу:'
        self.element_is_visible(self.Locators.LIST_DROPDOWN).send_keys(Keys.DOWN)
        text_check_script_finish = self.element_is_visible(self.Locators.TEXT_CHECK_SCRIPT_FINISH)
        text_check_script_finish_value = text_check_script_finish.text
        assert text_check_script_finish_value == 'Сценарий завершён'
        # print(text_check_script_finish_value)
        self.element_is_visible(self.Locators.GO_TO_STEP_ARROW).is_displayed()
        self.element_is_visible(self.Locators.DELETE_STEP_ICON).is_displayed()

    def delete_all(self):
        self.click_to_element(self.Locators.DELETE_STEP_ICON)
        self.click_to_element(self.Locators.DELETE_STEP)
        text_check_add_new_step = self.element_is_visible(self.Locators.TEXT_CHECK_ADD_NEW_STEP)
        text_check_add_new_step_value = text_check_add_new_step.text
        assert text_check_add_new_step_value == 'Для начала добавьте первый шаг', "not message add new step before use"

    def add_text_in_textarea(self, driver):
        """ADD TEXT IN TEXTAREA"""
        # для цифр заменить ascii_uppercase на digits
        text_area = ''.join(choice(ascii_uppercase) for i in range(10)) + str(777)
        """add text in textarea"""
        actions = ActionChains(driver)
        actions.send_keys(text_area)
        # actions.move_by_offset(0, 0)
        # actions
        actions.perform()
        time.sleep(1)

    def new_step(self, driver):
        actions = ActionChains(driver)
        person = generated_person()
        to_get_name = person.first_name + str(random.randint(99, 999))
        text_area = person.last_name + str(random.randint(99, 999))
        """add step"""
        self.click_to_element(self.Locators.ADD_STEP_BUTTON)
        text_check_name_new_step = self.element_is_visible(self.Locators.TEXT_CHECK_NAME_NEW_STEP).get_attribute("placeholder")
        assert text_check_name_new_step == 'Введите название'
        # self.click_to_element(self.Locators.TEXT_AREA)
        # self.element_is_visible(self.Locators.TEXT_AREA).send_keys(text_area)
        """minimap"""
        # self.element_is_visible(self.Locators.MINIMAP).is_displayed()
        self.element_is_visible(self.Locators.PLUS).is_displayed()
        self.element_is_visible(self.Locators.MINUS).is_displayed()
        self.element_is_visible(self.Locators.FANCYBOX).is_displayed()
        """check alerts"""
        self.click_to_element(self.Locators.BUTTON_SCRIPT_TYPOGRAPHY)
        check_alert_text_content_step = self.element_is_visible(self.Locators.CHECK_ALERT_TEXT_CONTENT_STEP).text
        assert check_alert_text_content_step == 'Не должно быть пустым', 'wrong or not alert'
        check_alert_text_name_step = self.element_is_visible(self.Locators.CHECK_ALERT_TEXT_NAME_STEP).text
        assert check_alert_text_name_step == 'Не должно быть пустым'
        """add text in textarea"""
        time.sleep(1)
        # text_content = " You can learn more about GPT-3 by visiting the https://openai.com/ and exploring their documentation and resources. " \
        #                "Feel free to click on the link to delve into the fascinating world of GPT-3 and discover its capabilities!"
        text_content = "Text Content Example"
        self.click_to_element(self.Locators.TEXT_CHECK_INPUT_CONTENT_OF_STEP)
        actions.send_keys(text_content)
        time.sleep(1)
        # actions.move_by_offset(1, 1)
        actions.move_to_element(self.element_is_visible(self.Locators.INPUT_NAME_FIRST_STEP))
        time.sleep(1)
        actions.click()
        actions.perform()
        # self.elements_is_present(self.Locators.INPUT_NAME_FIRST_STEP)
        # """check text link correct """
        # time.sleep(5)
        # check_link_correct = self.element_is_visible(self.Locators.TEXT_CHECK_LINK).get_attribute("href")
        # print(check_link_correct)
        # assert check_link_correct == 'https://openai.com/'
        # time.sleep(1)
        self.element_is_visible(self.Locators.INPUT_NAME_FIRST_STEP).send_keys(to_get_name)
        self.click_to_element(self.Locators.BUTTON_PREVIEW)
        check_text_chose_transaction = self.element_is_visible(self.Locators.CHECK_TEXT_CHOSE_TRANSACTION).text
        assert check_text_chose_transaction == 'Необходимо выбрать шаг'
        self.element_is_visible(self.Locators.LIST_DROPDOWN_FIRST_STEP).send_keys("Сценарий завершён")
        self.click_to_element(self.Locators.BUTTON_PREVIEW)
        check_text_preview = self.element_is_visible(self.Locators.CHECK_TEXT_PREVIEW).text
        assert check_text_preview == 'Предпросмотр'
        self.click_to_element(self.Locators.CLOSE_WINDOW_PREVIEW)
        """add step one more"""
        self.click_to_element(self.Locators.PLUS_BUTTON_ADD_STEP)
        time.sleep(2)
        try:
            self.click_to_element(self.Locators.TEXT_CHECK_INPUT_CONTENT_OF_STEP, timeout=3)
        except TimeoutException:
            assert 1 == 2, "БАГ, ВЕЧНЫЙ ЛОАДЕР"
        self.add_text_in_textarea(driver)
        self.click_to_element(self.Locators.INPUT_NAME_FIRST_STEP)
        self.element_is_visible(self.Locators.INPUT_NAME_FIRST_STEP).send_keys(text_area)
        self.element_is_visible(self.Locators.LIST_DROPDOWN_FIRST_STEP).send_keys("Сценарий завершён")
        time.sleep(1)
        text_end_script = self.element_is_clickable(self.Locators.TEXT_END_SCRIPT).text
        assert text_end_script == 'Завершение'
        """check blocks of field"""
        check_text_begin = self.element_is_visible(self.Locators.CHECK_TEXT_BEGIN).text
        assert check_text_begin == 'Начало'
        check_text_step1 = self.element_is_visible(self.Locators.CHECK_TEXT_STEP1).text
        assert check_text_step1 == 'Шаг 1'
        check_text_step2 = self.element_is_visible(self.Locators.CHECK_TEXT_STEP2).text
        assert check_text_step2 == 'Шаг 2'
        time.sleep(1)
        self.click_to_element(self.Locators.BUTTON_SCRIPT_TYPOGRAPHY)
        try:
            text_check_typography_window = self.element_is_visible(self.Locators.TEXT_CHECK_TYPOGRAPHY_WINDOW).text
        except TimeoutException:
            print("БАГ!!! БАГ!!! БАГ!!!")
            time.sleep(3)
            text_check_typography_window = self.element_is_visible(self.Locators.TEXT_CHECK_TYPOGRAPHY_WINDOW).text
        assert text_check_typography_window == 'Настройки публикации контента'

    def check_step_fixing(self, driver):
        actions = ActionChains(driver)
        driver.implicitly_wait(10)
        """fixing added script"""
        # to_get_name = self.elements_is_present(self.Locators.TO_GET_NAME)
        # to_get_name_text = to_get_name.get_attribute("value")
        # print(to_get_name_text)
        """create step script"""
        to_get_name = "NAME SCRIPT" + str(random.randint(99, 999))
        text_fixing = "как помыть крота" + str(random.randint(99, 999))
        text_content = "Text" + str(random.randint(99, 999))
        name_of_step = "Step" + str(random.randint(99, 999))
        self.element_is_visible(self.Locators.INPUT_NAME_PLACEHOLDER).send_keys(to_get_name)
        try:
            self.element_is_clickable(self.Locators.INPUT_TARGET_FOLDER).send_keys('Контент 1')
        except TimeoutException:
            time.sleep(3)
            self.element_is_clickable(self.Locators.INPUT_TARGET_FOLDER).send_keys('Контент 1')
        self.click_to_element(self.Locators.ADD_STEP_BUTTON)
        time.sleep(5)
        try:
            self.elements_is_present(self.Locators.TEXT_CHECK_INPUT_CONTENT_OF_STEP).click()
        except TimeoutException:
            time.sleep(3)
            self.elements_is_present(self.Locators.TEXT_CHECK_INPUT_CONTENT_OF_STEP).click()
        time.sleep(1)
        actions.send_keys(text_content)
        time.sleep(1)
        actions.move_to_element(self.element_is_visible(self.Locators.INPUT_NAME_FIRST_STEP))
        time.sleep(1)
        actions.click()
        actions.perform()
        self.element_is_visible(self.Locators.INPUT_NAME_FIRST_STEP).send_keys(name_of_step)
        # time.sleep(1)
        self.element_is_visible(self.Locators.LIST_DROPDOWN_FIRST_STEP).send_keys("Сценарий завершён")
        time.sleep(1)
        self.click_to_element(self.Locators.BUTTON_SCRIPT_TYPOGRAPHY)
        time.sleep(1)
        # to_get_name = self.element_is_visible(self.Locators.INPUT_NAME_PLACEHOLDER).get_attribute("value")
        self.element_is_visible(self.Locators.INPUT_FIXING_FIELD_REQUEST).send_keys(text_fixing)
        self.click_to_element(self.Locators.ADD_BUTTON_FIXING_FIELD_REQUEST)
        window_fixing_request = self.element_is_visible(self.Locators.WINDOW_FIXING_REQUEST_TEXT_CHECK).text
        assert window_fixing_request == "Закрепление контента"
        display_check_text = self.element_is_visible(self.Locators.DISPLAY_CHECK_TEXT).text
        assert display_check_text == "отображение"
        """check radio"""
        self.element_is_visible(self.Locators.CHECK_RADIO_LINK_CONTENT1).is_selected()
        self.element_is_visible(self.Locators.CHECK_RADIO_DISABLED).is_displayed()
        """check content name"""
        try:
            check_text_content_script = self.element_is_visible(self.Locators.CHECK_TEXT_CONTENT_SCRIPT).text
        except TimeoutException:
            time.sleep(3)
            check_text_content_script = self.element_is_visible(self.Locators.CHECK_TEXT_CONTENT_SCRIPT).text
        assert check_text_content_script == "Контент 1"
        """check name script"""
        time.sleep(1)
        check_text_name_script = driver.find_element(By.XPATH, f"//p[text()='{to_get_name}']")
        check_text_name_script_value = check_text_name_script.text
        assert check_text_name_script_value == to_get_name
        self.click_to_element(self.Locators.FINISH_BUTTON_SCRIPT)
        """check text wizard and search"""
        text_check_window_typography_content = self.element_is_visible(self.Locators.TEXT_CHECK_WINDOW_TYPOGRAPHY_CONTENT).text
        assert text_check_window_typography_content == 'Настройки публикации контента'
        text_check_search = self.element_is_visible(self.Locators.TEXT_CHECK_SEARCH).text
        assert text_check_search == 'поиск'
        """check text request search fixing"""
        check_text_request_search_fixing = driver.find_element(By.XPATH, f"//span[text()='{text_fixing}']")
        check_text_request_search_fixing_value = check_text_request_search_fixing.text
        assert check_text_request_search_fixing_value == text_fixing
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        self.element_is_visible(self.Locators.TEXT_AREA_ALERT_INPUT).send_keys("Alert")
        self.click_to_element(self.Locators.FINISH_BUTTON_SCRIPT)
        """content"""
        self.click_to_element(self.Locators.CONTENT_TRANSFER)
        time.sleep(3)
        self.click_to_element(self.Locators.CONTENT_SEARCH)
        search_of_contents = self.element_is_visible(Locators.SEARCH_OF_CONTENTS)
        search_of_contents.send_keys(text_fixing)
        search_of_contents.send_keys(Keys.RETURN)
        time.sleep(1)
        """text search of content"""
        try:
            check_text_search = driver.find_element(By.XPATH, f"//p[text()='{to_get_name}']")
        except TimeoutException:
            time.sleep(2)
            check_text_search = driver.find_element(By.XPATH, f"//p[text()='{to_get_name}']")

        check_text_search_value = check_text_search.text
        assert check_text_search_value == to_get_name
        check_text_fixing_expert = self.element_is_visible(self.Locators.CHECK_TEXT_FIXING_EXPERT).text
        assert check_text_fixing_expert == "Закреплено экспертом"


class CopyPastePage(Authorisation, BasePage):
    Locators = CopyPastePageLocators()

    def add_text_in_article(self, driver): # DISABLE
        person = generated_person()
        text_name = person.first_name + str(random.randint(99, 999))
        text_area = person.last_name + str(random.randint(99, 999))
        example_text = " You can learn more about GPT-3 by visiting the https://openai.com/ and exploring their documentation and resources. " \
                       "Feel free to click on the link to delve into the fascinating world of GPT-3 and discover its capabilities!"
        self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_ARTICLE)
        time.sleep(5)
        self.element_is_visible(self.Locators.FOLDER_DROPDOWN).send_keys("Контент 1")
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys(text_name)
        self.element_is_visible(Locators.TEXT_AREA_ARTICLE).send_keys(example_text)
        # self.screenshot()
        time.sleep(5)
        check_link_correct = self.element_is_visible(self.Locators.CHECK_LINK_CORRECT).get_attribute("href")
        # print(check_link_correct)
        assert check_link_correct == 'https://openai.com/'
        # time.sleep(3)
        time.sleep(0.5)
        self.click_to_element(Locators.TYPOGRAPHY_ARTICLE)
        self.click_to_element(Locators.SUBMIT_ARTICLE)
        self.click_to_element(Locators.SUBMIT_ARTICLE)
        self.click_to_element(Locators.SUBMIT_ARTICLE)
        self.element_is_visible(Locators.TEXTAREA_ARTICLE).send_keys(text_area)
        self.click_to_element(Locators.SUBMIT_ARTICLE)
        time.sleep(1)
        check_link_correct = self.element_is_visible(self.Locators.CHECK_LINK_CORRECT).get_attribute("href")
        # print(check_link_correct)
        assert check_link_correct == 'https://openai.com/'


class CreateDraftPage(Authorisation, BasePage):

    Locators = CreateDraftLocators()

    def create_name_article(self):
        person = generated_person()
        name_article = person.first_name + str(random.randint(99, 999))
        time.sleep(3)
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys(name_article)

    def alert_draft(self, driver):
        alert_create_draft = self.element_is_visible(self.Locators.ALERT_CREATE_DRAFT).text
        assert alert_create_draft == "Контент сохраняется автоматически"
        time.sleep(3)
        try:
            # alert_create_draft = self.element_is_visible(self.Locators.ALERT_CREATE_DRAFT).text
            # print(alert_create_draft)
            alert_create_draft = driver.find_element(By.XPATH, "//article[text()='Контент сохраняется автоматически']")
            alert_create_draft_value = alert_create_draft.text
            # print(alert_create_draft_value)
        except NoSuchElementException:
            print("плашка исчезла")

    def to_article(self, name="Article_Name1"):
        self.click_to_element(Locators.TEST_PROJECT)
        self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_ARTICLE)
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys(name)

    def open_4_tab(self, driver):
        """open draft"""
        person = generated_person()
        name_article = person.first_name + str(random.randint(99, 999))
        try:
            self.click_to_element(Locators.CREATE_BUTTON, timeout=2)
        except StaleElementReferenceException:
            time.sleep(5)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(self.Locators.FIELD_DRAFT)
        """open 4 tab"""
        for n in range(4):
            driver.execute_script(f"window.open('{url}')")
            time.sleep(0.5)
        time.sleep(10)
        """open tab and fill name article"""
        tab0 = driver.window_handles[0]
        tab4 = driver.window_handles[1]
        tab3 = driver.window_handles[2]
        tab2 = driver.window_handles[3]
        tab1 = driver.window_handles[4]
        self.browser.switch_to.window(tab1)
        driver.refresh()
        time.sleep(5)
        try:
            self.click_to_element(Locators.TEST_PROJECT)
        except TimeoutException:
            time.sleep(5)
            self.click_to_element(Locators.TEST_PROJECT)
        try:
            self.click_to_element(Locators.CREATE_BUTTON, timeout=2)
        except StaleElementReferenceException:
            time.sleep(2)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_ARTICLE)
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys("Article_Name1")
        self.browser.switch_to.window(tab2)
        self.click_to_element(Locators.TEST_PROJECT)
        try:
            self.click_to_element(Locators.CREATE_BUTTON, timeout=2)
        except StaleElementReferenceException:
            time.sleep(2)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_TEMPLATES)
        """create new template"""
        self.click_to_element(Locators.NEW_TEMPLATE)
        self.click_to_element(Locators.ADD_FIELD_BUTTON)
        self.click_to_element(Locators.LIST_OF_FIELDS_1)
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.click_to_element(Locators.SAVE_TEMPLATES)
        name_templates = "for download file testing" + str(random.randint(999, 99999))
        self.element_is_visible(Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name_templates)
        self.click_to_element(Locators.SAVE_TEMPLATES_CHANGE)
        self.click_to_element(Locators.FINISH_BUTTON_SCRIPT)
        time.sleep(1)
        # locator_scroller = self.element_is_visible(Locators.MODAL_WINDOW_SCROLLER, timeout=3)
        # frame = self.element_is_visible(Locators.WINDOW_POPUP_TEMPLATE)
        # self.switch_to_frame(frame)
        self.scroll_wizard_template(name_templates, driver)
        # templates_download = driver.find_element(By.XPATH, f"//span[text()='{name_templates}']")
        # templates_download
        # try:
        #     templates_download = driver.find_element(By.XPATH, f"//span[text()='{name_templates}']")
        # except NoSuchElementException:
        #     time.sleep(3)
        #     templates_download = driver.find_element(By.XPATH, f"//span[text()='{name_templates}']")
        # templates_download
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys("Template_Name2")
        time.sleep(1)
        self.browser.switch_to.window(tab3)
        self.click_to_element(Locators.TEST_PROJECT)
        try:
            self.click_to_element(Locators.CREATE_BUTTON, timeout=2)
        except StaleElementReferenceException:
            time.sleep(3)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_STEP_SCRIPT)
        self.element_is_visible(self.Locators.NAME_OF_STEP_SCRIPT).send_keys("Script_Name3")
        self.browser.switch_to.window(tab4)
        self.click_to_element(Locators.TEST_PROJECT)
        try:
            self.click_to_element(Locators.CREATE_BUTTON, timeout=2)
        except StaleElementReferenceException:
            time.sleep(5)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(self.Locators.CREATE_FILE)
        self.element_is_visible(self.Locators.INPUT_NAME_FILE).send_keys("File_Name4")
        try:
            self.element_is_visible(self.Locators.DIRECT_FOLDER).send_keys("Контент 1")
        except ElementNotInteractableException:
            time.sleep(3)
            self.element_is_visible(self.Locators.DIRECT_FOLDER).send_keys("Контент 1")
        """close article tab1"""
        self.browser.switch_to.window(tab2)
        time.sleep(3)
        try:
            self.click_to_element(Locators.CLOSE_PAGE_LIST)
        except ElementClickInterceptedException:
            time.sleep(5)
            self.click_to_element(Locators.CLOSE_PAGE_LIST)
        """check text all"""
        self.browser.switch_to.window(tab0)
        time.sleep(3)
        """time check"""
        i = 0
        text_time = self.elements_are_visible(self.Locators.TIME_TEXT_ALL)
        data_time = []
        for n in text_time:
            n.is_displayed()
            text_time_value = n.text
            data_time.append(text_time_value)
            print(n.is_displayed())
            i += 1
            if i == 4:
                break
        # print(data_time)
        """content check"""
        i = 0
        text_content = self.elements_are_visible(self.Locators.CONTENT_TEXT_ALL)
        data_content = []
        for n in text_content:
            # n.is_displayed()
            text_content_value = n.text
            data_content.append(text_content_value)
            i += 1
            if i == 4:
                break
        # print(data_content)
        content_list = ['Контент 1', 'Контент 1', 'Контент 1', 'Контент 1']
        assert content_list == data_content
        """check click"""
        try:
            self.element_is_clickable(self.Locators.SECTION2_CHECK).click()
        except ElementClickInterceptedException:
            print("некликабельный")
        # time.sleep(1)
        """check svg del"""
        self.element_is_visible(self.Locators.DEL_DRAFT_SVG).is_displayed()
        """check click"""
        # time.sleep(5)
        self.click_to_element(self.Locators.SECTION3)
        """check open edit text"""
        self.click_to_element(self.Locators.CHECK_TEXT_OPEN_EDIT_DRAFT)
        self.click_to_element(self.Locators.CHANGE_TEMPLATE)
        change_template_name_text_check = self.element_is_visible(self.Locators.CHANGE_TEMPLATE_NAME_TEXT_CHECK)
        change_template_name_text_check_value = change_template_name_text_check.text
        assert change_template_name_text_check_value == "Название шаблона"


class FilesPages(Authorisation, BasePage):
    Locators = FilesPagesLocators()

    def check_tooltip(self, driver):
        element = self.element_is_visible(self.Locators.BUTTON_DOWNLOAD)
        self.action_move_to_element(element, driver)
        self.element_is_visible(self.Locators.CHECK_TOOLTIP_TEXT)
        check_tooltip_text = self.element_is_visible(self.Locators.CHECK_TOOLTIP_TEXT).text
        assert check_tooltip_text == "Тип и размер файлов:"

    def generated_big_file_jpg(self):
        """created bigfile"""
        bf = open('bigfile.jpg', "wb")
        bf.seek(1073741824 - 1)
        bf.write(b"\0")
        bf.close()

    def generated_big_file_exe(self):
        """created bigfile"""
        bf = open('bigfile.exe', "wb")
        bf.seek(1073741824 - 1)
        bf.write(b"\0")
        bf.close()

    def generated_big_file_csv(self):
        """created bigfile"""
        bf = open('bigfile.csv', "wb")
        bf.seek(1073741824 - 1)
        bf.write(b"\0")
        bf.close()

    def add_big_file(self, driver):
        big_file = Path(pathlib.Path.cwd(), "bigfile.jpg")
        path = str(big_file)
        time.sleep(5)
        self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_ARTICLE)
        try:
            self.click_to_element(Locators.CREATE_ARTICLE)
        except TimeoutException:
            time.sleep(1)
        self.elements_is_present(self.Locators.UPLOAD_MEDIA).click()
        self.check_tooltip(driver)
        """input is visible for load files"""
        self.browser.execute_script("""document.querySelector(".popup__footer.file-manager__foot.file-manager--hidden").removeAttribute('class')""")
        self.browser.execute_script("""document.querySelector("form[enctype='multipart/form-data']").removeAttribute('style')""")
        # self.driver.execute_script("arguments[0].style.visibility = 'visible';", element)
        self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(path)
        self.click_to_element(self.Locators.CLOSE_DOWNLOAD_WINDOW)
        check_text_warning = self.element_is_visible(self.Locators.CHECK_TEXT_WARNING).text
        assert check_text_warning == "Ошибка загрузки файлов"
        self.click_to_element(self.Locators.SHOW_BUTTON)
        check_text_big_file_err = self.element_is_visible(self.Locators.CHECK_TEXT_BIG_FILE_ERR).text
        # assert check_text_big_file_err == "Размер файла не должен превышать 100 Мб", "В тексте всплывающего окна должно быть: 100 Мб!"
        time.sleep(2)
        os.remove(path)

    def create_data_files(self, driver):
        driver.implicitly_wait(10)
        data_files = generated_file()
        try:
            self.click_to_element(Locators.CREATE_BUTTON)
        except StaleElementReferenceException:
            time.sleep(2)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_ARTICLE)
        try:
            self.elements_is_present(self.Locators.UPLOAD_MEDIA).click()
        except TimeoutException:
            time.sleep(5)
            self.elements_is_present(self.Locators.UPLOAD_MEDIA).click()
        """input is visible for load files"""
        self.browser.execute_script(
            """document.querySelector(".popup__footer.file-manager__foot.file-manager--hidden").removeAttribute('class')""")
        self.browser.execute_script(
            """document.querySelector("form[enctype='multipart/form-data']").removeAttribute('style')""")
        # self.driver.execute_script("arguments[0].style.visibility = 'visible';", element)
        for n in data_files:
            file_type = Path(pathlib.Path.cwd(), f"{n}")
            path = str(file_type)
            # time.sleep(0.5)
            self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(path)
        time.sleep(5)  # ожидание перед удалением
        for n in data_files:
            file_type = Path(pathlib.Path.cwd(), f"{n}")
            path = str(file_type)
            os.remove(path)

    def check_template_download(self, driver):
        data_files = generated_file()
        try:
            self.click_to_element(Locators.CREATE_BUTTON)
        except StaleElementReferenceException:
            time.sleep(5)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_TEMPLATES)
        """create new template"""
        self.click_to_element(self.Locators.NEW_TEMPLATE)
        self.click_to_element(Locators.ADD_FIELD_BUTTON)
        self.click_to_element(Locators.LIST_OF_FIELDS_1)
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(1111, 99999)))
        self.click_to_element(Locators.SAVE_TEMPLATES)
        name_templates = "for download file testing" + str(random.randint(1111, 99999))
        self.element_is_visible(Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name_templates)
        self.click_to_element(Locators.SAVE_TEMPLATES_CHANGE)
        self.click_to_element(Locators.FINISH_BUTTON_SCRIPT)
        time.sleep(1)
        self.scroll_wizard_template(name_templates, driver)
        # try:
        #     templates_download = driver.find_element(By.XPATH, f"//span[text()='{name_templates}']")
        # except NoSuchElementException:
        #     time.sleep(3)
        #     templates_download = driver.find_element(By.XPATH, f"//span[text()='{name_templates}']")
        # templates_download
        try:
            self.click_to_element(Locators.TEXT_AREA_ARTICLE)
        except TimeoutException:
            time.sleep(10)
            self.click_to_element(Locators.TEXT_AREA_ARTICLE)
        self.click_to_element(self.Locators.DROPDOWN)
        frame = self.elements_is_present(self.Locators.FRAME)
        self.switch_to_frame(frame)
        self.click_to_element(self.Locators.DROP_DOWN_FILES)
        self.switch_out_frame()
        time.sleep(1)
        self.check_tooltip(driver)
        """for visible"""
        self.download_files_is_visible()
        for n in data_files:
            file_type = Path(pathlib.Path.cwd(), f"{n}")
            path = str(file_type)
            self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(path)
        time.sleep(5)  # ожидание перед удалением
        for n in data_files:
            file_type = Path(pathlib.Path.cwd(), f"{n}")
            path = str(file_type)
            os.remove(path)
        # time.sleep(100)

    def template_download_bigfile(self, driver):
        big_file = Path(pathlib.Path.cwd(), "bigfile.exe")
        path = str(big_file)
        try:
            self.click_to_element(Locators.CREATE_BUTTON)
        except StaleElementReferenceException:
            time.sleep(2)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_TEMPLATES)
        """create new template"""
        self.click_to_element(self.Locators.NEW_TEMPLATE)
        self.click_to_element(Locators.ADD_FIELD_BUTTON)
        self.click_to_element(Locators.LIST_OF_FIELDS_1)
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.click_to_element(Locators.SAVE_TEMPLATES)
        name_templates = "for download file testing" + str(random.randint(999, 99999))
        self.element_is_visible(Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name_templates)
        self.click_to_element(Locators.SAVE_TEMPLATES_CHANGE)
        self.click_to_element(Locators.FINISH_BUTTON_SCRIPT)
        time.sleep(2)
        self.scroll_wizard_template(name_templates, driver)
        # try:
        #     templates_download = driver.find_element(By.XPATH, f"//span[text()='{name_templates}']")
        # except NoSuchElementException:
        #     time.sleep(3)
        #     templates_download = driver.find_element(By.XPATH, f"//span[text()='{name_templates}']")
        # templates_download
        try:
            self.click_to_element(Locators.TEXT_AREA_ARTICLE)
        except TimeoutException:
            time.sleep(10)
            self.click_to_element(Locators.TEXT_AREA_ARTICLE)
        self.click_to_element(self.Locators.DROPDOWN)
        frame = self.elements_is_present(self.Locators.FRAME)
        self.switch_to_frame(frame)
        self.click_to_element(self.Locators.DROP_DOWN_FILES)
        self.switch_out_frame()
        self.download_files_is_visible()
        # time.sleep(1)
        self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(path)
        self.click_to_element(self.Locators.CLOSE_DOWNLOAD_WINDOW)
        check_text_warning = self.element_is_visible(self.Locators.CHECK_TEXT_WARNING).text
        assert check_text_warning == "Ошибка загрузки файлов"
        self.click_to_element(self.Locators.SHOW_BUTTON)
        check_text_big_file_err = self.element_is_visible(self.Locators.CHECK_TEXT_BIG_FILE_ERR).text
        # assert check_text_big_file_err == "Размер файла не должен превышать 100 Мб", "В тексте всплывающего окна должно быть: 100 Мб!"
        time.sleep(2)
        os.remove(path)

    def download_files_from_files(self):
        path_1 = Path(pathlib.Path.cwd(), "files", "png_g.png")
        path1 = str(path_1)
        path2 = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        path3 = str(Path(pathlib.Path.cwd(), "files", "animal.jpeg"))
        path4 = str(Path(pathlib.Path.cwd(), "files", "pe.pdf"))
        path5 = str(Path(pathlib.Path.cwd(), "files", "gomer.gif"))
        # path = str(big_file)
        data_path = [path1, path2, path3, path4, path5]
        try:
            self.click_to_element(Locators.CREATE_BUTTON)
        except StaleElementReferenceException:
            time.sleep(2)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_ARTICLE)
        try:
            self.click_to_element(Locators.CREATE_ARTICLE)
        except TimeoutException:
            time.sleep(5)
        self.elements_is_present(self.Locators.UPLOAD_MEDIA).click()
        self.download_files_is_visible()
        # time.sleep(1)
        """download files"""
        for n in data_path:
            self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(n)
        # time.sleep(1)

    def check_script_download_bigfile(self):
        path = str(Path(pathlib.Path.cwd(), "bigfile.csv"))
        # path = str(big_file)
        time.sleep(0.5)
        self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(self.Locators.CREATE_SCRIPT)
        self.click_to_element(self.Locators.ADD_STEP)
        self.click_to_element(self.Locators.TEXT_AREA)
        self.click_to_element(self.Locators.DROPDOWN)
        frame = self.elements_is_present(self.Locators.FRAME)
        self.switch_to_frame(frame)
        self.click_to_element(self.Locators.DROP_DOWN_FILES)
        self.switch_out_frame()
        self.download_files_is_visible()
        time.sleep(1)
        self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(path)
        self.click_to_element(self.Locators.CLOSE_DOWNLOAD_WINDOW)
        check_text_warning = self.element_is_visible(self.Locators.CHECK_TEXT_WARNING).text
        assert check_text_warning == "Ошибка загрузки файлов"
        self.click_to_element(self.Locators.SHOW_BUTTON)
        check_text_big_file_err = self.element_is_visible(self.Locators.CHECK_TEXT_BIG_FILE_ERR).text
        # assert check_text_big_file_err == "Размер файла не должен превышать 100 Мб", "В тексте всплывающего окна должно быть: 100 Мб!"
        time.sleep(2)
        os.remove(path)

    def check_script_download(self, driver):
        data_files = generated_file()
        try:
            self.click_to_element(Locators.CREATE_BUTTON)
        except StaleElementReferenceException:
            time.sleep(3)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(self.Locators.CREATE_SCRIPT)
        try:
            self.click_to_element(self.Locators.ADD_STEP)
        except (TimeoutException, ElementClickInterceptedException):
            time.sleep(3)
            self.click_to_element(self.Locators.ADD_STEP)
        try:
            self.click_to_element(self.Locators.TEXT_AREA)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.TEXT_AREA)
        self.click_to_element(self.Locators.DROPDOWN)
        frame = self.elements_is_present(self.Locators.FRAME)
        self.switch_to_frame(frame)
        self.click_to_element(self.Locators.DROP_DOWN_FILES)
        self.switch_out_frame()
        time.sleep(1)
        self.check_tooltip(driver)
        """for visible"""
        self.download_files_is_visible()
        for n in data_files:
            file_type = Path(pathlib.Path.cwd(), f"{n}")
            path = str(file_type)
            self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(path)
        time.sleep(5)  # ожидание перед удалением
        for n in data_files:
            file_type = Path(pathlib.Path.cwd(), f"{n}")
            path = str(file_type)
            os.remove(path)













































import pathlib
import random
import time
from pathlib import Path

from selenium.common import StaleElementReferenceException, ElementNotInteractableException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.form_pages_locators import FormPagesLocators
from locators.topic_database_locators import CreateTopicDatabaseLocators
from pages.base_page import BasePage


class RepeatFunction(BasePage):
    def create_and_open_new_article(self, driver):
        """CREATE AND OPEN NEW ARTICLE"""
        Locators = CreateTopicDatabaseLocators

        person = generated_person()
        first_name = person.first_name
        text = "Hello"
        # data_files = generated_file()
        """upload media"""
        try:
            self.element_is_visible(Locators.CREATE_BUTTON, timeout=1).click()
        except StaleElementReferenceException:
            time.sleep(2)
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        self.element_is_visible(Locators.CREATE_ARTICLE).click()
        """input name and text an folder direct"""
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys(first_name)
        try:
            self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE, timeout=2).send_keys("Контент 1")
        except ElementNotInteractableException:
            time.sleep(2)
            self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")
        try:
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE, timeout=2).send_keys(text)
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE).send_keys(text)
        try:
            self.elements_is_present(Locators.UPLOAD_MEDIA, timeout=2).click()
        except TimeoutException:
            time.sleep(5)
            self.elements_is_present(Locators.UPLOAD_MEDIA).click()
        """input is visible for load files"""
        self.driver.execute_script(
            """document.querySelector(".popup__footer.file-manager__foot.file-manager--hidden").removeAttribute('class')""")
        self.driver.execute_script(
            """document.querySelector("form[enctype='multipart/form-data']").removeAttribute('style')""")
        path1 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        data_path = [path1, path2]
        for n in data_path:
            self.element_is_visible(Locators.INPUT_INVISIBLE).send_keys(n)
        time.sleep(5)
        checkbox_insert_files = self.elements_are_visible(Locators.CHECKBOX_INSERT_FILES)
        for n in checkbox_insert_files:
            time.sleep(0.5)
            n.click()
        try:
            self.element_is_visible(Locators.INPUT_SELECTED, timeout=2).click()
        except ElementClickInterceptedException:
            time.sleep(2)
            self.element_is_visible(Locators.INPUT_SELECTED).click()
            # self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()



    def create_and_open_new_template(self, driver):
        """CREATE AND OPEN NEW TEMPLATE"""
        Locators = FormPagesLocators
        self.element_is_visible(Locators.NEW_TEMPLATE).click()
        self.element_is_visible(Locators.ADD_FIELD_BUTTON).click()
        self.element_is_visible(Locators.LIST_OF_FIELDS_1).click()
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(Locators.SAVE_TEMPLATES).click()
        name_templates = "for download file testing" + str(random.randint(999, 99999))
        self.element_is_visible(Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name_templates)
        self.element_is_visible(Locators.SAVE_TEMPLATES_CHANGE).click()
        self.element_is_visible(Locators.FINISH_BUTTON_SCRIPT).click()
        time.sleep(2)
        templates_download = driver.find_element(By.XPATH, f"//div[text()='{name_templates}']")
        templates_download.click()



    def add_edit_question_script(self):
        Locators = CreateTopicDatabaseLocators
        self.input_in_my_project(self.driver)
        try:
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        except StaleElementReferenceException:
            time.sleep(3)
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        self.element_is_visible(Locators.CREATE_SCRIPT).click()

        self.element_is_visible(Locators.NAME_OF_STEP_SCRIPT).send_keys("NAME_SCRIPT-"+str(random.randint(99, 999)))
        self.element_is_visible(Locators.DIRECT_FOLDER).send_keys("Контент 1")

        self.element_is_visible(Locators.ADD_STEP).click()

        self.element_is_visible(Locators.INPUT_NAME_STEP).send_keys("name_step-"+str(random.randint(99, 999)))
        self.element_is_visible(Locators.DROPDOWN_STEP).send_keys("Сценарий завершён")
        try:
            self.element_is_visible(Locators.TEXT_AREA).click()
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(Locators.TEXT_AREA).click()
        self.element_is_visible(Locators.DROPDOWN).click()
        frame = self.elements_is_present(Locators.FRAME)
        self.switch_to_frame(frame)
        self.element_is_visible(Locators.DROP_DOWN_FILES).click()
        self.switch_out_frame()
        time.sleep(1)
        """for visible"""
        self.download_files_is_visible()
        path1 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        data_path = [path1, path2]
        for n in data_path:
            self.element_is_visible(Locators.INPUT_INVISIBLE).send_keys(n)
        time.sleep(5)
        checkbox_insert_files = self.elements_are_visible(Locators.CHECKBOX_INSERT_FILES)
        for n in checkbox_insert_files:
            time.sleep(0.5)
            n.click()
        try:
            self.element_is_visible(Locators.INPUT_SELECTED).click()
        except ElementClickInterceptedException:
            time.sleep(2)
            self.element_is_visible(Locators.INPUT_SELECTED).click()
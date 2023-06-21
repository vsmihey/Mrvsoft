import pathlib
import random
import sys
import time
from pathlib import Path

from selenium.common import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.locators_checking_filter_changes import AddFilterChangesLocators
from locators.locators_form_pages import FormPagesLocators
from locators.locators_topic_database import CreateTopicDatabaseLocators
from pages import repeat_function
from pages.base_page import BasePage
from pages.data_login_password import url
from pages.repeat_function import RepeatFunction


class AddFilterChanges(BasePage):

    Locators = AddFilterChangesLocators()

    def add_filters_mass_change(self, count_filters=3):
        """ADD 3 FILTERS"""
        self.input_in_my_project(self.driver)
        self.element_is_visible(self.Locators.SETTINGS).click()
        self.element_is_visible(self.Locators.FILTERS_FOR_SEARCHING).click()
        try:
            self.element_is_visible(self.Locators.BUTTON_CREATE_GROUP_FILTER, timeout=2).click()
        except TimeoutException:
            """del 3 filters and group"""
            self.element_is_visible(self.Locators.SVG_DEL_1).click()
            self.element_is_visible(self.Locators.SVG_DEL_LIST_CONFIRM).click()
            self.element_is_visible(self.Locators.SVG_DEL_2).click()
            self.element_is_visible(self.Locators.SVG_DEL_LIST_CONFIRM).click()
            self.element_is_visible(self.Locators.SVG_DEL_3).click()
            self.element_is_visible(self.Locators.SVG_DEL_LIST_CONFIRM).click()
            # time.sleep(1)
            # svg_del_list = self.elements_are_visible(self.Locators.SVG_DEL_LIST)
            # for n in svg_del_list:
            #     time.sleep(1)
            #     n.click()
            #     time.sleep(1)
            #     self.element_is_visible(self.Locators.SVG_DEL_LIST_CONFIRM).click()
            self.element_is_visible(self.Locators.CHANGE_NAME_GROUP).click()
            self.element_is_visible(self.Locators.BUTTON_DEL_GROUP).click()
            self.element_is_visible(self.Locators.BUTTON_DEL_GROUP_CONFIRM).click()
            self.element_is_visible(self.Locators.BUTTON_CREATE_GROUP_FILTER).click()
        self.element_is_visible(self.Locators.INPUT_NAME_GROUP).send_keys("Groupname_1")
        self.element_is_visible(self.Locators.BUTTON_GROUP_ADD).click()
        """add filters"""
        for n in range(count_filters):
            self.element_is_visible(self.Locators.BUTTON_ADD_FILTER).click()
            self.element_is_visible(self.Locators.INPUT_NAME_FILTER).send_keys("Filtername"+str(random.randint(999, 9999)))
            self.element_is_visible(self.Locators.BUTTON_ADD_FILTER_ADD).click()
            """close window"""
        self.element_is_visible(self.Locators.SVF_CLOSE_WINDOW).click()

    def create_article_mass_change(self, driver):
        """CREATE AND OPEN NEW ARTICLE"""
        self.input_in_my_project(self.driver)
        Locators = CreateTopicDatabaseLocators
        person = generated_person()
        first_name = person.first_name + str(random.randint(999, 9999))
        text = "Hello"
        name_request = "Request for article " + str(random.randint(999, 9999))
        text_alert = "Alert " + str(random.randint(999, 9999))
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
        self.element_is_visible(Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request)
        self.element_is_visible(self.Locators.BUTTON_ADD).click()
        self.element_is_visible(self.Locators.RADIOBUTTON_INCLUDED_CONTENT).click()
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys(text_alert)
        print(first_name, name_request)
        return first_name, name_request

    # @staticmethod
    def add_article_by_template_mass_change(self, driver):
        self.input_in_my_project(self.driver)
        Locators = FormPagesLocators
        actions = ActionChains(driver)
        driver.implicitly_wait(10)
        person = generated_person()
        name = "Templates" + str(random.randint(999, 99999))
        name_content = "Content" + str(random.randint(999, 99999))
        try:
            self.element_is_visible(Locators.CREATE_BUTTON_ON_HEAD_PAGE).click()
        except StaleElementReferenceException:
            time.sleep(2)
            self.element_is_visible(Locators.CREATE_BUTTON_ON_HEAD_PAGE).click()
        self.element_is_visible(Locators.CREATE_TEMPLATES).click()
        self.element_is_visible(Locators.CREATE_TEMPLATES_NEW).click()
        for i in range(1, 6):
            time.sleep(1)
            self.element_is_visible(Locators.ADD_FIELD_BUTTON).click()
            list_of_fields = driver.find_element(By.XPATH,
                                                 f"//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[{i}]")
            list_of_fields.click()
            self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys(
                "Name" + str(random.randint(999, 99999)))
            self.element_is_visible(Locators.SAVE_TEMPLATES).click()
        self.element_is_visible(Locators.ADD_FIELD_BUTTON).click()
        list_of_fields = driver.find_element(By.XPATH,
                                             f"//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[6]")
        list_of_fields.click()
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(Locators.ANSWER).send_keys("answer 1")
        self.element_is_visible(Locators.ADD_ANSWER).click()
        self.element_is_visible(Locators.SAVE_BUTTON).click()
        """step 5"""
        self.element_is_visible(Locators.ADD_FIELD_BUTTON).click()
        self.element_is_visible(Locators.LIST_OF_FIELDS_2).click()
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(Locators.CHECKBOX_VALUE).click()
        self.element_is_visible(Locators.INPUT_VALUE).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(Locators.SAVE_TEMPLATES).click()
        """step 6"""
        self.element_is_visible(Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name)
        # print(name)
        self.element_is_visible(Locators.SAVE_CREATED_TEMPLATES).click()
        self.element_is_visible(Locators.SUBMIT_TEMPLATES).click()
        name_of_templates = driver.find_element(By.XPATH, f"//div[contains(text(),'{name}')]")
        name_of_templates.click()
        self.element_is_visible(Locators.check_name_input).send_keys(name_content)
        # print(name_content)
        time.sleep(3)
        self.element_is_visible(Locators.FOLDER_SAVE).send_keys("Контент 1")
        try:
            field_input = self.element_is_visible(Locators.EDIT_TEMPLATES)
        except TimeoutException:
            time.sleep(1)
            field_input = self.element_is_visible(Locators.EDIT_TEMPLATES)
        field_input_1 = self.element_is_visible(Locators.EDIT_TEMPLATES_1)
        field_input_2 = self.element_is_visible(Locators.EDIT_TEMPLATES_2)
        field_input_3 = self.element_is_visible(Locators.EDIT_TEMPLATES_3)
        field_input_4 = self.element_is_visible(Locators.EDIT_TEMPLATES_4)
        field_input_5 = self.element_is_visible(Locators.EDIT_TEMPLATES_5)
        # field_input_6 = self.element_is_visible(Locators.CHOSE_ANSWER)
        """add and check text correct link"""
        actions.click(field_input_1)
        actions.send_keys("some text")
        actions.click(field_input_2)
        actions.click(field_input_2)
        actions.send_keys("one more some text")
        actions.click(field_input_3)
        actions.click(field_input_3)
        actions.send_keys("777")
        actions.click(field_input_4)
        actions.click(field_input_4)
        actions.send_keys("https://www.something.com")
        actions.click(field_input_5)
        actions.click(field_input_5)
        mail = person.email
        actions.send_keys(mail)
        actions.click(field_input)
        actions.perform()
        time.sleep(1)
        check_name_of_templates = driver.find_element(By.XPATH, f"//h1[normalize-space()='{name}']")
        check_name_of_templates.is_displayed()
        self.element_is_visible(Locators.CHANGE_TEMPLATES_BUTTON).is_displayed()
        time.sleep(1)
        self.element_is_visible(Locators.TYPOGRAPHY_TEMPLATE).click()
        self.element_is_visible(Locators.SUBMIT_TEMPLATES).click()
        input_request = self.element_is_visible(Locators.INPUT_REQUEST)
        requests_name = "как помыть крота" + str(random.randint(999, 99999))
        input_request.send_keys(requests_name)
        self.element_is_visible(Locators.ADD_SEARCH_BUTTON).click()
        self.element_is_visible(Locators.FIELD_OF_CONTENT_RADIO).click()
        """fixing_all_fields"""
        select_field_for_fixing = self.element_is_visible(Locators.SELECT_FIELD_FOR_FIXING)
        for i in range(6):
            time.sleep(0.5)
            select_field_for_fixing.click()
            select_field_for_fixing.send_keys(Keys.DOWN)
            select_field_for_fixing.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.FINISH_BUTTON).click()
        self.element_is_visible(Locators.SUBMIT_TEMPLATES).click()
        self.element_is_visible(Locators.TEXT_AREA_ALERT).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(Locators.SUBMIT_TEMPLATES).click()
        print(name, name_content, name_of_templates, requests_name)
        return name, name_content, name_of_templates, requests_name

    def add_script_mass_change(self):
        self.input_in_my_project(self.driver)
        action = ActionChains(self.driver)
        Locators = CreateTopicDatabaseLocators
        name_request_script = "Request " + str(random.randint(999, 9999))
        try:
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        except StaleElementReferenceException:
            time.sleep(3)
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        self.element_is_visible(Locators.CREATE_SCRIPT).click()
        self.element_is_visible(Locators.NAME_OF_STEP_SCRIPT).send_keys("NAME_SCRIPT-" + str(random.randint(99, 999)))
        time.sleep(1)
        self.element_is_visible(self.Locators.DIRECT_FOLDER).send_keys("Контент 1")
        self.element_is_visible(Locators.ADD_STEP).click()
        self.element_is_visible(Locators.INPUT_NAME_STEP).send_keys("name_step-" + str(random.randint(99, 999)))
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
        button_typography = self.elements_is_present(self.Locators.BUTTON_TYPOGRAPHY)
        action.click(button_typography).perform()
        # action.perform()
        # self.element_is_visible(Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request_script)
        self.element_is_visible(self.Locators.BUTTON_ADD).click()
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.BUTTON_FINISH_CONFIRM).click()
        self.element_is_visible(self.Locators.BUTTON_FINISH_CONFIRM).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("Alert " + str(random.randint(999, 9999)))
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        print(name_request_script)
        return name_request_script

    def check_mass_change_filters_article(self):
        self.input_in_my_project(self.driver)
        self.element_is_visible(self.Locators.MEATBALL_MENU).click()
        self.element_is_visible(self.Locators.MASS_CHANGE).click()
        self.element_is_visible(self.Locators.DROPDOWN_FILTERS_FOR_SEARCHING).send_keys("Фильтры для поиска")
        """check dropdown"""
        dropdown_actions = self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).text
        assert dropdown_actions == 'Не выбрано\nДобавить\nУдалить'
        time.sleep(1)
        """check filters sort"""
        data = []
        # dropdown_filter = self.elements_is_present(self.Locators.DROPDOWN_FILTERS).text
        dropdown_filter1 = self.elements_is_present(self.Locators.FILTER1).text
        dropdown_filter2 = self.elements_is_present(self.Locators.FILTER2).text
        dropdown_filter3 = self.elements_is_present(self.Locators.FILTER3).text
        data.append(dropdown_filter1)
        data.append(dropdown_filter2)
        data.append(dropdown_filter3)
        data_sort = self.data_sort(data)
        # print(data, len(data), data_sort)
        assert data == data_sort
        dropdown_filter = self.elements_is_present(self.Locators.DROPDOWN_FILTERS_TEXT).text
        assert dropdown_filter == "Не выбрано"
        # data_text_in_filters = []
        # dropdown_filter = self.element_is_visible(self.Locators.DROPDOWN_FILTERS).text
        # data_text_in_filters.append(dropdown_filter)
        # print(data_text_in_filters)
        # assert data_text_in_filters[0] == 'Не выбрано'
        """check button click"""
        element = self.element_is_visible(self.Locators.BUTTON_BACK, timeout=1)
        self.check_button_click(element)
        element = self.element_is_visible(self.Locators.BUTTON_CONTINUE, timeout=1)
        self.check_button_click(element)
        """check tooltips"""




        time.sleep(3)




    # def ser(self, driver):
    #     self.input_in_my_project(driver)
    #     time.sleep(6)
        # rf = RepeatFunction
        # rf.create_article_by_templates_repeat(self.driver, driver)

        # name, name_content, name_of_templates, requests_name = RepeatFunction.create_article_by_templates_repeat(self.driver, driver)
        # print(name)











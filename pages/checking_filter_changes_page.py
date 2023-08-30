import pathlib
import random
import time
from pathlib import Path

from selenium.common import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException, NoSuchElementException, WebDriverException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.locators_checking_filter_changes import AddFilterChangesLocators
from locators.locators_form_pages import FormPagesLocators
from locators.locators_topic_database import CreateTopicDatabaseLocators
from pages.authorisation_page import Authorisation
from pages.base_page import BasePage


class AddFilterChanges(Authorisation, BasePage):

    Locators = AddFilterChangesLocators()

    def add_filters_mass_change(self, count_filters=3):
        """ADD 3 FILTERS"""
        # self.input_in_my_project(self.driver)
        self.click_to_element(self.Locators.SETTINGS)
        self.click_to_element(self.Locators.FILTERS_FOR_SEARCHING)
        try:
            self.click_to_element(self.Locators.BUTTON_CREATE_GROUP_FILTER, timeout=2)
        except TimeoutException:
            """del 3 filters and group"""
            self.click_to_element(self.Locators.SVG_DEL_1)
            self.click_to_element(self.Locators.SVG_DEL_LIST_CONFIRM)
            self.click_to_element(self.Locators.SVG_DEL_2)
            self.click_to_element(self.Locators.SVG_DEL_LIST_CONFIRM)
            self.click_to_element(self.Locators.SVG_DEL_3)
            self.click_to_element(self.Locators.SVG_DEL_LIST_CONFIRM)
            self.click_to_element(self.Locators.CHANGE_NAME_GROUP)
            self.click_to_element(self.Locators.BUTTON_DEL_GROUP)
            self.click_to_element(self.Locators.BUTTON_DEL_GROUP_CONFIRM)
            self.click_to_element(self.Locators.BUTTON_CREATE_GROUP_FILTER)
        self.element_is_visible(self.Locators.INPUT_NAME_GROUP).send_keys("Groupname_1")
        self.click_to_element(self.Locators.BUTTON_GROUP_ADD)
        """add filters"""
        for n in range(count_filters):
            self.click_to_element(self.Locators.BUTTON_ADD_FILTER)
            self.element_is_visible(self.Locators.INPUT_NAME_FILTER).send_keys("Filtername"+str(random.randint(999, 9999)))
            self.click_to_element(self.Locators.BUTTON_ADD_FILTER_ADD)
            """close window"""
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW)

    def create_article_mass_change(self, driver):
        """CREATE AND OPEN NEW ARTICLE"""
        # self.input_in_my_project(self.driver)
        Locators = CreateTopicDatabaseLocators
        person = generated_person()
        first_name = person.first_name + str(random.randint(999, 9999))
        text = "Hello"
        name_request = "request for article " + str(random.randint(999, 9999))
        text_alert = "Alert " + str(random.randint(999, 9999))
        """upload media"""
        try:
            self.click_to_element(Locators.CREATE_BUTTON, timeout=1)
        except StaleElementReferenceException:
            time.sleep(2)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_ARTICLE)
        """input name and text an folder direct"""
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys(first_name)
        try:
            self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE, timeout=2).send_keys("Контент 1")
        except ElementNotInteractableException:
            time.sleep(2)
            self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")
        time.sleep(1)
        try:
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE, timeout=2).send_keys(text)
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE).send_keys(text)
        try:
            self.click_to_element(Locators.UPLOAD_MEDIA, timeout=2)
        except TimeoutException:
            time.sleep(5)
            self.click_to_element(Locators.UPLOAD_MEDIA)
        """input is visible for load files"""
        time.sleep(1)
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
            self.click_to_element(Locators.INPUT_SELECTED, timeout=2)
        except ElementClickInterceptedException:
            time.sleep(2)
            self.click_to_element(Locators.INPUT_SELECTED)
        self.click_to_element(Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(Locators.BUTTON_SUBMIT)
        time.sleep(1)
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request)
        time.sleep(1)
        self.click_to_element(self.Locators.BUTTON_ADD)
        self.click_to_element(self.Locators.RADIOBUTTON_INCLUDED_CONTENT)
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys(text_alert)
        self.click_to_element(Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
        return first_name, name_request, text

    # @staticmethod
    def add_article_by_template_mass_change(self, driver):
        # self.input_in_my_project(self.driver)
        Locators = FormPagesLocators
        actions = ActionChains(driver)
        self.browser.implicitly_wait(10)
        person = generated_person()
        name = "Templates" + str(random.randint(9999, 99999))
        name_content = "Content" + str(random.randint(9999, 99999))
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
            list_of_fields = self.browser.find_element(By.XPATH,
                                                 f"//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[{i}]")
            list_of_fields.click()
            self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys(
                "Name" + str(random.randint(999, 99999)))
            self.click_to_element(Locators.SAVE_TEMPLATES)
        self.click_to_element(Locators.ADD_FIELD_BUTTON)
        list_of_fields = self.browser.find_element(By.XPATH,
                                             f"//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[6]")
        list_of_fields.click()
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(Locators.ANSWER).send_keys("answer 1")
        self.click_to_element(Locators.ADD_ANSWER)
        self.click_to_element(Locators.SAVE_BUTTON)
        """step 5"""
        self.click_to_element(Locators.ADD_FIELD_BUTTON)
        self.click_to_element(Locators.LIST_OF_FIELDS_2)
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.click_to_element(Locators.CHECKBOX_VALUE)
        self.element_is_visible(Locators.INPUT_VALUE).send_keys("Name" + str(random.randint(999, 99999)))
        self.click_to_element(Locators.SAVE_TEMPLATES)
        """step 6"""
        self.element_is_visible(Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name)
        self.click_to_element(Locators.SAVE_CREATED_TEMPLATES)
        self.click_to_element(Locators.SUBMIT_TEMPLATES)
        # скролл
        # locator_scroller = self.element_is_visible(Locators.MODAL_WINDOW_SCROLLER, timeout=3)
        self.scroll_wizard_template(name, driver)
        # n = 0
        # while True:
        #     if n == 7:
        #         break
        #     try:
        #         name_of_templates = self.browser.find_element(By.XPATH, f"//span[contains(text(),'{name}')]")
        #         name_of_templates.click()
        #         break
        #     except NoSuchElementException:
        #         self.scroll_wizard_template(name, driver)
        #         n += 1

        time.sleep(1)
        # name_of_templates.click()
        self.element_is_visible(Locators.check_name_input).send_keys(name_content)
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
        self.click_to_element(Locators.TYPOGRAPHY_TEMPLATE)
        self.click_to_element(Locators.SUBMIT_TEMPLATES)
        input_request = self.element_is_visible(Locators.INPUT_REQUEST)
        requests_name = "как помыть крота" + str(random.randint(999, 99999))
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
        self.element_is_visible(Locators.TEXT_AREA_ALERT).send_keys("Name" + str(random.randint(999, 99999)))
        self.click_to_element(Locators.SUBMIT_TEMPLATES)
        # print(name, name_content, requests_name)
        return name, name_content, requests_name

    def add_script_mass_change(self, driver):
        # self.input_in_my_project(self.driver)
        actions = ActionChains(driver)
        Locators = CreateTopicDatabaseLocators
        name_request_script = "request " + str(random.randint(999, 9999))
        name_script = "NAME_SCRIPT-" + str(random.randint(99, 999))
        try:
            self.click_to_element(Locators.CREATE_BUTTON)
        except StaleElementReferenceException:
            time.sleep(3)
            self.click_to_element(Locators.CREATE_BUTTON)
        self.click_to_element(Locators.CREATE_SCRIPT)
        self.element_is_visible(Locators.NAME_OF_STEP_SCRIPT).send_keys(name_script)
        time.sleep(2)
        self.element_is_visible(self.Locators.DIRECT_FOLDER).send_keys("Контент 1")
        self.click_to_element(Locators.ADD_STEP)
        self.element_is_visible(Locators.INPUT_NAME_STEP).send_keys("name_step-" + str(random.randint(99, 999)))
        self.element_is_visible(Locators.DROPDOWN_STEP).send_keys("Сценарий завершён")
        try:
            self.click_to_element(Locators.TEXT_AREA)
        except TimeoutException:
            time.sleep(5)
            self.click_to_element(Locators.TEXT_AREA)
        self.click_to_element(Locators.DROPDOWN)
        frame = self.elements_is_present(Locators.FRAME)
        self.switch_to_frame(frame)
        self.click_to_element(Locators.DROP_DOWN_FILES)
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
            self.click_to_element(Locators.INPUT_SELECTED)
        except ElementClickInterceptedException:
            time.sleep(5)
            self.click_to_element(Locators.INPUT_SELECTED)
        time.sleep(1)
        button_typography = self.elements_is_present(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        button_typography.click()
        # time.sleep(1)
        # actions.click(button_typography)
        # actions.perform()
        # actions.perform()
        # self.click_to_element(Locators.BUTTON_TYPOGRAPHY)
        self.element_is_visible(self.Locators.INPUT_NAME_REQUEST).send_keys(name_request_script)
        self.click_to_element(self.Locators.BUTTON_ADD)
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.BUTTON_FINISH_CONFIRM)
        self.click_to_element(self.Locators.BUTTON_FINISH_CONFIRM)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("Alert " + str(random.randint(999, 9999)))
        self.click_to_element(self.Locators.BUTTON_FINISH)
        # print(name_request_script)
        return name_request_script, name_script

    def check_mass_change_filters_article(self, driver):
        first_name, name_request, text = self.create_article_mass_change(driver)
        action = ActionChains(driver)
        try:
            self.click_to_element(self.Locators.MEATBALL_MENU, timeout=5)
        except (StaleElementReferenceException, WebDriverException):
            time.sleep(3)
            self.click_to_element(self.Locators.MEATBALL_MENU)
        time.sleep(1)
        try:
            self.click_to_element(self.Locators.MASS_CHANGE)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.MASS_CHANGE)
        self.element_is_visible(self.Locators.DROPDOWN_FILTERS_FOR_SEARCHING).send_keys("Фильтры для поиска")
        """check dropdown"""
        try:
            dropdown_actions = self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).text
        except TimeoutException:
            time.sleep(3)
            dropdown_actions = self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).text
        assert dropdown_actions == 'Не выбрано\nДобавить\nУдалить'
        time.sleep(1)
        """check filters sort"""
        dropdown_filter = self.elements_is_present(self.Locators.DROPDOWN_FILTERS)
        dropdown_filter_value = dropdown_filter.text
        list_split = dropdown_filter_value.split("\n")
        del list_split[0]
        data_sort = self.data_sort(data=list_split)
        assert data_sort == list_split
        """check button click"""
        element = self.element_is_visible(self.Locators.BUTTON_BACK, timeout=1)
        self.check_button_not_click(element)
        element = self.element_is_visible(self.Locators.BUTTON_CONTINUE, timeout=1)
        self.check_button_not_click(element)
        """check tooltips"""
        tooltip_action = self.elements_is_present(self.Locators.TOOLTIP_ACTION)
        ta = tooltip_action.get_attribute("data-tip")
        assert ta == "Выберите действие, которое необходимо сделать с контентом"
        tooltip_filters = self.elements_is_present(self.Locators.TOOLTIP_FILTERS)
        tf = tooltip_filters.get_attribute("data-tip")
        assert tf == "С помощью фильтров контент будет проще найти сокращая область поиска"
        """---add action---"""
        self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).send_keys("Добавить")
        """check button click"""
        element = self.element_is_visible(self.Locators.BUTTON_CONTINUE, timeout=1)
        self.check_button_not_click(element)
        """---add filter---"""
        self.click_to_element(self.Locators.DROPDOWN_FILTERS)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN).perform()
        try:
            self.element_is_visible(self.Locators.LIST_ADDED_FILTERS).is_displayed()
        except (TimeoutException, ElementClickInterceptedException):
            print("Сначала добавьте фильтры")
        """check button click"""
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        self.browser.refresh()
        self.element_is_visible(self.Locators.DROPDOWN_FILTERS_FOR_SEARCHING).send_keys("Фильтры для поиска")
        """---add filter---"""
        self.click_to_element(self.Locators.DROPDOWN_FILTERS)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN).perform()
        self.element_is_visible(self.Locators.LIST_ADDED_FILTERS).is_displayed()
        """check button click"""
        element = self.element_is_visible(self.Locators.BUTTON_CONTINUE, timeout=1)
        self.check_button_not_click(element)
        """---add action---"""
        self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).send_keys("Добавить")
        """check button click"""
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        self.element_is_visible(self.Locators.INPUT_SEARCH_CONTENT_BY_NAME_FOR_ADD_FILTERS).send_keys(first_name)
        time.sleep(1)
        self.click_to_element(self.Locators.CREATED_CONTENT_FOR_FILTERS)
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        # print(first_name, name_request, text)
        """check article after add filters"""
        time.sleep(5)
        try:
            self.click_to_element(self.Locators.FILTERS)
        except (StaleElementReferenceException, TimeoutException):
            time.sleep(5)
            self.click_to_element(self.Locators.FILTERS)
        try:
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{first_name}']")
            article_firs_name.click()
        except NoSuchElementException:
            time.sleep(5)
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{first_name}']")
            article_firs_name.click()
            # article_firs_name = self.browser.find_element(By.XPATH, f"//p[text()='{first_name}']")
        # self.click_to_element(self.Locators.FILTERS_FIRST_NAME)
        time.sleep(1)
        # try:
        #     article_firs_name.click()
        # except StaleElementReferenceException:
        #     time.sleep(3)
        #     article_firs_name.click()
        """check content"""
        self.element_is_visible(self.Locators.TEXT_ARTICLE).is_displayed()
        try:
            self.element_is_visible(self.Locators.VIDEO_ARTICLE).is_displayed()
        except (TimeoutException, StaleElementReferenceException):
            pass
        try:
            self.element_is_visible(self.Locators.AUDIO_ARTICLE).is_displayed()
        except TimeoutException:
            time.sleep(3)
            self.element_is_visible(self.Locators.AUDIO_ARTICLE).is_displayed()
        time.sleep(1)
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        time.sleep(2)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY, timeout=3)
        except (ElementClickInterceptedException, TimeoutException):
            time.sleep(2)
            "Если появляется сообщение о черновике"
            try:
                # self.element_is_visible(self.Locators.ALERT_FOR_DRAFT, timeout=3).is_displayed()
                self.delete_draft()
                time.sleep(3)
                self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
            # except TimeoutException:
            #     self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
            # self.click_to_element(self.Locators.CHANGE_ARTICLE)
            except (ElementClickInterceptedException, TimeoutException):
                self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_ARTICLE_BACK)
        time.sleep(1)
        self.click_to_element(self.Locators.BUTTON_ARTICLE_BACK)
        time.sleep(1)
        text_request_article = self.element_is_visible(self.Locators.TEXT_REQUEST_ARTICLE).text
        # print("Запрос-"+text_request_article)
        assert text_request_article == name_request
        """change filters"""
        self.click_to_element(self.Locators.SVG_DELETE_FILTER_ADDED)
        self.click_to_element(self.Locators.DROPDOWN_FILTERS_FOR_CHANGE)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN).perform()
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("Alert " + str(random.randint(9, 99)))
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
        """check article after add filters"""
        time.sleep(5)
        try:
            filters = self.elements_are_visible(self.Locators.FILTERS)
        except TimeoutException:
            time.sleep(3)
            filters = self.elements_are_visible(self.Locators.FILTERS)
        for n in filters:
            time.sleep(1)
            n.click()
        try:
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{first_name}']")
        except NoSuchElementException:
            time.sleep(5)
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{first_name}']")
        time.sleep(1)
        try:
            article_firs_name.click()
        except StaleElementReferenceException:
            time.sleep(3)
            article_firs_name.click()
        """check content"""
        self.element_is_visible(self.Locators.TEXT_ARTICLE).is_displayed()
        try:
            self.element_is_visible(self.Locators.VIDEO_ARTICLE).is_displayed()
        except (TimeoutException, StaleElementReferenceException):
            pass
        self.element_is_visible(self.Locators.AUDIO_ARTICLE).is_displayed()
        time.sleep(2)
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        time.sleep(3)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY, timeout=10)
        except TimeoutException:
            time.sleep(10)
            # driver.refresh()
            # self.click_to_element(self.Locators.CHANGE_ARTICLE)
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_ARTICLE_BACK)
        self.click_to_element(self.Locators.BUTTON_ARTICLE_BACK)
        try:
            text_request_article = self.element_is_visible(self.Locators.TEXT_REQUEST_ARTICLE).text
        except ElementNotInteractableException:
            time.sleep(3)
            text_request_article = self.element_is_visible(self.Locators.TEXT_REQUEST_ARTICLE).text
        # print(text_request_article)
        assert text_request_article == name_request

    def check_mass_change_filters_template(self, driver):
        name, name_content, requests_name = self.add_article_by_template_mass_change(driver)
        # self.input_in_my_project(self.driver)
        action = ActionChains(driver)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
        try:
            self.click_to_element(self.Locators.MEATBALL_MENU, timeout=5)
        except (StaleElementReferenceException, WebDriverException):
            time.sleep(3)
            self.click_to_element(self.Locators.MEATBALL_MENU)
        try:
            self.click_to_element(self.Locators.MASS_CHANGE)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.MASS_CHANGE)
        self.element_is_visible(self.Locators.DROPDOWN_FILTERS_FOR_SEARCHING).send_keys("Фильтры для поиска")
        """check dropdown"""
        try:
            dropdown_actions = self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).text
        except TimeoutException:
            time.sleep(3)
            dropdown_actions = self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).text
        assert dropdown_actions == 'Не выбрано\nДобавить\nУдалить'
        time.sleep(1)
        """check filters sort"""
        dropdown_filter = self.elements_is_present(self.Locators.DROPDOWN_FILTERS)
        dropdown_filter_value = dropdown_filter.text
        list_split = dropdown_filter_value.split("\n")
        del list_split[0]
        data_sort = self.data_sort(data=list_split)
        # print(data_sort, list_split)
        assert data_sort == list_split
        """check button click"""
        element = self.element_is_visible(self.Locators.BUTTON_BACK, timeout=1)
        self.check_button_not_click(element)
        element = self.element_is_visible(self.Locators.BUTTON_CONTINUE, timeout=1)
        self.check_button_not_click(element)
        """check tooltips"""
        tooltip_action = self.elements_is_present(self.Locators.TOOLTIP_ACTION)
        ta = tooltip_action.get_attribute("data-tip")
        assert ta == "Выберите действие, которое необходимо сделать с контентом"
        tooltip_filters = self.elements_is_present(self.Locators.TOOLTIP_FILTERS)
        tf = tooltip_filters.get_attribute("data-tip")
        assert tf == "С помощью фильтров контент будет проще найти сокращая область поиска"
        """---add action---"""
        self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).send_keys("Добавить")
        """check button click"""
        element = self.element_is_visible(self.Locators.BUTTON_CONTINUE, timeout=1)
        self.check_button_not_click(element)
        """---add filter---"""
        self.click_to_element(self.Locators.DROPDOWN_FILTERS)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN).perform()
        try:
            self.element_is_visible(self.Locators.LIST_ADDED_FILTERS).is_displayed()
        except TimeoutException:
            print("Сначала добавьте фильтры")
        """check button click"""
        time.sleep(3)
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        self.browser.refresh()
        self.element_is_visible(self.Locators.DROPDOWN_FILTERS_FOR_SEARCHING).send_keys("Фильтры для поиска")
        """---add filter---"""
        try:
            self.click_to_element(self.Locators.DROPDOWN_FILTERS)
        except ElementClickInterceptedException:
            time.sleep(3)
            self.click_to_element(self.Locators.DROPDOWN_FILTERS)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN).perform()
        self.element_is_visible(self.Locators.LIST_ADDED_FILTERS).is_displayed()
        """check button click"""
        element = self.element_is_visible(self.Locators.BUTTON_CONTINUE, timeout=1)
        self.check_button_not_click(element)
        """---add action---"""
        self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).send_keys("Добавить")
        """check button click"""
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        self.element_is_visible(self.Locators.INPUT_SEARCH_CONTENT_BY_NAME_FOR_ADD_FILTERS).send_keys(name_content)
        time.sleep(1)
        self.click_to_element(self.Locators.CREATED_CONTENT_FOR_FILTERS)
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        # print(name, requests_name, name_content)
        """check article after add filters"""
        time.sleep(5)
        try:
            self.click_to_element(self.Locators.FILTERS)
        except (StaleElementReferenceException, TimeoutException):
            time.sleep(5)
            self.click_to_element(self.Locators.FILTERS)
        try:
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{name_content}']")
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
            time.sleep(5)
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{name_content}']")
        time.sleep(2)
        article_firs_name.click()
        """check content"""
        self.element_is_visible(self.Locators.FIELD_TEXT).is_displayed()
        self.element_is_visible(self.Locators.FIELD_TEXT_2).is_displayed()
        self.element_is_visible(self.Locators.FIELD_TEXT_777).is_displayed()
        self.element_is_visible(self.Locators.FIELD_TEXT_WEBSITE).is_displayed()
        self.element_is_visible(self.Locators.FIELD_TEXT_MAIL).is_displayed()
        self.element_is_visible(self.Locators.FIELD_TEXT_NAME).is_displayed()
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        time.sleep(1)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY, timeout=20)
        except (ElementClickInterceptedException, TimeoutException):
            time.sleep(5)
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_ARTICLE_BACK)
        text_request_article = self.element_is_visible(self.Locators.TEXT_REQUEST_ARTICLE).text
        assert text_request_article == requests_name
        """change filters"""
        self.click_to_element(self.Locators.SVG_DELETE_FILTER_ADDED)
        self.click_to_element(self.Locators.DROPDOWN_FILTERS_FOR_CHANGE)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN).perform()
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("Alert " + str(random.randint(9, 99)))
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
        """check article after add filters"""
        time.sleep(5)
        filters = self.elements_are_visible(self.Locators.FILTERS)
        for n in filters:
            n.click()
        try:
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{name_content}']")
        except NoSuchElementException:
            time.sleep(5)
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{name_content}']")
        article_firs_name.click()
        """check content"""
        self.element_is_visible(self.Locators.FIELD_TEXT).is_displayed()
        self.element_is_visible(self.Locators.FIELD_TEXT_2).is_displayed()
        self.element_is_visible(self.Locators.FIELD_TEXT_777).is_displayed()
        self.element_is_visible(self.Locators.FIELD_TEXT_WEBSITE).is_displayed()
        self.element_is_visible(self.Locators.FIELD_TEXT_MAIL).is_displayed()
        self.element_is_visible(self.Locators.FIELD_TEXT_NAME).is_displayed()
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        time.sleep(1)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY, timeout=20)
        except TimeoutException:
            time.sleep(10)
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        time.sleep(6)
        self.click_to_element(self.Locators.BUTTON_ARTICLE_BACK)
        text_request_article = self.element_is_visible(self.Locators.TEXT_REQUEST_ARTICLE).text
        assert text_request_article == requests_name

    def check_mass_change_filters_script(self, driver):
        name_request_script, name_script = self.add_script_mass_change(driver)
        action = ActionChains(driver)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
        try:
            self.click_to_element(self.Locators.MEATBALL_MENU, timeout=10)
        except (StaleElementReferenceException, WebDriverException):
            time.sleep(5)
            self.click_to_element(self.Locators.MEATBALL_MENU)
        try:
            self.click_to_element(self.Locators.MASS_CHANGE)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.MASS_CHANGE)
        self.element_is_visible(self.Locators.DROPDOWN_FILTERS_FOR_SEARCHING).send_keys("Фильтры для поиска")
        """check dropdown"""
        try:
            dropdown_actions = self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).text
        except TimeoutException:
            time.sleep(3)
            dropdown_actions = self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).text
        assert dropdown_actions == 'Не выбрано\nДобавить\nУдалить'
        time.sleep(1)
        """check filters sort"""
        dropdown_filter = self.elements_is_present(self.Locators.DROPDOWN_FILTERS)
        dropdown_filter_value = dropdown_filter.text
        list_split = dropdown_filter_value.split("\n")
        del list_split[0]
        data_sort = self.data_sort(data=list_split)
        assert data_sort == list_split
        """check button click"""
        element = self.element_is_visible(self.Locators.BUTTON_BACK, timeout=1)
        self.check_button_not_click(element)
        element = self.element_is_visible(self.Locators.BUTTON_CONTINUE, timeout=1)
        self.check_button_not_click(element)
        """check tooltips"""
        tooltip_action = self.elements_is_present(self.Locators.TOOLTIP_ACTION)
        ta = tooltip_action.get_attribute("data-tip")
        assert ta == "Выберите действие, которое необходимо сделать с контентом"
        tooltip_filters = self.elements_is_present(self.Locators.TOOLTIP_FILTERS)
        tf = tooltip_filters.get_attribute("data-tip")
        assert tf == "С помощью фильтров контент будет проще найти сокращая область поиска"
        """---add action---"""
        self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).send_keys("Добавить")
        """check button click"""
        element = self.element_is_visible(self.Locators.BUTTON_CONTINUE, timeout=1)
        self.check_button_not_click(element)
        """---add filter---"""
        self.click_to_element(self.Locators.DROPDOWN_FILTERS)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN).perform()
        try:
            self.element_is_visible(self.Locators.LIST_ADDED_FILTERS).is_displayed()
        except TimeoutException:
            print("Сначала добавьте фильтры")
        """check button click"""
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        self.browser.refresh()
        self.element_is_visible(self.Locators.DROPDOWN_FILTERS_FOR_SEARCHING).send_keys("Фильтры для поиска")
        """---add filter---"""
        try:
            self.click_to_element(self.Locators.DROPDOWN_FILTERS)
        except ElementClickInterceptedException:
            time.sleep(3)
            self.click_to_element(self.Locators.DROPDOWN_FILTERS)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN).perform()
        self.element_is_visible(self.Locators.LIST_ADDED_FILTERS).is_displayed()
        """check button click"""
        element = self.element_is_visible(self.Locators.BUTTON_CONTINUE, timeout=1)
        self.check_button_not_click(element)
        """---add action---"""
        self.element_is_visible(self.Locators.DROPDOWN_ACTIONS).send_keys("Добавить")
        """check button click"""
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        self.element_is_visible(self.Locators.INPUT_SEARCH_CONTENT_BY_NAME_FOR_ADD_FILTERS).send_keys(name_script)
        time.sleep(1)
        self.click_to_element(self.Locators.CREATED_CONTENT_FOR_FILTERS)
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        # print(name_script, name_request_script)
        """check article after add filters"""
        time.sleep(5)
        try:
            self.click_to_element(self.Locators.FILTERS)
        except (StaleElementReferenceException, TimeoutException):
            time.sleep(5)
            self.click_to_element(self.Locators.FILTERS)
        time.sleep(1)
        try:
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{name_script}']")
        except NoSuchElementException:
            time.sleep(5)
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{name_script}']")
        article_firs_name.click()
        """check content"""
        try:
            self.element_is_visible(self.Locators.VIDEO_ARTICLE).is_displayed()
        except (TimeoutException, StaleElementReferenceException):
            pass
        self.element_is_visible(self.Locators.AUDIO_SCRIPT).is_displayed()
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        time.sleep(1)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT, timeout=20)
        except (ElementClickInterceptedException, TimeoutException):
            time.sleep(15)
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        self.click_to_element(self.Locators.BUTTON_ARTICLE_BACK)
        self.click_to_element(self.Locators.BUTTON_ARTICLE_BACK)
        text_request_article = self.element_is_visible(self.Locators.TEXT_REQUEST_SCRIPT).text
        # print(text_request_article)
        assert text_request_article == name_request_script
        """change filters"""
        self.click_to_element(self.Locators.SVG_DELETE_FILTER_ADDED)
        self.click_to_element(self.Locators.DROPDOWN_FILTERS_FOR_CHANGE)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.ARROW_DOWN)
        action.send_keys(Keys.RETURN).perform()
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("Alert " + str(random.randint(9, 99)))
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.GO_TO_CONTENT)
        """check article after add filters"""
        time.sleep(5)
        filters = self.elements_are_visible(self.Locators.FILTERS)
        for n in filters:
            n.click()
        try:
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{name_script}']")
        except NoSuchElementException:
            time.sleep(5)
            article_firs_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{name_script}']")
        article_firs_name.click()
        """check content"""
        try:
            self.element_is_visible(self.Locators.VIDEO_ARTICLE).is_displayed()
        except (TimeoutException, StaleElementReferenceException):
            pass
        self.element_is_visible(self.Locators.AUDIO_SCRIPT).is_displayed()
        self.click_to_element(self.Locators.CHANGE_ARTICLE)
        time.sleep(10)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT, timeout=20)
        except TimeoutException:
            time.sleep(10)
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        self.click_to_element(self.Locators.BUTTON_ARTICLE_BACK)
        self.click_to_element(self.Locators.BUTTON_ARTICLE_BACK)
        text_request_article = self.element_is_visible(self.Locators.TEXT_REQUEST_SCRIPT).text
        assert text_request_article == name_request_script

    def delete_all_filters(self, driver):
        self.input_in_my_project(driver)
        self.click_to_element(self.Locators.SETTINGS)
        self.click_to_element(self.Locators.FILTERS_FOR_SEARCHING)
        try:
            self.click_to_element(self.Locators.BUTTON_CREATE_GROUP_FILTER, timeout=2)
        except TimeoutException:
            """del 3 filters and group"""
            self.click_to_element(self.Locators.SVG_DEL_1)
            self.click_to_element(self.Locators.SVG_DEL_LIST_CONFIRM)
            self.click_to_element(self.Locators.SVG_DEL_2)
            self.click_to_element(self.Locators.SVG_DEL_LIST_CONFIRM)
            self.click_to_element(self.Locators.SVG_DEL_3)
            self.click_to_element(self.Locators.SVG_DEL_LIST_CONFIRM)
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW)




















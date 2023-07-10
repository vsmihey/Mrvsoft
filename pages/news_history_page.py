import random
import time

from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    InvalidSelectorException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By

import pages
from locators.locators_form_pages import FormPagesLocators
from locators.locators_news_history import LocatorsCheckNewsHistory
from pages.base_page import BasePage
from pages.data_login_password import login_person1, password_person1
from pages.form_page import FormPage


class CheckNewsHistoryPage(BasePage):

    Locators = LocatorsCheckNewsHistory()

    def create_change_del_restored_article(self):
        # self.input_in_my_project(self.driver)
        """create article"""
        first_name, name_request, text_alert = self.create_article_base()
        changed_name_1 = "_changed name " + str(random.randint(999, 9999))
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        time.sleep(2)
        try:
            self.element_is_visible(self.Locators.CHECKBOX_ADD_ALL_ROLE_FOR_ARTICLE).click()
        except ElementClickInterceptedException:
            time.sleep(3)
            self.element_is_visible(self.Locators.CHECKBOX_ADD_ALL_ROLE_FOR_ARTICLE).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("created 1")
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """change article"""
        self.element_is_visible(self.Locators.ARTICLE_CHANGE).click()


        time.sleep(1)
        # self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).clear()
        # time.sleep(1)
        # self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).clear()
        time.sleep(1)
        self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).send_keys(changed_name_1)
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("changed 1")
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """add comment"""
        self.element_is_visible(self.Locators.ADD_COMMENT).send_keys("comment 1")
        self.element_is_visible(self.Locators.SEND_COMMENT).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_ARTICLE).click()
        """del article"""
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        self.element_is_visible(self.Locators.ADDED_COMMENT).click()
        self.element_is_visible(self.Locators.OPEN_ARTICLE_FOR_DEL).click()
        self.element_is_visible(self.Locators.MEATBALL_MENU).click()
        self.element_is_visible(self.Locators.DEL_ARTICLE).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("deleted 1")
        self.element_is_visible(self.Locators.BUTTON_CONFIRM_DEL).click()
        """restored"""
        time.sleep(5)
        try:
            self.element_is_visible(self.Locators.SHOW_ALL_DELETED).click()
        except TimeoutException:
            time.sleep(3)
            self.element_is_visible(self.Locators.SHOW_ALL_DELETED).click()
        self.element_is_visible(self.Locators.BUTTON_ALL_DELETED).click()
        print(changed_name_1)
        time.sleep(2)
        try:
            deleted_article_search = self.driver.find_element(By.XPATH, f"//p[normalize-space()='{first_name + changed_name_1}']")
        except (TimeoutException, NoSuchElementException):
            time.sleep(3)
            # self.element_is_visible(self.Locators.BUTTON_HISTORY).click()
            deleted_article_search = self.driver.find_element(By.XPATH, f"//p[normalize-space()='{first_name + changed_name_1}']")
        deleted_article_search.click()
        self.element_is_visible(self.Locators.BUTTON_RESTORED).click()
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("restored 1")
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_RESTORED_ARTICLE).click()
        time.sleep(1)
        return first_name, changed_name_1

    def create_change_del_article(self):
        # self.input_in_my_project(self.driver)
        """create article"""
        first_name_2 = self.create_article_base()
        changed_name_2 = "changed name " + str(random.randint(999, 9999))
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()

        self.element_is_visible(self.Locators.CHECKBOX_ADD_ALL_ROLE_FOR_ARTICLE).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("created 2")
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """change article"""
        self.element_is_visible(self.Locators.ARTICLE_CHANGE).click()
        self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).clear()
        self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).send_keys(changed_name_2)
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("changed 2")
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """add comment"""
        time.sleep(6)
        self.element_is_visible(self.Locators.ADD_COMMENT).send_keys("comment 2")
        self.element_is_visible(self.Locators.SEND_COMMENT).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_ARTICLE).click()
        """del article"""
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        self.element_is_visible(self.Locators.ADDED_COMMENT).click()
        self.element_is_visible(self.Locators.OPEN_ARTICLE_FOR_DEL).click()
        time.sleep(1)
        self.element_is_visible(self.Locators.MEATBALL_MENU).click()
        time.sleep(1)
        self.element_is_visible(self.Locators.DEL_ARTICLE).click()
        time.sleep(1)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("deleted 2")
        time.sleep(1)
        self.element_is_visible(self.Locators.BUTTON_CONFIRM_DEL).click()
        time.sleep(1)

        self.element_is_visible(self.Locators.LABEL_ADMINISTRATOR_PERSON).click()
        self.element_is_visible(self.Locators.LABEL_ADMINISTRATOR_PERSON_OUT).click()
        time.sleep(2)
        return first_name_2, changed_name_2

    def persons_auth(self, login, password):
        # self.input_in_my_project(self.driver)
        Locators = FormPagesLocators()
        try:
            self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        except TimeoutException:
            time.sleep(2)
            self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.INPUT_BUTTON).click()
        # self.element_is_visible(self.Locators.TEST_PROJECT).click()
        # time.sleep(6)

    def add_role_content(self):
        name_role_content = "role content" + str(random.randint(999, 9999))
        # self.input_in_my_project(self.driver)
        self.element_is_visible(self.Locators.PERSONS).click()
        self.element_is_visible(self.Locators.ADD_ROLE).click()
        self.element_is_visible(self.Locators.INPUT_NAME_ROLE).send_keys(name_role_content)
        self.element_is_visible(self.Locators.SWITCH_BOX_CONTROL_CONTENT).click()
        self.element_is_visible(self.Locators.BUTTON_CREATE_ROLE).click()
        time.sleep(3)
        return name_role_content

    def add_role_no_content(self):
        name_role_no_content = "role no content" + str(random.randint(999, 9999))
        # self.input_in_my_project(self.driver)
        # self.element_is_visible(self.Locators.PERSONS).click()
        try:
            self.element_is_visible(self.Locators.ADD_ROLE).click()
        except StaleElementReferenceException:
            time.sleep(3)
            self.element_is_visible(self.Locators.ADD_ROLE).click()
        self.element_is_visible(self.Locators.INPUT_NAME_ROLE).send_keys(name_role_no_content)
        self.element_is_visible(self.Locators.SWITCH_BOX_CONTROL_CONTENT).click()
        content = self.element_is_visible(self.Locators.CHECKBOX_RESTORE_CONTENT)
        content.click()
        self.element_is_visible(self.Locators.BUTTON_CREATE_ROLE).click()
        return name_role_no_content

    def create_person1(self):
        self.input_in_my_project(self.driver)
        password_person1 = "97718d75"
        name_role_content = self.add_role_content()
        login1 = self.add_new_person_base(self.driver)
        try:
            self.element_is_visible(self.Locators.BUTTON_SETTING_ACCESS).click()
        except TimeoutException:
            time.sleep(3)
            self.element_is_visible(self.Locators.FRAME_PERSON_CLOSE).click()
            self.element_is_visible(self.Locators.BUTTON_SETTING_ACCESS).click()
        time.sleep(1)
        try:
            choose_name_role_content = self.driver.find_element(By.XPATH, f"//span[normalize-space()='{name_role_content}']")
        except TimeoutException:
            time.sleep(3)
            choose_name_role_content = self.driver.find_element(By.XPATH, f"//span[normalize-space()='{name_role_content}']")
        try:
            choose_name_role_content.click()
        except ElementNotInteractableException:
            time.sleep(3)
            choose_name_role_content.click()
        self.element_is_visible(self.Locators.BUTTON_SAVE_CHANGES).click()
        self.element_is_visible(self.Locators.BUTTON_SAVE_CHANGES_CONFIRM).click()
        self.element_is_visible(self.Locators.BUTTON_CHANGE_PASSWORD).click()
        self.element_is_visible(self.Locators.INPUT_NEW_PASSWORD).send_keys(password_person1)
        try:
            self.element_is_visible(self.Locators.INPUT_REPEAT_PASSWORD).send_keys(password_person1)
        except InvalidSelectorException:
            time.sleep(3)
            self.element_is_visible(self.Locators.INPUT_REPEAT_PASSWORD).send_keys(password_person1)
        self.element_is_visible(self.Locators.BUTTON_SAVE_CHANGES).click()
        self.element_is_visible(self.Locators.BUTTON_SAVE_CHANGES_CONFIRM).click()
        print(login1, password_person1)
        return login1, password_person1

    def create_person2(self):
        # self.input_in_my_project(self.driver)
        password_person2 = "97718d75"
        # name_role_content = self.add_role_content()
        self.element_is_visible(self.Locators.SVG_POPUP_CLOSE_CREATED_PERSON).click()
        self.element_is_visible(self.Locators.PERSONS_AND_ROLES).click()
        name_role_no_content = self.add_role_no_content()
        login2 = self.add_new_person_base(self.driver)
        self.element_is_visible(self.Locators.BUTTON_SETTING_ACCESS).click()
        time.sleep(1)
        try:
            choose_name_role_content = self.driver.find_element(By.XPATH,
                                                                f"//span[normalize-space()='{name_role_no_content}']")
        except TimeoutException:
            time.sleep(3)
            choose_name_role_content = self.driver.find_element(By.XPATH,
                                                                f"//span[normalize-space()='{name_role_no_content}']")
        choose_name_role_content.click()
        self.element_is_visible(self.Locators.BUTTON_SAVE_CHANGES).click()
        self.element_is_visible(self.Locators.BUTTON_SAVE_CHANGES_CONFIRM).click()
        self.element_is_visible(self.Locators.BUTTON_CHANGE_PASSWORD).click()
        self.element_is_visible(self.Locators.INPUT_NEW_PASSWORD).send_keys(password_person2)
        try:
            self.element_is_visible(self.Locators.INPUT_REPEAT_PASSWORD).send_keys(password_person2)
        except InvalidSelectorException:
            time.sleep(3)
            self.element_is_visible(self.Locators.INPUT_REPEAT_PASSWORD).send_keys(password_person2)
        self.element_is_visible(self.Locators.BUTTON_SAVE_CHANGES).click()
        self.element_is_visible(self.Locators.BUTTON_SAVE_CHANGES_CONFIRM).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_CREATED_PERSON).click()
        print(login2, password_person2)
        return login2, password_person2

    def check_restored_1(self):
        """check restored article for person 1: can restore article"""
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        try:
            self.element_is_visible(self.Locators.RESTORED_ARTICLE_1).click()
        except TimeoutException:
            time.sleep(3)
            self.element_is_visible(self.Locators.RESTORED_ARTICLE_1).click()
        self.element_is_visible(self.Locators.RESTORED_ARTICLE_1_CHECK_CHANGE).is_displayed()
        comment = self.element_is_visible(self.Locators.RESTORED_ARTICLE_1_CHECK_ADDED_COMMENT).is_displayed()
        print(comment)
        self.element_is_visible(self.Locators.SVG_CLOSE_CREATED_ARTICLE).click()

    def check_del_article_2(self):
        try:
            self.element_is_visible(self.Locators.DEL_ARTICLE_2).click()
        except TimeoutException:
            time.sleep(3)
            self.element_is_visible(self.Locators.DEL_ARTICLE_2).click()
        warning = self.element_is_visible(self.Locators.DEL_ARTICLE_2_WARNING).is_displayed()
        self.element_is_visible(self.Locators.SVG_CLOSE_CREATED_ARTICLE).click()
        print(warning)

    def check_comment_1(self):
        """check comment"""
        self.element_is_visible(self.Locators.COMMENT_CREATED).click()
        self.element_is_visible(self.Locators.TEXT_COMMENT_CHECK).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_CREATED_PERSON).click()
        """check del comment"""
        self.element_is_visible(self.Locators.DEL_ARTICLE_2).click()
        self.element_is_visible(self.Locators.TEXT_CHECK_CANT_COMMENT).is_displayed()

    def check_restored_1_person2(self):
        """check restored article for person 2: can not restore article"""
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        try:
            self.element_is_visible(self.Locators.RESTORED_ARTICLE_1_CHECK_CHANGE_PERSON2).click()
        except TimeoutException:
            time.sleep(3)
            self.element_is_visible(self.Locators.RESTORED_ARTICLE_1_CHECK_CHANGE_PERSON2).click()
        self.element_is_visible(self.Locators.RESTORED_ARTICLE_1_CHECK_CHANGE).is_displayed()
        comment = self.element_is_visible(self.Locators.RESTORED_ARTICLE_1_CHECK_ADDED_COMMENT).is_displayed()
        print(comment)
        self.element_is_visible(self.Locators.SVG_CLOSE_CREATED_ARTICLE).click()

    def check_del_article_2_person2(self):
        try:
            self.element_is_visible(self.Locators.DEL_ARTICLE_2, timeout=1).click()
            warning = True
        except TimeoutException:
            warning = False
            # warning = "Нет удаленной статьи"
            print("Нет удаленной статьи")
        assert warning == False

    def check_comment_1_person2(self):
        """check comment"""
        self.element_is_visible(self.Locators.COMMENT_CREATED).click()
        self.element_is_visible(self.Locators.TEXT_COMMENT_CHECK).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_WINDOW_CREATED_PERSON).click()
        """check del comment"""
        try:
            self.element_is_visible(self.Locators.DEL_ARTICLE_2).click()
            warning = True
        except TimeoutException:
            warning = False
            print("Нет удаленной статьи для проверки комментария")
        assert warning == False



    # def del_all_person(self):
    #     self.input_in_my_project(self.driver)
    #     self.element_is_visible(self.Locators.PERSONS).click()
    #     list_all_person = self.elements_are_visible(self.Locators.LIST_ALL_PERSON)
    #     while True:
    #         time.sleep(5)
    #         for n in list_all_person:
    #             n.click()
    #             self.element_is_visible(self.Locators.CHANGE_DATA_PERSON).click()
    #             self.element_is_visible(self.Locators.DEL_PERSON).click()
    #             self.element_is_visible(self.Locators.DEL_PERSON_CONFIRM).click()
    #         self.driver.refresh()


















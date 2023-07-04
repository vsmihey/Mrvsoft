import random
import time

from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    InvalidSelectorException
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
        self.input_in_my_project(self.driver)
        """create article"""
        first_name = self.create_article_base()
        changed_name = "changed name " + str(random.randint(999, 9999))
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("created")
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """change article"""
        self.element_is_visible(self.Locators.ARTICLE_CHANGE).click()
        self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).clear()
        self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).send_keys(changed_name)
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("changed")
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """add comment"""
        self.element_is_visible(self.Locators.ADD_COMMENT).send_keys("comment")
        self.element_is_visible(self.Locators.SEND_COMMENT).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_ARTICLE).click()
        """del article"""
        self.element_is_visible(self.Locators.HISTORY_BUTTON).click()
        self.element_is_visible(self.Locators.ADDED_COMMENT).click()
        self.element_is_visible(self.Locators.OPEN_ARTICLE_FOR_DEL).click()
        self.element_is_visible(self.Locators.MEATBALL_MENU).click()
        self.element_is_visible(self.Locators.DEL_ARTICLE).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("deleted")
        self.element_is_visible(self.Locators.BUTTON_CONFIRM_DEL).click()

        """restored"""
        self.element_is_visible(self.Locators.SHOW_ALL_DELETED).click()
        self.element_is_visible(self.Locators.BUTTON_ALL_DELETED).click()
        # time.sleep(16)
        # try:
        #     self.element_is_visible(self.Locators.BUTTON_ALL_DELETED, timeout=2).click()
        # except TimeoutException:
        #     time.sleep(3)
        #     self.element_is_visible(self.Locators.SHOW_ALL_DELETED).click()
        #     self.element_is_visible(self.Locators.BUTTON_ALL_DELETED).click()
        try:
            deleted_article_search = self.driver.find_element(By.XPATH, f"//p[normalize-space()='{changed_name}']")
        except (TimeoutException, NoSuchElementException):
            time.sleep(3)
            deleted_article_search = self.driver.find_element(By.ID, f"//p[normalize-space()='{changed_name}']")
        deleted_article_search.click()
        self.element_is_visible(self.Locators.BUTTON_RESTORED).click()
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("restored")
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        return first_name

    def person1_auth(self, login, password):
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
        # time.sleep(6)

    def add_role_content(self):
        name_role_content = "role content" + str(random.randint(999, 9999))
        # self.input_in_my_project(self.driver)
        self.element_is_visible(self.Locators.PERSONS).click()
        self.element_is_visible(self.Locators.ADD_ROLE).click()
        self.element_is_visible(self.Locators.INPUT_NAME_ROLE).send_keys(name_role_content)
        # self.element_is_visible(self.Locators.SWITCH_BOX_CONTROL_CONTENT).click()
        # content = self.element_is_visible(self.Locators.CHECKBOX_RESTORE_CONTENT)
        # content.click()
        self.element_is_visible(self.Locators.BUTTON_CREATE_ROLE).click()
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
        name_role_no_content = self.add_role_no_content()
        login1 = self.add_new_person_base(self.driver)
        self.element_is_visible(self.Locators.BUTTON_SETTING_ACCESS).click()
        try:
            choose_name_role_content = self.driver.find_element(By.XPATH, f"//span[normalize-space()='{name_role_content}']")
        except TimeoutException:
            time.sleep(3)
            choose_name_role_content = self.driver.find_element(By.XPATH, f"//span[normalize-space()='{name_role_content}']")
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
        # """ath"""
        # self.person1_auth(login=login, password=password_person1)

        # time.sleep(16)

        return login1, password_person1





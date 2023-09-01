import random
import time
import allure
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    InvalidSelectorException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from locators.locators_form_pages import FormPagesLocators
from locators.locators_news_history import LocatorsCheckNewsHistory
from pages.authorisation_page import Authorisation
from pages.base_page import BasePage


class CheckNewsHistoryPage(Authorisation, BasePage):

    Locators = LocatorsCheckNewsHistory()

    def create_change_del_restored_article(self):
        # self.input_in_my_project(self.driver)
        """create article"""
        first_name, name_request, text_alert = self.create_article_base()
        changed_name_1 = "_changed name " + str(random.randint(999, 9999))
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        time.sleep(2)
        try:
            self.click_to_element(self.Locators.CHECKBOX_ADD_ALL_ROLE_FOR_ARTICLE)
        except ElementClickInterceptedException:
            time.sleep(3)
            self.click_to_element(self.Locators.CHECKBOX_ADD_ALL_ROLE_FOR_ARTICLE)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("created 1")
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        """change article"""
        self.click_to_element(self.Locators.ARTICLE_CHANGE)
        time.sleep(1)
        # self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).clear()
        # time.sleep(1)
        # self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).clear()
        time.sleep(1)
        self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).send_keys(changed_name_1)
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("changed 1")
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        """add comment"""
        self.element_is_visible(self.Locators.ADD_COMMENT).send_keys("comment 1")
        self.click_to_element(self.Locators.SEND_COMMENT)
        self.click_to_element(self.Locators.SVG_CLOSE_ARTICLE)
        """del article"""
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        self.click_to_element(self.Locators.ADDED_COMMENT)
        self.click_to_element(self.Locators.OPEN_ARTICLE_FOR_DEL)
        self.click_to_element(self.Locators.MEATBALL_MENU)
        self.click_to_element(self.Locators.DEL_ARTICLE)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("deleted 1")
        self.click_to_element(self.Locators.BUTTON_CONFIRM_DEL)
        """restored"""
        time.sleep(2)
        try:
            self.click_to_element(self.Locators.SHOW_ALL_DELETED)
        except TimeoutException:
            time.sleep(5)
            self.click_to_element(self.Locators.HIDDEN_ALL_DELETED)
            self.click_to_element(self.Locators.SHOW_ALL_DELETED)
        self.click_to_element(self.Locators.BUTTON_ALL_DELETED)
        print(changed_name_1)
        time.sleep(2)
        try:
            deleted_article_search = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{first_name + changed_name_1}']")
        except (TimeoutException, NoSuchElementException):
            time.sleep(3)
            # self.click_to_element(self.Locators.BUTTON_HISTORY)
            deleted_article_search = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{first_name + changed_name_1}']")
        deleted_article_search.click()
        self.click_to_element(self.Locators.BUTTON_RESTORED)
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("restored 1")
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.SVG_CLOSE_RESTORED_ARTICLE)
        time.sleep(1)
        return first_name, changed_name_1

    def create_change_del_article(self):
        # self.input_in_my_project(self.driver)
        """create article"""
        first_name_2 = self.create_article_base()
        changed_name_2 = "changed name " + str(random.randint(999, 9999))
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.CHECKBOX_ADD_ALL_ROLE_FOR_ARTICLE)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("created 2")
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        """change article"""
        self.click_to_element(self.Locators.ARTICLE_CHANGE)
        # self.delete_draft()
        try:
            self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).clear()
        except TimeoutException:
            self.delete_draft()
            # time.sleep(3)
            self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).clear()
        self.element_is_visible(self.Locators.ARTICLE_NAME_CHANGE).send_keys(changed_name_2)
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("changed 2")
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        """add comment"""
        time.sleep(6)
        self.element_is_visible(self.Locators.ADD_COMMENT).send_keys("comment 2")
        self.click_to_element(self.Locators.SEND_COMMENT)
        self.click_to_element(self.Locators.SVG_CLOSE_ARTICLE)
        """del article"""
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        self.click_to_element(self.Locators.ADDED_COMMENT)
        self.click_to_element(self.Locators.OPEN_ARTICLE_FOR_DEL)
        time.sleep(1)
        self.click_to_element(self.Locators.MEATBALL_MENU)
        time.sleep(1)
        self.click_to_element(self.Locators.DEL_ARTICLE)
        time.sleep(1)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("deleted 2")
        time.sleep(1)
        self.click_to_element(self.Locators.BUTTON_CONFIRM_DEL)
        time.sleep(1)
        try:
            self.click_to_element(self.Locators.LABEL_ADMINISTRATOR_PERSON)
        except StaleElementReferenceException:
            time.sleep(3)
            self.click_to_element(self.Locators.LABEL_ADMINISTRATOR_PERSON)
        self.click_to_element(self.Locators.LABEL_ADMINISTRATOR_PERSON_OUT)
        time.sleep(2)
        # """выход пользователя"""
        # self.click_to_element(self.Locators.GO_TO_CONTENT)
        # self.click_to_element(self.Locators.AVATAR_MENU)
        # self.click_to_element(self.Locators.EXIT_PERSON)
        return first_name_2, changed_name_2

    def persons_auth(self, login, password):
        # self.input_in_my_project(driver)
        # self.open()
        Locators = FormPagesLocators()
        try:
            self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        time.sleep(1)
        self.click_to_element(Locators.INPUT_BUTTON)
        # self.click_to_element(self.Locators.TEST_PROJECT)
        # time.sleep(6)

    def add_role_content(self):
        name_role_content = "role content" + str(random.randint(999, 9999))
        # self.input_in_my_project(self.driver)
        self.click_to_element(self.Locators.PERSONS)
        self.click_to_element(self.Locators.ADD_ROLE)
        self.element_is_visible(self.Locators.INPUT_NAME_ROLE).send_keys(name_role_content)
        self.click_to_element(self.Locators.SWITCH_BOX_CONTROL_CONTENT)
        self.click_to_element(self.Locators.BUTTON_CREATE_ROLE)
        time.sleep(3)
        return name_role_content

    def add_role_no_content(self):
        name_role_no_content = "role no content" + str(random.randint(999, 9999))
        # self.input_in_my_project(self.driver)
        # self.click_to_element(self.Locators.PERSONS)
        try:
            self.click_to_element(self.Locators.ADD_ROLE)
        except StaleElementReferenceException:
            time.sleep(3)
            self.click_to_element(self.Locators.ADD_ROLE)
        self.element_is_visible(self.Locators.INPUT_NAME_ROLE).send_keys(name_role_no_content)
        self.click_to_element(self.Locators.SWITCH_BOX_CONTROL_CONTENT)
        content = self.element_is_visible(self.Locators.CHECKBOX_RESTORE_CONTENT)
        content.click()
        self.click_to_element(self.Locators.BUTTON_CREATE_ROLE)
        return name_role_no_content

    def create_person1(self, driver):
        # self.input_in_my_project(self.driver)
        password_person1 = "97718d75"
        name_role_content = self.add_role_content()
        login1 = self.add_new_person_base(driver)
        try:
            self.click_to_element(self.Locators.BUTTON_SETTING_ACCESS)
        except TimeoutException:
            time.sleep(3)
            # self.click_to_element(self.Locators.FRAME_PERSON_CLOSE)
            self.click_to_element(self.Locators.BUTTON_SETTING_ACCESS)
        time.sleep(1)
        try:
            choose_name_role_content = self.browser.find_element(By.XPATH, f"//span[normalize-space()='{name_role_content}']")
        except TimeoutException:
            time.sleep(3)
            choose_name_role_content = self.browser.find_element(By.XPATH, f"//span[normalize-space()='{name_role_content}']")
        try:
            choose_name_role_content.click()
        except ElementNotInteractableException:
            time.sleep(3)
            choose_name_role_content.click()
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES)
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES_CONFIRM)
        self.click_to_element(self.Locators.BUTTON_CHANGE_PASSWORD)
        self.element_is_visible(self.Locators.INPUT_NEW_PASSWORD).send_keys(password_person1)
        try:
            self.element_is_visible(self.Locators.INPUT_REPEAT_PASSWORD).send_keys(password_person1)
        except InvalidSelectorException:
            time.sleep(3)
            self.element_is_visible(self.Locators.INPUT_REPEAT_PASSWORD).send_keys(password_person1)
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES)
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES_CONFIRM)
        print(login1, password_person1)
        return login1, password_person1

    def create_person2(self, driver):
        # self.input_in_my_project(self.driver)
        password_person2 = "97718d75"
        # name_role_content = self.add_role_content()
        self.click_to_element(self.Locators.SVG_POPUP_CLOSE_CREATED_PERSON)
        self.click_to_element(self.Locators.PERSONS_AND_ROLES)
        name_role_no_content = self.add_role_no_content()
        login2 = self.add_new_person_base(driver)
        self.click_to_element(self.Locators.BUTTON_SETTING_ACCESS)
        time.sleep(1)
        try:
            choose_name_role_content = self.browser.find_element(By.XPATH,
                                                                f"//span[normalize-space()='{name_role_no_content}']")
        except TimeoutException:
            time.sleep(3)
            choose_name_role_content = self.browser.find_element(By.XPATH,
                                                                f"//span[normalize-space()='{name_role_no_content}']")
        choose_name_role_content.click()
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES)
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES_CONFIRM)
        self.click_to_element(self.Locators.BUTTON_CHANGE_PASSWORD)
        self.element_is_visible(self.Locators.INPUT_NEW_PASSWORD).send_keys(password_person2)
        try:
            self.element_is_visible(self.Locators.INPUT_REPEAT_PASSWORD).send_keys(password_person2)
        except InvalidSelectorException:
            time.sleep(3)
            self.element_is_visible(self.Locators.INPUT_REPEAT_PASSWORD).send_keys(password_person2)
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES)
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES_CONFIRM)
        self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_CREATED_PERSON)
        print(login2, password_person2)
        return login2, password_person2

    def check_restored_1(self):
        """check restored article for person 1: can restore article"""
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        try:
            self.click_to_element(self.Locators.RESTORED_ARTICLE_1)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.RESTORED_ARTICLE_1_)
            # self.click_to_element(self.Locators.RESTORED_ARTICLE_1)
        self.element_is_visible(self.Locators.RESTORED_ARTICLE_1_CHECK_CHANGE).is_displayed()
        comment = self.element_is_visible(self.Locators.RESTORED_ARTICLE_1_CHECK_ADDED_COMMENT).is_displayed()
        print(comment)
        self.click_to_element(self.Locators.SVG_CLOSE_CREATED_ARTICLE)

    def check_del_article_2(self):
        try:
            self.click_to_element(self.Locators.DEL_ARTICLE_2)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.DEL_ARTICLE_2)
        warning = self.element_is_visible(self.Locators.DEL_ARTICLE_2_WARNING).is_displayed()
        self.click_to_element(self.Locators.SVG_CLOSE_CREATED_ARTICLE)
        print(warning)

    def check_comment_1(self):
        """check comment"""
        with allure.step("Проверка новостей о комментариях в Истории - person1"):
            self.click_to_element(self.Locators.COMMENT_CREATED)
            self.click_to_element(self.Locators.TEXT_COMMENT_CHECK)
            self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_CREATED_PERSON)
            """check del comment"""
            self.click_to_element(self.Locators.DEL_ARTICLE_2)
            self.element_is_visible(self.Locators.TEXT_CHECK_CANT_COMMENT).is_displayed()
            """выход пользователя"""
            self.click_to_element(self.Locators.GO_TO_CONTENT)
            time.sleep(1)
            try:
                self.click_to_element(self.Locators.AVATAR_MENU)
            except StaleElementReferenceException:
                time.sleep(3)
                self.click_to_element(self.Locators.AVATAR_MENU)
            self.click_to_element(self.Locators.EXIT_PERSON)

    def check_restored_1_person2(self):
        """check restored article for person 2: can not restore article"""
        self.click_to_element(self.Locators.HISTORY_BUTTON)
        try:
            self.click_to_element(self.Locators.RESTORED_ARTICLE_1_CHECK_CHANGE_PERSON2)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.RESTORED_ARTICLE_1_CHECK_CHANGE_PERSON2)
        self.element_is_visible(self.Locators.RESTORED_ARTICLE_1_CHECK_CHANGE).is_displayed()
        comment = self.element_is_visible(self.Locators.RESTORED_ARTICLE_1_CHECK_ADDED_COMMENT).is_displayed()
        print(comment)
        self.click_to_element(self.Locators.SVG_CLOSE_CREATED_ARTICLE)

    def check_del_article_2_person2(self):
        try:
            self.click_to_element(self.Locators.DEL_ARTICLE_2, timeout=1)
            warning = True
        except TimeoutException:
            warning = False
            # warning = "Нет удаленной статьи"
            print("Нет удаленной статьи")
        assert warning == False

    def check_comment_1_person2(self):
        """check comment"""
        with allure.step("Проверка новостей о комментариях в Истории - person2"):
            self.click_to_element(self.Locators.COMMENT_CREATED)
            self.click_to_element(self.Locators.TEXT_COMMENT_CHECK)
            self.click_to_element(self.Locators.SVG_CLOSE_WINDOW_CREATED_PERSON)
            """check del comment"""
            try:
                self.click_to_element(self.Locators.DEL_ARTICLE_2)
                warning = True
            except TimeoutException:
                warning = False
                print("Нет удаленной статьи для проверки комментария")
            assert warning == False

    def create_person1_2(self):
        """create person for check  Alert"""
        # self.input_in_my_project(self.driver)
        password_person1_2 = "97718d75"
        self.click_to_element(self.Locators.SVG_POPUP_CLOSE_CREATED_PERSON)
        name_role_content = self.add_role_content()
        login1_2 = self.add_new_person_base(self.driver)
        try:
            self.click_to_element(self.Locators.BUTTON_SETTING_ACCESS)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.FRAME_PERSON_CLOSE)
            self.click_to_element(self.Locators.BUTTON_SETTING_ACCESS)
        time.sleep(1)
        try:
            choose_name_role_content = self.browser.find_element(By.XPATH,
                                                                f"//span[normalize-space()='{name_role_content}']")
        except TimeoutException:
            time.sleep(3)
            choose_name_role_content = self.browser.find_element(By.XPATH,
                                                                f"//span[normalize-space()='{name_role_content}']")
        try:
            choose_name_role_content.click()
        except ElementNotInteractableException:
            time.sleep(3)
            choose_name_role_content.click()
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES)
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES_CONFIRM)
        self.click_to_element(self.Locators.BUTTON_CHANGE_PASSWORD)
        self.element_is_visible(self.Locators.INPUT_NEW_PASSWORD).send_keys(password_person1_2)
        try:
            self.element_is_visible(self.Locators.INPUT_REPEAT_PASSWORD).send_keys(password_person1_2)
        except InvalidSelectorException:
            time.sleep(3)
            self.element_is_visible(self.Locators.INPUT_REPEAT_PASSWORD).send_keys(password_person1_2)
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES)
        self.click_to_element(self.Locators.BUTTON_SAVE_CHANGES_CONFIRM)
        self.click_to_element(self.Locators.SVG_POPUP_CLOSE_CREATED_PERSON)
        print(login1_2, password_person1_2)
        return login1_2, password_person1_2

    def create_and_add_comment(self):
        name = "name " + str(random.randint(999, 9999))
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.CHECKBOX_ADD_ALL_ROLE_FOR_ARTICLE)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_FIELD).send_keys("created")
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        """add comment"""
        time.sleep(6)
        self.element_is_visible(self.Locators.ADD_COMMENT).send_keys("comment_for_check")
        self.click_to_element(self.Locators.SEND_COMMENT)
        self.click_to_element(self.Locators.SVG_CLOSE_ARTICLE)



















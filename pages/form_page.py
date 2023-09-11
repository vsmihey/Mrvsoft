import datetime
import pathlib
import random
import time
from pathlib import Path
import allure
import selenium
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from generator.generator import generated_person
from pages.base_page import BasePage
from locators.locators_form_pages import FormPagesLocators as Locators
from selenium.webdriver.common.alert import Alert
from pages.authorisation_page import Authorisation
from pages.users import minervakms


class FormPage(Authorisation, BasePage):

    def screenshot(self):
        offset = datetime.timezone(datetime.timedelta(hours=3))  # timezone (+3)
        now_date = datetime.datetime.now(offset)
        now_date = now_date.strftime('%Y.%m.%d.%H.%M.%S')
        # now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        path = Path(pathlib.Path.cwd(), "screenshots", name_screenshot)
        path = str(path)
        self.browser.save_screenshot(path)

    def full_authorization(self):
        """CORRECT DATA"""
        self.open()
        self.authorization(minervakms.login, minervakms.password)

    def authorization(self, login, password):
        self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.click_to_element(Locators.INPUT_BUTTON)
        time.sleep(1)

    def input_in_my_project(self, driver):
        """INPUT IN MY PROJECT"""
        self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(minervakms.login)
        self.element_is_visible(Locators.PASSWORD).send_keys(minervakms.password)
        self.click_to_element(Locators.INPUT_BUTTON)
        try:
            time.sleep(1)
            self.click_to_element(Locators.TEST_PROJECT, timeout=3)
        except TimeoutException:
            self.click_to_element(Locators.ADD)
            self.element_is_visible(Locators.ADD_NAMES_PROJECT).send_keys("selen")
            self.element_is_visible(Locators.ADD_DESCRIPTION_PROJECT).send_keys("test_selenium")
            self.click_to_element(Locators.ADD_TEST_PROJECT)
            self.click_to_element(Locators.TEST_PROJECT)
            time.sleep(1)
            self.click_to_element(Locators.TEST_PROJECT)
            # self.click_to_element(Locators.HISTORY_BUTTON)
            time.sleep(2)
            self.click_to_element(Locators.CONTENT)
            time.sleep(10)
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
            self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys("Контент 1")
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        except ElementClickInterceptedException:
            self.click_to_element(Locators.ADD)
            self.element_is_visible(Locators.ADD_NAMES_PROJECT).send_keys("selen")
            self.element_is_visible(Locators.ADD_DESCRIPTION_PROJECT).send_keys("test_selenium")
            self.click_to_element(Locators.ADD_TEST_PROJECT)
            self.click_to_element(Locators.TEST_PROJECT)
            self.click_to_element(Locators.CONTENT)
            time.sleep(12)
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
            self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys("Контент 1")
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)

    def fill_fields(self, login, password):
        """FILL FIELDS PAGE OF AUTHORIZATION"""
        self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.click_to_element(Locators.INPUT_BUTTON)
        time.sleep(1)
        self.element_is_visible(Locators.LOGIN).clear()
        self.element_is_visible(Locators.PASSWORD).clear()
        time.sleep(1)

    def fill_fields_(self, login, password):
        self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.click_to_element(Locators.INPUT_BUTTON)

    def check_input_text(self):
        check_text_input_in_system = self.element_is_visible(Locators.CHECK_TEXT_INPUT_IN_SYSTEM).text
        print(check_text_input_in_system)
        return check_text_input_in_system

    def check_auth_text(self):
        """CHECK TEXT INCORRECT LOGIN AND PASSWORD"""
        check_logit_text = self.element_is_visible(Locators.INCORRECT_LOGIN_TEXT)
        check_logit_text_value = check_logit_text.text
        assert check_logit_text_value == 'Неверный логин'
        check_password_text = self.element_is_visible(Locators.INCORRECT_PASSWORD_TEXT)
        check_password_text_value = check_password_text.text
        assert check_password_text_value == 'Неверный пароль'
        # print(f'Текст: <{check_logit_text_value}> и <{check_password_text_value}> на странице авторизации УСПЕШНО')

    def restore_incorrect(self):
        """RESTORE INPUT INCORRECT LOGIN"""
        login_incorrect, password_incorrect = '123qwe', '321qwe'
        login = login_incorrect
        self.click_to_element(Locators.RESTORE)
        self.element_is_visible(Locators.RESTORE_LOGIN).send_keys(login)
        self.click_to_element(Locators.RESTORE_BUTTON)

    def check_restore_text(self):
        """CHECK TEXT INCORRECT LOGIN ON PAGE RESTORE"""
        check_logit_text = self.element_is_visible(Locators.INCORRECT_LOGIN_TEXT)
        check_logit_text_value = check_logit_text.text
        assert check_logit_text_value == 'Неверный логин'
        """я помню пароль"""
        self.click_to_element(Locators.I_REMEMBER_PASSWD)
        # """fill fields page of authorization"""
        # self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        # self.element_is_visible(Locators.LOGIN).send_keys(login)
        # self.element_is_visible(Locators.PASSWORD).send_keys(password)
        # self.click_to_element(Locators.INPUT_BUTTON)

    def restore_correct(self):
        """RESTORE PASSWORD BY CORRECT LOGIN END PUSH REMEMBER PASSWORD"""
        self.click_to_element(Locators.RESTORE)
        self.element_is_visible(Locators.RESTORE_LOGIN).send_keys(minervakms.login)
        self.click_to_element(Locators.RESTORE_BUTTON)
        time.sleep(1)
        # self.screenshot()
        self.click_to_element(Locators.REMEMBER_PASSWD)
        time.sleep(1)
        check_page_author = self.element_is_visible(Locators.PAGE_AUTH)
        check_page_author_value = check_page_author.text
        assert check_page_author_value == 'Вход в систему'
        # print('Письмо с новым паролем отправлено на почту УСПЕШНО')
        # print(f'Страница {check_page_author_value} УСПЕШНО')

    def check_project_page(self):
        """CHECK PAGE BY WORDS"""
        check_project = self.element_is_visible(Locators.CHANGE_PROJECT)
        check_project_value = check_project.text
        assert check_project_value == 'Выберите проект'
        # print('Страница ' + check_project_value + ' открыта')

    def logo_head(self):
        """LOGO"""
        logo = self.element_is_visible(Locators.LOGO_HEAD)
        print(logo.is_displayed())

    def input_project(self):
        """INPUT IN SELEN PROJECT"""
        self.click_to_element(Locators.TEST_PROJECT)
        time.sleep(1)

    def title_find(self):
        """TITLE"""
        # driver.title()
        title = self.browser.title
        # title = driver.execute_script("return document.title;")
        print(title)

    def assert_title(self, name_project='selen', name_='Контент 1'):
        """ASSERT"""
        time.sleep(1)
        title = self.browser.title
        time.sleep(1)
        result = f'{name_} / {name_project} — Minervasoft'
        time.sleep(1)
        assert title == result
        # print(result)

    def all_title(self):
        """CHECK ALL TITLE"""
        self.browser.implicitly_wait(10)
        # time.sleep(1)
        # driver.get_screenshot_as_file("scr.png")
        self.browser.refresh()
        self.click_to_element(Locators.CONTENT)
        self.click_to_element(Locators.ALL_CONTENT)
        time.sleep(1)
        self.assert_title(self.browser, name_='Весь контент')
        self.click_to_element(Locators.CONTENT1)
        time.sleep(1)
        self.assert_title(self.browser, name_='Контент 1')
        # self.screenshot()
        self.click_to_element(Locators.CREATE_BUTTON)
        self.element_is_visible(Locators.CHOOSE_PROJECT).send_keys("selen")
        time.sleep(1)
        self.click_to_element(Locators.CREATE_ARTICLE)
        self.assert_title(self.browser, name_='Добавить статью')
        time.sleep(2)
        # self.screenshot()
        try:
            self.click_to_element(Locators.CLOSE_PAGE_LIST)
        except ElementClickInterceptedException:
            time.sleep(5)
            self.click_to_element(Locators.CLOSE_PAGE_LIST)
        self.click_to_element(Locators.CREATE_STEP_SCRIPT)
        # # time.sleep(5)
        self.assert_title(self.browser, name_='Добавить пошаговый сценарий')
        time.sleep(1)
        self.click_to_element(Locators.CLOSE_PAGE_SCRIPT)
        self.click_to_element(Locators.CLOSE_CREATE_WINDOW)
        time.sleep(1)
        # self.click_to_element(Locators.SEARCH_PROJECT)
        self.click_to_element(Locators.SEARCH_PROJECT_TEST1)
        time.sleep(1)
        self.element_is_visible(Locators.SEARCH_INPUT).send_keys('название 1')
        time.sleep(1)
        self.element_is_visible(Locators.SEARCH_INPUT).send_keys(Keys.RETURN)
        time.sleep(2)
        try:
            self.assert_title(self.browser, name_='название 1')
        except TimeoutException:
            time.sleep(2)
            self.element_is_visible(Locators.SEARCH_INPUT).send_keys('название 1')
            self.element_is_visible(Locators.SEARCH_INPUT).send_keys(Keys.RETURN)
            time.sleep(2)
            self.assert_title(self.browser, name_='название 1')
        self.click_to_element(Locators.HISTORY_BUTTON_1)
        self.assert_title(self.browser, name_='История')
        self.click_to_element(Locators.LEARNING_BUTTON)
        time.sleep(1)
        self.assert_title(self.browser, name_='Обучение / Мое обучение')
        self.click_to_element(Locators.REPORT_BUTTON)
        time.sleep(1)
        self.assert_title(self.browser, name_='Обратная связь по контенту')
        self.click_to_element(Locators.PEOPLE_BUTTON)
        time.sleep(2)
        self.assert_title(self.browser, name_='Все участники')
        self.click_to_element(Locators.SETTINGS)
        time.sleep(3)
        self.assert_title(self.browser, name_='Настройки')

    def add_new_person(self):
        """ADD NEW PERSON"""
        self.browser.implicitly_wait(10)
        person = generated_person()
        last_name = person.last_name
        first_name = person.first_name
        email = person.email
        # self.screenshot()
        self.click_to_element(Locators.SETTINGS)
        self.click_to_element(Locators.PERSONS)
        self.click_to_element(Locators.NEW_PERSON)
        self.element_is_visible(Locators.CHANGE_ADMIN).send_keys('Администратор')
        time.sleep(1)
        self.remove_class_script()
        """add avatar"""
        avatar = Path(pathlib.Path.cwd(), "animal.jpeg")
        path = str(avatar)
        time.sleep(1)
        self.element_is_visible(Locators.UPLOAD_FILE).send_keys(path)
        time.sleep(3)
        text_name = self.element_is_visible(Locators.UPLOAD_FILE_NAME)
        text_name_value = text_name.text
        assert text_name_value == 'animal.jpeg'
        self.button_invisible_check()
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.button_invisible_check()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.button_invisible_check()
        self.element_is_visible(Locators.LOGIN_NEW_PERSON).send_keys(minervakms.login)
        self.button_invisible_check()
        self.click_to_element(Locators.SAVE_PERSON)
        check_text_must_be = self.element_is_visible(Locators.CHECK_MUST_BE_ADD)
        check_text_must_be_value = check_text_must_be.text
        assert check_text_must_be_value == 'Должно быть заполнено'
        # print(check_text_must_be_value)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.click_to_element(Locators.SAVE_PERSON)
        check_text_login_used = self.element_is_visible(Locators.CHECK_LOGIN_IS_USED)
        check_text_login_used_value = check_text_login_used.text
        assert check_text_login_used_value == 'Данный логин уже используется'
        # print(check_text_login_used_value)
        value_random = str(random.randint(999, 9999))
        self.element_is_visible(Locators.LOGIN_NEW_PERSON).clear()
        self.element_is_visible(Locators.LOGIN_NEW_PERSON).send_keys(minervakms.login + value_random)
        self.click_to_element(Locators.SAVE_PERSON)
        """check result create new person name"""
        name_check = last_name + ' ' + first_name
        time.sleep(1)
        text_check_created_new_user_name = self.browser.find_element(By.XPATH, f"//span[text()='{name_check}']")
        text_check_created_new_user_name_value = text_check_created_new_user_name.text
        assert text_check_created_new_user_name_value == name_check
        # print(text_check_created_new_user_name_value)
        print(minervakms.login + value_random)
        time.sleep(1)
        """check result create new person login"""
        login_admin = minervakms.login + value_random + ' (администратор)'
        text_check_created_new_user_login = self.browser.find_element(By.XPATH, f"//span[text()='{login_admin}']")
        text_check_created_new_user_value = text_check_created_new_user_login.text
        assert text_check_created_new_user_value == login_admin
        # print(text_check_created_new_user_value)
        """check result create new person mail"""
        email_check = email
        text_check_created_new_user_mail = self.browser.find_element(By.XPATH, f"//a[text()='{email_check}']")
        text_check_created_new_mail_value = text_check_created_new_user_mail.text
        assert text_check_created_new_mail_value == email_check
        # print(text_check_created_new_mail_value)

    def button_invisible_check(self):
        """CHECK INVISIBLE BUTTON"""
        try:
            time.sleep(1)
            save_person = self.browser.find_element(By.XPATH, "//p[text()='Сохранить пользователя']")
            save_person.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            print("Кнопка 'Сохранить пользователя' не активна")

    def button_invisible_role_check(self):
        try:
            self.click_to_element(Locators.CREATE_ROLE)
        except ElementClickInterceptedException:
            print("Кнопка 'Создать роль' не активна")

    def add_new_role(self):
        """ADD NEW ROLE"""
        self.browser.implicitly_wait(10)
        self.click_to_element(Locators.PEOPLE_BUTTON)
        try:
            add_new_role_button = self.browser.find_element(By.XPATH, "//p[text()='добавить роль']")
            add_new_role_button.click()
        except NoSuchElementException:
            self.click_to_element(Locators.ADD_NEW_ROLE)
        self.browser.implicitly_wait(10)
        person = generated_person()
        first_name = "role " + person.first_name + str(random.randint(999, 9999))
        self.button_invisible_role_check()
        self.element_is_visible(Locators.INPUT_NAME_ROLE).send_keys(first_name)
        # push 13 check boxes
        for x in range(1, 14):
            self.click_to_element(Locators.SWITCH_BOX)
        self.element_is_visible(Locators.SWITCH_BOX).is_displayed()
        self.click_to_element(Locators.CREATE_ROLE)
        """check result create new role"""
        check_role = first_name
        # print(check_role)
        time.sleep(0.5)
        text_check_created_new_role = self.browser.find_element(By.XPATH, f"//span[text()='{check_role}']")
        text_check_created_new_role_value = text_check_created_new_role.text
        assert text_check_created_new_role_value == check_role
        # print(text_check_created_new_role_value)
        # self.click_to_element(Locators.EDIT_NEW_ROLE)
        time.sleep(1)
        edit_new_role = self.browser.find_element(By.XPATH,
                                                  f"//span[text()='{first_name}']/..//div[@class='item-role__icon-edit']")
        edit_new_role.click()
        self.element_is_clickable(Locators.DEACTIVATE_ROLE)
        for x in range(1, 14):
            self.element_is_visible(Locators.SWITCH_BOX_CHECKED).is_displayed()
        self.element_is_visible(Locators.SWITCH_BOX).is_displayed()
        self.click_to_element(Locators.SAVE_CHANGES_ROLE)
        return first_name

    def create_new_folder(self):
        """CREATE NEW FOLDER"""
        # driver.implicitly_wait(10)
        person = generated_person()
        name_of_new_folder = person.first_name
        self.click_to_element(Locators.NEW_FOLDER)
        text_new_folder_check = self.element_is_visible(Locators.TEXT_NEW_FOLDER_CHECK)
        text_new_folder_check_value = text_new_folder_check.text
        assert text_new_folder_check_value == 'Новая папка'
        try:
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        except ElementClickInterceptedException:
            print("Кнопка 'Создать папку' НЕ активна")
        self.element_is_visible(Locators.PARENT_FOLDERS_CHOICE).send_keys('Нет')
        self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys(name_of_new_folder)
        self.click_to_element(Locators.RADIOBUTTON_SORT_BY_DATE)
        self.click_to_element(Locators.RADIOBUTTON_SORT_BY_POPULAR)
        self.click_to_element(Locators.RADIOBUTTON_SORT_BY_DATE)
        self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        time.sleep(1)
        self.click_to_element(Locators.CLOSE_WINDOW_STRUCTURE)
        try:
            text_all_content_check = self.browser.find_element(By.XPATH, "//h1[contains(text(),'Весь контент')]")
            text_all_content_check_value = text_all_content_check.text
            assert text_all_content_check_value == "Весь контент"
            # print(text_all_content_check_value)
        except NoSuchElementException:
            print('Контента пока нет')
        # time.sleep(1)
        self.browser.implicitly_wait(10)
        check_created_new_folder = self.browser.find_element(By.XPATH, f"//p[text()='{name_of_new_folder}']")
        check_created_new_folder_value = check_created_new_folder.text
        assert check_created_new_folder_value == name_of_new_folder
        # print(check_created_new_folder_value)
        # time.sleep(2)
        # for x in self.element_is_clickable(Locators.RADIOBUTTON_SEARCH).get_attribute("class"):
        #     print(x)
        # radio_on_check = self.element_is_clickable(Locators.RADIOBUTTON_SEARCH).get_attribute("class")
        # assert radio_on_check == 'radio-wrapper__icon radio-wrapper__icon--checked'
        # print(x)
        # self.element_is_visible(Locators.CREATE_FOLDER_BUTTON)

    def create_5_folder(self):
        """CREATE 5 FOLDERS"""
        n = 0
        while True:
            count_folders = n
            person = generated_person()
            name_of_new_folder = person.first_name
            self.click_to_element(Locators.NEW_FOLDER)
            self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys(name_of_new_folder)
            self.click_to_element(Locators.RADIOBUTTON_SORT_BY_DATE)
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
            time.sleep(1)
            n += 1
            if count_folders == 5:
                break
        # print("создано 5 папок")
        self.click_to_element(Locators.CLOSE_WINDOW_STRUCTURE)

    def delete_folder(self):
        """DELETE FOLDER"""
        self.click_to_element(Locators.FOLDERS_CHANGE)
        self.click_to_element(Locators.SECOND_FOLDER_IN_LIST)
        self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
        check_del_text = self.element_is_visible(Locators.DELETE_FOLDER_CONFIRM_TEXT)
        check_del_text_value = check_del_text.text
        assert check_del_text_value == 'Подтверждение действия'
        # print(check_del_text_value)
        self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
        print("папка удалена")
        self.click_to_element(Locators.CLOSE_WINDOW_STRUCTURE)
        time.sleep(2)

    def delete_some_folder(self, count_folders=3):  # ставить на 1 папку больше
        """DELETE SOME FOLDERS"""
        self.click_to_element(Locators.CONTENT)
        time.sleep(1)
        self.click_to_element(Locators.FOLDERS_CHANGE)
        n = 0
        try:
            while True:
                n += 1
                if n == count_folders:
                    break
                try:
                    time.sleep(1)
                    self.click_to_element(Locators.SECOND_FOLDER_IN_LIST_FOR_DEL, timeout=3)
                    # second_folder_in_list = driver.find_element(By.XPATH, "(//div[@class='tree-item-content'])[2]")
                    # second_folder_in_list
                    # self.click_to_element(Locators.SECOND_FOLDER_IN_LIST)
                    self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
                    time.sleep(1)
                    self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
                    time.sleep(1)
                except ElementClickInterceptedException:  # ElementClickInterceptedException
                    self.element_is_visible(Locators.MOVE_FROM_DEL_FOLDER).send_keys('Контент 1')
                    self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
                except TimeoutException:
                    self.element_is_visible(Locators.MOVE_FROM_DEL_FOLDER).send_keys('Контент 1')
                    self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
        except TimeoutException:
            print('папок нет больше')
        except NoSuchElementException:
            print('папок нет больше')

    def create_5_article(self):
        """ARTICLE"""
        n = 0
        x = 0
        name_folder = 'папка1'
        while True:
            self.browser.implicitly_wait(10)
            count_folders = n
            person = generated_person()
            name_article = person.first_name
            text_article = person.last_name
            try:
                self.click_to_element(Locators.CREATE_BUTTON_1)
            except TimeoutException:
                time.sleep(3)
            self.click_to_element(Locators.CREATE_ARTICLE)
            time.sleep(1)
            self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys(name_article)
            time.sleep(1)
            self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE).send_keys(name_folder)
            if x < 1:
                time.sleep(10)
            else:
                time.sleep(1)
            try:
                self.click_to_element(Locators.TYPOGRAPHY_ARTICLE)
            except ElementClickInterceptedException:
                time.sleep(5)
                self.click_to_element(Locators.TYPOGRAPHY_ARTICLE)
            self.click_to_element(Locators.SUBMIT_ARTICLE)
            self.click_to_element(Locators.SUBMIT_ARTICLE)
            self.click_to_element(Locators.SUBMIT_ARTICLE)
            self.element_is_visible(Locators.TEXTAREA_ARTICLE).send_keys(text_article)
            self.click_to_element(Locators.SUBMIT_ARTICLE)
            # при нажатии на SUBMIT_ARTICLE вечная загрузка
            time.sleep(5)
            try:
                self.click_to_element(Locators.CLOSE_CREATED_ARTICLE)
            except TimeoutException:
                time.sleep(5)
                # self.click_to_element(Locators.SUBMIT_ARTICLE)
                self.click_to_element(Locators.CLOSE_CREATED_ARTICLE)
            n += 1
            x += 1
            if count_folders >= 4:
                name_folder = "папка2"
                if count_folders >= 9:
                    break
        # print("создано по 5 статей")

    def create_del_recovery_folder_content(self):
        """CREATE DELETE RECOVERY FOLDER"""
        self.click_to_element(Locators.CONTENT)
        """check open text"""
        text_folder_check = self.element_is_visible(Locators.TEXT_FOLDERS_CHECK)
        text_folder_check_value = text_folder_check.text
        assert text_folder_check_value == "Папки"
        # print(text_folder_check_value)
        try:
            text_all_content_check = self.browser.find_element(By.XPATH, "//h1[contains(text(),'Весь контент')]")
            text_all_content_check_value = text_all_content_check.text
            assert text_all_content_check_value == "Весь контент"
            # print(text_all_content_check_value)
        except NoSuchElementException:
            print('Контента пока нет')
        """reproduce steps"""
        self.click_to_element(Locators.FOLDERS_CHANGE)
        text_open_form_check = self.element_is_visible(Locators.TEXT_OPEN_FORM_CHECK)
        text_open_form_check_value = text_open_form_check.text
        assert text_open_form_check_value == "Управление структурой"
        # print(text_open_form_check_value)
        """create folder"""
        person = generated_person()
        name_of_new_folder = person.first_name + str(random.randint(99, 999))
        self.click_to_element(Locators.NEW_FOLDER)
        text_new_folder_check = self.element_is_visible(Locators.TEXT_NEW_FOLDER_CHECK)
        text_new_folder_check_value = text_new_folder_check.text
        assert text_new_folder_check_value == 'Новая папка'
        try:
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        except ElementClickInterceptedException:
            print("Кнопка 'Создать папку' НЕ активна")
        self.element_is_visible(Locators.PARENT_FOLDERS_CHOICE).send_keys('Нет')
        self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys(name_of_new_folder)
        # self.screenshot()
        # print("check radiobutton")
        self.element_is_visible(Locators.CHECK_RADIO_POPULAR).is_displayed()
        self.click_to_element(Locators.RADIOBUTTON_SORT_BY_DATE)
        self.click_to_element(Locators.RADIOBUTTON_SORT_BY_POPULAR)
        self.click_to_element(Locators.RADIOBUTTON_SORT_BY_DATE)
        self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        time.sleep(1)
        self.click_to_element(Locators.CLOSE_WINDOW_STRUCTURE)
        try:
            text_all_content_check = self.browser.find_element(By.XPATH, "//h1[contains(text(),'Весь контент')]")
            text_all_content_check_value = text_all_content_check.text
            assert text_all_content_check_value == "Весь контент"
            # print(text_all_content_check_value)
        except NoSuchElementException:
            print('Контента пока нет')
        # time.sleep(1)
        self.browser.implicitly_wait(10)
        check_created_new_folder = self.browser.find_element(By.XPATH, f"//p[text()='{name_of_new_folder}']")
        check_created_new_folder_value = check_created_new_folder.text
        assert check_created_new_folder_value == name_of_new_folder
        # print(check_created_new_folder_value)
        """del folder"""
        self.click_to_element(Locators.FOLDERS_CHANGE)
        folder_fol_del_by_name = self.browser.find_element(By.XPATH, f"//div[contains(text(),'{name_of_new_folder}')]")
        folder_fol_del_by_name.click()
        self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
        check_del_text = self.element_is_visible(Locators.DELETE_FOLDER_CONFIRM_TEXT)
        check_del_text_value = check_del_text.text
        assert check_del_text_value == 'Подтверждение действия'
        # print(check_del_text_value)
        self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
        # print("папка удалена")
        self.click_to_element(Locators.CLOSE_WINDOW_STRUCTURE)
        time.sleep(2)
        """recovery folder"""
        self.click_to_element(Locators.SHOW_DELETED_FOLDERS)
        time.sleep(1)
        recovery_folder_by_name = self.browser.find_element(By.XPATH, f"//p[normalize-space()='{name_of_new_folder}']")
        recovery_folder_by_name.click()
        time.sleep(1)
        self.click_to_element(Locators.RECOVERY_FOLDER_BUTTON)
        time.sleep(1)
        self.click_to_element(Locators.RECOVERY_FOLDER_BUTTON_CONFIRM)
        # print("папка восстановлена")

        self.browser.refresh()
        self.click_to_element(Locators.FOLDERS_CHANGE)
        time.sleep(1)
        folder_fol_del_by_name = self.browser.find_element(By.XPATH, f"//div[contains(text(),'{name_of_new_folder}')]")
        folder_fol_del_by_name.click()
        time.sleep(1)
        # self.screenshot()
        self.click_to_element(Locators.CLOSE_EDIT_FOLDERS_WINDOW)
        time.sleep(2)
        """create 5 folder"""
        self.create_5_folder()
        """!!!!!check radiobutton by date!!!!!"""

    def folder1_folder2(self):
        """FOLDER 1 AND FOLDER 2"""
        folder1_name = "папка1"
        folder2_name = "папка2"
        self.click_to_element(Locators.CONTENT)
        self.click_to_element(Locators.FOLDERS_CHANGE)
        """folder1"""
        self.click_to_element(Locators.NEW_FOLDER)
        self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys(folder1_name)
        self.click_to_element(Locators.RADIOBUTTON_SORT_BY_DATE)
        self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        """folder2"""
        self.click_to_element(Locators.NEW_FOLDER)
        self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys(folder2_name)
        # self.click_to_element(Locators.RADIOBUTTON_SORT_BY_DATE)
        self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        time.sleep(1)
        self.click_to_element(Locators.CLOSE_WINDOW_STRUCTURE)
        """create 5 articles"""
        time.sleep(1)
        self.create_5_article()

    def check_folder1_folder2(self):
        """CHECK FOLDER 1 AND FOLDER 2"""
        self.browser.implicitly_wait(10)
        self.click_to_element(Locators.CONTENT)
        self.click_to_element(Locators.FOLDERS_CHANGE)
        self.click_to_element(Locators.FOLDER1)
        time.sleep(1)
        self.click_to_element(Locators.RADIOBUTTON_SORT_BY_DATE)
        time.sleep(1)
        self.click_to_element(Locators.SAVE_CHANGES_FOLDER)
        self.click_to_element(Locators.FOLDER2)
        time.sleep(1)
        self.click_to_element(Locators.RADIOBUTTON_SORT_BY_POPULAR)
        self.click_to_element(Locators.SAVE_CHANGES_FOLDER)
        """check radiobutton"""
        self.click_to_element(Locators.FOLDER1)
        time.sleep(1)
        self.element_is_visible(Locators.CHECK_RADIOBUTTON_DATE).is_selected()
        # time.sleep(1)
        self.click_to_element(Locators.SAVE_CHANGES_FOLDER)
        self.click_to_element(Locators.FOLDER2)
        time.sleep(1)
        self.element_is_visible(Locators.CHECK_RADIOBUTTON_POPULARITY).is_selected()
        # time.sleep(1)
        self.click_to_element(Locators.SAVE_CHANGES_FOLDER)
        time.sleep(1)
        # self.click_to_element(Locators.CLOSE_WINDOW_STRUCTURE)
        self.browser.back()
        # time.sleep(1)
        self.click_to_element(Locators.ALL_CONTENT)
        self.click_to_element(Locators.SORT_BY_ALL_CONTENT)
        self.click_to_element(Locators.FOLDERS_CHANGE)
        self.click_to_element(Locators.FOLDER2)
        time.sleep(1)
        self.element_is_visible(Locators.CHECK_RADIOBUTTON_POPULARITY).is_selected()
        self.click_to_element(Locators.RADIOBUTTON_SORT_BY_DATE)
        time.sleep(1)
        self.element_is_visible(Locators.CHECK_RADIOBUTTON_DATE).is_selected()
        time.sleep(1)
        self.click_to_element(Locators.SAVE_CHANGES_FOLDER)
        time.sleep(1)
        # self.click_to_element(Locators.CLOSE_WINDOW_STRUCTURE)
        self.browser.back()
        # time.sleep(1)
        self.click_to_element(Locators.ALL_CONTENT)
        text_sort_by_all_content = self.browser.find_element(By.XPATH, "//span[contains(text(),'по популярности')]")
        text_sort_by_all_content_value = text_sort_by_all_content.text
        assert text_sort_by_all_content_value == 'по популярности'
        # print("сортировка по популярности сохранена")

    def favourites(self):
        """FAVOURITES"""
        self.browser.implicitly_wait(10)
        "в избранном не должно быть папок"
        self.browser.implicitly_wait(10)
        person = generated_person()
        first_name = person.first_name
        self.click_to_element(Locators.CONTENT)
        self.click_to_element(Locators.FAVOURITES)
        check_text_structure = self.element_is_visible(Locators.CHECK_TEXT_STRUCTURE).text
        check_text_structure_value = check_text_structure
        assert check_text_structure_value == 'Управление структурой'
        # print("Управление структурой")
        check_text_favourites = self.element_is_visible(Locators.CHECK_TEXT_FAVOURITES).text
        check_text_favourites_value = check_text_favourites
        assert check_text_favourites_value == 'избранное'
        # print("избранное")
        self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        # self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        text_new_folder_check = self.element_is_visible(Locators.TEXT_NEW_FOLDER_CHECK).text
        text_new_folder_check_value = text_new_folder_check
        assert text_new_folder_check_value == "Новая папка"
        # print("Новая папка")
        self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys(first_name)
        self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        check_text_structure = self.element_is_visible(Locators.CHECK_TEXT_STRUCTURE).text
        check_text_structure_value = check_text_structure
        assert check_text_structure_value == 'Управление структурой'
        # print("Управление структурой")
        time.sleep(2)
        edit_new_folder = self.browser.find_element(By.XPATH, f"//div[text()='{first_name}']")
        edit_new_folder.click()
        edit_name = first_name + '777'
        # self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).clear()
        time.sleep(1)
        self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys("777")
        self.click_to_element(Locators.SAVE_CHANGES_FOLDER)
        time.sleep(2)
        edit_new_folder = self.browser.find_element(By.XPATH, f"//div[text()='{edit_name}']")
        edit_new_folder.click()
        self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
        time.sleep(1)
        self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
        time.sleep(1)
        text_not_folders = self.element_is_visible(Locators.TEXT_NOT_FOLDERS)
        text_not_folders_value = text_not_folders.text
        assert text_not_folders_value == "У вас нет избранного контента. Для начала создайте папку."
        # print("У вас нет избранных папок. Создайте папку.")

    def add_favourites_to_folder(self, folder="папка1"):
        self.click_to_element(Locators.ADD_TO_FAVOURITES_ARTICLE)
        # self.click_to_element(Locators.ADD_TO_FAVOURITES_ARTICLE)
        self.element_is_visible(Locators.ADD_FAVOURITES_TO_FOLDER).send_keys(folder)
        self.click_to_element(Locators.ADD_BUTTON)
        time.sleep(1)
        self.click_to_element(Locators.CLOSE_CREATED_ARTICLE)

    @allure.title("Добавление контента в Избранное")
    def add_to_favourites(self):
        """ДОЛЖНЫ БЫТЬ СОЗДАНЫ СТАТЬИ"""
        self.click_to_element(Locators.CONTENT)
        self.click_to_element(Locators.FAVOURITES)
        try:
            time.sleep(1)
            create_folder_button = self.browser.find_element(By.XPATH, "//p[contains(text(),'Создать папку')]")
            create_folder_button.click()
            # self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        except NoSuchElementException:
            """del all folder favourites"""
            # self.click_to_element(Locators.FAVOURITES)
            # time.sleep(1)
            n = 0
            while True:
                try:
                    time.sleep(1)
                    try:
                        # self.click_to_element(Locators.FOLDER1_FOR_DEL)
                        folder1_for_del = self.browser.find_element(By.XPATH,
                                                                    "//div[@class='m-tree-item__draggable-content']")
                        folder1_for_del.click()
                    except NoSuchElementException:
                        break
                    time.sleep(1)
                    # x
                    # time.sleep(1)
                    self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
                    time.sleep(1)
                    self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
                    n += 1
                    if n >= 3:
                        break
                except TimeoutException:
                    self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
            self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        time.sleep(1)
        self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys("папка1")
        self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        time.sleep(1)
        self.click_to_element(Locators.NEW_FOLDER)
        time.sleep(1)
        self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys("папка2")
        time.sleep(1)
        self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        time.sleep(1)
        self.click_to_element(Locators.NEW_FOLDER)
        self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys("папка3")
        self.click_to_element(Locators.CREATE_FOLDER_BUTTON)
        self.click_to_element(Locators.CLOSE_WINDOW_STRUCTURE)
        """add to folder1"""
        # self.click_to_element(Locators.CONTENT)
        time.sleep(2)
        try:
            self.click_to_element(Locators.ARTICLE_FIRST1)
        except TimeoutException:
            time.sleep(2)
            self.click_to_element(Locators.CLOSE_WINDOW_STRUCTURE)
            self.click_to_element(Locators.ARTICLE_FIRST1)
        time.sleep(1)
        self.add_favourites_to_folder(folder="папка1")
        self.click_to_element(Locators.ARTICLE_FIRST2)
        self.add_favourites_to_folder(folder="папка1")
        """add to folder2"""
        self.click_to_element(Locators.ARTICLE_FIRST3)
        self.add_favourites_to_folder(folder="папка2")
        self.click_to_element(Locators.ARTICLE_FIRST4)
        self.add_favourites_to_folder(folder="папка2")
        self.click_to_element(Locators.ARTICLE_FIRST5)
        self.add_favourites_to_folder(folder="папка2")
        self.click_to_element(Locators.ARTICLE_FIRST6)
        self.add_favourites_to_folder(folder="папка2")
        """add to folder3"""
        self.click_to_element(Locators.ARTICLE_FIRST7)
        self.add_favourites_to_folder(folder="папка3")
        self.click_to_element(Locators.ARTICLE_FIRST8)
        self.add_favourites_to_folder(folder="папка3")
        self.click_to_element(Locators.ARTICLE_FIRST9)
        self.add_favourites_to_folder(folder="папка3")
        """check count articles in folder 1"""
        self.click_to_element(Locators.CREATED_FOLDER1)
        time.sleep(2)
        check_text_count_of_articles = self.element_is_visible(Locators.CHECK_TEXT_COUNT_OF_ARTICLES1)
        check_text_count_of_articles_value = check_text_count_of_articles.text
        assert check_text_count_of_articles_value == '2 документа'
        """check count articles in folder 2"""
        self.click_to_element(Locators.CREATED_FOLDER2)
        check_text_count_of_articles = self.element_is_visible(Locators.CHECK_TEXT_COUNT_OF_ARTICLES2)
        check_text_count_of_articles_value = check_text_count_of_articles.text
        assert check_text_count_of_articles_value == '4 документа'
        """check count articles in folder 3"""
        self.click_to_element(Locators.CREATED_FOLDER3)
        check_text_count_of_articles = self.element_is_visible(Locators.CHECK_TEXT_COUNT_OF_ARTICLES3)
        check_text_count_of_articles_value = check_text_count_of_articles.text
        assert check_text_count_of_articles_value == '3 документа'
        """delete 3 folders"""
        self.click_to_element(Locators.FAVOURITES)
        time.sleep(1)

        n = 0
        while True:
            try:
                time.sleep(1)
                try:
                    # self.click_to_element(Locators.FOLDER1_FOR_DEL)
                    folder1_for_del = self.browser.find_element(By.XPATH,
                                                                "//div[@class='m-tree-item__draggable-content']")
                    folder1_for_del.click()
                except NoSuchElementException:
                    break
                time.sleep(1)
                # x
                # time.sleep(1)
                self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
                time.sleep(1)
                self.click_to_element(Locators.DELETE_FOLDER_BUTTON)
                n += 1
                if n >= 3:
                    break
            except TimeoutException:
                self.click_to_element(Locators.DELETE_FOLDER_BUTTON)

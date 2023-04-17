import datetime
import os
import random
import time
import pyautogui
import selenium
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from pages.base_page import BasePage
from locators.form_pages_locators import FormPagesLocators as Locators
from pages.data_login_password import *


class FormPage(BasePage):

    def full_authorization(self, driver):
        """CORRECT DATA"""
        self.login = login
        self.password = password
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.authorization(self.login, self.password)
        # form_page.check_project_page()
        # time.sleep(1)

    def authorization(self, login, password):
        self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.INPUT_BUTTON).click()
        time.sleep(1)

    def input_in_my_project(self, driver):
        """INPUT IN MY PROJECT"""
        # form_page = FormPage(driver, url)
        # form_page.open()
        # form_page.authorization(self.login, self.password)
        self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.INPUT_BUTTON).click()
        self.element_is_visible(Locators.TEST_PROJECT).click()
        # time.sleep(1)
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('enter')
        # driver.refresh()


    def fill_fields(self, login, password):
        """FILL FIELDS PAGE OF AUTHORIZATION"""
        self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.INPUT_BUTTON).click()
        time.sleep(1)
        self.element_is_visible(Locators.LOGIN).clear()
        self.element_is_visible(Locators.PASSWORD).clear()
        time.sleep(1)

    def check_auth_text(self):
        """CHECK TEXT INCORRECT LOGIN AND PASSWORD"""
        check_logit_text = self.element_is_visible(Locators.INCORRECT_LOGIN_TEXT)
        check_logit_text_value = check_logit_text.text
        assert check_logit_text_value == 'Неверный логин'
        check_password_text = self.element_is_visible(Locators.INCORRECT_PASSWORD_TEXT)
        check_password_text_value = check_password_text.text
        assert check_password_text_value == 'Неверный пароль'
        print(f'Текст: <{check_logit_text_value}> и <{check_password_text_value}> на странице авторизации УСПЕШНО')

    def restore_incorrect(self):
        """RESTORE INPUT INCORRECT LOGIN"""
        login = login_incorrect
        self.element_is_visible(Locators.RESTORE).click()
        self.element_is_visible(Locators.RESTORE_LOGIN).send_keys(login)
        self.element_is_visible(Locators.RESTORE_BUTTON).click()
        # self.element_is_visible(Locators.REMEMBER_PASSWD)

    def check_restore_text(self):
        """CHECK TEXT INCORRECT LOGIN ON PAGE RESTORE"""
        check_logit_text = self.element_is_visible(Locators.INCORRECT_LOGIN_TEXT)
        check_logit_text_value = check_logit_text.text
        assert check_logit_text_value == 'Неверный логин'
        print(f'Текст: <{check_logit_text_value}> на странице восстановления УСПЕШНО')

    def restore_correct(self):
        """RESTORE PASSWORD BY CORRECT LOGIN END PUSH REMEMBER PASSWORD"""
        self.element_is_visible(Locators.RESTORE).click()
        self.element_is_visible(Locators.RESTORE_LOGIN).send_keys(login)
        self.element_is_visible(Locators.RESTORE_BUTTON).click()
        time.sleep(1)
        self.screenshot()
        # self.element_is_visible(Locators.RESTORE_BUTTON).click()
        self.element_is_visible(Locators.REMEMBER_PASSWD).click()
        time.sleep(1)
        check_page_author = self.element_is_visible(Locators.PAGE_AUTH)
        check_page_author_value = check_page_author.text
        assert check_page_author_value == 'Вход в систему'
        print('Письмо с новым паролем отправлено на почту УСПЕШНО')
        print(f'Страница {check_page_author_value} УСПЕШНО')

    def screenshot(self):
        offset = datetime.timezone(datetime.timedelta(hours=3))  # timezone (+3)
        now_date = datetime.datetime.now(offset)
        now_date = now_date.strftime('%Y.%m.%d.%H.%M.%S')
        # now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot.png' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\User\\PycharmProjects\\Minervasoft\\screen\\' + name_screenshot)

    def check_project_page(self):
        """CHECK PAGE BY WORDS"""
        check_project = self.element_is_visible(Locators.CHANGE_PROJECT)
        check_project_value = check_project.text
        assert check_project_value == 'Выберите проект'
        print('Страница ' + check_project_value + ' открыта')

    def logo_head(self):
        """LOGO"""
        logo = self.element_is_visible(Locators.LOGO_HEAD)
        print(logo.is_displayed())

    # def hover(self, driver):
    #     """MOUSE"""
    #     element = self.element_is_visible(Locators.LOGO_HEAD)
    #     hov = ActionChains(driver).move_to_element(element)
    #     hov.perform()

    def input_project(self):
        """INPUT IN SELEN PROJECT"""
        self.element_is_visible(Locators.TEST_PROJECT).click()
        time.sleep(1)
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('enter')
        # driver.refresh()

    def title_find(self, driver):
        """TITLE"""
        # driver.title()
        title = driver.execute_script("return document.title;")
        print(title)

    def assert_title(self, driver, name_project='selen', name_='Контент 1'):
        """ASSERT"""
        # driver.implicitly_wait(10)
        time.sleep(0.5)
        # title = driver.execute_script("return document.title;")
        title = driver.title
        # title = title.text
        result = f'{name_} / {name_project} — Minervasoft'
        assert title == result
        print(result)

    def all_title(self, driver):
        # driver.implicitly_wait(10)
        # time.sleep(1)
        self.element_is_visible(Locators.CONTENT).click()
        self.element_is_visible(Locators.ALL_CONTENT).click()
        self.assert_title(driver, name_project='selen', name_='Весь контент')
        self.element_is_visible(Locators.CONTENT1).click()
        # time.sleep(5)
        # text_name = self.element_is_visible(Locators.CONTENT1_NAME).click()
        # text_name_value = text_name.text
        # print(text_name_value)
        self.assert_title(driver, name_project='selen', name_='Контент 1')
        self.element_is_visible(Locators.NAME_CONTENT).click()
        self.assert_title(driver, name_project='selen', name_='Название 1')

        driver.back()
        self.element_is_visible(Locators.CREATE_BUTTON).click()
        time.sleep(0.5)
        self.element_is_visible(Locators.CREATE_ARTICLE).click()
        self.assert_title(driver, name_project='selen', name_='Добавить статью')
        time.sleep(7)
        self.element_is_visible(Locators.CLOSE_PAGE_LIST).click()
        # self.element_is_visible(Locators.CLOSE_PAGE_LIST).click()
        self.element_is_visible(Locators.CREATE_STEP_SCRIPT).click()
        # # time.sleep(5)
        self.assert_title(driver, name_project='selen', name_='Добавить пошаговый сценарий')
        time.sleep(1)
        self.element_is_visible(Locators.CLOSE_PAGE_SCRIPT).click()
        self.element_is_visible(Locators.CLOSE_CREATE_WINDOW).click()
        self.element_is_visible(Locators.SEARCH_PROJECT).click()
        self.element_is_visible(Locators.SEARCH_INPUT).send_keys('название 1')
        self.element_is_visible(Locators.SEARCH_INPUT).send_keys(Keys.RETURN)
        self.assert_title(driver, name_project='selen', name_='название 1')
        self.element_is_visible(Locators.HISTORY_BUTTON).click()
        self.assert_title(driver, name_project='selen', name_='История')
        self.element_is_visible(Locators.LEARNING_BUTTON).click()
        time.sleep(0.5)
        self.assert_title(driver, name_project='selen', name_='Обучение / Мое обучение')
        self.element_is_visible(Locators.REPORT_BUTTON).click()
        time.sleep(0.5)
        self.assert_title(driver, name_project='selen', name_='Обратная связь по контенту')
        self.element_is_visible(Locators.PEOPLE_BUTTON).click()
        time.sleep(0.5)
        self.assert_title(driver, name_project='selen', name_='Все участники')
        self.element_is_visible(Locators.SETTINGS).click()
        time.sleep(0.5)
        self.assert_title(driver, name_project='selen', name_='Настройки')

    def add_new_person(self, driver):
        driver.implicitly_wait(10)
        person = generated_person()
        last_name = person.last_name
        first_name = person.first_name
        email = person.email

        self.element_is_visible(Locators.SETTINGS).click()
        print("settings")
        self.element_is_visible(Locators.PERSONS).click()
        print("person")
        self.element_is_visible(Locators.NEW_PERSON).click()
        print("new person")
        self.element_is_visible(Locators.CHANGE_ADMIN).send_keys('Администратор')
        print("administrator")
        self.remove_class_script()
        path = (r'C:\Users\User\PycharmProjects\Minervasoft\animal.jpeg')
        self.element_is_visible(Locators.UPLOAD_FILE).send_keys(path)
        text_name = self.element_is_visible(Locators.UPLOAD_FILE_NAME)
        text_name_value = text_name.text
        assert text_name_value == 'animal.jpeg'
        print('file name is correct')
        self.button_invisible_check(driver)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.button_invisible_check(driver)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.button_invisible_check(driver)
        self.element_is_visible(Locators.LOGIN_NEW_PERSON).send_keys(login)
        self.button_invisible_check(driver)
        self.element_is_visible(Locators.SAVE_PERSON).click()
        check_text_must_be = self.element_is_visible(Locators.CHECK_MUST_BE_ADD)
        check_text_must_be_value = check_text_must_be.text
        assert check_text_must_be_value == 'Должно быть заполнено'
        print(check_text_must_be_value)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.SAVE_PERSON).click()
        check_text_login_used = self.element_is_visible(Locators.CHECK_LOGIN_IS_USED)
        check_text_login_used_value = check_text_login_used.text
        assert check_text_login_used_value == 'Данный логин уже используется'
        print(check_text_login_used_value)
        value_random = str(random.randint(999,9999))
        self.element_is_visible(Locators.LOGIN_NEW_PERSON).clear()
        self.element_is_visible(Locators.LOGIN_NEW_PERSON).send_keys(login+value_random)
        # print(login+value_random)
        self.element_is_visible(Locators.SAVE_PERSON).click()
        """check result create new person name"""
        name_check = last_name + ' ' + first_name
        text_check_created_new_user_name = driver.find_element(By.XPATH, f"//span[text()='{name_check}']")
        text_check_created_new_user_name_value = text_check_created_new_user_name.text
        assert text_check_created_new_user_name_value == name_check
        print(text_check_created_new_user_name_value)
        """check result create new person login"""
        text_check_created_new_user_login = driver.find_element(By.XPATH, f"//span[text()='{login+value_random} ']")
        text_check_created_new_user_value = text_check_created_new_user_login.text
        assert text_check_created_new_user_value == login+value_random
        print(text_check_created_new_user_value)







        time.sleep(2)

    def button_invisible_check(self, driver):

        try:
            save_person = driver.find_element(By.XPATH, "//p[text()='Сохранить пользователя']")
            save_person.click()
        except ElementClickInterceptedException:
            print("Кнопка 'Сохранить пользователя' не активна")





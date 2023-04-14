import datetime
import time
import pyautogui
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
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

    def input_project(self, driver):
        """INPUT IN SELEN PROJECT"""
        self.element_is_visible(Locators.TEST_PROJECT).click()
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        driver.refresh()
        # self.element_is_visible(Locators.CONTENT).click()
        # self.element_is_visible(Locators.CONTENT1).click()
        # time.sleep(2)
        # title = driver.execute_script("return document.title;")
        # print(title)

    def title_find(self, driver):
        """TITLE"""
        title = driver.execute_script("return document.title;")
        print(title)

    def assert_title(self, driver, name_project='selen', name_='Контент 1'):
        """ASSERT"""
        driver.implicitly_wait(10)
        time.sleep(0.5)
        title = driver.execute_script("return document.title;")
        result = f'{name_} / {name_project} — Minervasoft'
        assert title == result
        print(result)

    def all_title(self, driver):
        # driver.implicitly_wait(10)
        self.element_is_visible(Locators.CONTENT).click()
        self.element_is_visible(Locators.ALL_CONTENT).click()
        self.assert_title(driver, name_project='selen', name_='Весь контент')
        self.element_is_visible(Locators.CONTENT1).click()
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



        time.sleep(5)

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class FormPagesLocators:
    TYPE_AUTHOR = (By.CSS_SELECTOR, '.m-ui-select__select')
    TYPE_AUTHOR_CHANGE = (By.XPATH, "//option[@type='EMBEDDED']")
    LOGIN = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    INPUT_BUTTON = (By.XPATH, "//button[@type='submit']")
    TEST_PROJECT = (By.XPATH, "//a[@href='/news/space/56']")
    """restore forms"""
    RESTORE = (By.XPATH, "//span[text()='Восстановить доступ']")
    RESTORE_LOGIN = (By.NAME, "username")
    RESTORE_BUTTON = (By.XPATH, "//button[@type='submit']")
    REMEMBER_PASSWD = (By.XPATH, "//span[text()='я помню пароль']")
    """text asserts"""
    INCORRECT_LOGIN_TEXT = (By.XPATH, "//div[text()='Неверный логин']")
    INCORRECT_PASSWORD_TEXT = (By.XPATH, "//div[text()='Неверный пароль']")
    CHANGE_PROJECT = (By.XPATH, "//h1[text()='Выберите проект']")
    """logo"""
    LOGO_HEAD = (By.CLASS_NAME, 'm-main-menu-logo__icon')
    LOGO_FAVICO = (By.ID, 'favicon')
    """title"""
    TAB2 = (Keys.TAB)
    ENTER1 = (Keys.RETURN)







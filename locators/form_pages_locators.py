from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class FormPagesLocators:
    TYPE_AUTHOR = (By.CSS_SELECTOR, '.m-ui-select__select')  # type author
    TYPE_AUTHOR_CHANGE = (By.XPATH, "//option[@type='EMBEDDED']")  # new type auth
    LOGIN = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    INPUT_BUTTON = (By.XPATH, "//button[@type='submit']")
    TEST_PROJECT = (By.XPATH, "//article[@class='m-main-modal__main']//a[1]")  # first name project
    """restore forms"""
    RESTORE = (By.XPATH, "//span[text()='Восстановить доступ']")
    RESTORE_LOGIN = (By.NAME, "username")
    RESTORE_BUTTON = (By.XPATH, "//button[@type='submit']")
    REMEMBER_PASSWD = (By.XPATH, "//span[text()='я помню пароль']")
    """text asserts"""
    PAGE_AUTH = (By.XPATH, "//h1[text()='Вход в систему']")
    INCORRECT_LOGIN_TEXT = (By.XPATH, "//div[text()='Неверный логин']")
    INCORRECT_PASSWORD_TEXT = (By.XPATH, "//div[text()='Неверный пароль']")
    CHANGE_PROJECT = (By.XPATH, "//h1[text()='Выберите проект']")
    """logo"""
    LOGO_HEAD = (By.CLASS_NAME, 'm-main-menu-logo__icon')
    LOGO_FAVICO = (By.ID, 'favicon')
    MOUSE_LOGO = (By.XPATH, "//img[@class='m-main-menu-logo__icon']")
    """title"""
    CONTENT = (By.XPATH, "//a[@data-tip='Контент']")  # content of page
    ALL_CONTENT = (By.CLASS_NAME, "folder-list-item__total")
    CONTENT1 = (By.XPATH, "//div[@id='245']")
    CONTENT1_NAME = (By.XPATH, "//p[contains(text(),'Контент 1')]")  # check name of content

    NAME_CONTENT = (By.XPATH, "//section[2]//article[1]//a[1]//section[1]")
    EDIT = (By.XPATH, "//body/div[@class='article-modal__portal']/div[@class='ReactModal__Overlay ReactModal__Overlay--after-open article-modal__overlay']/div[@role='dialog']/article[@class='article-modal']/div[@class='article-modal__main']/div[@class='scroller article-modal__scroller']/div[@class='scroller__wrap']/div[@class='scroller__body']/div[@class='scroller__content article-modal__scroller-content']/div[@class='article-modal__container']/header[@id='article-content-modal-header']/div[@class='article-modal__controls']/button[2]")
    CREATE_BUTTON = (By.CSS_SELECTOR, ".m-button.m-button--default")
    CREATE_ARTICLE = (By.XPATH, "(//div[@class='m-lms-action-tooltip'])[1]")
    CREATE_STEP_SCRIPT = (By.XPATH, "(//div[@class='m-lms-action-tooltip'])[3]")
    CLOSE_PAGE_LIST = (By.XPATH, "//div[@class='article-editor__controls']//*[name()='svg']")
    CLOSE_PAGE_SCRIPT = (By.XPATH, "(//*[name()='svg'][@class='m-scenario-flow__close'])[1]")
    CLOSE_CREATE_WINDOW = (By.XPATH, "//div[@class='m-popup__close']//*[name()='svg']")
    SEARCH_PROJECT = (By.CSS_SELECTOR, ".m-dashboard-top__search")
    SEARCH_INPUT = (By.XPATH, "//input[@class='dashboard-search__input']")
    HISTORY_BUTTON = (By.XPATH, "//a[@data-tip='История']")
    LEARNING_BUTTON = (By.XPATH, "//a[@data-tip='Обучение']")
    REPORT_BUTTON = (By.XPATH, "//a[@data-tip='Отчеты']")
    PEOPLE_BUTTON = (By.XPATH, "//a[@data-tip='Участники']")
    SETTINGS = (By.XPATH, "//a[@data-tip='Настройки']")
    """add new person"""
    PERSONS = (By.XPATH, "//a[2]//article[1]//pre[1]")
    NEW_PERSON = (By.XPATH, "//button[@class='m-button m-button--default m-button--medium']")
    CHANGE_ADMIN = (By.XPATH, "//select[@class='m-ui-select__select']")
    UPLOAD_FILE = (By.XPATH, "//input[@type='file']")
    UPLOAD_FILE_NAME = (By.XPATH, "//span[@class='m-upload__file-name']")
    LAST_NAME = (By.XPATH, "//input[@data-type='surname']")
    FIRST_NAME = (By.XPATH, "//input[@data-type='firstname']")
    EMAIL = (By.XPATH, "//input[@data-type='email']")
    LOGIN_NEW_PERSON = (By.XPATH, "//input[@data-type='login']")
    SAVE_PERSON = (By.XPATH, "//p[text()='Сохранить пользователя']")
    CHECK_MUST_BE_ADD = (By.XPATH, "//div[text()='Должно быть заполнено']")
    CHECK_LOGIN_IS_USED = (By.XPATH, "//div[text()='Данный логин уже используется']")
    # CHECH_NEW_CREATED_USER = (By.XPATH, f"//span[text()={}]")














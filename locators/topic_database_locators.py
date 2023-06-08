from selenium.webdriver.common.by import By


class CreateTopicDatabaseLocators:
    LEARNING_BUTTON = (By.XPATH, "//a[@data-html='true']")
    TAB_ALL_COURSES = (By.XPATH, "//p[contains(text(),'все курсы')]")
    DATABASE_OF_QUESTIONS = (By.XPATH, "//p[contains(text(),'База вопросов')]")
    """check text open form"""
    TEXT_DATABASE_OF_QUESTIONS = (By.XPATH, "//p[contains(text(),'База вопросов')]")
    TEXT_NOT_QUESTIONS_NOW = (By.XPATH, "//p[text()='В этом проекте пока нет вопросов. Создайте структуру тем для его размещения']")
    BUTTON_ADD_TOPIC = (By.XPATH, "//p[contains(text(),'Создать темы')]")
    """check text open form new topic"""
    TEXT_NEW_QUESTION_WINDOW = (By.XPATH, "//h3[contains(text(),'Новая тема')]")
    TEXT_NAME = (By.XPATH, "//div[text()= 'название']")
    TEXT_PLACEHOLDER_INPUT_NAME_TOPIC = (By.XPATH, "//input[@placeholder='Введите название темы']")
    TEXT_PARENT_TOPIC = (By.XPATH, "//div[text()='родительская тема']")
    TEXT_DROPDOWN_DEFAULT = (By.XPATH, "//select[@class='m-ui-select__select']//option[text()='Нет']") # ПРОВЕРИТЬ
    BUTTON_CREATE_TOPIC = (By.XPATH, "//footer[@class='m-popup__footer lms-edit-theme-popup__footer']//p[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x16 m-button__text'][contains(text(),'Создать тему')]") # ПРОВЕРИТЬ



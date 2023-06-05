from selenium.webdriver.common.by import By


class FilesFormatPageLocators:
    CREATE_BUTTON = (By.XPATH, "//div[text()='Создать']")
    BUTTON_FILE = (By.XPATH, "//div[contains(text(),'Файл')]")
    DIRECT_FOLDER = (By.XPATH, "//div[@class='m-ui-select m-ui-input-wrapper-2']//select[@class='m-ui-select__select']")
    INPUT_FIELD_SELECT_FILE = (By.CSS_SELECTOR, "input[type='file']")
    """check picture"""
    CHECK_FILE_PICTURES = (By.CSS_SELECTOR, "img[alt='animal1']")
    """typography"""
    BUTTON_TYPOGRAPHY = (By.XPATH, "//p[text()='Опубликовать файл']")
    BUTTON_CONTINUE = (By.XPATH, "//p[contains(text(),'Продолжить')]")
    TEXTAREA_INPUT_TEXT = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    BUTTON_FINISH = (By.XPATH, "//p[contains(text(),'Завершить')]")
    SVG_CLOSE_ARTICLE = (By.XPATH, "(//*[local-name()='svg'][@class='article-modal__close article-modal__close--white'])[1]")




from selenium.webdriver.common.by import By


class AddViewContentWizardLocators:
    """create article"""
    INPUT_NAME_REQUEST = (By.CSS_SELECTOR, "input[placeholder='Введите запрос']")
    BUTTON_ADD = (By.XPATH, "//p[contains(text(),'Добавить')]")
    RADIOBUTTON_INCLUDED_CONTENT = (By.XPATH, "//span[contains(text(),'Содержимое контента')]")
    BUTTON_FINISH = (By.XPATH, "//p[contains(text(),'Завершить')]")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    INPUT_TEXTAREA_FIELD = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    GO_TO_CONTENT = (By.XPATH, "(//div[text()='Контент 1'])[2]")
    BUTTON_TYPOGRAPHY = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--small']")
    """tooltip"""
    SVG_TOOLTIP_REQUEST_FIELD = (By.XPATH, "//h4[contains(text(),'Закрепление контента в поисковой выдаче')]//*[local-name()='svg']")
    """check radio request"""
    RADIO_LINK_TO_CONTENT = (By.XPATH, "//span[contains(text(),'Ссылка на контент')]/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    CHECK_REQUEST = (By.CSS_SELECTOR, ".m-content-fix-wizard__content-wrapper")
    FOLDER_CONTENT = (By.XPATH, "//p[text()='Контент 1']")
    NAME_ARTICLE = (By.CSS_SELECTOR, ".m-content-fix-wizard__article-name")
    BUTTON_FINISH_1 = (By.XPATH, "//p[contains(text(),'Завершить')]")
    TEXT_LINK_TO_CONTENT = (By.CSS_SELECTOR, ".both-sides-alignment-card-line__bottom-text")
    """search"""
    SEARCH = (By.XPATH, "//div[text()='Поиск']")
    INPUT_SEARCH_NAME = (By.XPATH, "//input[@placeholder='Поиск контента']")
    CHECK_SEARCH_RESULT = (By.XPATH, "//p[@class='article-preview__title title-element']")
    TEXT_FIXING_BY_EXPERT = (By.XPATH, "//p[text()='Закреплено экспертом']")
    CHANGE_FIXING_CONTENT = (By.XPATH, "//span[contains(text(),'изменить')]")
    INPUT_FIELD_NAME_REQUEST = (By.XPATH, "(//input[@placeholder='Введите запрос'])[1]")


















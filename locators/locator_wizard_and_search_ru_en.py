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
    INPUT_SEARCH = (By.XPATH, "//input[@placeholder='Поиск по истории']")
    INPUT_SEARCH_NAME = (By.XPATH, "//input[@placeholder='Поиск контента']")
    CHECK_SEARCH_RESULT = (By.XPATH, "//p[@class='article-preview__title title-element']")
    TEXT_FIXING_BY_EXPERT = (By.XPATH, "//p[text()='Закреплено экспертом']")
    CHANGE_FIXING_CONTENT = (By.XPATH, "//span[contains(text(),'изменить')]")
    INPUT_FIELD_NAME_REQUEST = (By.XPATH, "(//input[@placeholder='Введите запрос'])[1]")
    SVG_CLOSE_WINDOWS_CHECK = (By.XPATH, "(//div[@role='presentation'])[2]")
    """create more requests"""
    HISTORY_BUTTON = (By.XPATH, "//span[text()='История']")
    CHANGE_ARTICLE = (By.XPATH, "//div[contains(text(),'изменить')]")
    BUTTON_BACK = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium wizard-wrapper__action']")
    TO_GET_NAME_ADDED_REQUEST = (By.CSS_SELECTOR, ".m-content-fix-wizard__content-wrapper")
    INPUT_TEXT_ALERT_NAME = (By.CSS_SELECTOR, "textarea[placeholder='Введите текст сообщения']")
    """check added request"""
    TO_GET_NAME_REQUEST = (By.CSS_SELECTOR, ".both-sides-alignment-card-line__text")
    BUTTON_ADD_REQUEST = (By.CSS_SELECTOR, "div[class='search-wrapper__form-field'] button[type='button']")
    LIST_ADDED_REQUEST = (By.CSS_SELECTOR, "span[class='both-sides-alignment-card-line__text']")
    BUTTON_CONTINUE_DRAFT = (By.XPATH, "//p[text()='Продолжить']")
    SVG_CLOSE_WINDOW_REQUEST = (By.CSS_SELECTOR, "div[class='popup__close']")
    SVG_CLOSE_WINDOW_ARTICLE = (By.CSS_SELECTOR, "div[class='article-editor__controls'] svg path")
    """check template"""
    TYPOGRAPHY_TEMPLATE = (By.XPATH, "//p[contains(text(),'Опубликовать')]")
    SUBMIT_TEMPLATES = (By.XPATH, "//button[@type='submit']")
    INPUT_REQUEST = (By.XPATH, "//input[@placeholder='Введите запрос']")
    SVG_CLOSE_WINDOW_ARTICLE_BY_TEMPLATE = (By.CSS_SELECTOR, "div[class='article-editor__controls'] svg")
    """check script"""
    BUTTON_TYPOGRAPHY_SCRIPT = (By.XPATH, "//p[contains(text(),'Опубликовать')]")
    SVG_CLOSE_WINDOW_EDIT_SCRIPT = (By.CSS_SELECTOR, "section[class='m-scenario-flow__editor-actions'] svg path")
    """check files"""
    FILES_NAME = (By.CSS_SELECTOR, ".m-content-fix-wizard__article-name")
    INPUT_NAME_FILE = (By.CSS_SELECTOR, "input[placeholder='Введите название']")
    CLOSE_WINDOW_FILES = (By.CSS_SELECTOR, ".article-editor-container-document__close-button-wrapper svg path")


class SearchRuEnLocators:
    SVG_CLOSE_WINDOW_ARTICLE_RU_EN = (By.XPATH, "(//*[local-name()='svg'][@class='article-modal__close'])[1]")
    BUTTON_TYPOGRAPHY = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--small']")
    HISTORY_BUTTON = (By.XPATH, "//span[text()='История']")
    """del article created"""
    MEATBALL_ARTICLE = (By.CSS_SELECTOR, ".popuper__wrapper")
    SVG_DEL = (By.XPATH, "//p[contains(text(),'Удалить')]")
    INPUT_ALERT_FOR_DEL = (By.CSS_SELECTOR, "textarea[placeholder='Введите текст сообщения']")
    BUTTON_EXECUTE = (By.CSS_SELECTOR, "button[class='m-button m-button--success m-button--medium wizard-wrapper__action']")
    LIST_ARTICLE_FOR_DEL = (By.XPATH, "//div[contains(text(),'text_alert')]")
    """check search"""
    SEARCH = (By.XPATH, "//div[text()='Поиск']")
    LIST_RESULT_SEARCH_RU_FIRST = (By.XPATH, "//span[contains(text(),'Соображения')]")
    LIST_RESULT_SEARCH_EN_SECOND = (By.XPATH, "//span[contains(text(),'высшего')]")
    LIST_RESULT_SEARCH_INVERSION = (By.XPATH, "//span[contains(text(),'Соображения высшего')]")
    LIST_RESULT_SEARCH_EN_FIRST_EN = (By.XPATH, "//span[contains(text(),'said')]")
    LIST_RESULT_SEARCH_EN_SECOND_EN = (By.XPATH, "//span[contains(text(),'dovish')]")
    LIST_RESULT_SEARCH_EN_INVERSION_EN = (By.XPATH, "//span[contains(text(),'more dovish')]")




























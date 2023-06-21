from selenium.webdriver.common.by import By


class AddFilterChangesLocators:

    SETTINGS = (By.XPATH, "//a[@data-tip='Настройки']")
    FILTERS_FOR_SEARCHING = (By.CSS_SELECTOR, ".m-ui-paper.m-big-card.m-tags-button.m-ui-paper--hoverable.m-ui-paper--shadowed")
    BUTTON_CREATE_GROUP_FILTER = (By.CSS_SELECTOR, ".empty-layout__upload")
    INPUT_NAME_GROUP = (By.CSS_SELECTOR, "input[class='m-ui-text-input__input']")
    BUTTON_GROUP_ADD = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium']")
    """add filters"""
    SEARCH_INPUT_BY_NAME_FILTER = (By.ID, "#tagManagerSearchInput")
    BUTTON_ADD_FILTER = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium single-editable-item__button']")
    INPUT_NAME_FILTER = (By.CSS_SELECTOR, "input[class='form-input-wrapper__input']")
    BUTTON_ADD_FILTER_ADD = (By.CSS_SELECTOR, "div[class='single-editable-item__actions single-editable-item__actions--edit'] button[type='button']")
    """del filters"""
    # SVG_DEL_LIST = (By.XPATH, "//button[@class='both-sides-alignment-card-line__action single-editable-item__action single-editable-item__action--remove icon-button']")
    SVG_DEL_LIST = (By.XPATH, "//span[1]//button[2]//*[local-name()='svg']")
    SVG_DEL_1 = (By.XPATH, "(//button[@class='both-sides-alignment-card-line__action single-editable-item__action single-editable-item__action--remove icon-button'])[1]")
    SVG_DEL_2 = (By.XPATH, "(//button[@class='both-sides-alignment-card-line__action single-editable-item__action single-editable-item__action--remove icon-button'])[2]")
    SVG_DEL_3 = (By.XPATH, "//button[@class='both-sides-alignment-card-line__action single-editable-item__action single-editable-item__action--remove icon-button']")
    SVG_DEL_LIST_CONFIRM = (By.CSS_SELECTOR, "button[class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    CHANGE_NAME_GROUP = (By.CSS_SELECTOR, ".m-ui-typography.m-ui-typography--bold.m-ui-typography--14x14.m-ui-button-text__label")
    BUTTON_DEL_GROUP = (By.CSS_SELECTOR, "button[class='m-button m-button--danger m-button--medium editable-items-list__action']")
    BUTTON_DEL_GROUP_CONFIRM = (By.CSS_SELECTOR, "button[class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    """close window"""
    SVF_CLOSE_WINDOW = (By.CSS_SELECTOR, "div[class='popup__close']")
    """mass change"""
    MEATBALL_MENU = (By.CSS_SELECTOR, "button[class='m-button-basic-wrapper m-button-basic m-button-basic--tertiary m-button-basic--medium m-button-basic-wrapper--tertiary m-button-basic-wrapper--medium m-button-basic-wrapper--square']")
    MASS_CHANGE = (By.XPATH, "//div[text()='Массовое изменение']")
    DROPDOWN_FILTERS_FOR_SEARCHING = (By.CSS_SELECTOR, "div[class='m-ui-select m-ui-input-wrapper-2'] select[class='m-ui-select__select']")
    """article by template"""
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    INPUT_NAME_REQUEST = (By.CSS_SELECTOR, "input[placeholder='Введите запрос']")
    BUTTON_ADD = (By.XPATH, "//p[contains(text(),'Добавить')]")
    RADIOBUTTON_INCLUDED_CONTENT = (By.XPATH, "//span[contains(text(),'Содержимое контента')]")
    BUTTON_FINISH = (By.XPATH, "//p[contains(text(),'Завершить')]")
    INPUT_TEXTAREA_FIELD = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    """script"""
    BUTTON_TYPOGRAPHY = (By.XPATH, "//p[contains(text(),'Опубликовать')]")
    DIRECT_FOLDER = (By.XPATH, "//div[@class='m-ui-paper m-ui-select__paper m-ui-paper--hoverable m-ui-paper--shadowed m-ui-paper--filled']//select[@class='m-ui-select__select']")
    BUTTON_FINISH_CONFIRM = (By.XPATH, "//p[contains(text(),'Продолжить')]")
    """check article"""
    DROPDOWN_ACTIONS = (By.XPATH, "(//select[@class='m-ui-select__select'])[4]")
    DROPDOWN_FILTERS = (By.XPATH, "(//select[@class='m-ui-select__select'])[5]")
    DROPDOWN_FILTERS_TEXT = (By.XPATH, "(//select[@class='m-ui-select__select'])[5]//option[1]")
    BUTTON_BACK = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium']")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "button[class='m-button m-button--success m-button--medium']")
    FILTER1 = (By.CSS_SELECTOR, "option[value='403']")
    FILTER2 = (By.CSS_SELECTOR, "option[value='402']")
    FILTER3 = (By.CSS_SELECTOR, "option[value='404']")










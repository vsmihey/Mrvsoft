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
    SVG_CLOSE_WINDOW = (By.CSS_SELECTOR, "div[class='popup__close']")
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
    # BUTTON_TYPOGRAPHY = (By.XPATH, "//p[contains(text(),'опубликовать')]")
    BUTTON_TYPOGRAPHY_SCRIPT = (By.XPATH, "//p[contains(text(),'Опубликовать')]")
    BUTTON_TYPOGRAPHY = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--small']")
    BUTTON_DELETE_DRAFT = (By.XPATH, "//p[text()='Удалить черновик']")
    # DIRECT_FOLDER = (By.XPATH, "//div[@class='m-ui-paper m-ui-select__paper m-ui-paper--hoverable m-ui-paper--shadowed m-ui-paper--filled']//select[@class='m-ui-select__select']")
    DIRECT_FOLDER = (By.CSS_SELECTOR, ".m-ui-select__select")
    BUTTON_FINISH_CONFIRM = (By.XPATH, "//p[contains(text(),'Продолжить')]")
    """check article"""
    DROPDOWN_ACTIONS = (By.XPATH, "(//select[@class='m-ui-select__select'])[2]")
    DROPDOWN_FILTERS = (By.XPATH, "(//select[@class='m-ui-select__select'])[3]")
    DROPDOWN_FILTERS_TEXT = (By.XPATH, "(//select[@class='m-ui-select__select'])[5]//option[1]")
    BUTTON_BACK = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium']")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "button[class='m-button m-button--success m-button--medium']")
    FILTER1 = (By.CSS_SELECTOR, "option[value='403']")
    FILTER2 = (By.CSS_SELECTOR, "option[value='402']")
    FILTER3 = (By.CSS_SELECTOR, "option[value='404']")
    """tooltips"""
    # TOOLTIP_ACTION = (By.XPATH, "(//style[@aria-hidden='true'])[4]")
    # TOOLTIP_ACTION = (By.XPATH, "//style[@aria-hidden='true']")
    # TOOLTIP_ACTION = (By.XPATH, "//h4[contains(text(),'Действие')]")
    TOOLTIP_ACTION = (By.XPATH, "//h4[contains(text(),'Действие')]//*[local-name()='svg']")
    TOOLTIP_FILTERS = (By.XPATH, "//h4[contains(text(),'Фильтры')]//*[local-name()='svg']")
    # TOOLTIP_ALL_LIST = (By.CSS_SELECTOR, "div[class='m-role-tooltip__toggler-icon m-role-tooltip__toggler-icon--simple m-title__icon']")
    # TOOLTIP_ALL_LIST = (By.XPATH, "//style[@aria-hidden='true']")
    """check click button"""
    ACTION_CHECK_VISIBLE = (By.XPATH, "//option[@value='add']")
    LIST_ADDED_FILTERS = (By.CSS_SELECTOR, ".massive-change__tags-item")
    # FIRST_OF_CONTENT_FOR_CHOOSE = (By.XPATH, "//div[@class='m-selection-card massive-change__content_item'][1]")
    GO_TO_CONTENT = (By.CSS_SELECTOR, "section[class='m-bread-crumbs'] p[class='m-ui-typography m-bread-crumbs__link__title-text']")
    # GO_TO_CONTENT = (By.XPATH, "(//div[text()='Контент 1'])[2]")
    INPUT_SEARCH_CONTENT_BY_NAME_FOR_ADD_FILTERS = (By.CSS_SELECTOR, "input[placeholder='Введите название контента']")
    CREATED_CONTENT_FOR_FILTERS = (By.CSS_SELECTOR, ".massive-change__check-all-wrapper")
    # FILTERS = (By.CSS_SELECTOR, ".action-button__icon")
    FILTERS = (By.XPATH, "//div[@class='m-ui-paper tag-item button-sort__item action-button m-ui-paper--hoverable m-ui-paper--shadowed']")
    ARTICLE_BY_FILTERS = (By.CSS_SELECTOR, ".m-ui-paper.article-preview__body.m-ui-paper--shadowed")
    """check article"""
    TEXT_ARTICLE = (By.XPATH, "//section[@class='article-modal__content article-modal--unique-class reader']//p[contains(text(),'Hello')]")
    VIDEO_ARTICLE = (By.XPATH, "//section[@class='article-modal__content article-modal--unique-class reader']//div[@class='m-video']")
    AUDIO_ARTICLE = (By.XPATH, "//section[@class='article-modal__content article-modal--unique-class reader']//div[@class='m-audio']")
    AUDIO_SCRIPT = (By.CSS_SELECTOR, "audio[title='undefined']")
    CHANGE_ARTICLE = (By.XPATH, "//div[text()='изменить']")
    BUTTON_TYPOGRAPHY_ARTICLE = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--small']")
    BUTTON_ARTICLE_BACK = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium wizard-wrapper__action']")
    TEXT_REQUEST_ARTICLE = (By.CSS_SELECTOR, "div[class='both-sides-alignment-card-line__left-side both-sides-alignment-card-line__left-side--bottom-text both-sides-alignment-card-line--black-label-text'] span[class='both-sides-alignment-card-line__text']")
    TEXT_REQUEST_SCRIPT = (By.XPATH, "(//span[@class='both-sides-alignment-card-line__text'])[2]")
    SVG_DELETE_FILTER_ADDED = (By.CSS_SELECTOR, ".both-sides-alignment-card-line__action.search-wrapper__tag-btn--delete.icon-button")
    DROPDOWN_FILTERS_FOR_CHANGE = (By.XPATH, "//div[@class='m-ui-select m-ui-input-wrapper-2']//div[@class='m-ui-paper m-ui-select__paper m-ui-paper--hoverable m-ui-paper--shadowed']//select[@class='m-ui-select__select']")
    # TO_GO_CONTENT = (By.CSS_SELECTOR, "section[class='m-bread-crumbs'] div[class='m-button-basic__text']")
    # TO_GO_CONTENT = (By.CSS_SELECTOR, "section[class='m-bread-crumbs'] div[title='Контент 1']")
    CLOSE_WINDOW = (By.CSS_SELECTOR, "//div[class='popup__close']")
    """check template"""
    FIELD_TEXT = (By.XPATH, "(//p[contains(text(),'some text')])[1]")
    FIELD_TEXT_2 = (By.XPATH, "//section[@class='m-article-editor-templated article-modal__content article-modal--unique-class']//pre[@class='m-article-editor-templated__field-value'][normalize-space()='one more some text']")
    FIELD_TEXT_777 = (By.XPATH, "(//pre[@class='m-article-editor-templated__field-value'][normalize-space()='777'])[1]")
    FIELD_TEXT_WEBSITE = (By.XPATH, "(//a[@href='https://www.something.com'])[1]")
    FIELD_TEXT_MAIL = (By.XPATH, "(//a[@class='m-article-editor-templated__field-value m-article-editor-templated__field-value--link'])[2]")
    FIELD_TEXT_NAME = (By.XPATH, "(//pre[@class='m-article-editor-templated__field-value'])[3]")


















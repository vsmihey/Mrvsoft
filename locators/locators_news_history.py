from selenium.webdriver.common.by import By


class LocatorsCheckNewsHistory:
    FRAME_PERSON_CLOSE = (By.XPATH, "//div[@role='presentation']")
    BUTTON_TYPOGRAPHY = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--small']")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    BUTTON_FINISH_1 = (By.XPATH, "//p[contains(text(),'Завершить')]")
    INPUT_TEXTAREA_FIELD = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    """change article"""
    ARTICLE_CHANGE = (By.XPATH, "//div[text()='изменить']")
    ARTICLE_NAME_CHANGE = (By.CSS_SELECTOR, "input[class='m-ui-text-input__input']")
    # ARTICLE_NAME_CHANGE = (By.CSS_SELECTOR, "input[placeholder='Введите название контента']")
    CHECKBOX_ADD_ALL_ROLE_FOR_ARTICLE = (By.CSS_SELECTOR, "div[class='access-wrapper__header-block'] svg")
    """add comment"""
    ADD_COMMENT = (By.CSS_SELECTOR, "textarea[placeholder='Введите текст комментария']")
    SEND_COMMENT = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium discuss-form__button-send']")
    SVG_CLOSE_ARTICLE = (By.XPATH, "//body/div[@class='article-modal__portal']/div[@class='ReactModal__Overlay ReactModal__Overlay--after-open article-modal__overlay']/div[@role='dialog']/article[@class='article-modal']/div[@class='article-modal__main']/div[@class='article-modal__breadcrumbs-wrapper']/div[2]//*[local-name()='svg']")
    """del article"""
    HISTORY_BUTTON = (By.XPATH, "//span[text()='История']")
    ADDED_COMMENT = (By.XPATH, "(//div[@data-title='Добавлен комментарий'])[1]")
    OPEN_ARTICLE_FOR_DEL = (By.CSS_SELECTOR, ".link-iconed__label-text")
    MEATBALL_MENU = (By.CSS_SELECTOR, ".popuper__wrapper")
    DEL_ARTICLE = (By.XPATH, "//p[contains(text(),'Удалить')]")
    BUTTON_CONFIRM_DEL = (By.CSS_SELECTOR, "button[class='m-button m-button--success m-button--medium wizard-wrapper__action']")
    """restored"""
    BUTTON_ALL_DELETED = (By.CSS_SELECTOR, "#all-trashed-folders-item")
    BUTTON_RESTORED = (By.CSS_SELECTOR, ".warning-block__action")
    SHOW_ALL_DELETED = (By.XPATH, "//span[contains(text(),'показать')]")
    HIDDEN_ALL_DELETED = (By.XPATH, "//span[contains(text(),'свернуть')]")
    SVG_CLOSE_RESTORED_ARTICLE = (By.XPATH, "(//*[local-name()='svg'][@class='article-modal__close'])[1]")
    """add new role"""
    PERSONS = (By.XPATH, "//a[@data-tip='Участники']")
    ADD_ROLE = (By.CSS_SELECTOR, "button[class='m-ui-button-text']")
    INPUT_NAME_ROLE = (By.CSS_SELECTOR, "input[placeholder='Введите название роли']")
    SWITCH_BOX_CONTROL_CONTENT = (By.XPATH, "//span[contains(text(),'Управление контентом')]/../label[@class='m-switch-box']")
    CHECKBOX_RESTORE_CONTENT = (By.XPATH, "//span[contains(text(),'Восстановление контента')]")
    BUTTON_CREATE_ROLE = (By.CSS_SELECTOR, "button[class='m-button m-button--success m-button--medium']")
    BUTTON_SETTING_ACCESS = (By.XPATH, "//p[contains(text(),'Настроить доступы')]")
    BUTTON_SAVE_CHANGES = (By.CSS_SELECTOR, "button[class='m-button m-button--success m-button--medium']")
    BUTTON_SAVE_CHANGES_CONFIRM = (By.CSS_SELECTOR, "button[class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    BUTTON_CHANGE_PASSWORD = (By.XPATH, "//p[contains(text(),'Сменить пароль')]")
    INPUT_NEW_PASSWORD = (By.CSS_SELECTOR, "#newPass")
    INPUT_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#repPass")
    TEST_PROJECT = (By.XPATH, "//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-space-list-item__title'][normalize-space()='selen']")  # name project
    SVG_POPUP_CLOSE_CREATED_PERSON = (By.XPATH, "//div[@class='popup__close']")
    PERSONS_AND_ROLES = (By.XPATH, "//span[text()='Участники']")
    BUTTON_HISTORY = (By.XPATH, "//a[@data-tip='История']")
    SVG_CLOSE_WINDOW_CREATED_PERSON = (By.CSS_SELECTOR, "div[role='presentation']")
    """check del article person1"""
    DEL_ARTICLE_2 = (By.XPATH, "(//header[@class='m-news-item__header'])[1]/../div[text()='deleted 2']")
    DEL_ARTICLE_2_WARNING = (By.XPATH, "//div[text()='Внимание! Этот контент удален']")
    RESTORED_ARTICLE_1 = (By.XPATH, "(//header[@class='m-news-item__header'])[4]/../div[text()='restored 1']")
    RESTORED_ARTICLE_1_ = (By.XPATH, "//div[normalize-space()='restored 1']")
    RESTORED_ARTICLE_1_CHECK_CHANGE = (By.XPATH, "//div[@class='article-modal__header-wrapper']//span[contains(text(),'changed name')]")
    RESTORED_ARTICLE_1_CHECK_ADDED_COMMENT = (By.XPATH, "//p[text()='1 комментарий']")
    SVG_CLOSE_CREATED_ARTICLE = (By.XPATH, "//body/div[@class='article-modal__portal']/div[@class='ReactModal__Overlay ReactModal__Overlay--after-open article-modal__overlay']/div[@role='dialog']/article[@class='article-modal']/div[@class='article-modal__main']/div[@class='article-modal__breadcrumbs-wrapper']/div[2]//*[local-name()='svg']")
    """check del article person2"""
    RESTORED_ARTICLE_1_CHECK_CHANGE_PERSON2 = (By.CSS_SELECTOR, "div[data-title='Восстановлен контент']")
    LABEL_ADMINISTRATOR_PERSON = (By.CSS_SELECTOR, "article[class='m-ui-avatar-default m-ui-avatar-default--small']")
    LABEL_ADMINISTRATOR_PERSON_OUT = (By.XPATH, "//p[contains(text(),'выйти')]")
    """del person"""
    LIST_ALL_PERSON = (By.CSS_SELECTOR, "div[class='m-user-card-info user-card__item m-user-card-info--without-checkbox']")
    CHANGE_DATA_PERSON = (By.XPATH, "//p[contains(text(),'Изменить данные')]")
    DEL_PERSON = (By.XPATH, "//p[contains(text(),'Удалить пользователя')]")
    DEL_PERSON_CONFIRM = (By.CSS_SELECTOR, "button[class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    """comment check"""
    COMMENT_CREATED = (By.CSS_SELECTOR, ".m-ui-paper.m-news-item__canvas.m-news-item__canvas--ticket.m-ui-paper--hoverable.m-ui-paper--shadowed")
    TEXT_COMMENT_CHECK = (By.XPATH, "//div[contains(text(),'Комментарий к контенту')]")
    FIRST_DELETED_CONTENT = (By.XPATH, "(//div[normalize-space()='deleted 2'])[1]")
    TEXT_CHECK_CANT_COMMENT = (By.XPATH, "//span[text()='Комментирование в этом контенте запрещено']")
    SVG_CLOSE_ARTICLE_ALERT = (By.CSS_SELECTOR, "div[class='article-editor__controls'] svg")
    GO_TO_CONTENT = (By.XPATH, "//section[@class='m-bread-crumbs']/..//p[@class='m-ui-typography m-bread-crumbs__link__title-text']")
    AVATAR_MENU = (By.CSS_SELECTOR, "article[class='m-ui-avatar-default m-ui-avatar-default--small m-ui-avatar-default--pic']")
    EXIT_PERSON = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium user-profile__footer__last_button'] p[class='m-ui-typography m-ui-typography--bold m-ui-typography--16x16 m-button__text']")










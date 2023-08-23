from selenium.webdriver.common.by import By


class FormPagesLocators:
    """CREATE PROJECT"""
    ADD = (By.XPATH, "//div[@class='m-titled-group__aside-content']")
    ADD_NAMES_PROJECT = (By.XPATH, "//input[@placeholder='Введите название проекта']")
    ADD_DESCRIPTION_PROJECT = (By.XPATH, "//input[@placeholder='Введите описание проекта']")
    # ADD_PROJECT_BUTTON = (By.XPATH, "//button[@type='button']")
    ADD_PROJECT_BUTTON = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium']")
    TYPE_AUTHOR = (By.CSS_SELECTOR, '.m-ui-select__select')  # type author
    TYPE_AUTHOR_CHANGE = (By.XPATH, "//option[@type='EMBEDDED']")  # new type auth
    LOGIN = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    INPUT_BUTTON = (By.XPATH, "//button[@type='submit']")
    HISTORY_BUTTON = (By.XPATH, "//a[@data-html='true']")
    """name project selen"""
    TEST_PROJECT = (By.XPATH,
                    "//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-space-list-item__title'][normalize-space()='selen']")  # name project
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
    CONTENT1 = (By.XPATH, "(//a[@class='folder-list-item__head'])[2]")
    # CONTENT1_NAME = (By.XPATH, "//p[contains(text(),'Контент 1')]")  # check name of content
    NAME_CONTENT = (By.XPATH, "//section[2]//article[1]//a[1]//section[1]")
    EDIT = (By.XPATH,
            "//body/div[@class='article-modal__portal']/div[@class='ReactModal__Overlay ReactModal__Overlay--after-open article-modal__overlay']/div[@role='dialog']/article[@class='article-modal']/div[@class='article-modal__main']/div[@class='scroller article-modal__scroller']/div[@class='scroller__wrap']/div[@class='scroller__body']/div[@class='scroller__content article-modal__scroller-content']/div[@class='article-modal__container']/header[@id='article-content-modal-header']/div[@class='article-modal__controls']/button[2]")
    # CREATE_BUTTON = (By.CSS_SELECTOR, ".m-button.m-button--default")
    CREATE_BUTTON = (By.XPATH, "//div[text()='Создать']")
    CREATE_BUTTON_1 = (By.XPATH, "//div[text()='Создать']")
    """article"""
    CREATE_ARTICLE = (By.XPATH, "(//div[@class='m-lms-action-tooltip'])[1]")
    NAME_OF_ARTICLE = (By.XPATH, "//input[@placeholder='Введите название контента']")
    FOLDER_SAVE_ARTICLE = (By.XPATH, "//select[@class='m-ui-select__select']")
    TYPOGRAPHY_ARTICLE = (By.XPATH, "//p[contains(text(),'опубликовать')]")
    SUBMIT_ARTICLE = (By.XPATH, "//button[@type='submit']")
    TEXTAREA_ARTICLE = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    CREATE_STEP_SCRIPT = (By.XPATH, "(//div[@class='m-lms-action-tooltip'])[3]")
    INPUT_INVISIBLE = (By.XPATH, "//input[@type='file']")
    CHECKBOX_INSERT_FILES = (By.XPATH, "//section[@class='m-file-view__content-block']")
    # CLOSE_CREATED_ARTICLE = (By.XPATH, "//header[@id='article-content-modal-header']//span[@class='link-iconed__label-text'][normalize-space()='selen']")
    CLOSE_CREATED_ARTICLE = (By.CSS_SELECTOR, ".article-modal__close")
    CLOSE_PAGE_LIST = (By.CSS_SELECTOR, "div[class='article-editor__controls'] svg")
    CLOSE_PAGE_SCRIPT = (By.XPATH, "(//*[name()='svg'][@class='m-scenario-flow__close'])[1]")
    CLOSE_CREATE_WINDOW = (By.XPATH, "//div[@class='m-popup__close']//*[name()='svg']")
    SEARCH_PROJECT = (By.CSS_SELECTOR, ".m-dashboard-top__search")
    SEARCH_PROJECT_TEST1 = (By.XPATH, "//div[text()='Поиск']")
    CHOOSE_PROJECT = (By.CSS_SELECTOR, ".m-ui-select__select")
    SEARCH_INPUT = (By.XPATH, "//input[@class='dashboard-search__input']")
    HISTORY_BUTTON_1 = (By.XPATH, "//a[@data-tip='История']")
    LEARNING_BUTTON = (By.XPATH, "//a[@data-tip='Обучение']")
    REPORT_BUTTON = (By.XPATH, "//a[@data-tip='Отчеты']")
    PEOPLE_BUTTON = (By.XPATH, "//a[@data-tip='Участники']")
    SETTINGS = (By.XPATH, "//a[@data-tip='Настройки']")
    ALERT_FILL_1 = (By.XPATH, "//textarea[text()='Введите текст сообщения]")
    """add new person"""
    PERSONS = (By.XPATH,
               "//article[@class='m-ui-paper m-big-card m-users-management-button m-ui-paper--hoverable m-ui-paper--shadowed']")
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
    """add new role"""
    ADD_NEW_ROLE_BUTTON = (By.XPATH, "//p[text()='добавить роль']")
    ADD_NEW_ROLE = (By.XPATH, "//span[contains(text(),'добавить роль')]")
    CREATE_ROLE = (By.XPATH, "//p[text()='Создать роль']")
    INPUT_NAME_ROLE = (By.XPATH, "//input[@placeholder='Введите название роли']")
    SWITCH_BOX = (By.XPATH, "//label[@class='m-switch-box']")  # 14 switch_boxes ('m-switch-box' mean: do not pushed
    SWITCH_BOX_CHECKED = (By.CSS_SELECTOR, ".m-switch-box.m-switch-box--checked")  # 14 switch_boxes  checked
    CHECK_NEW_ROLE = (By.XPATH, "//span[text()='Role 1']")  # check new  Role 1 in list new roles
    EDIT_NEW_ROLE = (By.XPATH, "//div[@class='item-role__icon-edit']")
    SAVE_CHANGES_ROLE = (By.XPATH, "//p[contains(text(),'Сохранить изменения')]")
    DEACTIVATE_ROLE = (By.XPATH, "//p[contains(text(),'Деактивировать роль')]")
    CHECK_WINDOWS_ALL_ROLES_TEXT = (By.XPATH, "//h1[contains(text(),'Все участники')]")
    CHECK_LAST_ELEMENT = (By.XPATH, "//span[contains(text(),'Запретить получение уведомлений об изменении конте')]")
    """create delete recovery folder"""
    TEXT_FOLDERS_CHECK = (By.XPATH, "//p[contains(text(),'Папки')]")  #
    TEXT_ALL_CONTENT_CHECK = (By.XPATH, "//h1[contains(text(),'Весь контент')]")
    FOLDERS_CHANGE = (By.XPATH, "//button[@data-element='folders']")
    TEXT_OPEN_FORM_CHECK = (By.XPATH, "//h3[contains(text(),'Управление структурой')]")
    NEW_FOLDER = (By.XPATH, "//p[contains(text(),'Новая папка')]")
    TEXT_NEW_FOLDER_CHECK = (By.XPATH, "//h3[contains(text(),'Новая папка')]")
    CREATE_FOLDER_BUTTON = (By.XPATH, "//p[contains(text(),'Создать папку')]")
    PARENT_FOLDERS_CHOICE = (By.XPATH, "//select[@name='parentId']")
    CREATE_NAME_NEW_FOLDER = (By.XPATH, "//input[@placeholder='Введите название папки']")
    RADIOBUTTON_SORT_BY_DATE = (By.XPATH, "//span[contains(text(),'По дате')]")
    RADIOBUTTON_NON_ACTIVE_CHECK = (By.XPATH, "(//div[@class='radio-wrapper__icon'])[1]")  # non activated
    RADIOBUTTON_SORT_BY_POPULAR = (By.XPATH, "//span[contains(text(),'По популярности')]")
    RADIOBUTTON_ACTIVE_CHECK = (
        By.XPATH, "//div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")  # activated
    RADIOBUTTON_SEARCH = (By.CSS_SELECTOR, ".radio-wrapper__icon")
    CHECK_RADIOBUTTON_DATE = (
        By.XPATH, "//input[@value='DATE']/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    CHECK_RADIOBUTTON_POPULARITY = (
        By.XPATH, "//input[@value='POPULARITY']/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    CHECK_CREATED_NEW_FOLDER = (By.XPATH, "//p[text()='{name_of_new_folder}']")
    SECOND_FOLDER_IN_LIST = (By.XPATH, "(//div[@class='tree-item-content'])[2]")
    FOLDER_FOR_DEL_BY_NAME = (By.XPATH, "//div[contains(text(),'Adam')]")
    DELETE_FOLDER_BUTTON = (By.XPATH, "//p[contains(text(),'Удалить папку')]")
    DELETE_FOLDER_CONFIRM_TEXT = (By.XPATH, "//h3[text()='Подтверждение действия']")
    CLOSE_WINDOW_STRUCTURE = (By.XPATH, "//div[@class='popup__close']")
    # CLOSE_WINDOW_STRUCTURE = (By.XPATH, "//*[name()='svg']/../../div[@class='popup__close']")
    SHOW_DELETED_FOLDERS = (By.XPATH, "//span[contains(text(),'показать')]")
    RECOVERY_FOLDER_BY_NAME = (By.XPATH, "//p[normalize-space()='Sherri153']")
    # RECOVERY_FOLDER_BUTTON = (By.XPATH, "//div[@class='action-button-group']")
    RECOVERY_FOLDER_BUTTON = (By.XPATH, "//div[text()='Восстановить папку']")
    CHECK_RADIO_POPULAR = (By.XPATH,
                           "//span[contains(text(),'По популярности')]/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    RECOVERY_FOLDER_BUTTON_CONFIRM = (By.XPATH, "//p[contains(text(),'восстановить папку')]")
    CHECK_TEXT_ALL_CONTENT_SORT_BY_POPULAR = (By.XPATH, "//span[contains(text(),'по популярности')]")
    CHECK_TEXT_ALL_CONTENT_SORT_BY_DATA = (By.XPATH, "//span[contains(text(),'по дате')]")
    CLOSE_EDIT_FOLDERS_WINDOW = (By.XPATH, "//div[@class='popup__close']")
    MOVE_FROM_DEL_FOLDER = (By.XPATH, "//select[@class='m-ui-select__select']")
    MOVE_FROM_DEL_FOLDER_TEXT = (By.XPATH, "//h4[contains(text(),'Папка для перемещения')]")
    FOLDER1 = (By.XPATH, "//div[contains(text(),'папка1')]")
    FOLDER2 = (By.XPATH, "//div[contains(text(),'папка2')]")
    # SAVE_CHANGES_FOLDER = (By.XPATH, "//p[contains(text(),'Сохранить изменения')]")
    SAVE_CHANGES_FOLDER = (By.XPATH,
                           "//button[@class='m-button m-button--default m-button--medium folder-editor__action folder-editor__save']")
    SORT_BY_ALL_CONTENT = (By.XPATH, "//button[@class='m-ui-button-text content-layout__sorted']")
    """favourites"""
    FAVOURITES = (By.XPATH, "//button[@data-element='bookmarks']")
    CHECK_TEXT_STRUCTURE = (By.XPATH, "//h3[contains(text(),'Управление структурой')]")
    CHECK_TEXT_FAVOURITES = (By.XPATH, "//p[contains(text(),'избранное')]")
    EDIT_NEW_FOLDER = (By.XPATH, "//div[text()='wwww']")  # change wwww {}
    TEXT_NOT_FOLDERS = (By.XPATH, "//span[text()='У вас нет избранных папок. Создайте папку.']")
    CREATE_NEW_FOLDER = (By.XPATH, "//p[contains(text(),'Новая папка')]")
    ARTICLE_FIRST1 = (By.XPATH, "(//section[@class='article-preview'])[1]")  # первая статья в списке статей всех
    # ADD_TO_FAVOURITES_ARTICLE = (By.XPATH, "//*[name()='svg']/../button[@class='article-modal__controls-item article-modal__controls-item--bookmark icon-button']")
    ADD_TO_FAVOURITES_ARTICLE = (By.XPATH, "//*[name()='svg']/../../div[contains(text(),'избранное')]")
    ADD_FAVOURITES_TO_FOLDER = (By.XPATH, "//select[@name='id']")
    ADD_BUTTON = (By.XPATH, "//p[text()='Добавить']")
    """number of articles"""
    ARTICLE_FIRST2 = (By.XPATH, "(//section[@class='article-preview'])[2]")  # folder 1
    ARTICLE_FIRST3 = (By.XPATH, "(//section[@class='article-preview'])[3]")  # folder 2
    ARTICLE_FIRST4 = (By.XPATH, "(//section[@class='article-preview'])[4]")  # folder 2
    ARTICLE_FIRST5 = (By.XPATH, "(//section[@class='article-preview'])[5]")  # folder 2
    ARTICLE_FIRST6 = (By.XPATH, "(//section[@class='article-preview'])[6]")  # folder 2
    ARTICLE_FIRST7 = (By.XPATH, "(//section[@class='article-preview'])[7]")  # folder 3
    ARTICLE_FIRST8 = (By.XPATH, "(//section[@class='article-preview'])[8]")  # folder 3
    ARTICLE_FIRST9 = (By.XPATH, "(//section[@class='article-preview'])[9]")  # folder 3
    CREATED_FOLDER1 = (By.CSS_SELECTOR,
                       "body > div:nth-child(2) > div:nth-child(2) > section:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > article:nth-child(4) > section:nth-child(2) > nav:nth-child(1) > div:nth-child(1)")
    # CREATED_FOLDER1 = (By.XPATH, "//a[@class='folder-list-item__head folder-list-item__head--active']//p[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 folder-list-item__title-text'][contains(text(),'папка1')]")
    CREATED_FOLDER2 = (By.CSS_SELECTOR,
                       "body > div:nth-child(2) > div:nth-child(2) > section:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > article:nth-child(4) > section:nth-child(2) > nav:nth-child(1) > div:nth-child(2)")
    CREATED_FOLDER3 = (By.CSS_SELECTOR,
                       "body > div:nth-child(2) > div:nth-child(2) > section:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > aside:nth-child(1) > article:nth-child(4) > section:nth-child(2) > nav:nth-child(1) > div:nth-child(3)")
    CHECK_TEXT_COUNT_OF_ARTICLES1 = (By.XPATH, "//span[contains(text(),'2 документа')]")
    CHECK_TEXT_COUNT_OF_ARTICLES2 = (By.XPATH, "//span[contains(text(),'4 документа')]")
    CHECK_TEXT_COUNT_OF_ARTICLES3 = (By.XPATH, "//span[contains(text(),'3 документа')]")
    # FOLDER1_FOR_DEL = (By.XPATH, "//li[@class='m-tree-item__wrapper']")
    FOLDER1_FOR_DEL = (By.XPATH, "//div[@class='m-tree-item__draggable-content']")
    """adding normal article"""
    CHECK_RADIOBUTTON_DATA_OF_TYPOGRAPHY = (
        By.XPATH,
        "//div[@class='radio-wrapper__icon radio-wrapper__icon--checked']/../span[text()='Опубликовать сейчас']")
    CHECK_RADIOBUTTON_DATA_OF_DELETE = (
        By.XPATH, "//div[@class='radio-wrapper__icon radio-wrapper__icon--checked']/../span[text()='Не удалять']")
    # CREATE_BUTTON = (By.XPATH, "//p[contains(text(),'Создать')]")
    TEXT_AREA_ARTICLE = (By.XPATH, "//div[@aria-label='false']")
    TEXT_BOLD_FORMAT = (By.XPATH, "//span[@class='cke_button_icon cke_button__bold_icon']")
    TEXT_ITALIC_FORMAT = (By.XPATH, "//span[@class='cke_button_icon cke_button__italic_icon']")
    TEXT_UNDERLINE_FORMAT = (By.XPATH, "//span[@class='cke_button_icon cke_button__underline_icon']")
    TEXT_COLOR_FORMAT = (By.XPATH, "//span[@class='cke_button_icon cke_button__textcolor_icon']")
    TEXT_OTHER_COLOR_FORMAT = (By.XPATH, "//a[contains(text(),'другие цвета')]")
    TEXT_COLOR_RED_FORMAT = (By.XPATH, "//span[normalize-space()='dfdf']")
    TEXT_BG_FORMAT = (By.XPATH, "//span[@class='cke_button_icon cke_button__bgcolor_icon']")
    UPLOAD_MEDIA_INPUT = (By.XPATH, "//input[@type='file']")
    UPLOAD_MEDIA1 = (By.XPATH, "//div[@class='m-file-view__name']")
    INPUT_SELECTED = (By.XPATH, "//p[contains(text(),'Вставить выбранные')]")
    CHECK_EMOJI = (By.XPATH, "//p[contains(text(),'😀')]")
    EMOJI = (By.XPATH, "//span[@class='cke_button_icon cke_button__emojipanel_icon']")
    CHECK_UPLOAD_MEDIA = (By.XPATH, "//img[@alt='animal1']")
    SETTINGS_TYPOGRAPHY = (By.XPATH, "//h3[contains(text(),'Настройки публикации контента')]")
    NAVIGATION = (By.XPATH, "//p[contains(text(),'навигация')]")
    SEARCH = (By.XPATH, "//p[contains(text(),'поиск')]")
    ACCESS = (By.XPATH, "//p[contains(text(),'доступ')]")
    VERSION = (By.XPATH, "//p[contains(text(),'версионность')]")
    SEARCH_INPUT_REQUEST = (By.XPATH, "//input[@placeholder='Введите запрос']")
    ADD_SEARCH_BUTTON = (By.XPATH, "//p[contains(text(),'Добавить')]")
    FINISH_BUTTON = (By.XPATH, "//p[contains(text(),'Завершить')]")
    CHECK_TEXT_FILLED_NEED = (By.XPATH, "//div[text()='Должно быть заполнено']")
    TEXT_AREA_ALERT = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    # CHECK_NEW_ARTICLE = (By.XPATH, "//h3[contains(text(),'Информация о контенте')]")
    CHECK_NEW_ARTICLE = (By.XPATH,
                         "//section[@class='article-modal__content article-modal--unique-class reader']//strong[contains(text(),'Hello')]")
    SELECTED_CHECKBOX = (By.XPATH, "//div[@class='button-action__icon-wrapper']")
    CHECK_RADIOBUTTON_TYPOGRAPHY_NOW = (
        By.XPATH,
        "//span[text()='Опубликовать сейчас']/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    CHECK_RADIOBUTTON_NO_DELETE = (
        By.XPATH, "//span[text()='Не удалять']/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    CHECK_TEXT_ROLE = (By.XPATH, "//span[contains(text(),'роль')]")
    FRAME_PERSON_CLOSE = (By.XPATH, "//div[@role='presentation']")
    """FIXING ARTICLE"""
    # SEARCH_HEAD_PAGE = (By.XPATH, "//p[contains(text(),'Поиск')]")
    SEARCH_HEAD_PAGE = (By.XPATH, "//div[contains(text(),'Поиск')]")
    BUTTON_FIXING_CONTENT = (By.XPATH, "//p[contains(text(),'Закрепить контент')]")
    INPUT_REQUEST = (By.XPATH, "//input[@placeholder='Введите запрос']")
    CHECK_ADD_FIXING_CONTENT = (By.XPATH, "//h3[contains(text(),'Добавление закрепленного контента')]")
    BUTTON_FIXING_CONTENT1 = (By.XPATH, "//p[text()='закрепить контент']")
    BUTTON_FIXING_CONTENT_CHANGE = (
        By.CSS_SELECTOR,
        "button[class='m-button m-button--default m-button--medium m-content-fix-manager__empty-button']")
    ARTICLE_1_IN_LIST = (By.XPATH, "//span[normalize-space()='tesss']")
    BUTTON_SUBMIT = (By.XPATH, "//p[contains(text(),'Продолжить')]")
    CHECK_LINK_OF_CONTENT_RADIO = (
        By.XPATH,
        "//span[text()='Ссылка на контент']/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    SEARCH_TEST_ARTICLE = (By.XPATH, "//input[@placeholder='Введите название контента']")
    TEST_ARTICLE_NAME = (By.XPATH, "//article[@class='m-content-fix-wizard__content_item']")
    CHECK_NAME_CONTENT = (By.XPATH,
                          "//section[@class='m-content-fix-wizard__link']//p[@class='m-content-fix-wizard__meta'][contains(text(),'Контент 1')]")
    CHECK_NAME_ARTICLE = (By.XPATH, "//section[@class='m-content-fix-wizard__link']/./p[text()='Alan']")
    INCLUDED_CONTENT_RADIO = (By.XPATH, "//span[contains(text(),'Содержимое контента')]")
    INCLUDED_CONTENT = (By.XPATH, "//section[@class='reader']")
    FIXING = (By.XPATH, "//button[@type='submit']")
    LIST_OF_ARTICLES = (By.XPATH, "//p[@class='article-preview__title title-element']")
    POPUP_CLOSE_SVG = (By.XPATH, "//div[@class='popup__close']")
    SEARCH_OF_CONTENTS = (By.XPATH, "//input[@placeholder='Поиск контента']")
    FIND_OF_CONTENT = (By.XPATH, "//span[@class='m-ui-button-hint__highlight']")
    CHECK_TEXT_HELLO = (By.XPATH, "//p[text()='Hello']")
    """ADD ARTICLE BY TEMPLATES"""
    # CREATE_BUTTON_ON_HEAD_PAGE = (By.XPATH, "//p[contains(text(),'Создать')]")
    CREATE_BUTTON_ON_HEAD_PAGE = (By.XPATH, "//div[contains(text(),'Создать')]")
    CREATE_TEMPLATES = (By.XPATH, "//div[contains(text(),'Шаблон')]")
    CREATE_TEMPLATES_NEW = (By.XPATH, "//div[contains(text(),'Новый')]")
    ADD_FIELD_BUTTON = (By.XPATH, "//button[contains(text(),'Добавить поле')]")
    LIST_OF_FIELDS_1 = (
        By.XPATH, "//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[1]")
    LIST_OF_FIELDS_2 = (
        By.XPATH, "//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[2]")
    INPUT_NAME_OF_FIELD = (By.XPATH, "//input[@placeholder='Введите название поля']")
    SAVE_TEMPLATES = (By.XPATH,
                      "//button[@class='m-button m-button--success m-button--medium']//p[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x16 m-button__text'][contains(text(),'сохранить')]")
    CHECKBOX_VALUE = (By.XPATH, "//p[contains(text(),'Запретить изменение значения по умолчанию')]")
    SAVE_TEMPLATES_CHANGE = (By.XPATH, "//p[text()='Сохранить']")
    INPUT_VALUE = (By.XPATH, "//input[@placeholder='Не указано']")
    INPUT_NAME_OF_TEMPLATES = (By.XPATH, "//input[@placeholder='Введите название шаблона']")
    # SAVE_CREATED_TEMPLATES = (By.XPATH, "//p[contains(text(),'сохранить')]")
    SAVE_CREATED_TEMPLATES = (By.XPATH, "//p[contains(text(),'Сохранить')]")
    SUBMIT_TEMPLATES = (By.XPATH, "//button[@type='submit']")
    SUBMIT_TEMPLATES_FINISH_EDIT = (By.XPATH, "//p[contains(text(),'Завершить')]")
    BACK_TEMPLATES_FINISH_EDIT = (By.XPATH, "//p[contains(text(),'Назад')]")
    CHANGE_TEMPLATES_BUTTON_CONFIRM = (By.XPATH, "//p[contains(text(),'Изменить шаблон')]")
    CHANGE_TEMPLATES_BUTTON = (By.XPATH, "//span[text()='изменить']")
    # CHANGE_TEMPLATES_BUTTON = (By.XPATH, "(//span[text()='изменить'])[3]")
    CHANGE_TEMPLATES = (By.XPATH, "//button[@class='m-ui-button-text']")
    CHANGE_TEMPLATES_BUTTON_1 = (By.XPATH,
                                 "//button[@class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']//p[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x16 m-button__text'][contains(text(),'Изменить шаблон')]")
    check_text_name = (By.XPATH,
                       "//div[@class='m-ui-text-input m-ui-input-wrapper-2']//div[@class='m-ui-typography m-ui-typography--14x14 m-ui-input-wrapper-2__label']")
    check_name_input = (By.XPATH, "//input[@placeholder='Введите название контента']")
    EDIT_TEMPLATES = (By.XPATH, "//div[@aria-label='false']")
    EDIT_TEMPLATES_1 = (By.XPATH, "//div[@class='cke_inner cke_reset']")
    EDIT_TEMPLATES_2 = (By.XPATH, "//span[contains(text(),'Введите текст')]")
    EDIT_TEMPLATES_3 = (By.XPATH, "//span[contains(text(),'Введите число')]")
    EDIT_TEMPLATES_4 = (By.XPATH, "//span[contains(text(),'Введите ссылку')]")
    EDIT_TEMPLATES_5 = (By.XPATH, "//span[contains(text(),'Введите Email-адрес')]")
    EDIT_TEMPLATES_ERRORS_CHECK = (
        By.XPATH, "//pre[@class='m-article-editor-templated__field-value form-input-wrapper__input']")
    FOLDER_SAVE = (By.XPATH,
                   "//div[@class='m-ui-paper m-ui-select__paper m-ui-paper--hoverable m-ui-paper--shadowed m-ui-paper--filled']//select[@class='m-ui-select__select']")
    # TYPOGRAPHY_TEMPLATE = (By.XPATH, "//p[contains(text(),'опубликовать')]")
    TYPOGRAPHY_TEMPLATE = (By.XPATH, "//p[contains(text(),'Опубликовать')]")
    # UTILITY_TEMPLATE = (By.XPATH, "//h3[contains(text(),'Полезность')]")
    UTILITY_TEMPLATE = (By.XPATH, "//div[text()='полезен']")
    NO_UTILITY_TEMPLATE = (By.XPATH, "//div[text()='не полезен']")
    FIELD_OF_CONTENT_RADIO = (By.XPATH, "//span[contains(text(),'Содержимое контента')]")
    SELECT_FIELD_FOR_FIXING = (By.XPATH,
                               "//div[@class='m-content-fix-wizard__select-template m-ui-select m-ui-input-wrapper-2']//select[@class='m-ui-select__select']")
    """CHECK_FIXING_TEMPLATES"""
    # EDIT_ARTICLE = (By.XPATH, "//*[name()='svg']/../button[@class='article-modal__controls-item icon-button']")
    EDIT_ARTICLE = (By.XPATH, "//div[text()='изменить']")
    ANSWER = (By.XPATH, "//input[@placeholder='Введите название ответа']")
    ADD_ANSWER = (By.XPATH, "//p[contains(text(),'добавить')]")
    SAVE_BUTTON = (By.XPATH, "//button[@class='m-button m-button--success m-button--medium']")
    EDIT_ARTICLE_1 = (By.XPATH, "//div[text()='Редактировать']")
    TEXT_FIELD_FOR_CLEAR = (By.XPATH, "//div[@class='cke_inner cke_reset']")
    NUMBER_FIELD_FOR_CLEAR = (By.XPATH, "//pre[normalize-space()='777']")
    LINK_FIELD_FOR_CLEAR = (By.XPATH, "//pre[normalize-space()='https://www.something.com']")
    CHECK_NAME_OF_CONTENT = (By.XPATH, "//p[@class='article-preview__title title-element']")
    CHANGE_OF_CONTENT = (By.XPATH, "//span[contains(text(),'изменить')]")
    EDIT_OF_CONTENT = (
        By.XPATH, "//body/div[5]/div[1]/div[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
    CHECK_RADIO_LINK_CONTENT = (By.XPATH,
                                "//span[contains(text(),'Ссылка на контент')]/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    SAVE_CHANGE_CONTENT = (By.XPATH, "//p[contains(text(),'Сохранить изменения')]")
    POPUP_CLOSE_SVG_1 = (By.XPATH, "//body/div[3]/div[1]/div[1]/div[1]")
    CHECK_LINK_OF_CONTENT = (By.XPATH, "//span[text()='Ссылка на контент']")
    BUTTON_BACK = (
        By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium wizard-wrapper__action']")
    CLOSE_LINK_OF_CONTENT = (By.XPATH, "//span[@class='both-sides-alignment-card-line__container']")
    # TEXT_FIELD_ONE_MORE = (By.XPATH, "//pre[text()='one more some text']")
    TEXT_FIELD_ONE_MORE = (By.XPATH,
                           "//pre[text()='one more some text']/../../div[@class='form-input-wrapper__field form-input-wrapper__field-arrow']")
    LINK_FIELD_FOR_CLEAR_1 = (By.XPATH, "//pre[text()='https://www.something.com']")
    EMAIL_FIELD_FOR_CLEAR_1 = (By.XPATH, "//pre[text()='gdyer@example.org']")
    FIELD_FOR_DEL = (By.XPATH, "//div[@class='m-template-field__type'][contains(text(),'Любой контент')]")
    FIELD_FOR_DEL_TEXT = (By.XPATH, "//div[@class='m-template-field__type'][contains(text(),'Текст')]")
    ALL_FIELDS_DEL = (By.XPATH, "//div[@class='rst__node']")
    FIELD_LINK_CHECK = (By.XPATH, "//section[text()='https://www.something.com']")
    FIELD_TEXT_CHECK = (By.XPATH, "//section[text()='Текст']")
    FIELD_ANY_CONTENT_CHECK = (By.XPATH, "//section[text()='Любой контент']")
    CHOSE_ANSWER = (By.XPATH, "//span[text()='Выберите ответ']")
    ANSWER_1 = (By.XPATH, "//pre[text()='answer 1']")
    DELETE_ANSWER = (By.XPATH, "//*[name()='path' and contains(@fill,'#C23E42')]")
    FILD_TEXT = (By.XPATH, "//div[@class='m-template-field__type'][contains(text(),'Текст')]")
    CHECKBOX_OFF = (By.XPATH, "//p[text()='Запретить изменение значения по умолчанию']")
    LIST_FOR_DEL = (By.XPATH, "//div[@class='m-template-field__type']")
    LIST_FOR_DEL_1 = (By.XPATH, "//h3[@class='m-template-field__name title-element']")
    LIST_FOR_DEL_2 = (By.XPATH, "//*[name()='svg']/../../div[@class='m-template-field__type']")
    # ANSWER_FOR_DEL = (By.XPATH, "//div[text()='Варианты ответа, несколько']")
    LINK_FOR_DEL = (By.XPATH, "//div[@class='m-template-field__type'][contains(text(),'Ссылка')]")
    EMAIL_FOR_DEL = (By.XPATH, "//div[@class='m-template-field__type'][contains(text(),'Email-адрес')]")
    ANSWER_FOR_DEL_1 = (By.XPATH, "//div[@class='m-template-field__type'][contains(text(),'Варианты ответа')]")
    NUMBER_FOR_DEL = (By.XPATH, "//div[@class='m-template-field__type'][contains(text(),'Число')]")
    TEXT_FOR_DEL = (By.XPATH, "//div[@class='m-template-field__type'][contains(text(),'Текст')]")
    CHECK_FIXING_CONTENT_TEXT = (
        By.XPATH, "//span[text()='В этой папке пока нет контента, но Вы можете это изменить.']")
    CONFIRM_DEL = (By.XPATH, "//p[contains(text(),'удалить')]")
    CONFIRM_DEL_ONE_MORE = (By.XPATH, "//p[contains(text(),'Удалить поле')]")
    # CONFIRM_SAVE = (By.XPATH, "//p[text()='сохранить']")
    CONFIRM_SAVE = (By.XPATH, "//button[@class='m-button m-button--default m-button--small']")
    FOR_CLICK = (By.XPATH, "//span[text()='Выберите ответ']")
    ddd = (By.XPATH, "//input[@type='file']")
    UPLOAD_MEDIA = (By.XPATH, "//span[@class='cke_button_icon cke_button__uploadminerva_icon']")
    D = (By.XPATH, "//form[@enctype='multipart/form-data']")
    ADD_TEST_PROJECT = (By.XPATH, "//p[text()='добавить проект']")
    TEXT_CHECK_LINK = (By.XPATH, "//a[text()='https://openai.com/']")
    TARGET_FOLDER_CONTENT = (By.XPATH, "//div[text()='расположение контента']")
    FINISH_BUTTON_SCRIPT = (By.XPATH, "//p[contains(text(),'Завершить')]")
    EDIT_TEMPLATE_1 = (By.XPATH, "//div[@class='m-popup__root']//a[1]")
    NEW_TEMPLATE = (By.XPATH, "//div[@class='m-lms-action-tooltip m-modal-templates__template-card']")
    SECOND_FOLDER_IN_LIST_FOR_DEL = (By.XPATH, "(//li[@class='m-tree-item m-tree-item__wrapper'])[2]")
    MODAL_WINDOW_SCROLLER = (
        By.XPATH,
        "//div[@class='scroller m-modal-templates__scroller']//div[@class='scroller__thumb scroller__thumb--Y']")


class StepByScriptLocators:
    ADD_SCRIPT = (By.XPATH, "//div[text()='Пошаговый сценарий']")
    ADD_STEP_BUTTON = (By.XPATH, "//p[text()='добавить шаг']")
    """block scripts"""
    CHECK_TEXT_BEGIN = (By.XPATH, "//p[text()='Начало']")
    CHECK_TEXT_STEP1 = (By.XPATH, "//p[text()='Шаг 1']")
    CHECK_TEXT_STEP2 = (By.XPATH, "//p[text()='Шаг 2']")
    TEXT_END_SCRIPT = (By.XPATH, "//p[contains(text(),'Завершение')]")
    PLUS_BUTTON_ADD_STEP = (By.XPATH, "//button[@data-tip='добавить шаг']")
    BUTTON_SCRIPT_TYPOGRAPHY = (By.XPATH, "//p[text()='Опубликовать']")
    # INPUT_NAME_PLACEHOLDER = (By.XPATH, "//input[@placeholder='Введите название контента']")
    INPUT_NAME_PLACEHOLDER = (By.XPATH, "//input[@class='m-ui-text-input__input']")
    TARGET_FOLDER_NAME = (By.XPATH, "//div[text()='расположение контента']")
    INPUT_NAME_STEP = (By.XPATH,
                       "//div[@class='scenario-question__name m-ui-text-input m-ui-input-wrapper-2']//input[@placeholder='Введите название']")
    INPUT_TARGET_FOLDER = (By.XPATH,
                           "//div[@class='m-ui-paper m-ui-select__paper m-ui-paper--hoverable m-ui-paper--shadowed m-ui-paper--filled']//select[@class='m-ui-select__select']")
    EDIT_STEP_TEXT_CHECK = (By.XPATH, "//p[text()='Редактор шага']")
    EDIT_NAME_TEXT_CHECK = (By.XPATH, "//div[text()='название']")
    EDIT_CONTENT_TEXT_CHECK = (By.XPATH, "//section[text()='контент шага']")
    ADD_TRANSITION = (By.XPATH, "//p[contains(text(),'добавить переход')]")
    DELETE_STEP = (By.XPATH, "//p[contains(text(),'удалить шаг')]")
    NEW_TRANSITION = (By.XPATH, "//div[3]/div[3]")
    # INPUT_NAME_FIELDS = (By.XPATH, "//input[@class='m-ui-text-input__input']")
    GO_TO_STEP_ARROW = (By.XPATH, "//button[@class='scenario-answer-button scenario-answer-button__go']")
    DELETE_STEP_ICON = (By.XPATH, "//div[3]/div[2]/button[2]")
    # NAME_TRANSACTION_FIELD = (By.XPATH, "//div[@class='scenario-answer__fields-wrapper']//input[@class='m-ui-text-input__input']")
    NAME_TRANSACTION_FIELD = (
        By.XPATH,
        "//div[3]/div[3]//div[@class='scenario-answer__fields-wrapper']//input[@class='m-ui-text-input__input']")
    TEXT_TRANSACTION_TO_STEP = (By.XPATH, "//div[3]/div[1]/div[2]/div/label/div[1]")
    LIST_DROPDOWN = (By.XPATH, "//div[3]/div[3]//select/option/..")
    TEXT_CHECK_SCRIPT_FINISH = (By.XPATH, "//div[3]/div[3]//select/option/../option[text()='Сценарий завершён']")
    TEXT_CHECK_ADD_NEW_STEP = (By.XPATH, "//p[text()='Для начала добавьте первый шаг']")
    TEXT_CHECK_NAME_NEW_STEP = (By.XPATH,
                                "//div[@class='scenario-question__name m-ui-text-input m-ui-input-wrapper-2']//input[@placeholder='Введите название']")
    TEXT_CHECK_INPUT_CONTENT_OF_STEP = (By.XPATH, "//div[@aria-label='false']")
    TEXT_AREA = (By.XPATH, "//article/label/div/div/textarea")
    """minimap"""
    # MINIMAP = (By.CLASS_NAME, "react-flow__minimap m-scenario-flow__minimap")
    MINIMAP = (By.CSS_SELECTOR, "svg[class='react-flow__minimap m-scenario-flow__minimap']")
    PLUS = (By.XPATH, "//section[@class='m-scenario-flow__main']//button[1]")
    MINUS = (By.XPATH, "//section[@class='m-scenario-flow__main']//button[2]")
    FANCYBOX = (By.XPATH, "//section[@class='m-scenario-flow__main']//button[3]")
    """alerts text"""
    CHECK_ALERT_TEXT_CONTENT_STEP = (By.XPATH, "//div[text()='Не должно быть пустым']/../div[2]")
    CHECK_ALERT_TEXT_NAME_STEP = (
        By.XPATH, "//div[@class='m-ui-typography m-ui-typography--14x14'][contains(text(),'Не должно быть пустым')]")
    # INPUT_NAME_FIRST_STEP = (By.XPATH, "//input[@name='articleName']")
    INPUT_NAME_FIRST_STEP = (By.XPATH, "(//input[@placeholder='Введите название'])[2]")
    BUTTON_PREVIEW = (By.CSS_SELECTOR, "button[data-tip='предпросмотр']")
    """drop down step"""
    CHECK_TEXT_CHOSE_TRANSACTION = (By.XPATH, "//div[text()='Необходимо выбрать шаг']")
    LIST_DROPDOWN_FIRST_STEP = (By.XPATH, "//select[@name='id']")
    CHECK_TEXT_PREVIEW = (By.XPATH, "//h3[text()='Предпросмотр']")
    CLOSE_WINDOW_PREVIEW = (By.CSS_SELECTOR, "div[class='popup__close']")
    # TEXT_BOLD_IN_TEXTAREA_EDITOR = (By.CSS_SELECTOR, "//span[@class='cke_button_icon cke_button__bold_icon']")
    TEXT_BOLD_IN_TEXTAREA_EDITOR = (By.XPATH, "//span[text()='полужирный']")
    # LIST_DROPDOWN_FIRST_STEP1 = (By.CSS_SELECTOR, "option[label='Выберите шаг']")
    # TEXT_CHECK_TYPOGRAPHY_WINDOW = (By.XPATH, "//h3[contains(text(),'Настройки публикации контента')]")
    TEXT_CHECK_TYPOGRAPHY_WINDOW = (By.XPATH, "//h3[text()='Настройки публикации контента']")
    TEXT_CHECK_LINK = (By.XPATH, "//a[text()='https://openai.com/']")
    """fixing script"""
    INPUT_FIXING_FIELD_REQUEST = (By.XPATH, "//input[@placeholder='Введите запрос']")
    ADD_BUTTON_FIXING_FIELD_REQUEST = (By.XPATH, "//p[contains(text(),'Добавить')]")
    WINDOW_FIXING_REQUEST_TEXT_CHECK = (By.XPATH, "//h3[contains(text(),'Закрепление контента')]")
    DISPLAY_CHECK_TEXT = (By.XPATH, "//p[contains(text(),'отображение')]")
    CHECK_RADIO_LINK_CONTENT1 = (By.XPATH,
                                 "//span[contains(text(),'Ссылка на контент')]/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    CHECK_RADIO_DISABLED = (By.XPATH,
                            "//span[contains(text(),'Содержимое контента')]/../../label[@class='radio-wrapper m-content-fix-wizard__radio-button radio-wrapper--disabled']")
    CHECK_TEXT_CONTENT_SCRIPT = (By.XPATH, "//p[text()='Контент 1']")
    # CHECK_TEXT_CONTENT_SCRIPT = (By.XPATH, "(//p[text()='Контент 1'])[2]")
    FINISH_BUTTON_SCRIPT = (By.XPATH, "//p[contains(text(),'Завершить')]")
    TEXT_CHECK_WINDOW_TYPOGRAPHY_CONTENT = (By.XPATH, "//h3[contains(text(),'Настройки публикации контента')]")
    TEXT_CHECK_SEARCH = (By.XPATH, "//p[contains(text(),'поиск')]")
    BUTTON_CONTINUE = (By.XPATH, "//p[contains(text(),'Продолжить')]")
    TEXT_AREA_ALERT_INPUT = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    CONTENT_TRANSFER = (
        By.XPATH,
        "//section[@class='m-bread-crumbs']//div[@class='m-button-basic__text'][contains(text(),'Контент 1')]")
    CONTENT_SEARCH = (By.XPATH, "//div[text()='Поиск']")
    CHECK_TEXT_FIXING_EXPERT = (By.XPATH, "//p[text()='Закреплено экспертом']")
    TO_GET_NAME = (By.XPATH, "//input[@class='m-ui-text-input__input']")
    CLOSE_SCRIPT = (By.XPATH, "//div[@class='popup__close']")
    TEXTAREA_INVISIBLE = (By.XPATH, "//textarea[@style='visibility: hidden; display: none;']")
    TEXTAREA_VISIBLE = (By.XPATH, "//textarea[@style='visibility:visible;']")


class CopyPastePageLocators:
    START = (By.XPATH, "//b[contains(text(),'Пикабу́ (Pikabu)')]")
    FINISH = (By.XPATH, "//a[normalize-space()='iOS']")
    CHECK_LINK_CORRECT = (By.XPATH, "//a[@href='https://openai.com/']")
    CHECK_TEXT_CORRECT = (By.XPATH, "//div/div/div/p/text()[1]")
    # FOLDER_DROPDOWN = (By.XPATH, "(//select[@class='m-ui-select__select'])[3]")
    FOLDER_DROPDOWN = (By.XPATH, "//select[@class='m-ui-select__select']")


class CreateDraftLocators:
    ALERT_CREATE_DRAFT = (By.XPATH, "//article[text()='Контент сохраняется автоматически']")
    FIELD_DRAFT = (By.XPATH, "//p[contains(text(),'Черновики')]")
    CLOSE_PAGE_ARTICLE = (By.XPATH, "//div[@class='article-editor__controls']//*[local-name()='svg']")
    # CLOSE_CREATE_EDIT_CONTENT_WINDOW = (By.XPATH, "//div[@class='m-popup__close']//*[name()='svg']")
    CREATE_ARTICLE = (By.XPATH, "//div[contains(text(),'Статья')]")
    CREATE_BUTTON = (By.XPATH, "//div[text()='Создать']")
    CHECK_TEXT_FIELD = (By.XPATH, "//div[@class='m-popup__root']//section[3]//span[text()='Контент 1']")
    CHECK_TEXT_NAMES_ARTICLE = (By.XPATH, "//div[@class='m-popup__root']//section[3]//span[text()='Mihey Andrey']")
    DEL_DRAFT_SVG = (By.XPATH, "(//div[@class='m-draft-card__top-right-element'])[3]")
    TIME_OF_CREATE_ARTICLE = (By.XPATH, "(//div[@class='m-drafts-list__date'])[3]")
    TIME_OF_CREATE_ARTICLE1 = (By.XPATH, "(//div[@class='m-drafts-list__date'])[2]")
    EDIT_TEMPLATE_1 = (By.XPATH, "//div[@class='m-popup__root']//a[1]")
    NAME_OF_STEP_SCRIPT = (By.XPATH, "//input[@placeholder='Введите название контента']")
    CREATE_FILE = (By.XPATH, "//div[text()='Файл']")
    INPUT_NAME_FILE = (By.XPATH, "//input[@placeholder='Введите название']")
    DIRECT_FOLDER = (By.XPATH, "//div[@class='m-ui-select m-ui-input-wrapper-2']//select[@class='m-ui-select__select']")
    """check text"""
    TIME_FIRST_SECTION = (By.XPATH, "(//div[@class='m-drafts-list__date'])[1]")
    TIME_FIRST_SECTION_TEXT = (By.XPATH, "(//div[@class='m-drafts-list__date-text'])[1]")
    TIME_ALL_SECTION = (By.CSS_SELECTOR, ".m-drafts-list__date")
    TIME_TEXT_ALL = (By.XPATH, "//div[@class='m-drafts-list__date-text']")
    CONTENT_TEXT_ALL = (By.XPATH, "//span[text()='Контент 1']")
    SECTION2_CHECK = (By.XPATH, "(//div[@class='m-draft-card__top-side'])[2]")
    SECTION3 = (By.XPATH, "(//div[@class='m-draft-card__top-side'])[3]")
    # CHECK_TEXT_OPEN_EDIT_DRAFT = (By.XPATH, "//span[text()='изменить']")
    CHECK_TEXT_OPEN_EDIT_DRAFT = (By.XPATH, "//button[@class='m-ui-button-text']")
    CHECK_TEXT_OPEN_EDIT_DRAFT_NAME_CONTENT = (By.XPATH, "//div[text()='название контента']")
    CHANGE_TEMPLATE = (By.XPATH, "//p[text()='Изменить шаблон']")
    CHANGE_TEMPLATE_NAME_TEXT_CHECK = (By.XPATH, "//div[text()='Название шаблона']")


class FilesPagesLocators:
    NEW_TEMPLATE = (By.XPATH, "//div[@class='m-lms-action-tooltip m-modal-templates__template-card']")
    TEST_PROJECT = (By.XPATH,
                    "//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-space-list-item__title'][normalize-space()='selen']")  # name project
    UPLOAD_MEDIA = (By.XPATH, "//span[@class='cke_button_icon cke_button__uploadminerva_icon']")
    INPUT_INVISIBLE = (By.XPATH, "//input[@type='file']")
    FILES_MANAGER = (By.XPATH, "//span[text()='менеджер файлов']")
    FOOTER_HIDDEN = (By.XPATH, "//footer[@class='popup__footer file-manager__foot file-manager--hidden']")
    FORM_INVISIBLE_INPUT = (By.XPATH, "//form[@enctype='multipart/form-data']")
    CLOSE_DOWNLOAD_WINDOW = (By.XPATH, "//div[@class='popup__close']")
    CHECK_TEXT_WARNING = (By.XPATH, "//div[@class='warning-block__text']")
    SHOW_BUTTON = (By.XPATH, "//p[contains(text(),'показать')]")
    CHECK_TEXT_BIG_FILE_ERR = (By.XPATH, "//div[@class='error-list-item__body']")
    """check tooltip"""
    CHECK_TOOLTIP_TEXT = (By.XPATH, "(//div[text()='Тип и размер файлов:'])[1]")
    # BUTTON_DOWNLOAD = (By.XPATH, "//div[@class='empty-layout__upload']//button[@type='button']")
    BUTTON_DOWNLOAD = (By.XPATH, "//div[@class='empty-layout__upload']")
    """check for templates"""
    DROPDOWN = (By.XPATH, "//span[@class='cke_button_icon cke_button__inserttemplated_icon']")
    EDIT_TEMPLATES_FIRST = (By.XPATH, "(//a[@class='m-modal-templates__template-card'])[1]")
    DROP_DOWN_FILES = (By.XPATH, "//a[@title='Файлы']")
    FIELD_INPUT = (By.XPATH, "//div[@class='form-input-wrapper__field form-input-wrapper__field-arrow']")
    # FRAME = (By.XPATH, "//div[@title='Параметры']")
    # FRAME_PERSON_CLOSE = (By.XPATH, "//div[@role='presentation']")
    FRAME = (By.XPATH, "//iframe[@class='cke_panel_frame']")
    """check for script"""
    ADD_STEP = (By.XPATH, "//p[contains(text(),'добавить шаг')]")
    CREATE_SCRIPT = (By.XPATH, "//div[contains(text(),'Пошаговый сценарий')]")
    TEXT_AREA = (By.XPATH, "//div[@aria-label='false']")


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
    SVG_CLOSE_ARTICLE = (
        By.XPATH, "(//*[local-name()='svg'][@class='article-modal__close article-modal__close--white'])[1]")
    """check audio"""
    CHECK_AUDIO = (By.XPATH,
                   "//div[@class='article-modal__container article-modal__container--type-file']//audio[@class='article-modal__content-file']")
    """replacement"""
    CHECK_TEXT_TYPE_FILE = (By.XPATH, "//div[text()='Тип файла:']")
    CHECK_TEXT_TYPE_DOWNLOAD_FILE_VIDEO = (By.XPATH, "//div[text()='Видео']")
    SVG_INFORMATION_FOR_TOOLTIP = (
        By.XPATH, "//div[@class='article-editor-container-document__sidebar-file-type']//*[local-name()='svg']")
    CHANGE_FILE = (By.XPATH, "//div[contains(text(),'изменить')]")
    CHECK_TEXT_REPLACEMENT_ALERT = (By.XPATH, "//p[text()='При замене необходимо использовать тот же тип файла']")
    CHECK_TOOLTIP_TEXT_AUDIO = (By.XPATH, "//b[text()='Аудио']")
    LIST_TOOLTIP = (By.XPATH, "//div[@class='scroller__content m-role-tooltip__scroller-content']")
    CHECK_TOOLTIP_FORMAT_SUPPORT_AUDIO = (By.XPATH,
                                          "//p[text()='- файлы форматов: mp3, aac, ac3, aiff, au, dts, flac, m4a, m4p, m4r, mp2, ogg, opus, ra, tta, voc, vox, wav, wma.']")
    CHECK_TOOLTIP_FORMAT_SUPPORT_VIDEO = (By.XPATH,
                                          "//p[text()='- файлы форматов: mp4, avi, flv, mov, 3gp, m4v, asf, m2ts, m4v, mkv, mts, swf, vob, wmv, webm.']")
    CHECK_TOOLTIP_FORMAT_SUPPORT_PICT = (By.XPATH, "//p[text()='- файлы форматов: jpg, jpeg, png, gif.']")
    CHECK_TOOLTIP_FORMAT_SUPPORT_OTHER = (By.XPATH, "//p[text()='- все остальные файлы.']")
    CHECK_TEXT_INCORRECT_FORMAT_REPLACEMENT = (By.XPATH, "//div[text()='Неверный формат файла для замены']")
    SVG_TEXT_INCORRECT_FORMAT_CLOSE = (By.XPATH, "//div[@class='m-popup__close']")
    # AVI_FILE_CREATED = (By.XPATH, "//p[text()='avi.avi']")
    AVI_FILE_CREATED = (By.XPATH, "(//h3[text()='avi.avi'])[1]")
    # MP3_FILE_CREATED = (By.XPATH, "//p[text()='mp3.mp3']")
    MP3_FILE_CREATED = (By.XPATH, "(//h3[text()='mp3.mp3'])[1]")
    # JPEG_FILE_CREATED = (By.XPATH, "//p[text()='media.jpg']")
    JPEG_FILE_CREATED = (By.XPATH, "(//h3[text()='media.jpg'])[1]")
    DELETE_DRAFT = (By.XPATH, "//p[contains(text(),'Удалить черновик')]")
    TEXT_FILE_DOWNLOADS = (By.XPATH, "//h2[contains(text(),'Файл загружается')]")
    INPUT_NAME_FILE = (By.CSS_SELECTOR, "input[placeholder='Введите название']")


class UnformatFilePageLocators:
    """check add unformat files"""
    CHECK_TEXT_ONLY_DOWNLOAD_ALERT = (By.XPATH, "//h2[contains(text(),'Файл будет доступен только для скачивания')]")
    CHECK_TEXT_NOT_PREVIEW = (By.XPATH, "//h3[contains(text(),'Для этого формата не доступен предпросмотр')]")
    BUTTON_DOWNLOAD_FILE = (By.XPATH, "//p[contains(text(),'Скачать файл')]")
    BUTTON_TYPOGRAPHY = (By.XPATH, "//p[text()='Опубликовать файл']")
    # BUTTON_TYPOGRAPHY = (By.XPATH, "article-editor-container-document__publish-button-wrapper")
    BUTTON_CONTINUE = (By.XPATH, "//p[contains(text(),'Продолжить')]")
    TEXTAREA_INPUT_TEXT_ALERT = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    BUTTON_FINISH = (By.XPATH, "//p[contains(text(),'Завершить')]")
    """check after typography"""
    TEXT_CHECK_AFTER_TYPOGRAPHY = (
        By.XPATH,
        "(//h2[@class='article-modal__view-unavailable-title'][contains(text(),'Просмотр файла недоступен')])[1]")
    BUTTON_DOWNLOAD_CHECK_AFTER_TYPOGRAPHY = (By.XPATH, "(//p[text()='Скачать файл'])[1]")
    """input file"""
    CREATE_BUTTON = (By.XPATH, "//div[text()='Создать']")
    BUTTON_FILE = (By.XPATH, "//div[contains(text(),'Файл')]")
    DIRECT_FOLDER = (By.XPATH, "(//select[@class='m-ui-select__select'])[3]")
    INPUT_FIELD_SELECT_FILE = (By.CSS_SELECTOR, "input[type='file']")
    SVG_CLOSE_DOWNLOADED_FILE = (
        By.XPATH, "(//*[local-name()='svg'][@class='article-modal__close article-modal__close--white'])[1]")
    """check text convert files"""
    CHECK_TEXT_NOT_PREVIEW_1 = (By.XPATH, "//h2[text()='Просмотр файла недоступен']")
    TEXT_FILE_DOWNLOADS = (By.XPATH, "//h2[contains(text(),'Файл загружается')]")


class CreateTopicDatabaseLocators:
    LEARNING_BUTTON = (By.XPATH, "//a[@data-html='true']")
    TAB_ALL_COURSES = (By.XPATH, "//p[contains(text(),'все курсы')]")
    DATABASE_OF_QUESTIONS = (By.XPATH, "//p[contains(text(),'База вопросов')]")
    """check text open form"""
    TEXT_DATABASE_OF_QUESTIONS = (By.XPATH, "//p[contains(text(),'База вопросов')]")
    TEXT_NOT_QUESTIONS_NOW = (
        By.XPATH, "//p[text()='В этом проекте пока нет вопросов. Создайте структуру тем для его размещения']")
    BUTTON_ADD_TOPIC = (By.XPATH, "//p[contains(text(),'Создать темы')]")
    """check text open form new topic"""
    TEXT_NEW_QUESTION_TOPIC_WINDOW = (By.XPATH, "//h3[contains(text(),'Новая тема')]")
    TEXT_NAME = (By.XPATH, "//div[text()= 'название']")
    TEXT_PLACEHOLDER_INPUT_NAME_TOPIC = (By.XPATH, "//input[@placeholder='Введите название темы']")
    TEXT_PARENT_TOPIC = (By.XPATH, "//div[text()='родительская тема']")
    TEXT_DROPDOWN_DEFAULT = (By.XPATH, "//select[@class='m-ui-select__select']//option[text()='Нет']")  # ПРОВЕРИТЬ
    BUTTON_CREATE_TOPIC = (By.XPATH,
                           "//footer[@class='m-popup__footer lms-edit-theme-popup__footer']//p[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x16 m-button__text'][contains(text(),'Создать тему')]")  # ПРОВЕРИТЬ
    """input name topic and check len"""
    INPUT_NAME_TOPIC = (By.XPATH, "//input[@placeholder='Введите название темы']")
    """check text structure"""
    TEXT_RULE_STRUCTURE = (By.XPATH, "//h3[contains(text(),'Управление структурой')]")
    TEXT_CREATED_TOPIC_NAME = (By.XPATH, "//div[@class='tree-item-content__name']")
    """function create new topic"""
    BUTTON_NEW_TOPIC = (By.XPATH, "//p[contains(text(),'Новая тема')]")
    """del created topics"""
    LIST_CREATED_TOPICS = (By.CSS_SELECTOR, "li[class='m-tree-item m-tree-item__wrapper']")
    BUTTON_DELETE_TOPIC = (
        By.XPATH, "//button[@class='m-button m-button--danger m-button--medium lms-edit-theme-popup__delete']")
    BUTTON_CONFIRM_DELETE_TOPIC = (By.XPATH,
                                   "//button[@class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    SVG_CLOSE_DELETED_WINDOW = (By.XPATH, "//div[@class='m-popup__close']")
    """question add"""
    BUTTON_QUESTION_ADD = (By.XPATH, "//p[contains(text(),'Добавить')]")
    BUTTON_CHANGE_QUESTION = (By.XPATH, "//p[contains(text(),'Изменить тему')]")
    TEXT_DATABASE_OF_QUESTION = (By.XPATH, "//p[text()='В этом проекте пока нет вопросов. Вы можете это исправить']")
    TEXT_DATABASE_OF_QUESTION_HEAD = (By.XPATH, "//h3[contains(text(),'База вопросов')]")
    """new question form"""
    TEXT_NEW_QUESTION = (By.XPATH, "//h3[contains(text(),'Новый вопрос')]")
    TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION = (By.XPATH, "//textarea[@placeholder='Введите текст вопроса']")
    DROPDOWN_TIPE_OF_QUESTION = (By.XPATH,
                                 "//div[@class='lms-question-editor__field m-ui-select m-ui-input-wrapper-2']//select[@class='m-ui-select__select']")
    DROPDOWN_TOPIC = (By.XPATH,
                      "//div[@class='lms-question-editor__input m-ui-select m-ui-input-wrapper-2']//select[@class='m-ui-select__select']")
    ANSWER_AND_CHECKBOX = (By.XPATH, "//textarea[@placeholder='Введите текст ответа']")
    ANSWER_CHECKBOX = (By.XPATH, "//label[@class='radio-wrapper lms-answer-field__radio radio-wrapper--no-label']")
    BUTTON_CREATE_QUESTION = (By.XPATH, "//p[contains(text(),'Создать вопрос')]")
    """check created window question"""
    SVG_SLIDERS = (By.XPATH, "//div[@class='themes-side-popup-filter__icon-container']")
    TEXT_MODAL_WINDOW_TOPICS = (By.XPATH, "//h3[contains(text(),'Темы')]")
    CHANGE_TOPICS_WINDOW = (By.XPATH, "//span[contains(text(),'изменить')]")
    TEXT_CREATED_NEW_QUESTION = (By.XPATH, "//span[@class='lms-question-bar__text']")
    SVG_DEL_QUESTION = (
        By.XPATH, "(//*[local-name()='svg'][@class='lms-question-bar__icon lms-question-bar__icon-trash'])")
    SVG_DEL_QUESTION_CONFIRM = (By.XPATH, "//p[contains(text(),'Удалить вопрос')]")
    """check all created topics"""
    TEXT_FIRST_TOPIC = (By.XPATH, "(//div[@class='tree-item-content__name'])[1]")
    DROPDOWN_PARENTS_TOPIC = (By.XPATH, "//select[@class='m-ui-select__select']")
    BUTTON_SAVE_TOPIC = (By.XPATH, "//p[contains(text(),'Сохранить тему')]")
    BUTTON_DELETE_TOPIC_CONFIRM = (By.XPATH, "//p[contains(text(),'Удалить тему')]")
    BUTTON_CREATE_TOPIC_CONFIRM = (By.XPATH, "//p[contains(text(),'Создать тему')]")
    """check same name and last in list"""""
    GO_TO_TOPICS_LIST = (
        By.XPATH,
        "//div[@class='ReactModal__Content ReactModal__Content--after-open lms-theme-structure m-popup__window']")
    NAME_1 = (By.XPATH, "(//div[contains(text(),'THE SAME NAME')])[1]")
    NAME_2 = (By.XPATH, "(//div[contains(text(),'THE SAME NAME')])[2]")
    NAME_2_LAST_IN_LIST = (By.XPATH, "(//li[@class='m-tree-item m-tree-item__wrapper'])[23]")
    THE_SAME_NAME_LIST = (By.XPATH, "//div[text()='THE SAME NAME']")
    SVG_CLOSE_TOPICS_WINDOW = (By.XPATH, "//div[@class='button-action__icon-wrapper']")
    """edit question"""
    TEXT_SETTINGS_QUESTION = (By.XPATH, "//h4[contains(text(),'Настройка вопроса')]")
    TEXT_QUESTIONS_TEXT = (By.XPATH, "//div[text()='текст вопроса']")
    TEXT_QUESTIONS_TYPE = (By.XPATH, "//div[text()='тип вопроса']")
    TEXT_QUESTIONS_OPTIONS = (By.XPATH, "//h4[contains(text(),'Варианты ответа')]")
    TEXT_TOPIC = (By.XPATH, "//h4[contains(text(),'Тема')]")
    TEXT_CHOOSE_TOPIC = (By.XPATH, "//div[text()='выберите тему']")
    ANSWER_CHECKBOX_1 = (By.XPATH, "//label[@class='checkbox-wrapper checkbox-wrapper--no-label']")
    ANSWER_CHECKBOX_1_1 = (By.CSS_SELECTOR, "label[class='checkbox-wrapper checkbox-wrapper--no-label']")
    """edit"""
    SVG_EDIT_QUESTION = (By.XPATH, "//div[@class='lms-question-bar__wrapper']//a[@class='m-link']")
    BUTTON_EDIT_QUESTION_SAVE = (By.XPATH, "//p[contains(text(),'Сохранить изменения')]")
    """new question"""
    BUTTON_NEW_QUESTION = (By.XPATH, "//p[contains(text(),'Новый вопрос')]")
    NEW_ANSWER_PLACEHOLDER = (By.XPATH, "(//textarea[@placeholder='Введите текст ответа'])[2]")
    ANSWER_CHECKBOX_ADD = (By.XPATH, "(//label[@class='checkbox-wrapper checkbox-wrapper--no-label'])[2]")
    TEXT_CHECK_RESULT_CREATED_QUESTIONS_FIRST = (By.XPATH, "(//div[@class='lms-question-bar__wrapper'])[1]")
    TEXT_CHECK_RESULT_CREATED_QUESTIONS_SECOND = (By.XPATH, "(//div[@class='lms-question-bar__wrapper'])[2]")
    LIST_QUESTIONS = (By.XPATH, "//span[contains(text(),'Вопрос')]")
    """add and edit question in article"""
    CREATE_BUTTON = (By.XPATH, "//div[text()='Создать']")
    CREATE_ARTICLE = (By.XPATH, "//div[contains(text(),'Статья')]")
    UPLOAD_MEDIA = (By.XPATH, "//span[@class='cke_button_icon cke_button__uploadminerva_icon']")
    INPUT_INVISIBLE = (By.XPATH, "//input[@type='file']")
    # NAME_OF_ARTICLE = (By.XPATH, "//input[@placeholder='Введите название контента']")
    # NAME_OF_ARTICLE = (By.CSS_SELECTOR, ".m-ui-paper.m-ui-text-input__main.m-ui-paper--shadowed.m-ui-paper--filled")
    NAME_OF_ARTICLE = (By.XPATH, "//input[@placeholder='Введите название']")
    # FOLDER_SAVE_ARTICLE = (By.CSS_SELECTOR, "select[class='m-ui-select__select']")
    # FOLDER_SAVE_ARTICLE = (By.XPATH, "(//select[@class='m-ui-select__select'])[3]")
    FOLDER_SAVE_ARTICLE = (By.CSS_SELECTOR,
                           "div[class='m-ui-paper m-ui-select__paper m-ui-paper--hoverable m-ui-paper--shadowed m-ui-paper--filled'] select[class='m-ui-select__select']")
    TEXT_AREA_ARTICLE = (By.XPATH, "//div[@aria-label='false']")
    CHECKBOX_INSERT_FILES = (By.XPATH, "//section[@class='m-file-view__content-block']")
    INPUT_SELECTED = (By.XPATH, "//p[contains(text(),'Вставить выбранные')]")
    BUTTON_TYPOGRAPHY = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--small']")
    # TEXT_TYPOGRAPHY_CONTENT = (By.XPATH, "//h3[contains(text(),'Настройки публикации контента')]")
    TEXT_TYPOGRAPHY_CONTENT = (By.XPATH, "//h3[text()='Настройки публикации контента']")
    BUTTON_JUST_NOTIFY = (By.XPATH, "(//span[contains(text(),'только оповестить')])[1]")
    TEXT_CONFIRM_READ = (By.XPATH, "//span[contains(text(),'подтвердить прочтение')]")
    TEXT_TAB_TEST = (By.XPATH, "//p[text()='тест']")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    TEXTAREA_ALERT = (By.CSS_SELECTOR, "textarea[placeholder='Введите текст сообщения']")
    """check checked"""
    CHECKED_CHECK = (By.XPATH,
                     "//section[@class='m-file-view m-file-view--selected m-file-view--image-cover m-file-view--selectable file-manager__item']")
    # LIST_TABS = (By.CSS_SELECTOR, "li[class='tabs__list-item']")
    LIST_TABS = (By.CSS_SELECTOR, "ul[class='tabs']")
    """add question"""
    BUTTON_ADD_QUESTION = (By.XPATH, "//p[contains(text(),'Добавить вопрос')]")
    """check text an checkboxes"""
    TEXT_CHOOSE_QUESTION_FOR_TEST = (By.CSS_SELECTOR, "header[class='m-popup__header']")
    LIST_CHECKBOXES = (By.CSS_SELECTOR, "label[class='m-switch-box lms-question-bar__switch']")
    ON_CHECKBOX_ALL_QUESTIONS = (By.XPATH, "//label[@class='m-switch-box lms-questions-lib__header-switch']")
    """move questions"""
    QUESTIONS_FIRST_POSITION_CHECK = (By.XPATH, "(//p[normalize-space()='Edit question'])[1]")
    INPUT_TEXTAREA_ALERT = (By.CSS_SELECTOR, "textarea[class='m-ui-textarea__textarea']")
    BUTTON_CONTINUE = (By.XPATH, "//p[text()='Продолжить']")
    QUESTIONS_FIRST_POSITION = (By.XPATH, "(//div[@class='article-wizard-tests-question-row__left-side'])[1]")
    SVG_CLOSE_CREATED_ARTICLE = (By.CSS_SELECTOR, "svg[class='article-modal__close']")
    QUESTIONS_FIRST_POSITION_CSS = (By.CSS_SELECTOR,
                                    "body > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
    QUESTIONS_SECOND_POSITION = (By.XPATH, "(//div[@class='article-wizard-tests-question-row__left-side'])[2]")
    QUESTIONS_SECOND_POSITION_CSS = (By.CSS_SELECTOR,
                                     "body > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
    # TAB_ACTIVE = (By.XPATH, "//div[@class='tab-item tab-item--active']")
    TAB_ACTIVE = (By.XPATH, "(//div[@class='tab-item tab-item--active'])[2]")
    BUTTON_FINISH = (By.XPATH, "//button[@type='submit']")
    EDIT_ARTICLE = (By.XPATH, "//div[text()='изменить']")
    BUTTON_GO_BACK = (
        By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium wizard-wrapper__action']")
    TEXT_GET_TESTED = (By.XPATH, "//span[contains(text(),'пройти тестирование')]")
    RADIOBUTTON_SMALL_CORRECT_CONTENT = (By.XPATH, "//span[contains(text(),'Небольшие корректировки контента')]")
    RADIOBUTTON_BIG_CORRECT_CONTENT = (By.XPATH, "//span[contains(text(),'Значительные изменения контента')]")
    """check position"""
    LIST_QUESTIONS_POSITION = (By.CSS_SELECTOR, "div[class='article-wizard-tests-question-row__left-side']")
    """del question from test"""
    SVG_DEL_FIRST_QUESTION = (
        By.XPATH, "(//*[local-name()='svg'][@class='article-wizard-tests-question-row__control-icon'])[3]")
    SVG_DEL_SECOND_QUESTION = (
        By.XPATH, "(//*[local-name()='svg'][@class='article-wizard-tests-question-row__control-icon'])[6]")
    LIST_SVG_DEL_QUESTION = (By.XPATH,
                             "//div[@class='article-wizard-tests-question-row__control-button article-wizard-tests-question-row__control-button--remove']")
    CONFIRM_BUTTON_DELETE = (By.XPATH,
                             "//button[@class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    """check by template"""
    CREATE_TEMPLATES = (By.XPATH, "//div[contains(text(),'Шаблон')]")
    NEW_TEMPLATE = (By.XPATH, "//div[@class='m-lms-action-tooltip m-modal-templates__template-card']")
    ADD_FIELD_BUTTON = (By.XPATH, "//button[contains(text(),'Добавить поле')]")
    LIST_OF_FIELDS_1 = (
        By.XPATH, "//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[1]")
    INPUT_NAME_OF_FIELD = (By.XPATH, "//input[@placeholder='Введите название поля']")
    SAVE_TEMPLATES = (By.XPATH,
                      "//button[@class='m-button m-button--success m-button--medium']//p[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x16 m-button__text'][contains(text(),'сохранить')]")
    INPUT_NAME_OF_TEMPLATES = (By.XPATH, "//input[@placeholder='Введите название шаблона']")
    SAVE_TEMPLATES_CHANGE = (By.XPATH, "//p[text()='Сохранить']")
    FINISH_BUTTON_SCRIPT = (By.XPATH, "//p[contains(text(),'Завершить')]")
    DROPDOWN = (By.XPATH, "//span[@class='cke_button_icon cke_button__inserttemplated_icon']")
    FRAME = (By.XPATH, "//iframe[@class='cke_panel_frame']")
    DROP_DOWN_FILES = (By.XPATH, "//a[@title='Файлы']")
    FOLDER_SAVE = (By.XPATH,
                   "//div[@class='m-ui-paper m-ui-select__paper m-ui-paper--hoverable m-ui-paper--shadowed m-ui-paper--filled']//select[@class='m-ui-select__select']")
    INPUT_NAME_CONTENT = (By.XPATH, "//input[@placeholder='Введите название контента']")
    TABS_CHECK_TEXT_ALL = (By.XPATH, "//div[@class='wizard-wrapper__head']//ul[@class='tabs']")
    """conversation status check"""
    CONVERSATION_CHECK = (By.XPATH, "//div[@class='m-file-view__status']")
    """script"""
    CREATE_SCRIPT = (By.XPATH, "//div[contains(text(),'Пошаговый сценарий')]")
    ADD_STEP = (By.XPATH, "//p[contains(text(),'добавить шаг')]")
    TEXT_AREA = (By.XPATH, "//div[@aria-label='false']")
    # BUTTON_TYPOGRAPHY_SCRIPT = (By.XPATH, "//section[@class='m-scenario-flow__editor-actions']//button[@type='button']")
    # BUTTON_TYPOGRAPHY_SCRIPT = (By.CSS_SELECTOR, "section[class='m-scenario-flow__editor-actions'] button[type='button']")
    DIRECT_FOLDER_NAME = (By.XPATH, "(//select[@class='m-ui-select__select'])[3]")
    BUTTON_TYPOGRAPHY_SCRIPT = (By.XPATH, "//p[contains(text(),'Опубликовать')]")
    NAME_OF_STEP_SCRIPT = (By.XPATH, "//input[@placeholder='Введите название контента']")
    # DIRECT_FOLDER = (By.XPATH, "//div[@class='m-ui-select m-ui-input-wrapper-2']//select[@class='m-ui-select__select']")
    DIRECT_FOLDER = (By.XPATH, "//select[@class='m-ui-select__select']")
    INPUT_NAME_STEP = (By.XPATH, "//input[@name='articleName']")
    DROPDOWN_STEP = (By.CSS_SELECTOR, "select[name='id']")
    BUTTON_DELETE_DRAFT = (By.XPATH, "//p[text()='Удалить черновик']")
    INPUT_NAME_REQUEST = (By.CSS_SELECTOR, "input[placeholder='Введите запрос']")
    BUTTON_ADD = (By.XPATH, "//p[contains(text(),'Добавить')]")
    RADIOBUTTON_INCLUDED_CONTENT = (By.XPATH, "//span[contains(text(),'Содержимое контента')]")
    BUTTON_FINISH_1 = (By.XPATH, "//p[contains(text(),'Завершить')]")
    INPUT_TEXTAREA_FIELD = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    GO_TO_CONTENT = (By.XPATH, "(//div[text()='Контент 1'])[2]")
    BUTTON_FINISH_CONFIRM = (By.XPATH, "//p[contains(text(),'Продолжить')]")


class LocatorsCheckNewsHistory:
    FRAME_PERSON_CLOSE = (By.XPATH, "//div[@role='presentation']")
    BUTTON_TYPOGRAPHY = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--small']")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    BUTTON_FINISH_1 = (By.XPATH, "//p[contains(text(),'Завершить')]")
    INPUT_TEXTAREA_FIELD = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    """change article"""
    ARTICLE_CHANGE = (By.XPATH, "//div[text()='изменить']")
    ARTICLE_NAME_CHANGE = (By.CSS_SELECTOR, "input[placeholder='Введите название контента']")
    CHECKBOX_ADD_ALL_ROLE_FOR_ARTICLE = (By.CSS_SELECTOR, "div[class='access-wrapper__header-block'] svg")
    """add comment"""
    ADD_COMMENT = (By.CSS_SELECTOR, "textarea[placeholder='Введите текст комментария']")
    SEND_COMMENT = (
        By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium discuss-form__button-send']")
    SVG_CLOSE_ARTICLE = (By.XPATH,
                         "//body/div[@class='article-modal__portal']/div[@class='ReactModal__Overlay ReactModal__Overlay--after-open article-modal__overlay']/div[@role='dialog']/article[@class='article-modal']/div[@class='article-modal__main']/div[@class='article-modal__breadcrumbs-wrapper']/div[2]//*[local-name()='svg']")
    """del article"""
    HISTORY_BUTTON = (By.XPATH, "//span[text()='История']")
    ADDED_COMMENT = (By.XPATH, "(//div[@data-title='Добавлен комментарий'])[1]")
    OPEN_ARTICLE_FOR_DEL = (By.CSS_SELECTOR, ".link-iconed__label-text")
    MEATBALL_MENU = (By.CSS_SELECTOR, ".popuper__wrapper")
    DEL_ARTICLE = (By.XPATH, "//p[contains(text(),'Удалить')]")
    BUTTON_CONFIRM_DEL = (
        By.CSS_SELECTOR, "button[class='m-button m-button--success m-button--medium wizard-wrapper__action']")
    """restored"""
    BUTTON_ALL_DELETED = (By.CSS_SELECTOR, "#all-trashed-folders-item")
    BUTTON_RESTORED = (By.CSS_SELECTOR, ".warning-block__action")
    SHOW_ALL_DELETED = (By.XPATH, "//span[contains(text(),'показать')]")
    SVG_CLOSE_RESTORED_ARTICLE = (By.XPATH, "(//*[local-name()='svg'][@class='article-modal__close'])[1]")
    """add new role"""
    PERSONS = (By.XPATH, "//a[@data-tip='Участники']")
    ADD_ROLE = (By.CSS_SELECTOR, "button[class='m-ui-button-text']")
    INPUT_NAME_ROLE = (By.CSS_SELECTOR, "input[placeholder='Введите название роли']")
    SWITCH_BOX_CONTROL_CONTENT = (
        By.XPATH, "//span[contains(text(),'Управление контентом')]/../label[@class='m-switch-box']")
    CHECKBOX_RESTORE_CONTENT = (By.XPATH, "//span[contains(text(),'Восстановление контента')]")
    BUTTON_CREATE_ROLE = (By.CSS_SELECTOR, "button[class='m-button m-button--success m-button--medium']")
    BUTTON_SETTING_ACCESS = (By.XPATH, "//p[contains(text(),'Настроить доступы')]")
    BUTTON_SAVE_CHANGES = (By.CSS_SELECTOR, "button[class='m-button m-button--success m-button--medium']")
    BUTTON_SAVE_CHANGES_CONFIRM = (By.CSS_SELECTOR,
                                   "button[class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    BUTTON_CHANGE_PASSWORD = (By.XPATH, "//p[contains(text(),'Сменить пароль')]")
    INPUT_NEW_PASSWORD = (By.CSS_SELECTOR, "#newPass")
    INPUT_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#repPass")
    TEST_PROJECT = (By.XPATH,
                    "//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-space-list-item__title'][normalize-space()='selen']")  # name project
    SVG_POPUP_CLOSE_CREATED_PERSON = (By.XPATH, "//div[@class='popup__close']")
    PERSONS_AND_ROLES = (By.XPATH, "//span[text()='Участники']")
    BUTTON_HISTORY = (By.XPATH, "//a[@data-tip='История']")
    SVG_CLOSE_WINDOW_CREATED_PERSON = (By.CSS_SELECTOR, "div[role='presentation']")
    """check del article person1"""
    DEL_ARTICLE_2 = (By.XPATH, "(//header[@class='m-news-item__header'])[1]/../div[text()='deleted 2']")
    DEL_ARTICLE_2_WARNING = (By.XPATH, "//div[text()='Внимание! Этот контент удален']")
    RESTORED_ARTICLE_1 = (By.XPATH, "(//header[@class='m-news-item__header'])[4]/../div[text()='restored 1']")
    RESTORED_ARTICLE_1_CHECK_CHANGE = (
        By.XPATH, "//div[@class='article-modal__header-wrapper']//span[contains(text(),'changed name')]")
    RESTORED_ARTICLE_1_CHECK_ADDED_COMMENT = (By.XPATH, "//p[text()='1 комментарий']")
    SVG_CLOSE_CREATED_ARTICLE = (By.XPATH,
                                 "//body/div[@class='article-modal__portal']/div[@class='ReactModal__Overlay ReactModal__Overlay--after-open article-modal__overlay']/div[@role='dialog']/article[@class='article-modal']/div[@class='article-modal__main']/div[@class='article-modal__breadcrumbs-wrapper']/div[2]//*[local-name()='svg']")
    """check del article person2"""
    RESTORED_ARTICLE_1_CHECK_CHANGE_PERSON2 = (By.CSS_SELECTOR, "div[data-title='Восстановлен контент']")
    LABEL_ADMINISTRATOR_PERSON = (By.CSS_SELECTOR, "article[class='m-ui-avatar-default m-ui-avatar-default--small']")
    LABEL_ADMINISTRATOR_PERSON_OUT = (By.XPATH, "//p[contains(text(),'выйти')]")
    """del person"""
    LIST_ALL_PERSON = (
        By.CSS_SELECTOR, "div[class='m-user-card-info user-card__item m-user-card-info--without-checkbox']")
    CHANGE_DATA_PERSON = (By.XPATH, "//p[contains(text(),'Изменить данные')]")
    DEL_PERSON = (By.XPATH, "//p[contains(text(),'Удалить пользователя')]")
    DEL_PERSON_CONFIRM = (By.CSS_SELECTOR,
                          "button[class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    """comment check"""
    COMMENT_CREATED = (By.CSS_SELECTOR,
                       ".m-ui-paper.m-news-item__canvas.m-news-item__canvas--ticket.m-ui-paper--hoverable.m-ui-paper--shadowed")
    TEXT_COMMENT_CHECK = (By.XPATH, "//div[contains(text(),'Комментарий к контенту')]")
    FIRST_DELETED_CONTENT = (By.XPATH, "(//div[normalize-space()='deleted 2'])[1]")
    TEXT_CHECK_CANT_COMMENT = (By.XPATH, "//span[text()='Комментирование в этом контенте запрещено']")
    SVG_CLOSE_ARTICLE_ALERT = (By.CSS_SELECTOR, "div[class='article-editor__controls'] svg")


class AddFilterChangesLocators:
    SETTINGS = (By.XPATH, "//a[@data-tip='Настройки']")
    FILTERS_FOR_SEARCHING = (
        By.CSS_SELECTOR, ".m-ui-paper.m-big-card.m-tags-button.m-ui-paper--hoverable.m-ui-paper--shadowed")
    BUTTON_CREATE_GROUP_FILTER = (By.CSS_SELECTOR, ".empty-layout__upload")
    INPUT_NAME_GROUP = (By.CSS_SELECTOR, "input[class='m-ui-text-input__input']")
    BUTTON_GROUP_ADD = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium']")
    """add filters"""
    SEARCH_INPUT_BY_NAME_FILTER = (By.ID, "#tagManagerSearchInput")
    BUTTON_ADD_FILTER = (
        By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium single-editable-item__button']")
    INPUT_NAME_FILTER = (By.CSS_SELECTOR, "input[class='form-input-wrapper__input']")
    BUTTON_ADD_FILTER_ADD = (By.CSS_SELECTOR,
                             "div[class='single-editable-item__actions single-editable-item__actions--edit'] button[type='button']")
    """del filters"""
    # SVG_DEL_LIST = (By.XPATH, "//button[@class='both-sides-alignment-card-line__action single-editable-item__action single-editable-item__action--remove icon-button']")
    SVG_DEL_LIST = (By.XPATH, "//span[1]//button[2]//*[local-name()='svg']")
    SVG_DEL_1 = (By.XPATH,
                 "(//button[@class='both-sides-alignment-card-line__action single-editable-item__action single-editable-item__action--remove icon-button'])[1]")
    SVG_DEL_2 = (By.XPATH,
                 "(//button[@class='both-sides-alignment-card-line__action single-editable-item__action single-editable-item__action--remove icon-button'])[2]")
    SVG_DEL_3 = (By.XPATH,
                 "//button[@class='both-sides-alignment-card-line__action single-editable-item__action single-editable-item__action--remove icon-button']")
    SVG_DEL_LIST_CONFIRM = (By.CSS_SELECTOR,
                            "button[class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    CHANGE_NAME_GROUP = (
        By.CSS_SELECTOR, ".m-ui-typography.m-ui-typography--bold.m-ui-typography--14x14.m-ui-button-text__label")
    BUTTON_DEL_GROUP = (
        By.CSS_SELECTOR, "button[class='m-button m-button--danger m-button--medium editable-items-list__action']")
    BUTTON_DEL_GROUP_CONFIRM = (By.CSS_SELECTOR,
                                "button[class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    """close window"""
    SVG_CLOSE_WINDOW = (By.CSS_SELECTOR, "div[class='popup__close']")
    """mass change"""
    MEATBALL_MENU = (By.CSS_SELECTOR,
                     "button[class='m-button-basic-wrapper m-button-basic m-button-basic--tertiary m-button-basic--medium m-button-basic-wrapper--tertiary m-button-basic-wrapper--medium m-button-basic-wrapper--square']")
    MASS_CHANGE = (By.XPATH, "//div[text()='Массовое изменение']")
    DROPDOWN_FILTERS_FOR_SEARCHING = (
        By.CSS_SELECTOR, "div[class='m-ui-select m-ui-input-wrapper-2'] select[class='m-ui-select__select']")
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
    DIRECT_FOLDER = (By.XPATH,
                     "//div[@class='m-ui-paper m-ui-select__paper m-ui-paper--hoverable m-ui-paper--shadowed m-ui-paper--filled']//select[@class='m-ui-select__select']")
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
    GO_TO_CONTENT = (By.XPATH, "(//div[text()='Контент 1'])[2]")
    INPUT_SEARCH_CONTENT_BY_NAME_FOR_ADD_FILTERS = (By.CSS_SELECTOR, "input[placeholder='Введите название контента']")
    CREATED_CONTENT_FOR_FILTERS = (By.CSS_SELECTOR, ".massive-change__check-all-wrapper")
    # FILTERS = (By.CSS_SELECTOR, ".action-button__icon")
    FILTERS = (By.XPATH,
               "//div[@class='m-ui-paper tag-item button-sort__item action-button m-ui-paper--hoverable m-ui-paper--shadowed']")
    ARTICLE_BY_FILTERS = (By.CSS_SELECTOR, ".m-ui-paper.article-preview__body.m-ui-paper--shadowed")
    """check article"""
    TEXT_ARTICLE = (By.XPATH,
                    "//section[@class='article-modal__content article-modal--unique-class reader']//p[contains(text(),'Hello')]")
    VIDEO_ARTICLE = (
        By.XPATH,
        "//section[@class='article-modal__content article-modal--unique-class reader']//div[@class='m-video']")
    AUDIO_ARTICLE = (
        By.XPATH,
        "//section[@class='article-modal__content article-modal--unique-class reader']//div[@class='m-audio']")
    AUDIO_SCRIPT = (By.CSS_SELECTOR, "audio[title='undefined']")
    CHANGE_ARTICLE = (By.XPATH, "//div[text()='изменить']")
    BUTTON_TYPOGRAPHY_ARTICLE = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--small']")
    BUTTON_ARTICLE_BACK = (
        By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium wizard-wrapper__action']")
    TEXT_REQUEST_ARTICLE = (By.CSS_SELECTOR,
                            "div[class='both-sides-alignment-card-line__left-side both-sides-alignment-card-line__left-side--bottom-text both-sides-alignment-card-line--black-label-text'] span[class='both-sides-alignment-card-line__text']")
    TEXT_REQUEST_SCRIPT = (By.XPATH, "(//span[@class='both-sides-alignment-card-line__text'])[2]")
    SVG_DELETE_FILTER_ADDED = (
        By.CSS_SELECTOR, ".both-sides-alignment-card-line__action.search-wrapper__tag-btn--delete.icon-button")
    DROPDOWN_FILTERS_FOR_CHANGE = (By.XPATH,
                                   "//div[@class='m-ui-select m-ui-input-wrapper-2']//div[@class='m-ui-paper m-ui-select__paper m-ui-paper--hoverable m-ui-paper--shadowed']//select[@class='m-ui-select__select']")
    TO_GO_CONTENT = (By.CSS_SELECTOR, "section[class='m-bread-crumbs'] div[class='m-button-basic__text']")
    CLOSE_WINDOW = (By.CSS_SELECTOR, "//div[class='popup__close']")
    """check template"""
    FIELD_TEXT = (By.XPATH, "(//p[contains(text(),'some text')])[1]")
    FIELD_TEXT_2 = (By.XPATH,
                    "//section[@class='m-article-editor-templated article-modal__content article-modal--unique-class']//pre[@class='m-article-editor-templated__field-value'][normalize-space()='one more some text']")
    FIELD_TEXT_777 = (By.XPATH, "(//pre[@class='m-article-editor-templated__field-value'][normalize-space()='777'])[1]")
    FIELD_TEXT_WEBSITE = (By.XPATH, "(//a[@href='https://www.something.com'])[1]")
    FIELD_TEXT_MAIL = (By.XPATH,
                       "(//a[@class='m-article-editor-templated__field-value m-article-editor-templated__field-value--link'])[2]")
    FIELD_TEXT_NAME = (By.XPATH, "(//pre[@class='m-article-editor-templated__field-value'])[3]")


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
    SVG_TOOLTIP_REQUEST_FIELD = (
        By.XPATH, "//h4[contains(text(),'Закрепление контента в поисковой выдаче')]//*[local-name()='svg']")
    """check radio request"""
    RADIO_LINK_TO_CONTENT = (By.XPATH,
                             "//span[contains(text(),'Ссылка на контент')]/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
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
    BUTTON_BACK = (
        By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium wizard-wrapper__action']")
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
    BUTTON_EXECUTE = (
        By.CSS_SELECTOR, "button[class='m-button m-button--success m-button--medium wizard-wrapper__action']")
    LIST_ARTICLE_FOR_DEL = (By.XPATH, "//div[contains(text(),'text_alert')]")
    """check search"""
    SEARCH = (By.XPATH, "//div[text()='Поиск']")
    LIST_RESULT_SEARCH_RU_FIRST = (By.XPATH, "//span[contains(text(),'Соображения')]")
    LIST_RESULT_SEARCH_EN_SECOND = (By.XPATH, "//span[contains(text(),'высшего')]")
    LIST_RESULT_SEARCH_INVERSION = (By.XPATH, "//span[contains(text(),'Соображения высшего')]")
    LIST_RESULT_SEARCH_EN_FIRST_EN = (By.XPATH, "//span[contains(text(),'said')]")
    LIST_RESULT_SEARCH_EN_SECOND_EN = (By.XPATH, "//span[contains(text(),'dovish')]")
    LIST_RESULT_SEARCH_EN_INVERSION_EN = (By.XPATH, "//span[contains(text(),'more dovish')]")


##################################################################################################
class Comments:
    EXPERT_QUESTION = (By.XPATH, "//span[@class='checkbox__label']")
    ADD_COMMENT = (By.CSS_SELECTOR, "textarea[placeholder='Введите текст комментария']")
    # SEND_COMMENT = (By.CSS_SELECTOR, "p[class='m-ui-typography m-ui-typography--bold m-ui-typography--16x16 m-button__text']")
    SEND_COMMENT = (By.XPATH, "//p[text()='Отправить']")
    CHECK_COUNT_COMMENT = (By.XPATH, "//p[text()='5 комментариев']")
    SEND_COMMENT_FOR_CLOSE = (
        By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium discuss-form__button-send']")

    TEST_COMMENT_1 = (
        By.XPATH, "//pre[@class='m-discuss-text discuss-comment__text'][contains(text(),'Тестовый комментарий 1')]")
    TO_ANSWER_COMMENT_1 = (By.XPATH,
                           "//pre[@class='m-discuss-text discuss-comment__text'][contains(text(),'Тестовый комментарий 1')]/..//span[text()='ответить']")
    TEST_COMMENT_2 = (
        By.XPATH, "//pre[@class='m-discuss-text discuss-comment__text'][contains(text(),'Тестовый комментарий 2')]")
    TO_ANSWER_COMMENT_2 = (By.XPATH,
                           "//pre[@class='m-discuss-text discuss-comment__text'][contains(text(),'Тестовый комментарий 2')]/..//span[text()='ответить']")
    TEST_COMMENT_3 = (
        By.XPATH, "//pre[@class='m-discuss-text discuss-comment__text'][contains(text(),'Тестовый комментарий 3')]")
    TO_ANSWER_COMMENT_3 = (By.XPATH,
                           "//pre[@class='m-discuss-text discuss-comment__text'][contains(text(),'Тестовый комментарий 3')]/..//span[text()='ответить']")
    COMMENT_BOX = (
        By.XPATH, "//div[@class='m-ui-paper m-ui-paper--shadowed']//textarea[@placeholder='Введите текст комментария']")
    CHECK_BOX_TICK_SOLVED = (By.CSS_SELECTOR,
                             "label[class='m-ui-paper checkbox discuss-form__tag-item m-ui-paper--hoverable m-ui-paper--shadowed'] span[class='checkbox__label']")

    CLOSE_COMMENT = (
        By.CSS_SELECTOR, 'button[class="m-button m-button--default m-button--medium discuss-form__button-send"]')


class WizardPublic:
    BUTTON_TYPOGRAPHY = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--small']")
    BUTTON_NEXT = (By.CLASS_NAME,
                   'm-button.m-button--success.m-button--medium.wizard-wrapper__action')
    CHECKBOX_ALL_ROLES = (
        By.CLASS_NAME, "access-wrapper__check-all")
    ROLE_2 = (By.XPATH, "//p[contains(text(),'2 роль - редактор')]")
    ROLE_1 = (By.XPATH, "//p[contains(text(),'1 роль - нет права создания и редактирования контента')]")
    ROLE_2_NOTIFICATION = (
        By.XPATH, "//p[contains(text(),'2 роль - редактор')]/../..//span[text()='только оповестить']")
    ROLE_3 = (By.XPATH, "//p[contains(text(),'3 роль - редактор')]")
    ROLE_3_NOTIFICATION = (
        By.XPATH, "//p[contains(text(),'3 роль - редактор')]/../..//span[text()='только оповестить']")
    ROLE_4 = (By.XPATH, "//p[contains(text(),'4 роль - редактор')]")
    ROLE_4_NOTIFICATION = (
        By.XPATH, "//p[contains(text(),'4 роль - редактор')]/../..//span[text()='только оповестить']")
    INPUT_TEXT_TEXTAREA = (By.CSS_SELECTOR, "textarea[placeholder='Введите текст сообщения']")
    BUTTON_FINISH = (By.CSS_SELECTOR, "button[type='submit']")
    CHECKBOX_MINOR_EDIT = (By.XPATH, "//span[contains(text(),'Небольшие корректировки контента')]")
    BUTTON_EXECUTE = (
        By.CSS_SELECTOR, "button[class='m-button m-button--success m-button--medium wizard-wrapper__action']")


class CKERedactor:
    """Менеджер файлов"""
    UPLOAD_MEDIA = (By.XPATH, "//span[@class='cke_button_icon cke_button__uploadminerva_icon']")
    INPUT_INVISIBLE = (By.XPATH, "//input[@type='file']")
    CHECKBOX_INSERT_FILES = (By.XPATH, "//section[@class='m-file-view__content-block']")
    INPUT_SELECTED = (By.XPATH, "//p[contains(text(),'Вставить выбранные')]")


class AuthorisationPage:
    TYPE_AUTHOR = (By.CSS_SELECTOR, '.m-ui-select__select')  # type author
    TYPE_AUTHOR_CHANGE = (By.XPATH, "//option[@type='EMBEDDED']")
    LOGIN = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    INPUT_BUTTON = (By.XPATH, "//button[@type='submit']")
    TEST_PROJECT = (By.XPATH,
                    "//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-space-list-item__title'][normalize-space()='selen']")  # name project
    SUPER_BANK_PROJECT = (By.XPATH,
                          "//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-space-list-item__title'][normalize-space()='СуперБанк']")  # name project
    TESTING_PROJECT = (By.XPATH,
                       "//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-space-list-item__title'][normalize-space()='СуперБанк']")  # name project
    INPUT_IN_SYSTEM_TEXT = (
        By.CSS_SELECTOR, '.m-ui-typography.m-ui-typography--bold.m-ui-typography--22x26.login__header')


class CheckCommentsPersons:
    """Комментарии и уведомления"""
    EMPTY_HISTORY_CHECK = (By.CLASS_NAME, "m-news-empty__title")
    # через get_attribute("data-tip") получаем количество уведомлений
    BELL_ALERT = (By.CSS_SELECTOR,
                  ".m-button-main-menu.m-button-main-menu--collapsed.m-button-notification.m-button-notification"
                  "--collapsed.m-dashboard-top-right-side__notifications")
    EMPTY_BELL__CHECK = (By.CSS_SELECTOR, '.dashboard-notification-empty-layout__title')
    CREATE_ARTICLE_CHECK = (By.XPATH, "(//div[contains(text(),'Создание статьи')])[1]")
    MAJOR_EDIT_ARTICLE_CHECK = (By.XPATH, "(//div[contains(text(),'Мажорное редактирование')])[1]")
    DELETE_ARTICLE_CHECK = (By.XPATH, "(//div[contains(text(),'Удаление')])[1]")
    RESTORE_ARTICLE_CHECK = (By.XPATH, "(//div[contains(text(),'Восстановление')])[1]")
    # здесь проверка тестового комментария 1 и статуса не решено через is_displayed()
    CHECK_TEST_COMMENT_1 = (By.XPATH,
                            f"//h3[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../../div[text()='не решено']/../..//pre[text()='Тестовый комментарий 1']")
    CHECK_TEST_COMMENT_2 = (By.XPATH,
                            f"//h3[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../../div[text()='не решено']/../..//pre[text()='Тестовый комментарий 2']")
    CHECK_TEST_COMMENT_3 = (By.XPATH,
                            f"//h3[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../../div[text()='не решено']/../..//pre[text()='Тестовый комментарий 3']")
    CHECK_TEST_COMMENT_4 = (By.XPATH,
                            f"//h3[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../../div[text()='не решено']/../..//pre[text()='Тестовый комментарий 4']")
    CHECK_GRAY_COMMENT = (By.XPATH, "(//pre[contains(text(),'Серый комментарий')])[1]")
    # открытие статьи проверка комментариев (проверка, что не решено)
    TEST_COMMENT_1_NOT_SOLVED = (By.XPATH, "//div[text()='не решено']/..//pre[text()='Тестовый комментарий 1']")
    TEST_COMMENT_2_NOT_SOLVED = (By.XPATH, "//div[text()='не решено']/..//pre[text()='Тестовый комментарий 2']")
    TEST_COMMENT_3_NOT_SOLVED = (By.XPATH, "//div[text()='не решено']/..//pre[text()='Тестовый комментарий 3']")
    TEST_COMMENT_4_NOT_SOLVED = (By.XPATH, "//div[text()='не решено']/..//pre[text()='Тестовый комментарий 4']")
    GRAY_COMMENT_ARTICLE = (By.CSS_SELECTOR,
                            "div[class='discuss__block discuss__block--COMMENT'] pre[class='m-discuss-text discuss-comment__text']")


class MenuNavigation:
    # TODO: написать нормальные локаторы для навигации по левому меню
    """Навигация по левому меню"""
    HISTORY_BUTTON = (By.XPATH, "//span[text()='История']")
    CONTENT = (By.XPATH, "//a[@data-tip='Контент']")  # content of page


class OpenArticle:
    # ARTICLE_TITLE = (By.XPATH, '//*[@id="article-content-modal-header"]/div/h2/span')
    # через .text  получаем название
    ARTICLE_TITLE = (By.CSS_SELECTOR, "div[class='article-modal__header-wrapper'] span")
    CHECK_ARTICLE_BOTTOM_BANNER = (By.CLASS_NAME, 'warning-block-router')
    BOTTOM_BANNER_BUTTON = (By.CLASS_NAME, "warning-block__action")


class CheckBellComments:
    # Колокольчик
    RED_NEW = (By.CSS_SELECTOR, "button[class='m-ui-button-text']")
    #  Проверка Персоном 2
    BELL_CHECK_TEST_COMMENT_1 = (
        By.XPATH, f"//div[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../..//div[text()='Тестовый комментарий 1']")
    BELL_CHECK_TEST_COMMENT_2 = (
        By.XPATH, f"//div[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../..//div[text()='Тестовый комментарий 2']")
    BELL_CHECK_TEST_COMMENT_3 = (
        By.XPATH, f"//div[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../..//div[text()='Тестовый комментарий 3']")
    BELL_CHECK_TEST_COMMENT_4 = (
        By.XPATH, f"//div[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../..//div[text()='Тестовый комментарий 4']")
    BELL_CHECK_TEST_COMMENT_GRAY = (
        By.XPATH, f"//div[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../..//div[text()='Серый комментарий']")
    BELL_CHECK_TEST_CREATE_ARTICLE = (
        By.XPATH, f"//div[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../..//div[text()='Создание статьи']")
    BELL_CHECK_TEST_MAJOR_EDIT = (
        By.XPATH, f"//div[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../..//div[text()='Мажорное редактирование']")
    BELL_CHECK_TEST_CLOSE_3 = (By.XPATH, f"//div[text()='{'НАЗВАНИЕ СТАТЬИ'}']/../..//div[text()='Закрытие 3']")
    #  Проверка Персоном 3 (остальные локаторы как из персона 2)
    BELL_CREATE_ARTICLE_CONFIRM = (By.XPATH,
                                   f"//div[text()='подтвердите']/../..//div[text()='Название статьи 9881']/../..//div[text()='Создание статьи']")


class CheckAfterUpdating:
    """Локаторы проверки контента в статье после обновления"""
    CHECK_NAME_ARTICLE = (By.XPATH, "//div[@class='article-modal__header-wrapper']//span[contains(text(),'Обычная статья')]")
    VERSION_CHECK = (By.CSS_SELECTOR, "button[class='m-button-basic-wrapper m-button-basic m-button-date m-button-basic--tertiary m-button-basic--small m-button-basic-wrapper--tertiary m-button-basic-wrapper--small']")
    SVG_VERSION_WINDOW_CLOSE = (By.XPATH, "//div[@class='m-popup__close']")
    NUMBER_VERSION_CHECK = (By.CSS_SELECTOR, "div[class='scroller__content version-select-diff__scroller'] div:nth-child(1) div:nth-child(3) h3:nth-child(1)")
    "Локаторы изображений"
    IMG1_IN_ARTICLE = (By.XPATH,
                       "(//img[@alt='girl-ga8f2187eb_640'])[1]")
    IMG2_IN_ARTICLE = (By.XPATH,
                       "(//img[@alt='122'])[1]")
    "Локаторы видео"
    VIDEO1_IN_ARTICLE = (By.XPATH,
                         "(//video[@title='загруженное'])[1]")
    VIDEO2_IN_ARTICLE = (By.XPATH,
                         "(//video[@title='Sunset - 86879'])[1]")
    "Локаторы аудио"
    AUDIO_IN_ARTICLE = (By.XPATH,
                        "(//audio[@title='perry-como-magic-moments-mp3'])[1]")
    "Локаторы таблица и текст стили"
    # TABLE_IN_ARTICLE = (By.XPATH, "//div[@class='m-table-widget__wrapper m-table-widget__wrapper--extendable']//table[@class='m-cke-table']")
    # TABLE_IN_ARTICLE = (By.XPATH, "//section[@class='article-modal__content article-modal--unique-class reader reader--narrow']//div[@class='os-viewport os-viewport-scrollbar-hidden']")
    TABLE_IN_ARTICLE = (By.XPATH, "(//div[@class='os-viewport os-viewport-scrollbar-hidden'])[3]")
    # CHECK_TEXT_IN_TABLE = (By.XPATH, "//div[@class='m-table-widget__wrapper m-table-widget__wrapper--extendable']//table[@class='m-cke-table']//td[@data-cell='1_0']")
    # CHECK_TEXT_IN_TABLE = (By.XPATH, "//section[@class='article-modal__content article-modal--unique-class reader reader--narrow']//div[@class='os-viewport os-viewport-scrollbar-hidden']//p[text()='Строка']")
    CHECK_TEXT_IN_TABLE = (By.XPATH, "(//p[contains(text(),'Строка')])[1]")
    CHECK_H1_TEXT = (By.XPATH, "(//h1[@id='chapter_1'])[1]")
    CHECK_H2_TEXT = (By.XPATH, "(//h2[@id='chapter_2'])[1]")
    CHECK_H3_TEXT = (By.XPATH, "(//h3[@id='chapter_3'])[1]")
    CHECK_P_TEXT = (By.XPATH,  "(//p[contains(text(),'Обычный текст')])[1]")
    CHECK_STRONG_TEXT = (By.XPATH, "(//strong[contains(text(),'Жирный')])[1]")
    CHECK_ITALICS_TEXT = (By.XPATH,"(//em[contains(text(),'Курсив')])[1]")
    CHECK_UNDERLINED_TEXT = (By.XPATH, "(//u[contains(text(),'Подчеркнутый')])[1]")
    CHECK_SUPERSCRIPT_TEXT = (By.XPATH, "(//sup[contains(text(),'Надстрочный')])[1]")
    CHECK_SUBSCRIPT_TEXT = (By.XPATH, "(//sub[contains(text(),'Подстрочный')])[1]")
    CHECK_CROSSED_OUT_TEXT = (By.XPATH, "(//s[contains(text(),'Перечеркнутый')])[1]")
    "Локаторы выравнивания текста"
    CHECK_ALIGN_CENTER_TEXT = (By.XPATH,
                               "(//p[contains(text(),'Выравнивание по центру')])[1]")
    CHECK_ALIGN_RIGHT_TEXT = (By.XPATH,
                              "(//p[contains(text(),'Выравнивание справа')])[1]")
    CHECK_ALIGN_JUSTIFY_TEXT = (By.XPATH,
                                "(//p[contains(text(),'Выравнивание по ширине текст текст текст текст тек')])[1]")
    "Локаторы цвета текста"
    CHECK_COLOR_TEXT = (By.XPATH,
                        "(//span[contains(text(),'Цвет шрифта')])[1]")
    CHECK_HIGHLIGHT_COLOR_TEXT = (By.XPATH,
                                  "(//span[contains(text(),'Выделение текста')])[1]")
    "Важное"
    CHECK_IMPORTANT_BLOCK_RED = (By.XPATH,
                                 "(//div[@class='m-important-info'])[1]")
    "Спойлер"
    CHECK_SPOILER = (By.XPATH,
                     "(//div[@class='m-spoiler__header'][contains(text(),'Спойлер')])[1]")
    CHECK_SPOILER_SHOW = (By.XPATH,
                          "(//div[@class='m-spoiler m-spoiler--show'])[1]")
    LINK_HREF = (By.XPATH,
                          "(//a[contains(text(),'Задача')])[1]")
    LINK_HREF_ZRJHM = (By.XPATH,
                 "(//a[@href='#zrjhm'][normalize-space()='#zrjhm'])[1]")
    LINK_HREF_PHONE = (By.XPATH,
                       "(//a[contains(text(),'tel:89367776777')])[1]")
    LINK_HREF_MAIL = (By.XPATH,
                       "(//a[contains(text(),'admin@minervakms.ru')])[1]")
    "Локаторы проверка статьи по шаблону"
    IMG1_IN_TEMPLATE = (By.XPATH,
                      "(//img[@alt='Germany_Winter_Trains_Brocken_Railway_Rails_Snow_609681_1280x853'])[1]")
    VIDEO_IN_TEMPLATE = (By.XPATH,
                        "(//video[@title='Sunset - 86879'])[1]")
    TEXT_TEMPLATE = (By.XPATH,
                     "(//span[contains(text(),'Шаблонная статья')])[1]")
    LINK1 = (By.XPATH,
             "//p[contains(text(),'1 Ссылка')]")
    TASK = (By.XPATH,
             "//li[@title='Задача']")
    HEADING = (By.XPATH,
             "//p[contains(text(),'Оглавление')]")
    LINK3 = (By.XPATH,
                     "//p[contains(text(),'3 Ссылки')]")


class Test:
    """Локаторы для работы с тестами"""
    CREATING_TEST_BUTTON = (By.XPATH, "(//div[@class='m-lms-action-tooltip'])[5]")
    TEST_NAME = (By.NAME, "name")
    TEST_DESCRIPTION = (By.NAME, "description")
    SAVE_BUTTON = (By.XPATH,
                   "//button[@class='m-button m-button--default m-button--small lms-quiz-editor__save lms-quiz-editor__control-button']")
    NEW_QUESTION_BUTTON = (By.XPATH, "//p[contains(text(),'Добавить вопрос')]")
    MODAL_WINDOW_NAME = (By.XPATH, "//h3[@class='title-block']")
    ALL_QUESTIONS_SELECT = (By.CSS_SELECTOR, ".m-switch-box.lms-questions-lib__header-switch")
    QUESTIONS_LIMIT_STATUS = (By.CSS_SELECTOR, ".m-ui-typography.m-ui-typography--16x18.m-ui-slider__text")
    QUESTIONS_LIMIT_VALUE = (By.NAME, "randomQuestionCount")
    COUNT_OF_CORRECT_ANSWERS = (By.CSS_SELECTOR, ".m-ui-select__select")
    NAME_CREATED_TEST = (By.CSS_SELECTOR, ".popup__title.title-block")


class Quiz:
    """Локаторы для работы с опросами"""
    CREATING_QUIZ_BUTTON = (By.XPATH, "//div[contains(text(),'Опрос')]")
    QUIZ_NAME = (By.XPATH, "//input[@placeholder='Введите название опроса']")
    QUIZ_DESCRIPTION = (By.XPATH, "//input[@placeholder='Введите описание опроса']")
    SAVE_BUTTON = (By.XPATH, "//button[@class='m-button m-button--default m-button--medium m-lms-quiz-editor__save']")
    NEW_QUESTION_BUTTON = (By.CLASS_NAME, "button-transparent")
    TEXT_QUESTION = (By.XPATH, "//textarea[@placeholder='Введите текст вопроса']")
    TEXT_ANSWER = (By.XPATH, "//textarea[@placeholder='Введите текст ответа']")
    ADD_ANSWER_BUTTON = (By.XPATH, "//button[@class='m-button m-button--default m-button--medium']")
    CREATE_QUESTION_BUTTON = (
        By.XPATH, "//button[@class='m-button m-button--success m-button--medium m-lms-question-editor__footer-button']")


class Course:
    """Локаторы для работы с курсами"""
    CREATING_COURSE_BUTTON = (By.XPATH, "//div[contains(text(),'Курс')]")

    COURSE_NAME = (
        By.XPATH,
        "//div[@class='textarea-wrapper-form m-lms-course-cover__name']//textarea[@class='textarea-wrapper-form__textarea']")
    COURSE_DESCRIPTION = (
        By.XPATH,
        "//div[@class='textarea-wrapper-form m-lms-course-cover__description']//textarea[@class='textarea-wrapper-form__textarea']")

    ADD_MATERIAL_BUTTON = (By.XPATH, "//button[@class='m-button m-button--default m-button--medium']")

    SAVE_BUTTON = (
        By.XPATH,
        "//button[@class='m-button m-button--success m-button--medium lms-course-editor-sidebar__save-button']")

    CLOSE_WINDOW = (By.XPATH, "//*[name()='path' and contains(@d,'M19.5327 1')]")

    DRAFT_SAVE_CONFIRM_BUTTON = (
        By.XPATH, "//button[@class='m-button m-button--success m-button--medium lms-save-draft-confirm__left-btn']")
    DRAFT_SAVE_ABORT_BUTTON = (By.XPATH, "//p[contains(text(),'не сохранять')]")
    CONTENT_BUTTON = (By.XPATH, "//div[@class='m-lms-action-tooltip']")

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class FormPagesLocators:
    """CREATE PROJECT"""
    ADD = (By.XPATH, "//div[@class='m-titled-group__aside-content']")
    ADD_NAMES_PROJECT = (By.XPATH, "//input[@placeholder='Введите название проекта']")
    ADD_DESCRIPTION_PROJECT = (By.XPATH, "//input[@placeholder='Введите описание проекта']")
    # ADD_PROJECT_BUTTON = (By.XPATH, "//button[@type='button']")
    ADD_PROJECT_BUTTON = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium']")
    TYPE_AUTHOR = (By.CSS_SELECTOR, "select[class='m-ui-select__select']")  # type author
    TYPE_AUTHOR_CHANGE = (By.XPATH, "//option[@type='EMBEDDED']")  # new type auth
    LOGIN = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    INPUT_BUTTON = (By.XPATH, "//button[@type='submit']")
    HISTORY_BUTTON = (By.XPATH, "//a[@data-html='true']")
    """name project selen"""
    TEST_PROJECT = (By.XPATH,
                    "//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-space-list-item__title'][normalize-space()='selen']")  # name project
    SUPER_BANK_PROJECT = (By.XPATH,
                          "//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-space-list-item__title'][normalize-space()='СуперБанк']")  # name project
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
    I_REMEMBER_PASSWD = (By.CSS_SELECTOR, "button[class='m-ui-button-text login__restore-password']")
    CHECK_TEXT_INPUT_IN_SYSTEM = (
    By.CSS_SELECTOR, "h1[class='m-ui-typography m-ui-typography--bold m-ui-typography--22x26 m-titled-group__title']")
    """logo"""
    LOGO_HEAD = (By.CLASS_NAME, 'm-main-menu-logo__icon')
    LOGO_FAVICO = (By.ID, 'favicon')
    MOUSE_LOGO = (By.XPATH, "//img[@class='m-main-menu-logo__icon']")
    """title"""
    CONTENT = (By.XPATH, "//a[@data-tip='Контент']")  # content of page
    ALL_CONTENT = (By.CLASS_NAME, "folder-list-item__total")
    # CONTENT1 = (By.XPATH, "(//a[@class='folder-list-item__head'])[2]")
    CONTENT1 = (By.XPATH, "//div[@title='Контент 1']")
    # CONTENT1_NAME = (By.XPATH, "//p[contains(text(),'Контент 1')]")  # check name of content
    NAME_CONTENT = (By.XPATH, "//section[2]//article[1]//a[1]//section[1]")
    EDIT = (By.XPATH,
            "//body/div[@class='article-modal__portal']/div[@class='ReactModal__Overlay ReactModal__Overlay--after-open article-modal__overlay']/div[@role='dialog']/article[@class='article-modal']/div[@class='article-modal__main']/div[@class='scroller article-modal__scroller']/div[@class='scroller__wrap']/div[@class='scroller__body']/div[@class='scroller__content article-modal__scroller-content']/div[@class='article-modal__container']/header[@id='article-content-modal-header']/div[@class='article-modal__controls']/button[2]")
    # CREATE_BUTTON = (By.CSS_SELECTOR, ".m-button.m-button--default")
    CREATE_BUTTON = (By.XPATH, "//div[text()='Создать']")
    CREATE_BUTTON_1 = (By.XPATH, "//div[text()='Создать']")
    """article"""
    CREATE_ARTICLE = (By.XPATH, "(//div[@class='m-lms-action-tooltip'])[1]")
    # NAME_OF_ARTICLE = (By.XPATH, "//input[@placeholder='Введите название контента']")
    NAME_OF_ARTICLE = (By.CSS_SELECTOR, "input[class='m-ui-text-input__input']")
    FOLDER_SAVE_ARTICLE = (By.XPATH, "//select[@class='m-ui-select__select']")
    TYPOGRAPHY_ARTICLE = (By.XPATH, "//p[contains(text(),'опубликовать')]")
    SUBMIT_ARTICLE = (By.XPATH, "//button[@type='submit']")
    CHECKBOX_SETTINGS_COMMENTS = (By.XPATH,
                                  "//span[text()='Комментирование']/..//label[@class='m-switch-box m-switch-box--checked m-switch__checkbox-switch']")
    CHECKBOX_SETTINGS_DOWNLOADS = (By.XPATH,
                                   "//span[text()='Скачивание']/..//label[@class='m-switch-box m-switch-box--checked m-switch__checkbox-switch']")
    CHECKBOX_SETTINGS_PRINTING = (By.XPATH,
                                  "//span[text()='Печать']/..//label[@class='m-switch-box m-switch-box--checked m-switch__checkbox-switch']")
    TEXTAREA_ARTICLE = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    CREATE_STEP_SCRIPT = (By.XPATH, "(//div[@class='m-lms-action-tooltip'])[3]")
    INPUT_INVISIBLE = (By.XPATH, "//input[@type='file']")
    CHECKBOX_INSERT_FILES = (By.XPATH, "//section[@class='m-file-view__content-block']")
    # CLOSE_CREATED_ARTICLE = (By.XPATH, "//header[@id='article-content-modal-header']//span[@class='link-iconed__label-text'][normalize-space()='selen']")
    CLOSE_CREATED_ARTICLE = (By.CSS_SELECTOR, ".article-modal__close")
    # CLOSE_PAGE_LIST = (By.XPATH, "//div[@class='article-editor__controls']//*[name()='svg']")
    # CLOSE_PAGE_LIST = (By.XPATH, "//div[@class='article-editor__controls']//*[local-name()='svg']")
    # CLOSE_PAGE_LIST = (By.XPATH, "//div[@class='article-editor__controls']//*[local-name()='svg']")
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
    # PERSONS = (By.XPATH, "//a[2]//article[1]//pre[1]")
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
    TEXT_NOT_FOLDERS = (By.XPATH, "//span[text()='У вас нет избранного контента. Для начала создайте папку.']")
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
    By.XPATH, "//div[@class='radio-wrapper__icon radio-wrapper__icon--checked']/../span[text()='Опубликовать сейчас']")
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
    By.XPATH, "//span[text()='Опубликовать сейчас']/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    CHECK_RADIOBUTTON_NO_DELETE = (
    By.XPATH, "//span[text()='Не удалять']/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    CHECK_TEXT_ROLE = (By.XPATH, "//span[contains(text(),'роль')]")
    # FRAME_PERSON_CLOSE = (By.XPATH, "//div[@role='presentation']")
    FRAME_PERSON_CLOSE = (By.CSS_SELECTOR, ".popup__close svg")
    """FIXING ARTICLE"""
    # SEARCH_HEAD_PAGE = (By.XPATH, "//p[contains(text(),'Поиск')]")
    SEARCH_HEAD_PAGE = (By.XPATH, "//div[contains(text(),'Поиск')]")
    BUTTON_FIXING_CONTENT = (By.XPATH, "//p[contains(text(),'Закрепить контент')]")
    INPUT_REQUEST = (By.XPATH, "//input[@placeholder='Введите запрос']")
    CHECK_ADD_FIXING_CONTENT = (By.XPATH, "//h3[contains(text(),'Добавление закрепленного контента')]")
    BUTTON_FIXING_CONTENT1 = (By.XPATH, "//p[text()='закрепить контент']")
    # BUTTON_FIXING_CONTENT_CHANGE = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium m-content-fix-manager__empty-button']")
    BUTTON_FIXING_CONTENT_CHANGE = (
    By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium m-pin-manager-tab__empty-button']")
    ARTICLE_1_IN_LIST = (By.XPATH, "//span[normalize-space()='tesss']")
    BUTTON_SUBMIT = (By.XPATH, "//p[contains(text(),'Продолжить')]")
    CHECK_LINK_OF_CONTENT_RADIO = (
    By.XPATH, "//span[text()='Ссылка на контент']/../div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")
    SEARCH_TEST_ARTICLE = (By.XPATH, "//input[@placeholder='Введите название контента']")
    TEST_ARTICLE_NAME = (By.XPATH, "//article[@class='m-content-fix-wizard__content_item']")
    CHECK_NAME_CONTENT = (By.XPATH,
                          "//section[@class='m-content-fix-wizard__link']//p[@class='m-content-fix-wizard__meta'][contains(text(),'Контент 1')]")
    CHECK_NAME_ARTICLE = (By.XPATH, "//section[@class='m-content-fix-wizard__link']/./p[text()='Alan']")
    INCLUDED_CONTENT_RADIO = (By.XPATH, "//span[contains(text(),'Содержимое контента')]")
    INCLUDED_CONTENT = (By.XPATH, "//section[@class='reader']")
    FIXING = (By.XPATH, "//button[@type='submit']")
    # LIST_OF_ARTICLES = (By.XPATH, "//p[@class='article-preview__title title-element']")
    LIST_OF_ARTICLES = (
    By.XPATH, "//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-card-article__link-title']")
    # POPUP_CLOSE_SVG = (By.XPATH, "//div[@class='popup__close']")
    POPUP_CLOSE_SVG = (By.CSS_SELECTOR, "div[data-testid='testModalClose']")
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
    WINDOW_POPUP_TEMPLATE = (By.CSS_SELECTOR, ".m-popup__container")
    MODAL_WINDOW_FOR_TEMPLATE = (By.XPATH, "//div[@role='dialog']")
    MODAL_WINDOW_SCROLLER = (
    By.XPATH, "//div[@class='scroller m-modal-templates__scroller']//div[@class='scroller__thumb scroller__thumb--Y']")
    MODAL_WIZARD_SCROLLER_TEMPLATE = (
    By.XPATH, "//div[@class='scroller m-modal-templates__scroller']//div[@class='scroller__track scroller__track--y']")
    SUBMIT_TEMPLATES_FINISH_EDIT = (By.XPATH, "//p[contains(text(),'Завершить')]")
    BACK_TEMPLATES_FINISH_EDIT = (By.XPATH, "//p[contains(text(),'Назад')]")
    CHANGE_TEMPLATES_BUTTON_CONFIRM = (By.XPATH, "//p[contains(text(),'Изменить шаблон')]")
    CHANGE_TEMPLATES_BUTTON = (By.XPATH, "//button[@class='m-ui-button-text']//span[text()='изменить']")
    # CHANGE_TEMPLATES_BUTTON = (By.XPATH, "//span[text()='изменить']")
    # CHANGE_TEMPLATES_BUTTON = (By.XPATH, "(//span[text()='изменить'])[3]")
    CHANGE_TEMPLATES = (By.XPATH, "//button[@class='m-ui-button-text']")
    CHANGE_TEMPLATES_BUTTON_1 = (By.XPATH,
                                 "//button[@class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']//p[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x16 m-button__text'][contains(text(),'Изменить шаблон')]")
    check_text_name = (By.XPATH,
                       "//div[@class='m-ui-text-input m-ui-input-wrapper-2']//div[@class='m-ui-typography m-ui-typography--14x14 m-ui-input-wrapper-2__label']")
    check_name_input = (By.CSS_SELECTOR, "input[class='m-ui-text-input__input']")
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
    BUTTON_DELETE_DRAFT = (By.XPATH, "//p[text()='Удалить черновик']")
    # FIELD_CAN_NOT_DEL = (By.XPATH, "//body/div[@class='ReactModalPortal']/div[@class='ReactModal__Overlay ReactModal__Overlay--after-open article-editor-container__overlay']/div[@role='dialog']/article[@class='article-editor article-editor--templated']/div[@class='article-editor__container']/div[@class='article-editor__content article-editor__content--templated']/div[@class='scroller']/div[@class='scroller__wrap article-editor__scroller-wrap']/div[@class='scroller__body article-editor__scroller-body']/div[@class='scroller__content article-editor__scroller-content']/div[@class='article-editor__editor article-editor__editor--templated']/div[@class='m-article-editor-templated__content']/div[@class='m-article-editor-templated__loader-wrapper']/section[@class='m-templated-layouts m-templated-layouts--one-column m-article-editor-templated__layout m-article-editor-templated__layout--tail']/div[@class='m-templated-layouts__column']/div[7]/div[1]")
    FIELD_CAN_NOT_DEL = (By.XPATH, "//div[text()='название']")
    FIELD_CAN_NOT_DEL_1 = (By.XPATH,
                           "//body/div[@class='ReactModalPortal']/div[@class='ReactModal__Overlay ReactModal__Overlay--after-open article-editor-container__overlay']/div[@role='dialog']/article[@class='article-editor article-editor--templated']/div[@class='article-editor__container']/div[@class='article-editor__content article-editor__content--templated']/div[@class='scroller']/div[@class='scroller__wrap article-editor__scroller-wrap']/div[@class='scroller__body article-editor__scroller-body']/div[@class='scroller__content article-editor__scroller-content']/div[@class='article-editor__editor article-editor__editor--templated']/div[@class='m-article-editor-templated__content']/div[@class='m-article-editor-templated__loader-wrapper']/section[@class='m-templated-layouts m-templated-layouts--one-column m-article-editor-templated__layout m-article-editor-templated__layout--tail']/div[@class='m-templated-layouts__column']/div[7]/div[1]")
    FIELD_CAN_NOT_DEL_2 = (By.XPATH,
                           "//body/div[@class='ReactModalPortal']/div[@class='ReactModal__Overlay ReactModal__Overlay--after-open article-editor-container__overlay']/div[@role='dialog']/article[@class='article-editor article-editor--templated']/div[@class='article-editor__container']/div[@class='article-editor__content article-editor__content--templated']/div[@class='scroller']/div[@class='scroller__wrap article-editor__scroller-wrap']/div[@class='scroller__body article-editor__scroller-body']/div[@class='scroller__content article-editor__scroller-content']/div[@class='article-editor__editor article-editor__editor--templated']/div[@class='m-article-editor-templated__content']/div[@class='m-article-editor-templated__loader-wrapper']/section[@class='m-templated-layouts m-templated-layouts--one-column m-article-editor-templated__layout m-article-editor-templated__layout--tail']/div[@class='m-templated-layouts__column']/div[7]/div[1]")
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
    # CHECK_FIXING_CONTENT_TEXT = (By.XPATH, "//span[text()='В этой папке пока нет контента, но Вы можете это изменить.']")
    CHECK_FIXING_CONTENT_TEXT = (By.XPATH, "//p[contains(text(),'ничего не найдено')]")
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



class StepByScriptLocators:
    ADD_SCRIPT = (By.XPATH, "//div[text()='Пошаговый сценарий']")
    ADD_STEP_BUTTON = (By.XPATH, "//p[text()='добавить шаг']")
    """block scripts"""
    CHECK_TEXT_BEGIN = (By.XPATH, "//p[text()='Начало']")
    CHECK_TEXT_STEP1 = (By.XPATH, "//p[text()='Шаг 1']")
    CHECK_TEXT_STEP2 = (By.XPATH, "//p[text()='Шаг 2']")
    TEXT_END_SCRIPT = (By.XPATH, "//p[contains(text(),'Завершение')]")
    PLUS_BUTTON_ADD_STEP = (By.XPATH, "//button[@data-tip='добавить шаг']")
    INPUT_NAME_CONTENT = (By.CSS_SELECTOR,
                          "div[class='cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']")
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
    By.XPATH, "//div[3]/div[3]//div[@class='scenario-answer__fields-wrapper']//input[@class='m-ui-text-input__input']")
    TEXT_TRANSACTION_TO_STEP = (By.XPATH, "//div[3]/div[1]/div[2]/div/label/div[1]")
    LIST_DROPDOWN = (By.XPATH, "//div[3]/div[3]//select/option/..")
    TEXT_CHECK_SCRIPT_FINISH = (By.XPATH, "//div[3]/div[3]//select/option/../option[text()='Сценарий завершён']")
    TEXT_CHECK_ADD_NEW_STEP = (By.XPATH, "//p[text()='Для начала добавьте первый шаг']")
    TEXT_CHECK_NAME_NEW_STEP = (By.XPATH,
                                "//div[@class='scenario-question__name m-ui-text-input m-ui-input-wrapper-2']//input[@placeholder='Введите название']")
    TEXT_CHECK_INPUT_CONTENT_OF_STEP = (By.XPATH, "//div[@aria-label='false']")
    INPUT_CONTENT_OF_STEP = (By.CSS_SELECTOR, "label[class='m-ui-input-wrapper__body']")
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
    CHECK_TEXT_CONTENT_SCRIPT = (By.XPATH, "//p[@class='m-content-fix-wizard__meta']")
    # CHECK_TEXT_CONTENT_SCRIPT = (By.XPATH, "//p[text()='Контент 1']")
    # CHECK_TEXT_CONTENT_SCRIPT = (By.XPATH, "(//p[text()='Контент 1'])[2]")
    FINISH_BUTTON_SCRIPT = (By.XPATH, "//p[contains(text(),'Завершить')]")
    TEXT_CHECK_WINDOW_TYPOGRAPHY_CONTENT = (By.XPATH, "//h3[contains(text(),'Настройки публикации контента')]")
    TEXT_CHECK_SEARCH = (By.XPATH, "//p[contains(text(),'поиск')]")
    BUTTON_CONTINUE = (By.XPATH, "//p[contains(text(),'Продолжить')]")
    TEXT_AREA_ALERT_INPUT = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    # CONTENT_TRANSFER = (By.XPATH, "//section[@class='m-bread-crumbs']//div[@class='m-button-basic__text'][contains(text(),'Контент 1')]")
    CONTENT_TRANSFER = (By.XPATH, "//section[@class='m-bread-crumbs']//div[@title='Контент 1']")
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

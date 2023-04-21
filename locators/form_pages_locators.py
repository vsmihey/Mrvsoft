from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class FormPagesLocators:
    TYPE_AUTHOR = (By.CSS_SELECTOR, '.m-ui-select__select')  # type author
    TYPE_AUTHOR_CHANGE = (By.XPATH, "//option[@type='EMBEDDED']")  # new type auth
    LOGIN = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    INPUT_BUTTON = (By.XPATH, "//button[@type='submit']")
    """name project selen"""
    TEST_PROJECT = (By.XPATH, "//div[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x20 m-space-list-item__title'][normalize-space()='selen']")  # name project
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
    EDIT = (By.XPATH, "//body/div[@class='article-modal__portal']/div[@class='ReactModal__Overlay ReactModal__Overlay--after-open article-modal__overlay']/div[@role='dialog']/article[@class='article-modal']/div[@class='article-modal__main']/div[@class='scroller article-modal__scroller']/div[@class='scroller__wrap']/div[@class='scroller__body']/div[@class='scroller__content article-modal__scroller-content']/div[@class='article-modal__container']/header[@id='article-content-modal-header']/div[@class='article-modal__controls']/button[2]")
    CREATE_BUTTON = (By.CSS_SELECTOR, ".m-button.m-button--default")
    """article"""
    CREATE_ARTICLE = (By.XPATH, "(//div[@class='m-lms-action-tooltip'])[1]")
    NAME_OF_ARTICLE = (By.XPATH, "//input[@placeholder='Введите название контента']")
    FOLDER_SAVE_ARTICLE = (By.XPATH, "//select[@class='m-ui-select__select']")
    TYPOGRAPHY_ARTICLE = (By.XPATH, "//p[contains(text(),'опубликовать')]")
    SUBMIT_ARTICLE = (By.XPATH, "//button[@type='submit']")
    TEXTAREA_ARTICLE = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    CREATE_STEP_SCRIPT = (By.XPATH, "(//div[@class='m-lms-action-tooltip'])[3]")
    CLOSE_CREATED_ARTICLE = (By.XPATH, "//header[@id='article-content-modal-header']//span[@class='link-iconed__label-text'][normalize-space()='selen']")
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
    TEXT_FOLDERS_CHECK = (By.XPATH, "//p[contains(text(),'Папки')]") #
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
    RADIOBUTTON_ACTIVE_CHECK = (By.XPATH, "//div[@class='radio-wrapper__icon radio-wrapper__icon--checked']")  # activated
    RADIOBUTTON_SEARCH = (By.CSS_SELECTOR, ".radio-wrapper__icon")
    CHECK_CREATED_NEW_FOLDER = (By.XPATH, "//p[text()='{name_of_new_folder}']")
    SECOND_FOLDER_IN_LIST = (By.XPATH, "(//div[@class='tree-item-content'])[2]")
    FOLDER_FOR_DEL_BY_NAME = (By.XPATH, "//div[contains(text(),'Adam')]")
    DELETE_FOLDER_BUTTON = (By.XPATH, "//p[contains(text(),'Удалить папку')]")
    DELETE_FOLDER_CONFIRM_TEXT = (By.XPATH, "//h3[text()='Подтверждение действия']")
    CLOSE_WINDOW_STRUCTURE = (By.XPATH, "//div[@class='popup__close']")
    SHOW_DELETED_FOLDERS = (By.XPATH, "//span[contains(text(),'показать')]")
    RECOVERY_FOLDER_BY_NAME = (By.XPATH, "//p[normalize-space()='Sherri153']")
    RECOVERY_FOLDER_BUTTON = (By.XPATH, "//div[@class='action-button-group']")
    RECOVERY_FOLDER_BUTTON_CONFIRM = (By.XPATH, "//p[contains(text(),'восстановить папку')]")
    CHECK_TEXT_ALL_CONTENT_SORT_BY_POPULAR = (By.XPATH, "//span[contains(text(),'по популярности')]")
    CLOSE_EDIT_FOLDERS_WINDOW = (By.XPATH, "//div[@class='popup__close']")
    MOVE_FROM_DEL_FOLDER = (By.XPATH, "//select[@class='m-ui-select__select']")
    MOVE_FROM_DEL_FOLDER_TEXT = (By.XPATH, "//h4[contains(text(),'Папка для перемещения')]")
    FOLDER1 = (By.XPATH, "//div[contains(text(),'папка1')]")
    FOLDER2 = (By.XPATH, "//div[contains(text(),'папка2')]")
    SAVE_CHANGES_FOLDER = (By.XPATH, "//p[contains(text(),'сохранить изменения')]")

















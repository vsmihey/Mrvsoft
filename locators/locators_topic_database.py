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
    TEXT_NEW_QUESTION_TOPIC_WINDOW = (By.XPATH, "//h3[contains(text(),'Новая тема')]")
    TEXT_NAME = (By.XPATH, "//div[text()= 'название']")
    TEXT_PLACEHOLDER_INPUT_NAME_TOPIC = (By.XPATH, "//input[@placeholder='Введите название темы']")
    TEXT_PARENT_TOPIC = (By.XPATH, "//div[text()='родительская тема']")
    TEXT_DROPDOWN_DEFAULT = (By.XPATH, "//select[@class='m-ui-select__select']//option[text()='Нет']") # ПРОВЕРИТЬ
    BUTTON_CREATE_TOPIC = (By.XPATH, "//footer[@class='m-popup__footer lms-edit-theme-popup__footer']//p[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x16 m-button__text'][contains(text(),'Создать тему')]") # ПРОВЕРИТЬ
    """input name topic and check len"""
    INPUT_NAME_TOPIC = (By.XPATH, "//input[@placeholder='Введите название темы']")
    """check text structure"""
    TEXT_RULE_STRUCTURE = (By.XPATH, "//h3[contains(text(),'Управление структурой')]")
    TEXT_CREATED_TOPIC_NAME = (By.XPATH, "//div[@class='tree-item-content__name']")
    """function create new topic"""
    BUTTON_NEW_TOPIC = (By.XPATH, "//p[contains(text(),'Новая тема')]")
    """del created topics"""
    LIST_CREATED_TOPICS = (By.CSS_SELECTOR, "li[class='m-tree-item m-tree-item__wrapper']")
    BUTTON_DELETE_TOPIC = (By.XPATH, "//button[@class='m-button m-button--danger m-button--medium lms-edit-theme-popup__delete']")
    BUTTON_CONFIRM_DELETE_TOPIC = (By.XPATH, "//button[@class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    SVG_CLOSE_DELETED_WINDOW = (By.XPATH, "//div[@class='m-popup__close']")
    """question add"""
    BUTTON_QUESTION_ADD = (By.XPATH, "//p[contains(text(),'Добавить')]")
    BUTTON_CHANGE_QUESTION = (By.XPATH, "//p[contains(text(),'Изменить тему')]")
    TEXT_DATABASE_OF_QUESTION = (By.XPATH, "//p[text()='В этом проекте пока нет вопросов. Вы можете это исправить']")
    TEXT_DATABASE_OF_QUESTION_HEAD = (By.XPATH, "//h3[contains(text(),'База вопросов')]")
    """new question form"""
    TEXT_NEW_QUESTION = (By.XPATH, "//h3[contains(text(),'Новый вопрос')]")
    TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION = (By.XPATH, "//textarea[@placeholder='Введите текст вопроса']")
    DROPDOWN_TIPE_OF_QUESTION = (By.XPATH, "//div[@class='lms-question-editor__field m-ui-select m-ui-input-wrapper-2']//select[@class='m-ui-select__select']")
    DROPDOWN_TOPIC = (By.XPATH, "//div[@class='lms-question-editor__input m-ui-select m-ui-input-wrapper-2']//select[@class='m-ui-select__select']")
    ANSWER_AND_CHECKBOX = (By.XPATH, "//textarea[@placeholder='Введите текст ответа']")
    ANSWER_CHECKBOX = (By.XPATH, "//label[@class='radio-wrapper lms-answer-field__radio radio-wrapper--no-label']")
    BUTTON_CREATE_QUESTION = (By.XPATH, "//p[contains(text(),'Создать вопрос')]")
    """check created window question"""
    SVG_SLIDERS = (By.XPATH, "//div[@class='themes-side-popup-filter__icon-container']")
    TEXT_MODAL_WINDOW_TOPICS = (By.XPATH, "//h3[contains(text(),'Темы')]")
    CHANGE_TOPICS_WINDOW = (By.XPATH, "//span[contains(text(),'изменить')]")
    TEXT_CREATED_NEW_QUESTION = (By.XPATH, "//span[@class='lms-question-bar__text']")
    SVG_DEL_QUESTION = (By.XPATH, "(//*[local-name()='svg'][@class='lms-question-bar__icon lms-question-bar__icon-trash'])")
    SVG_DEL_QUESTION_CONFIRM = (By.XPATH, "//p[contains(text(),'Удалить вопрос')]")
    """check all created topics"""
    TEXT_FIRST_TOPIC = (By.XPATH, "(//div[@class='tree-item-content__name'])[1]")
    DROPDOWN_PARENTS_TOPIC = (By.XPATH, "//select[@class='m-ui-select__select']")
    BUTTON_SAVE_TOPIC = (By.XPATH, "//p[contains(text(),'Сохранить тему')]")
    BUTTON_DELETE_TOPIC_CONFIRM = (By.XPATH, "//p[contains(text(),'Удалить тему')]")
    BUTTON_CREATE_TOPIC_CONFIRM = (By.XPATH, "//p[contains(text(),'Создать тему')]")
    """check same name and last in list"""""
    GO_TO_TOPICS_LIST = (By.XPATH, "//div[@class='ReactModal__Content ReactModal__Content--after-open lms-theme-structure m-popup__window']")
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
    NAME_OF_ARTICLE = (By.XPATH, "//input[@placeholder='Введите название контента']")
    # FOLDER_SAVE_ARTICLE = (By.CSS_SELECTOR, "select[class='m-ui-select__select']")
    FOLDER_SAVE_ARTICLE = (By.XPATH, "(//select[@class='m-ui-select__select'])[3]")
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
    CHECKED_CHECK = (By.XPATH, "//section[@class='m-file-view m-file-view--selected m-file-view--image-cover m-file-view--selectable file-manager__item']")
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
    QUESTIONS_FIRST_POSITION = (By.XPATH, "(//div[@class='article-wizard-tests-question-row__left-side'])[1]")
    QUESTIONS_FIRST_POSITION_CSS = (By.CSS_SELECTOR, "body > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
    QUESTIONS_SECOND_POSITION = (By.XPATH, "(//div[@class='article-wizard-tests-question-row__left-side'])[2]")
    QUESTIONS_SECOND_POSITION_CSS = (By.CSS_SELECTOR, "body > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
    # TAB_ACTIVE = (By.XPATH, "//div[@class='tab-item tab-item--active']")
    TAB_ACTIVE = (By.XPATH, "(//div[@class='tab-item tab-item--active'])[2]")
    BUTTON_FINISH = (By.XPATH, "//button[@type='submit']")
    EDIT_ARTICLE = (By.XPATH, "//div[text()='изменить']")
    BUTTON_GO_BACK = (By.CSS_SELECTOR, "button[class='m-button m-button--default m-button--medium wizard-wrapper__action']")
    TEXT_GET_TESTED = (By.XPATH, "//span[contains(text(),'пройти тестирование')]")
    RADIOBUTTON_SMALL_CORRECT_CONTENT = (By.XPATH, "//span[contains(text(),'Небольшие корректировки контента')]")
    RADIOBUTTON_BIG_CORRECT_CONTENT = (By.XPATH, "//span[contains(text(),'Значительные изменения контента')]")
    """check position"""
    LIST_QUESTIONS_POSITION = (By.CSS_SELECTOR, "div[class='article-wizard-tests-question-row__left-side']")
    """del question from test"""
    SVG_DEL_FIRST_QUESTION = (By.XPATH, "(//*[local-name()='svg'][@class='article-wizard-tests-question-row__control-icon'])[3]")
    SVG_DEL_SECOND_QUESTION = (By.XPATH, "(//*[local-name()='svg'][@class='article-wizard-tests-question-row__control-icon'])[6]")
    LIST_SVG_DEL_QUESTION = (By.XPATH, "//div[@class='article-wizard-tests-question-row__control-button article-wizard-tests-question-row__control-button--remove']")
    CONFIRM_BUTTON_DELETE = (By.XPATH, "//button[@class='m-button m-button--danger m-button--medium popup-confirm__action popup-confirm__danger']")
    """check by template"""
    CREATE_TEMPLATES = (By.XPATH, "//div[contains(text(),'Шаблон')]")
    NEW_TEMPLATE = (By.XPATH, "//div[@class='m-lms-action-tooltip m-modal-templates__template-card']")
    ADD_FIELD_BUTTON = (By.XPATH, "//button[contains(text(),'Добавить поле')]")
    LIST_OF_FIELDS_1 = (By.XPATH, "//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[1]")
    INPUT_NAME_OF_FIELD = (By.XPATH, "//input[@placeholder='Введите название поля']")
    SAVE_TEMPLATES = (By.XPATH, "//button[@class='m-button m-button--success m-button--medium']//p[@class='m-ui-typography m-ui-typography--bold m-ui-typography--16x16 m-button__text'][contains(text(),'сохранить')]")
    INPUT_NAME_OF_TEMPLATES = (By.XPATH, "//input[@placeholder='Введите название шаблона']")
    SAVE_TEMPLATES_CHANGE = (By.XPATH, "//p[text()='Сохранить']")
    FINISH_BUTTON_SCRIPT = (By.XPATH, "//p[contains(text(),'Завершить')]")
    DROPDOWN = (By.XPATH, "//span[@class='cke_button_icon cke_button__inserttemplated_icon']")
    FRAME = (By.XPATH, "//iframe[@class='cke_panel_frame']")
    DROP_DOWN_FILES = (By.XPATH, "//a[@title='Файлы']")
    FOLDER_SAVE = (By.XPATH, "//div[@class='m-ui-paper m-ui-select__paper m-ui-paper--hoverable m-ui-paper--shadowed m-ui-paper--filled']//select[@class='m-ui-select__select']")
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



















    # DROPDOWN_TIPE_OF_QUESTION = (By.XPATH, "(//select[@class='m-ui-select__select'])[1]")










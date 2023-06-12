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

    # DROPDOWN_TIPE_OF_QUESTION = (By.XPATH, "(//select[@class='m-ui-select__select'])[1]")










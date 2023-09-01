import pathlib
import random
import time
from pathlib import Path
from selenium.common import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver import Keys, ActionChains
from generator.generator import generated_person
from locators.locators_topic_database import CreateTopicDatabaseLocators
from pages.authorisation_page import Authorisation
from pages.base_page import BasePage


class CreateTopicDatabase(Authorisation, BasePage):
    Locators = CreateTopicDatabaseLocators

    def add_topic_database(self, driver):
        """ADD TOPIC AND CHECK TEXTS, LEN INPUT NAME"""
        # self.input_in_my_project(driver)
        self.click_to_element(self.Locators.LEARNING_BUTTON)
        self.click_to_element(self.Locators.TAB_ALL_COURSES)
        self.click_to_element(self.Locators.DATABASE_OF_QUESTIONS)
        """проверка текста названия открытого окна"""
        text_database_of_questions = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTIONS).text
        assert text_database_of_questions == "База вопросов"

        time.sleep(10)
        try:
            text_not_questions_now = self.element_is_visible(self.Locators.TEXT_NOT_QUESTIONS_NOW, timeout=2).text
            assert text_not_questions_now == "В этом проекте пока нет вопросов. Создайте структуру тем для его размещения"
        except TimeoutException:
            try:
                self.click_to_element(self.Locators.BUTTON_QUESTION_ADD, timeout=2)
            except TimeoutException:
                time.sleep(2)
                list_question = self.elements_are_visible(self.Locators.SVG_DEL_QUESTION)
                for n in list_question:
                    time.sleep(1)
                    n.click()
                    time.sleep(0.5)
                    self.click_to_element(self.Locators.SVG_DEL_QUESTION_CONFIRM)
                # try:
                #     self.click_to_element(self.Locators.BUTTON_QUESTION_ADD, timeout=2)
                # except TimeoutException:
                #     time.sleep(2)
                #     self.click_to_element(self.Locators.SVG_DEL_QUESTION)
                #     time.sleep(1)
                #     self.click_to_element(self.Locators.SVG_DEL_QUESTION_CONFIRM)
                #     self.click_to_element(self.Locators.BUTTON_QUESTION_ADD, timeout=2)
            self.click_to_element(self.Locators.BUTTON_QUESTION_ADD)
            self.click_to_element(self.Locators.BUTTON_CHANGE_QUESTION)
            self.delete_created_topics()  # не удаляется тема
            try:
                self.click_to_element(self.Locators.SVG_CLOSE_DELETED_WINDOW, timeout=5)
            except TimeoutException:
                print("БАГ! НЕ УДАЛЯЕТСЯ ТЕМА! БАГ!")
            self.click_to_element(self.Locators.SVG_CLOSE_DELETED_WINDOW)
        button_add_topic = self.element_is_visible(self.Locators.BUTTON_ADD_TOPIC).text
        assert button_add_topic == 'Создать темы'
        self.click_to_element(self.Locators.BUTTON_ADD_TOPIC)
        """input name topic and check len"""
        try:
            element = self.element_is_visible(self.Locators.INPUT_NAME_TOPIC)
        except TimeoutException:
            print("БАГ НЕ УДАЛЯЕТСЯ ТЕМА")
            element = self.element_is_visible(self.Locators.INPUT_NAME_TOPIC)
        name_content, get_name = self.check_len_name(driver, element, n=65)
        self.element_is_visible(self.Locators.INPUT_NAME_TOPIC).send_keys(name_content)
        assert len(get_name) == 64
        """create topic"""
        self.click_to_element(self.Locators.BUTTON_CREATE_TOPIC)
        """check text open window"""
        text_rule_structure = self.element_is_visible(self.Locators.TEXT_RULE_STRUCTURE).text
        assert text_rule_structure == "Управление структурой"
        text_created_topic_name = self.element_is_visible(self.Locators.TEXT_CREATED_TOPIC_NAME).text
        assert text_created_topic_name == get_name
        button_new_topic = self.element_is_visible(self.Locators.BUTTON_NEW_TOPIC).text
        assert button_new_topic == "Новая тема"
        self.create_new_topic()
        """close window created topics"""
        self.click_to_element(self.Locators.SVG_CLOSE_DELETED_WINDOW)
        self.create_new_question(driver)
        # self.delete_created_topics()

    def create_new_topic(self):
        """CREATE NEW TOPICS"""
        person = generated_person()
        for i in range(21):
            self.click_to_element(self.Locators.BUTTON_NEW_TOPIC)
            self.element_is_visible(self.Locators.INPUT_NAME_TOPIC).send_keys(person.first_name + str(random.randint(99, 999)))
            self.click_to_element(self.Locators.BUTTON_CREATE_TOPIC)

    def delete_created_topics(self):
        """DELETE CREATED TOPICS"""
        list_created_topics = self.elements_are_visible(self.Locators.LIST_CREATED_TOPICS)
        for n in list_created_topics:
            time.sleep(1)
            n.click()
            time.sleep(0.5)
            try:
                self.click_to_element(self.Locators.BUTTON_DELETE_TOPIC)
            except TimeoutException:
                time.sleep(3)
                n.click()
                self.click_to_element(self.Locators.BUTTON_DELETE_TOPIC)
            time.sleep(1)
            self.click_to_element(self.Locators.BUTTON_CONFIRM_DELETE_TOPIC)

    def create_new_question(self, driver):
        """CREATE AN CHECK NEW QUESTION"""
        """check open form"""
        text_of_question = "Здесь должен быть текст вопроса"+str(random.randint(99, 999))
        answer_of_question = "Ответ на вопрпос"+str(random.randint(99, 999))
        text_database_of_question_head = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTION_HEAD).text
        assert text_database_of_question_head == "База вопросов"
        text_database_of_question = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTION).text
        assert text_database_of_question == "В этом проекте пока нет вопросов. Вы можете это исправить"
        self.click_to_element(self.Locators.BUTTON_QUESTION_ADD)
        text_new_question = self.element_is_visible(self.Locators.TEXT_NEW_QUESTION).text
        assert text_new_question == "Новый вопрос"
        """fill in the placeholder"""
        self.element_is_visible(self.Locators.TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION).send_keys(text_of_question)
        """dropdown tipe"""
        self.click_to_element(self.Locators.DROPDOWN_TIPE_OF_QUESTION)
        self.element_is_visible(self.Locators.DROPDOWN_TIPE_OF_QUESTION).send_keys(Keys.ARROW_DOWN)
        self.element_is_visible(self.Locators.DROPDOWN_TIPE_OF_QUESTION).send_keys(Keys.RETURN)
        """dropdown topic"""
        self.click_to_element(self.Locators.DROPDOWN_TOPIC)
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).send_keys(Keys.ARROW_DOWN)
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).send_keys(Keys.RETURN)
        """answer"""
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).send_keys(answer_of_question)
        self.click_to_element(self.Locators.ANSWER_CHECKBOX)
        self.click_to_element(self.Locators.BUTTON_CREATE_QUESTION)
        """created question window"""
        text_database_of_question_head = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTION_HEAD).text
        assert text_database_of_question_head == "База вопросов"
        text_created_new_question = self.element_is_visible(self.Locators.TEXT_CREATED_NEW_QUESTION).text
        assert text_created_new_question == text_of_question
        self.click_to_element(self.Locators.SVG_SLIDERS)
        text_modal_window_topics = self.element_is_visible(self.Locators.TEXT_MODAL_WINDOW_TOPICS).text
        assert text_modal_window_topics == "Темы"
        self.click_to_element(self.Locators.CHANGE_TOPICS_WINDOW)
        text_rule_structure = self.element_is_visible(self.Locators.TEXT_RULE_STRUCTURE).text
        assert text_rule_structure == "Управление структурой"
        """check all created topics"""
        text_first_topic = self.element_is_visible(self.Locators.TEXT_FIRST_TOPIC).text
        len_text_first_topic = len(text_first_topic)
        assert len_text_first_topic == 64
        self.click_to_element(self.Locators.TEXT_FIRST_TOPIC)
        self.element_is_visible(self.Locators.TEXT_PLACEHOLDER_INPUT_NAME_TOPIC).clear()
        self.element_is_visible(self.Locators.TEXT_PLACEHOLDER_INPUT_NAME_TOPIC).send_keys("THE SAME NAME")
        self.click_to_element(self.Locators.BUTTON_SAVE_TOPIC)
        """the same name create"""
        self.click_to_element(self.Locators.BUTTON_NEW_TOPIC)
        self.element_is_visible(self.Locators.TEXT_PLACEHOLDER_INPUT_NAME_TOPIC).send_keys("THE SAME NAME")
        self.click_to_element(self.Locators.BUTTON_CREATE_TOPIC_CONFIRM)
        """check count the same name, locators: name_1 and name_2 contains text THE SAME NAME """
        data_same_name = []
        name_1 = self.element_is_visible(self.Locators.NAME_1)
        data_same_name.append(name_1)
        time.sleep(1)
        try:
            name_2 = self.elements_is_present(self.Locators.NAME_2)
        except TimeoutException:
            time.sleep(3)
            name_2 = self.elements_is_present(self.Locators.NAME_2)
        data_same_name.append(name_2)
        self.go_to_element(name_2)
        """check name las topic"""
        self.click_to_element(self.Locators.NAME_2)
        name_2_value = self.element_is_visible(self.Locators.TEXT_PLACEHOLDER_INPUT_NAME_TOPIC).get_attribute("value")
        assert name_2_value == "THE SAME NAME"
        print(len(data_same_name))
        assert len(data_same_name) == 2
        self.click_to_element(self.Locators.BUTTON_SAVE_TOPIC)
        try:
            self.click_to_element(self.Locators.SVG_CLOSE_DELETED_WINDOW)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.SVG_CLOSE_DELETED_WINDOW)
        """delete question"""
        self.click_to_element(self.Locators.SVG_DEL_QUESTION)
        self.click_to_element(self.Locators.SVG_DEL_QUESTION_CONFIRM)

    def check_text_questions(self):
        """CHECK QUESTION TEXT"""
        text_settings_question = self.element_is_visible(self.Locators.TEXT_SETTINGS_QUESTION).text
        assert text_settings_question == "Настройка вопроса"
        text_questions_text = self.element_is_visible(self.Locators.TEXT_QUESTIONS_TEXT).text
        assert text_questions_text == "текст вопроса:"
        textarea_placeholder_input_name_question = self.element_is_visible(
            self.Locators.TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION).get_attribute("placeholder")
        assert textarea_placeholder_input_name_question == "Введите текст вопроса"
        """check first dropdown"""
        text_questions_type = self.element_is_visible(self.Locators.TEXT_QUESTIONS_TYPE).text
        assert text_questions_type == "тип вопроса:"
        text_dropdown = self.element_is_visible(self.Locators.DROPDOWN_TIPE_OF_QUESTION).text
        assert text_dropdown == 'Выбор нескольких ответов\nВыбор одного ответа\nВвод ответа'
        """check topic text"""
        text_topic = self.element_is_visible(self.Locators.TEXT_TOPIC).text
        assert text_topic == "Тема"
        text_choose_topic = self.element_is_visible(self.Locators.TEXT_CHOOSE_TOPIC).text
        assert text_choose_topic == "выберите тему:"
        """questions options check"""
        text_questions_options = self.element_is_visible(self.Locators.TEXT_QUESTIONS_OPTIONS).text
        assert text_questions_options == "Варианты ответа"

    def edit_topic_in_database(self):
        # self.input_in_my_project(driver)
        self.click_to_element(self.Locators.LEARNING_BUTTON)
        self.click_to_element(self.Locators.TAB_ALL_COURSES)
        self.click_to_element(self.Locators.DATABASE_OF_QUESTIONS)
        """check text and button"""
        try:
            text_database_of_question = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTION, timeout=3).text
            assert text_database_of_question == "В этом проекте пока нет вопросов. Вы можете это исправить"
        except TimeoutException:
            try:
                list_delete = self.elements_are_visible(self.Locators.SVG_DEL_QUESTION)
                for n in list_delete:
                    time.sleep(1)
                    n.click()
                    time.sleep(0.5)
                    self.click_to_element(self.Locators.SVG_DEL_QUESTION_CONFIRM)
                text_database_of_question = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTION).text
                assert text_database_of_question == "В этом проекте пока нет вопросов. Вы можете это исправить"
            except TimeoutException:
                time.sleep(5)
                text_database_of_question = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTION).text
                assert text_database_of_question == "В этом проекте пока нет вопросов. Вы можете это исправить"
        button_question_add = self.element_is_clickable(self.Locators.BUTTON_QUESTION_ADD).text
        assert button_question_add == "Добавить"
        self.element_is_clickable(self.Locators.BUTTON_QUESTION_ADD).click()
        """check add new question"""
        text_new_question = self.element_is_visible(self.Locators.TEXT_NEW_QUESTION).text
        assert text_new_question == "Новый вопрос"
        """check function text"""
        self.check_text_questions()
        """dropdown topic"""
        self.click_to_element(self.Locators.DROPDOWN_TOPIC)
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).send_keys(Keys.ARROW_DOWN)
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).send_keys(Keys.RETURN)
        """input random text"""
        element = self.element_is_visible(self.Locators.TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION)
        name_content = self.input_random_symbols(element, 20)
        """dropdown choose answer"""
        self.element_is_visible(self.Locators.DROPDOWN_TIPE_OF_QUESTION).send_keys("Выбор одного ответа")
        """add questions options answers"""
        element = self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX)
        self.input_random_symbols(element, 5)
        self.click_to_element(self.Locators.ANSWER_CHECKBOX)
        self.click_to_element(self.Locators.BUTTON_CREATE_QUESTION)
        """check open modal window"""
        text_database_of_question_head = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTION_HEAD).text
        assert text_database_of_question_head == "База вопросов"
        text_created_new_question = self.element_is_visible(self.Locators.TEXT_CREATED_NEW_QUESTION).text
        assert text_created_new_question == name_content

    def edit_question(self):
        self.click_to_element(self.Locators.SVG_EDIT_QUESTION)
        self.check_text_questions()
        self.element_is_visible(self.Locators.TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION).clear()
        self.element_is_visible(self.Locators.TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION).send_keys("Edit question")
        self.click_to_element(self.Locators.BUTTON_EDIT_QUESTION_SAVE)
        """check text edit question"""
        text_edit_new_question = self.element_is_visible(self.Locators.TEXT_CREATED_NEW_QUESTION).text
        assert text_edit_new_question == "Edit question"
        """add new question 2 option questions"""
        self.click_to_element(self.Locators.BUTTON_NEW_QUESTION)
        """dropdown topic"""
        self.click_to_element(self.Locators.DROPDOWN_TOPIC)
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).send_keys(Keys.ARROW_DOWN)
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).send_keys(Keys.RETURN)
        """input random text"""
        element = self.element_is_visible(self.Locators.TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION)
        name_content = self.input_random_symbols(element, 20)
        """add questions options answers"""
        element = self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX)
        self.input_random_symbols(element, 5)
        self.click_to_element(self.Locators.BUTTON_QUESTION_ADD)
        self.element_is_visible(self.Locators.NEW_ANSWER_PLACEHOLDER).send_keys("adding answer")
        list_checkboxes = self.elements_are_visible(self.Locators.ANSWER_CHECKBOX_1_1)
        for n in list_checkboxes:
            n.click()
        self.click_to_element(self.Locators.BUTTON_CREATE_QUESTION)
        try:
            text_check_result_created_questions_second = self.element_is_visible(
                self.Locators.TEXT_CHECK_RESULT_CREATED_QUESTIONS_SECOND, timeout=3).text
            assert text_check_result_created_questions_second == name_content
        except AssertionError:
            self.click_to_element(self.Locators.LIST_QUESTIONS)
            text_check_result_created_questions_second = self.element_is_visible(
                self.Locators.TEXT_CHECK_RESULT_CREATED_QUESTIONS_SECOND).text
            assert text_check_result_created_questions_second == name_content
        text_check_result_created_questions_first = self.element_is_visible(
            self.Locators.TEXT_CHECK_RESULT_CREATED_QUESTIONS_FIRST).text
        assert text_check_result_created_questions_first == "Edit question"
        """delete all questions"""
        # list_delete = self.elements_are_visible(self.Locators.SVG_DEL_QUESTION)
        # for n in list_delete:
        #     n.click()
        #     self.click_to_element(self.Locators.SVG_DEL_QUESTION_CONFIRM)

    def add_edit_question_article(self, driver):
        """ADD AND EDIT QUESTION IN ARTICLE
        В БАЗЕ ДОЛЖНЫ БЫТЬ ВОПРОСЫ С ПРЕДЫДУЩЕГО ТЕСТА"""
        person = generated_person()
        first_name = person.first_name
        text = "Hello"
        # self.input_in_my_project(driver)
        # data_files = generated_file()
        """upload media"""
        time.sleep(2)
        try:
            self.click_to_element(self.Locators.CREATE_BUTTON, timeout=1)
        except (TimeoutException, StaleElementReferenceException):
            time.sleep(2)
            self.click_to_element(self.Locators.CREATE_BUTTON)
        self.click_to_element(self.Locators.CREATE_ARTICLE)
        """input name and text an folder direct"""
        self.element_is_visible(self.Locators.NAME_OF_ARTICLE).send_keys(first_name)
        try:
            self.element_is_visible(self.Locators.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")
        except ElementNotInteractableException:
            time.sleep(2)
            driver.refresh()
            time.sleep(5)
            self.element_is_visible(self.Locators.NAME_OF_ARTICLE).send_keys(first_name)
            self.element_is_visible(self.Locators.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")
            time.sleep(3)
        try:
            self.element_is_visible(self.Locators.TEXT_AREA_ARTICLE).send_keys(text)
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(self.Locators.TEXT_AREA_ARTICLE).send_keys(text)
        try:
            self.click_to_element(self.Locators.UPLOAD_MEDIA, timeout=2)
        except TimeoutException:
            time.sleep(5)
            self.click_to_element(self.Locators.UPLOAD_MEDIA)
        """input is visible for load files"""
        # self.driver.execute_script(
        #     """document.querySelector(".popup__footer.file-manager__foot.file-manager--hidden").removeAttribute('class')""")
        # self.driver.execute_script(
        #     """document.querySelector("form[enctype='multipart/form-data']").removeAttribute('style')""")
        self.download_files_is_visible()
        path1 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        data_path = [path1, path2]
        for n in data_path:
            self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(n)
        time.sleep(5)
        checkbox_insert_files = self.elements_are_visible(self.Locators.CHECKBOX_INSERT_FILES)
        for n in checkbox_insert_files:
            time.sleep(0.5)
            n.click()
        try:
            self.click_to_element(self.Locators.INPUT_SELECTED)
        except ElementClickInterceptedException:
            time.sleep(10)
            self.click_to_element(self.Locators.INPUT_SELECTED)
        self.element_is_visible(self.Locators.DIRECT_FOLDER_NAME).send_keys("Контент")
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        """open vizard"""
        text_typography_content = self.element_is_visible(self.Locators.TEXT_TYPOGRAPHY_CONTENT).text
        assert text_typography_content == "Настройки публикации контента"
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность'
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        """change testing"""
        self.click_to_element(self.Locators.BUTTON_JUST_NOTIFY)
        self.click_to_element(self.Locators.TEXT_CONFIRM_READ)
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность\nтест'
        # self.element_is_visible(self.Locators.TEXT_TAB_TEST).is_displayed()
        text_alert = "ALERT-" + str(random.randint(99, 999))
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        """add question"""
        self.click_to_element(self.Locators.BUTTON_ADD_QUESTION)
        """check text and checkboxes"""
        text_choose_question_for_test = self.element_is_visible(self.Locators.TEXT_CHOOSE_QUESTION_FOR_TEST).text
        assert text_choose_question_for_test == "Выберите вопросы для теста"
        list_checkboxes = self.elements_are_visible(self.Locators.LIST_CHECKBOXES)
        for n in list_checkboxes:
            attribute_class = n.get_attribute("class")
            assert attribute_class == "m-switch-box lms-question-bar__switch"
        # assert text_choose_question_for_test == "Выберите вопросы для теста"
        self.click_to_element(self.Locators.ON_CHECKBOX_ALL_QUESTIONS)
        time.sleep(1)
        try:
            self.click_to_element(self.Locators.SVG_CLOSE_DELETED_WINDOW)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.SVG_CLOSE_DELETED_WINDOW)
        """check first position by index xpath dom and active tab"""
        tab_active = self.element_is_visible(self.Locators.TAB_ACTIVE).text
        assert tab_active == 'тест'
        time.sleep(1)
        try:
            questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        except TimeoutException:
            time.sleep(2)
            questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        assert questions_first_position_check == "Edit question"
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.EDIT_ARTICLE)
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        """go tu test tab"""
        # self.click_to_element(self.Locators.BUTTON_FINISH)
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert + " new")
        self.click_to_element(self.Locators.BUTTON_CONTINUE)
        # self.click_to_element(self.Locators.BUTTON_FINISH)
        # time.sleep(3)
        # self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert + " new")
        # self.click_to_element(self.Locators.BUTTON_FINISH)
        """check position"""
        try:
            self.click_to_element(self.Locators.QUESTIONS_FIRST_POSITION_CHECK)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.QUESTIONS_FIRST_POSITION_CHECK)
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).clear()
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).send_keys("edit answer")
        self.click_to_element(self.Locators.BUTTON_EDIT_QUESTION_SAVE)
        self.click_to_element(self.Locators.BUTTON_GO_BACK)
        self.click_to_element(self.Locators.TEXT_GET_TESTED)
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность'
        # self.element_is_visible(self.Locators.TEXTAREA_ALERT).clear()
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert + " new")
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.EDIT_ARTICLE)
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY, timeout=2)
        except TimeoutException:
            time.sleep(2)
            self.click_to_element(self.Locators.BUTTON_DELETE_DRAFT)
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.BUTTON_JUST_NOTIFY)
        self.click_to_element(self.Locators.TEXT_CONFIRM_READ)
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность\nтест'
        self.click_to_element(self.Locators.RADIOBUTTON_SMALL_CORRECT_CONTENT)
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность'
        self.click_to_element(self.Locators.RADIOBUTTON_BIG_CORRECT_CONTENT)
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность\nтест'
        self.click_to_element(self.Locators.BUTTON_FINISH)
        """check position"""
        """del question from test"""
        # del1
        self.click_to_element(self.Locators.SVG_DEL_FIRST_QUESTION)
        self.click_to_element(self.Locators.CONFIRM_BUTTON_DELETE)
        # del2
        self.click_to_element(self.Locators.SVG_DEL_FIRST_QUESTION)
        self.click_to_element(self.Locators.CONFIRM_BUTTON_DELETE)

    def check_add_question_func(self, driver):
        path1 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        data_path = [path1, path2]
        for n in data_path:
            time.sleep(1)
            self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(n)
        time.sleep(2)
        try:
            checkbox_insert_files = self.elements_are_visible(self.Locators.CHECKBOX_INSERT_FILES)
        except TimeoutException:
            time.sleep(1)
            checkbox_insert_files = self.elements_are_visible(self.Locators.CHECKBOX_INSERT_FILES)
        for n in checkbox_insert_files:
            time.sleep(2)
            n.click()
        time.sleep(1)
        try:
            self.click_to_element(self.Locators.INPUT_SELECTED)
        except ElementClickInterceptedException:
            time.sleep(2)
            self.click_to_element(self.Locators.INPUT_SELECTED)
        typography_for_click = self.elements_is_present(self.Locators.BUTTON_TYPOGRAPHY)
        action = ActionChains(driver)
        action.click(typography_for_click)
        action.perform()
        self.element_is_visible(self.Locators.FOLDER_SAVE).send_keys("Контент 1")
        self.element_is_visible(self.Locators.INPUT_NAME_CONTENT).send_keys("NAME-"+str(random.randint(99, 999)))
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        """open vizard"""
        text_typography_content = self.element_is_visible(self.Locators.TEXT_TYPOGRAPHY_CONTENT).text
        assert text_typography_content == "Настройки публикации контента"
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nверсионность'
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        # self.click_to_element(self.Locators.BUTTON_SUBMIT)
        # self.click_to_element(self.Locators.BUTTON_SUBMIT)
        """change testing"""
        self.click_to_element(self.Locators.BUTTON_JUST_NOTIFY)
        self.click_to_element(self.Locators.TEXT_CONFIRM_READ)
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nверсионность\nтест'
        """text test tab check"""
        text_alert = "ALERT-"+str(random.randint(99, 999))
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        """add question step 10"""
        self.click_to_element(self.Locators.BUTTON_ADD_QUESTION)
        """check text and checkboxes step 10"""
        text_choose_question_for_test = self.element_is_visible(self.Locators.TEXT_CHOOSE_QUESTION_FOR_TEST).text
        assert text_choose_question_for_test == "Выберите вопросы для теста"
        list_checkboxes = self.elements_are_visible(self.Locators.LIST_CHECKBOXES)
        for n in list_checkboxes:
            attribute_class = n.get_attribute("class")
            assert attribute_class == "m-switch-box lms-question-bar__switch"
        time.sleep(1)
        self.click_to_element(self.Locators.ON_CHECKBOX_ALL_QUESTIONS)
        time.sleep(3)
        try:
            self.click_to_element(self.Locators.SVG_CLOSE_DELETED_WINDOW)
        except TimeoutException:
            time.sleep(3)
            self.click_to_element(self.Locators.SVG_CLOSE_DELETED_WINDOW)
        """check first position by index xpath dom and active tab"""
        tab_active = self.element_is_visible(self.Locators.TAB_ACTIVE).text
        assert tab_active == 'тест'
        time.sleep(1)
        try:
            questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        except TimeoutException:
            time.sleep(2)
            questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        assert questions_first_position_check == "Edit question"
        time.sleep(1)
        self.click_to_element(self.Locators.BUTTON_FINISH)
        time.sleep(6)
        self.click_to_element(self.Locators.EDIT_ARTICLE)
        time.sleep(1)
        # self.click_to_element(self.Locators.EDIT_ARTICLE)
        # self.element_is_visible(self.Locators.INPUT_NAME_STEP).send_keys("Edit")
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        except TimeoutException:
            time.sleep(2)
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        """go tu test tab"""
        # self.click_to_element(self.Locators.TEXTAREA_ALERT)
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys("One More" + text_alert)
        self.click_to_element(self.Locators.BUTTON_FINISH)
        # self.click_to_element(self.Locators.BUTTON_FINISH)
        # self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.QUESTIONS_FIRST_POSITION_CHECK)
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).clear()
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).send_keys("edit answer")
        self.click_to_element(self.Locators.BUTTON_EDIT_QUESTION_SAVE)
        self.click_to_element(self.Locators.BUTTON_GO_BACK)
        self.click_to_element(self.Locators.TEXT_GET_TESTED)
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nверсионность'
        #
        # list_tabs = self.elements_are_visible(self.Locators.LIST_TABS)
        # data_tabs = []
        # for n in list_tabs:
        #     value_text = n.text
        #     data_tabs.append(value_text)
        # assert ['поиск', 'версионность'] == data_tabs
        # self.element_is_visible(self.Locators.TEXTAREA_ALERT).clear()
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert+" new")
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.EDIT_ARTICLE)
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY)
        self.click_to_element(self.Locators.BUTTON_FINISH)
        time.sleep(1)
        try:
            self.click_to_element(self.Locators.BUTTON_JUST_NOTIFY)
        except ElementClickInterceptedException:
            time.sleep(3)
            self.click_to_element(self.Locators.BUTTON_JUST_NOTIFY)
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert)
        self.click_to_element(self.Locators.TEXT_CONFIRM_READ)
        """text test tab check"""
        list_tabs_test = self.elements_are_visible(self.Locators.LIST_TABS)
        data_tabs = []
        for n in list_tabs_test:
            value_text = n.text
            data_tabs.append(value_text)
        # print(data_tabs)
        assert ['поиск\nверсионность\nтест'] == data_tabs
        self.click_to_element(self.Locators.RADIOBUTTON_SMALL_CORRECT_CONTENT)
        """check tab text"""
        list_tabs = self.elements_are_visible(self.Locators.LIST_TABS)
        data_tabs = []
        for n in list_tabs:
            value_text = n.text
            data_tabs.append(value_text)
        assert ['поиск\nверсионность'] == data_tabs
        self.click_to_element(self.Locators.RADIOBUTTON_BIG_CORRECT_CONTENT)
        """text test tab check"""
        list_tabs_test = self.elements_are_visible(self.Locators.LIST_TABS)
        data_tabs = []
        for n in list_tabs_test:
            value_text = n.text
            data_tabs.append(value_text)
        assert ['поиск\nверсионность\nтест'] == data_tabs
        self.click_to_element(self.Locators.BUTTON_FINISH)
        """check position"""
        # questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        # assert questions_first_position_check == "Edit question"
        # questions_first_position_check = self.elements_are_visible(self.Locators.LIST_QUESTIONS_POSITION)
        # dada_name_text = []
        # for n in questions_first_position_check:
        #     text_name_question = n.text
        #     dada_name_text.append(text_name_question)
        # print(dada_name_text)
        # assert dada_name_text[1] == "Edit question"
        """del question from test"""
        # del1
        self.click_to_element(self.Locators.SVG_DEL_FIRST_QUESTION)
        self.click_to_element(self.Locators.CONFIRM_BUTTON_DELETE)
        # del2
        self.click_to_element(self.Locators.SVG_DEL_FIRST_QUESTION)
        self.click_to_element(self.Locators.CONFIRM_BUTTON_DELETE)

    def add_edit_question_template(self, driver):
        person = generated_person()
        first_name = person.first_name
        text = "Hello"
        # self.input_in_my_project(driver)
        try:
            self.click_to_element(self.Locators.CREATE_BUTTON)
        except StaleElementReferenceException:
            time.sleep(2)
            self.click_to_element(self.Locators.CREATE_BUTTON)
        self.click_to_element(self.Locators.CREATE_TEMPLATES)
        """create new template"""
        self.click_to_element(self.Locators.NEW_TEMPLATE)
        self.click_to_element(self.Locators.ADD_FIELD_BUTTON)
        self.click_to_element(self.Locators.LIST_OF_FIELDS_1)
        self.element_is_visible(self.Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.click_to_element(self.Locators.SAVE_TEMPLATES)
        name_templates = "for download file testing" + str(random.randint(999, 99999))
        self.element_is_visible(self.Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name_templates)
        self.click_to_element(self.Locators.SAVE_TEMPLATES_CHANGE)
        self.click_to_element(self.Locators.FINISH_BUTTON_SCRIPT)
        time.sleep(2)
        self.scroll_wizard_template(name_templates, driver)
        # try:
        #     templates_download = self.browser.find_element(By.XPATH, f"//span[text()='{name_templates}']")
        # except (InvalidSelectorException, NoSuchElementException):
        #     # прокрутка окна вниз на 100 пикселей
        #     action = ActionChains(driver)
        #     scroller = self.element_is_visible(self.Locators.MODAL_WINDOW_SCROLLER)
        #     action.drag_and_drop_by_offset(scroller, "0", "300")
        #     action.perform()
        #     time.sleep(1)
            # templates_download = self.browser.find_element(By.XPATH, f"//span[text()='{name_templates}']")

        # templates_download.click()
        try:
            self.click_to_element(self.Locators.TEXT_AREA_ARTICLE)
        except TimeoutException:
            time.sleep(10)
            self.click_to_element(self.Locators.TEXT_AREA_ARTICLE)
        self.click_to_element(self.Locators.DROPDOWN)
        frame = self.elements_is_present(self.Locators.FRAME)
        self.switch_to_frame(frame)
        self.click_to_element(self.Locators.DROP_DOWN_FILES)
        self.switch_out_frame()
        self.download_files_is_visible()
        self.check_add_question_func(driver)
        # time.sleep(1)
        # self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(path)

    def add_edit_question_script(self, driver):
        # self.input_in_my_project(self.driver)
        try:
            self.click_to_element(self.Locators.CREATE_BUTTON)
        except StaleElementReferenceException:
            time.sleep(3)
            self.click_to_element(self.Locators.CREATE_BUTTON)
        self.click_to_element(self.Locators.CREATE_SCRIPT)
        self.element_is_visible(self.Locators.NAME_OF_STEP_SCRIPT).send_keys("NAME_SCRIPT-"+str(random.randint(99, 999)))
        time.sleep(3)
        try:
            self.element_is_visible(self.Locators.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")
        except ElementNotInteractableException:
            time.sleep(2)
            self.driver.refresh()
            time.sleep(5)
            self.element_is_visible(self.Locators.NAME_OF_STEP_SCRIPT).send_keys(
                "NAME_SCRIPT-" + str(random.randint(99, 999)))
            self.element_is_visible(self.Locators.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")
        self.click_to_element(self.Locators.ADD_STEP)
        try:
            self.element_is_visible(self.Locators.INPUT_NAME_STEP).send_keys("name_step-"+str(random.randint(99, 999)))
        except TimeoutException:
            time.sleep(3)
            self.element_is_visible(self.Locators.INPUT_NAME_STEP).send_keys("name_step-"+str(random.randint(99, 999)))
        self.element_is_visible(self.Locators.DROPDOWN_STEP).send_keys("Сценарий завершён")
        try:
            self.click_to_element(self.Locators.TEXT_AREA)
        except TimeoutException:
            time.sleep(5)
            self.click_to_element(self.Locators.TEXT_AREA)
        self.click_to_element(self.Locators.DROPDOWN)
        frame = self.elements_is_present(self.Locators.FRAME)
        self.switch_to_frame(frame)
        self.click_to_element(self.Locators.DROP_DOWN_FILES)
        self.switch_out_frame()
        time.sleep(1)
        """for visible"""
        self.download_files_is_visible()
        path1 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        data_path = [path1, path2]
        for n in data_path:
            self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(n)
        time.sleep(5)
        checkbox_insert_files = self.elements_are_visible(self.Locators.CHECKBOX_INSERT_FILES)
        for n in checkbox_insert_files:
            time.sleep(0.5)
            n.click()
        try:
            self.click_to_element(self.Locators.INPUT_SELECTED)
        except ElementClickInterceptedException:
            time.sleep(2)
            self.click_to_element(self.Locators.INPUT_SELECTED)
        typography_for_click = self.elements_is_present(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        action = ActionChains(driver)
        action.click(typography_for_click)
        action.perform()
        """open vizard"""
        try:
            text_typography_content = self.element_is_visible(self.Locators.TEXT_TYPOGRAPHY_CONTENT, timeout=2).text
        except TimeoutException:
            time.sleep(5)
            text_typography_content = self.element_is_visible(self.Locators.TEXT_TYPOGRAPHY_CONTENT).text
        assert text_typography_content == "Настройки публикации контента"
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nдоступ\nверсионность'
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        # self.click_to_element(self.Locators.BUTTON_SUBMIT)
        """change testing"""
        self.click_to_element(self.Locators.BUTTON_JUST_NOTIFY)
        self.click_to_element(self.Locators.TEXT_CONFIRM_READ)
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nдоступ\nверсионность\nтест'
        text_alert = "ALERT-" + str(random.randint(99, 999))
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert)
        self.click_to_element(self.Locators.BUTTON_SUBMIT)
        """add question"""
        self.click_to_element(self.Locators.BUTTON_ADD_QUESTION)
        """check text and checkboxes"""
        text_choose_question_for_test = self.element_is_visible(self.Locators.TEXT_CHOOSE_QUESTION_FOR_TEST).text
        assert text_choose_question_for_test == "Выберите вопросы для теста"
        list_checkboxes = self.elements_are_visible(self.Locators.LIST_CHECKBOXES)
        for n in list_checkboxes:
            attribute_class = n.get_attribute("class")
            assert attribute_class == "m-switch-box lms-question-bar__switch"
        self.click_to_element(self.Locators.ON_CHECKBOX_ALL_QUESTIONS)
        time.sleep(1)
        self.click_to_element(self.Locators.SVG_CLOSE_DELETED_WINDOW)
        """check first position by index xpath dom and active tab"""
        tab_active = self.element_is_visible(self.Locators.TAB_ACTIVE).text
        assert tab_active == 'тест'
        try:
            questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        except TimeoutException:
            time.sleep(2)
            questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        assert questions_first_position_check == "Edit question"
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.EDIT_ARTICLE)
        self.element_is_visible(self.Locators.INPUT_NAME_STEP).send_keys("Edit")
        try:
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        except TimeoutException:
            time.sleep(2)
            self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        """go tu test tab"""
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_ALERT).send_keys("Alert")
        self.click_to_element(self.Locators.BUTTON_FINISH)
        # self.click_to_element(self.Locators.BUTTON_FINISH)
        # self.click_to_element(self.Locators.BUTTON_FINISH)
        # self.click_to_element(self.Locators.BUTTON_FINISH)
        """check position"""
        try:
            self.click_to_element(self.Locators.QUESTIONS_FIRST_POSITION_CHECK)
        except StaleElementReferenceException:
            time.sleep(3)
            self.click_to_element(self.Locators.QUESTIONS_FIRST_POSITION_CHECK)
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).clear()
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).send_keys("edit answer")
        self.click_to_element(self.Locators.BUTTON_EDIT_QUESTION_SAVE)
        self.click_to_element(self.Locators.BUTTON_GO_BACK)
        self.click_to_element(self.Locators.TEXT_GET_TESTED)
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nдоступ\nверсионность'
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert + " new")
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.EDIT_ARTICLE)
        self.click_to_element(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        self.click_to_element(self.Locators.BUTTON_FINISH)
        self.click_to_element(self.Locators.BUTTON_FINISH)
        try:
            self.click_to_element(self.Locators.BUTTON_JUST_NOTIFY)
        except ElementClickInterceptedException:
            time.sleep(3)
            self.click_to_element(self.Locators.BUTTON_JUST_NOTIFY)
        self.click_to_element(self.Locators.TEXT_CONFIRM_READ)
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nдоступ\nверсионность\nтест'
        self.click_to_element(self.Locators.RADIOBUTTON_SMALL_CORRECT_CONTENT)
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nдоступ\nверсионность'
        self.click_to_element(self.Locators.RADIOBUTTON_BIG_CORRECT_CONTENT)
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nдоступ\nверсионность\nтест'
        self.click_to_element(self.Locators.BUTTON_FINISH)
        """check position"""
        """del question from test"""
        # del1
        self.click_to_element(self.Locators.SVG_DEL_FIRST_QUESTION)
        self.click_to_element(self.Locators.CONFIRM_BUTTON_DELETE)
        # del2
        self.click_to_element(self.Locators.SVG_DEL_FIRST_QUESTION)
        self.click_to_element(self.Locators.CONFIRM_BUTTON_DELETE)
        # """del all question"""
        # self.click_to_element(self.Locators.BUTTON_ADD_QUESTION)
        # list_delete = self.elements_are_visible(self.Locators.SVG_DEL_QUESTION)
        # for n in list_delete:
        #     time.sleep(0.5)
        #     n.click()
        #     self.click_to_element(self.Locators.SVG_DEL_QUESTION_CONFIRM)


























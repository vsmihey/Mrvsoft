import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from conftest import driver
from generator.generator import generated_person
from locators.topic_database_locators import CreateTopicDatabaseLocators
from pages.base_page import BasePage
from pages.data_login_password import url


class CreateTopicDatabase(BasePage):
    Locators = CreateTopicDatabaseLocators

    def add_topic_database(self, driver):
        """ADD TOPIC AND CHECK TEXTS, LEN INPUT NAME"""
        self.input_in_my_project(driver)
        self.element_is_visible(self.Locators.LEARNING_BUTTON).click()
        self.element_is_visible(self.Locators.TAB_ALL_COURSES).click()
        self.element_is_visible(self.Locators.DATABASE_OF_QUESTIONS).click()
        """check text open form"""
        text_database_of_questions = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTIONS).text
        assert text_database_of_questions == "База вопросов"
        try:
            text_not_questions_now = self.element_is_visible(self.Locators.TEXT_NOT_QUESTIONS_NOW, timeout=2).text
            assert text_not_questions_now == "В этом проекте пока нет вопросов. Создайте структуру тем для его размещения"
        except TimeoutException:
            try:
                self.element_is_visible(self.Locators.BUTTON_QUESTION_ADD, timeout=2).click()
            except TimeoutException:
                self.element_is_visible(self.Locators.SVG_DEL_QUESTION).click()
                self.element_is_visible(self.Locators.SVG_DEL_QUESTION_CONFIRM).click()
                self.element_is_visible(self.Locators.BUTTON_QUESTION_ADD).click()
            self.element_is_visible(self.Locators.BUTTON_CHANGE_QUESTION).click()
            self.delete_created_topics()
            self.element_is_visible(self.Locators.SVG_CLOSE_DELETED_WINDOW).click()
            self.element_is_visible(self.Locators.SVG_CLOSE_DELETED_WINDOW).click()
        button_add_topic = self.element_is_visible(self.Locators.BUTTON_ADD_TOPIC).text
        assert button_add_topic == 'Создать темы'
        self.element_is_visible(self.Locators.BUTTON_ADD_TOPIC).click()
        """input name topic and check len"""
        element = self.element_is_visible(self.Locators.INPUT_NAME_TOPIC)
        name_content, get_name = self.check_len_name(driver, element, n=65)
        self.element_is_visible(self.Locators.INPUT_NAME_TOPIC).send_keys(name_content)
        assert len(get_name) == 64
        """create topic"""
        self.element_is_visible(self.Locators.BUTTON_CREATE_TOPIC).click()
        """check text open window"""
        text_rule_structure = self.element_is_visible(self.Locators.TEXT_RULE_STRUCTURE).text
        assert text_rule_structure == "Управление структурой"
        text_created_topic_name = self.element_is_visible(self.Locators.TEXT_CREATED_TOPIC_NAME).text
        assert text_created_topic_name == get_name
        button_new_topic = self.element_is_visible(self.Locators.BUTTON_NEW_TOPIC).text
        assert button_new_topic == "Новая тема"
        self.create_new_topic()
        """close window created topics"""
        self.element_is_visible(self.Locators.SVG_CLOSE_DELETED_WINDOW).click()
        self.create_new_question(driver)
        # self.delete_created_topics()

    def create_new_topic(self):
        """CREATE NEW TOPICS"""
        person = generated_person()
        for i in range(21):
            self.element_is_visible(self.Locators.BUTTON_NEW_TOPIC).click()
            self.element_is_visible(self.Locators.INPUT_NAME_TOPIC).send_keys(person.first_name + str(random.randint(99, 999)))
            self.element_is_visible(self.Locators.BUTTON_CREATE_TOPIC).click()

    def delete_created_topics(self):
        """DELETE CREATED TOPICS"""
        list_created_topics = self.elements_are_visible(self.Locators.LIST_CREATED_TOPICS)
        for n in list_created_topics:
            time.sleep(1)
            n.click()
            try:
                self.element_is_visible(self.Locators.BUTTON_DELETE_TOPIC).click()
            except TimeoutException:
                time.sleep(2)
                self.element_is_visible(self.Locators.BUTTON_DELETE_TOPIC).click()
            self.element_is_visible(self.Locators.BUTTON_CONFIRM_DELETE_TOPIC).click()

    def create_new_question(self, driver):
        """CREATE AN CHECK NEW QUESTION"""
        """check open form"""
        text_of_question = "Здесь должен быть текст вопроса"+str(random.randint(99, 999))
        answer_of_question = "Ответ на вопрпос"+str(random.randint(99, 999))
        text_database_of_question_head = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTION_HEAD).text
        assert text_database_of_question_head == "База вопросов"
        text_database_of_question = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTION).text
        assert text_database_of_question == "В этом проекте пока нет вопросов. Вы можете это исправить"
        self.element_is_visible(self.Locators.BUTTON_QUESTION_ADD).click()
        text_new_question = self.element_is_visible(self.Locators.TEXT_NEW_QUESTION).text
        assert text_new_question == "Новый вопрос"
        """fill in the placeholder"""
        self.element_is_visible(self.Locators.TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION).send_keys(text_of_question)
        """dropdown tipe"""
        self.element_is_visible(self.Locators.DROPDOWN_TIPE_OF_QUESTION).click()
        self.element_is_visible(self.Locators.DROPDOWN_TIPE_OF_QUESTION).send_keys(Keys.ARROW_DOWN)
        self.element_is_visible(self.Locators.DROPDOWN_TIPE_OF_QUESTION).send_keys(Keys.RETURN)
        """dropdown topic"""
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).click()
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).send_keys(Keys.ARROW_DOWN)
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).send_keys(Keys.RETURN)
        """answer"""
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).send_keys(answer_of_question)
        self.element_is_visible(self.Locators.ANSWER_CHECKBOX).click()
        self.element_is_visible(self.Locators.BUTTON_CREATE_QUESTION).click()
        """created question window"""
        text_database_of_question_head = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTION_HEAD).text
        assert text_database_of_question_head == "База вопросов"
        text_created_new_question = self.element_is_visible(self.Locators.TEXT_CREATED_NEW_QUESTION).text
        assert text_created_new_question == text_of_question
        self.element_is_visible(self.Locators.SVG_SLIDERS).click()
        text_modal_window_topics = self.element_is_visible(self.Locators.TEXT_MODAL_WINDOW_TOPICS).text
        assert text_modal_window_topics == "Темы"
        self.element_is_visible(self.Locators.CHANGE_TOPICS_WINDOW).click()
        text_rule_structure = self.element_is_visible(self.Locators.TEXT_RULE_STRUCTURE).text
        assert text_rule_structure == "Управление структурой"
        """check all created topics"""
        text_first_topic = self.element_is_visible(self.Locators.TEXT_FIRST_TOPIC).text
        len_text_first_topic = len(text_first_topic)
        assert len_text_first_topic == 64
        self.element_is_visible(self.Locators.TEXT_FIRST_TOPIC).click()
        self.element_is_visible(self.Locators.TEXT_PLACEHOLDER_INPUT_NAME_TOPIC).clear()
        self.element_is_visible(self.Locators.TEXT_PLACEHOLDER_INPUT_NAME_TOPIC).send_keys("THE SAME NAME")
        self.element_is_visible(self.Locators.BUTTON_SAVE_TOPIC).click()
        """the same name create"""
        self.element_is_visible(self.Locators.BUTTON_NEW_TOPIC).click()
        self.element_is_visible(self.Locators.TEXT_PLACEHOLDER_INPUT_NAME_TOPIC).send_keys("THE SAME NAME")
        self.element_is_visible(self.Locators.BUTTON_CREATE_TOPIC_CONFIRM).click()
        """check count the same name, locators: name_1 and name_2 contains text THE SAME NAME """
        data_same_name = []
        name_1 = self.element_is_visible(self.Locators.NAME_1)
        data_same_name.append(name_1)
        name_2 = self.elements_is_present(self.Locators.NAME_2)
        data_same_name.append(name_2)
        self.go_to_element(name_2)
        """check name las topic"""
        self.element_is_visible(self.Locators.NAME_2).click()
        name_2_value = self.element_is_visible(self.Locators.TEXT_PLACEHOLDER_INPUT_NAME_TOPIC).get_attribute("value")
        assert name_2_value == "THE SAME NAME"
        print(len(data_same_name))
        assert len(data_same_name) == 2
        self.element_is_visible(self.Locators.BUTTON_SAVE_TOPIC).click()
        try:
            self.element_is_visible(self.Locators.SVG_CLOSE_DELETED_WINDOW).click()
        except TimeoutException:
            time.sleep(3)
            self.element_is_visible(self.Locators.SVG_CLOSE_DELETED_WINDOW).click()
        """delete question"""
        self.element_is_visible(self.Locators.SVG_DEL_QUESTION).click()
        self.element_is_visible(self.Locators.SVG_DEL_QUESTION_CONFIRM).click()

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
        self.input_in_my_project(driver)
        self.element_is_visible(self.Locators.LEARNING_BUTTON).click()
        self.element_is_visible(self.Locators.TAB_ALL_COURSES).click()
        self.element_is_visible(self.Locators.DATABASE_OF_QUESTIONS).click()
        """check text and button"""
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
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).click()
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
        self.element_is_visible(self.Locators.ANSWER_CHECKBOX).click()
        self.element_is_visible(self.Locators.BUTTON_CREATE_QUESTION).click()
        """check open modal window"""
        text_database_of_question_head = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTION_HEAD).text
        assert text_database_of_question_head == "База вопросов"
        text_created_new_question = self.element_is_visible(self.Locators.TEXT_CREATED_NEW_QUESTION).text
        assert text_created_new_question == name_content

    def edit_question(self):
        self.element_is_visible(self.Locators.SVG_EDIT_QUESTION).click()
        self.check_text_questions()
        self.element_is_visible(self.Locators.TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION).clear()
        self.element_is_visible(self.Locators.TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION).send_keys("Edit question")
        self.element_is_visible(self.Locators.BUTTON_EDIT_QUESTION_SAVE).click()
        """check text edit question"""
        text_edit_new_question = self.element_is_visible(self.Locators.TEXT_CREATED_NEW_QUESTION).text
        assert text_edit_new_question == "Edit question"
        """add new question 2 option questions"""
        self.element_is_visible(self.Locators.BUTTON_NEW_QUESTION).click()
        """dropdown topic"""
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).click()
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).send_keys(Keys.ARROW_DOWN)
        self.element_is_visible(self.Locators.DROPDOWN_TOPIC).send_keys(Keys.RETURN)
        """input random text"""
        element = self.element_is_visible(self.Locators.TEXTAREA_PLACEHOLDER_INPUT_NAME_QUESTION)
        name_content = self.input_random_symbols(element, 20)
        """add questions options answers"""
        element = self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX)
        self.input_random_symbols(element, 5)
        self.element_is_visible(self.Locators.BUTTON_QUESTION_ADD).click()
        self.element_is_visible(self.Locators.NEW_ANSWER_PLACEHOLDER).send_keys("adding answer")
        list_checkboxes = self.elements_are_visible(self.Locators.ANSWER_CHECKBOX_1_1)
        for n in list_checkboxes:
            n.click()
        self.element_is_visible(self.Locators.BUTTON_CREATE_QUESTION).click()
        try:
            text_check_result_created_questions_second = self.element_is_visible(
                self.Locators.TEXT_CHECK_RESULT_CREATED_QUESTIONS_SECOND, timeout=3).text
            assert text_check_result_created_questions_second == name_content
        except AssertionError:
            self.element_is_visible(self.Locators.LIST_QUESTIONS).click()
            text_check_result_created_questions_second = self.element_is_visible(
                self.Locators.TEXT_CHECK_RESULT_CREATED_QUESTIONS_SECOND).text
            assert text_check_result_created_questions_second == name_content
        text_check_result_created_questions_first = self.element_is_visible(
            self.Locators.TEXT_CHECK_RESULT_CREATED_QUESTIONS_FIRST).text
        assert text_check_result_created_questions_first == "Edit question"
        """delete all questions"""
        list_delete = self.elements_are_visible(self.Locators.SVG_DEL_QUESTION)
        for n in list_delete:
            n.click()
            self.element_is_visible(self.Locators.SVG_DEL_QUESTION_CONFIRM).click()
















































        time.sleep(5)




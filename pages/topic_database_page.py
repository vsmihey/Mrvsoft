import pathlib
import random
import time
from pathlib import Path

from selenium.common import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException, WebDriverException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from conftest import driver
from generator.generator import generated_person, generated_file
from locators.locators_topic_database import CreateTopicDatabaseLocators
from pages import article_page
from pages.authorisation_page import Authorisation
from pages.base_page import BasePage
from pages.data_login_password import url


class CreateTopicDatabase(Authorisation, BasePage):
    Locators = CreateTopicDatabaseLocators

    def add_topic_database(self, driver):
        """ADD TOPIC AND CHECK TEXTS, LEN INPUT NAME"""
        # self.input_in_my_project(driver)
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
                time.sleep(2)
                list_question = self.elements_are_visible(self.Locators.SVG_DEL_QUESTION)
                for n in list_question:
                    time.sleep(1)
                    n.click()
                    time.sleep(0.5)
                    self.element_is_visible(self.Locators.SVG_DEL_QUESTION_CONFIRM).click()
                # try:
                #     self.element_is_visible(self.Locators.BUTTON_QUESTION_ADD, timeout=2).click()
                # except TimeoutException:
                #     time.sleep(2)
                #     self.element_is_visible(self.Locators.SVG_DEL_QUESTION).click()
                #     time.sleep(1)
                #     self.element_is_visible(self.Locators.SVG_DEL_QUESTION_CONFIRM).click()
                #     self.element_is_visible(self.Locators.BUTTON_QUESTION_ADD, timeout=2).click()
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
                time.sleep(3)
                n.click()
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
        time.sleep(1)
        try:
            name_2 = self.elements_is_present(self.Locators.NAME_2)
        except TimeoutException:
            time.sleep(3)
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
                    self.element_is_visible(self.Locators.SVG_DEL_QUESTION_CONFIRM).click()
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
        # list_delete = self.elements_are_visible(self.Locators.SVG_DEL_QUESTION)
        # for n in list_delete:
        #     n.click()
        #     self.element_is_visible(self.Locators.SVG_DEL_QUESTION_CONFIRM).click()

    def add_edit_question_article(self, driver):
        """ADD AND EDIT QUESTION IN ARTICLE
        В БАЗЕ ДОЛЖНЫ БЫТЬ ВОПРОСЫ С ПРЕДЫДУЩЕГО ТЕСТА"""
        person = generated_person()
        first_name = person.first_name
        text = "Hello"
        self.input_in_my_project(driver)
        # data_files = generated_file()
        """upload media"""
        try:
            self.element_is_visible(self.Locators.CREATE_BUTTON, timeout=1).click()
        except StaleElementReferenceException:
            time.sleep(2)
            self.element_is_visible(self.Locators.CREATE_BUTTON).click()
        self.element_is_visible(self.Locators.CREATE_ARTICLE).click()
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
        try:
            self.element_is_visible(self.Locators.TEXT_AREA_ARTICLE).send_keys(text)
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(self.Locators.TEXT_AREA_ARTICLE).send_keys(text)
        try:
            self.elements_is_present(self.Locators.UPLOAD_MEDIA, timeout=2).click()
        except TimeoutException:
            time.sleep(5)
            self.elements_is_present(self.Locators.UPLOAD_MEDIA).click()
        """input is visible for load files"""
        self.driver.execute_script(
            """document.querySelector(".popup__footer.file-manager__foot.file-manager--hidden").removeAttribute('class')""")
        self.driver.execute_script(
            """document.querySelector("form[enctype='multipart/form-data']").removeAttribute('style')""")
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
            self.element_is_visible(self.Locators.INPUT_SELECTED).click()
        except ElementClickInterceptedException:
            time.sleep(10)
            self.element_is_visible(self.Locators.INPUT_SELECTED).click()
        self.element_is_visible(self.Locators.DIRECT_FOLDER_NAME).send_keys("Контент")
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        """open vizard"""
        text_typography_content = self.element_is_visible(self.Locators.TEXT_TYPOGRAPHY_CONTENT).text
        assert text_typography_content == "Настройки публикации контента"
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность'
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """change testing"""
        self.element_is_visible(self.Locators.BUTTON_JUST_NOTIFY).click()
        self.element_is_visible(self.Locators.TEXT_CONFIRM_READ).click()
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность\nтест'
        # self.element_is_visible(self.Locators.TEXT_TAB_TEST).is_displayed()
        text_alert = "ALERT-" + str(random.randint(99, 999))
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert)
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """add question"""
        self.element_is_visible(self.Locators.BUTTON_ADD_QUESTION).click()
        """check text and checkboxes"""
        text_choose_question_for_test = self.element_is_visible(self.Locators.TEXT_CHOOSE_QUESTION_FOR_TEST).text
        assert text_choose_question_for_test == "Выберите вопросы для теста"
        list_checkboxes = self.elements_are_visible(self.Locators.LIST_CHECKBOXES)
        for n in list_checkboxes:
            attribute_class = n.get_attribute("class")
            assert attribute_class == "m-switch-box lms-question-bar__switch"
        # assert text_choose_question_for_test == "Выберите вопросы для теста"
        self.element_is_visible(self.Locators.ON_CHECKBOX_ALL_QUESTIONS).click()
        time.sleep(1)
        self.element_is_visible(self.Locators.SVG_CLOSE_DELETED_WINDOW).click()
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
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.EDIT_ARTICLE).click()
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        """go tu test tab"""
        # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert + " new")
        self.element_is_visible(self.Locators.BUTTON_CONTINUE).click()
        # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        # time.sleep(3)
        # self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert + " new")
        # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        """check position"""
        try:
            self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).click()
        except TimeoutException:
            time.sleep(3)
            self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).click()
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).clear()
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).send_keys("edit answer")
        self.element_is_visible(self.Locators.BUTTON_EDIT_QUESTION_SAVE).click()
        self.element_is_visible(self.Locators.BUTTON_GO_BACK).click()
        self.element_is_visible(self.Locators.TEXT_GET_TESTED).click()
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность'
        # self.element_is_visible(self.Locators.TEXTAREA_ALERT).clear()
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert + " new")
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.EDIT_ARTICLE).click()
        try:
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY, timeout=2).click()
        except TimeoutException:
            time.sleep(2)
            self.element_is_visible(self.Locators.BUTTON_DELETE_DRAFT).click()
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.BUTTON_JUST_NOTIFY).click()
        self.element_is_visible(self.Locators.TEXT_CONFIRM_READ).click()
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность\nтест'
        self.element_is_visible(self.Locators.RADIOBUTTON_SMALL_CORRECT_CONTENT).click()
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность'
        self.element_is_visible(self.Locators.RADIOBUTTON_BIG_CORRECT_CONTENT).click()
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'навигация\nпоиск\nдоступ\nверсионность\nтест'
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        """check position"""
        """del question from test"""
        # del1
        self.element_is_visible(self.Locators.SVG_DEL_FIRST_QUESTION).click()
        self.element_is_visible(self.Locators.CONFIRM_BUTTON_DELETE).click()
        # del2
        self.element_is_visible(self.Locators.SVG_DEL_FIRST_QUESTION).click()
        self.element_is_visible(self.Locators.CONFIRM_BUTTON_DELETE).click()

    def check_add_question_func(self):
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
            self.element_is_visible(self.Locators.INPUT_SELECTED).click()
        except ElementClickInterceptedException:
            time.sleep(2)
            self.element_is_visible(self.Locators.INPUT_SELECTED).click()
        typography_for_click = self.elements_is_present(self.Locators.BUTTON_TYPOGRAPHY)
        action = ActionChains(self.driver)
        action.click(typography_for_click)
        action.perform()
        self.element_is_visible(self.Locators.FOLDER_SAVE).send_keys("Контент 1")
        self.element_is_visible(self.Locators.INPUT_NAME_CONTENT).send_keys("NAME-"+str(random.randint(99, 999)))
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        """open vizard"""
        text_typography_content = self.element_is_visible(self.Locators.TEXT_TYPOGRAPHY_CONTENT).text
        assert text_typography_content == "Настройки публикации контента"
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nверсионность'
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        # self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        # self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """change testing"""
        self.element_is_visible(self.Locators.BUTTON_JUST_NOTIFY).click()
        self.element_is_visible(self.Locators.TEXT_CONFIRM_READ).click()
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nверсионность\nтест'
        """text test tab check"""
        text_alert = "ALERT-"+str(random.randint(99, 999))
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert)
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """add question step 10"""
        self.element_is_visible(self.Locators.BUTTON_ADD_QUESTION).click()
        """check text and checkboxes step 10"""
        text_choose_question_for_test = self.element_is_visible(self.Locators.TEXT_CHOOSE_QUESTION_FOR_TEST).text
        assert text_choose_question_for_test == "Выберите вопросы для теста"
        list_checkboxes = self.elements_are_visible(self.Locators.LIST_CHECKBOXES)
        for n in list_checkboxes:
            attribute_class = n.get_attribute("class")
            assert attribute_class == "m-switch-box lms-question-bar__switch"
        self.element_is_visible(self.Locators.ON_CHECKBOX_ALL_QUESTIONS).click()
        time.sleep(1)
        self.element_is_visible(self.Locators.SVG_CLOSE_DELETED_WINDOW).click()
        """check first position by index xpath dom and active tab"""
        tab_active = self.element_is_visible(self.Locators.TAB_ACTIVE).text
        assert tab_active == 'тест'
        try:
            questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        except TimeoutException:
            time.sleep(2)
            questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        assert questions_first_position_check == "Edit question"




        """-------------------"""
        #
        # # time.sleep(5)
        # # """change position move drag and drop"""
        # # f = open("script.js", "r")
        # # javascript = f.read()
        # # f.close()
        # # target = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION)
        # # source = self.element_is_visible(self.Locators.QUESTIONS_SECOND_POSITION)
        # # driver.execute_script(javascript, source, target)
        # # time.sleep(10)
        # # action = ActionChains(self.driver)
        # # questions_second_position = self.element_is_visible(self.Locators.QUESTIONS_SECOND_POSITION_CHECK)
        # # # action.drag_and_drop(questions_first_position_check, questions_second_position).perform()
        # # # self.action_drag_and_drop_by_offset(questions_second_position, 0, 8)
        # # # action.click_and_hold(questions_first_position_check).move_to_element(questions_second_position).release().perform()
        # "step 14"
        # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        # "step 15"
        # self.element_is_visible(self.Locators.EDIT_ARTICLE).click()
        # "step 16"
        # self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        # """go tu test tab"""
        # # time.sleep(5)
        # self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert + " new")
        # """change testing"""
        # # self.element_is_visible(self.Locators.BUTTON_JUST_NOTIFY).click()
        # # self.element_is_visible(self.Locators.TEXT_CONFIRM_READ).click()
        # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        # # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        # # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        # # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        # """check position"""
        # # questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        # # assert questions_first_position_check == "Edit question"
        # # questions_first_position_check = self.elements_are_visible(self.Locators.LIST_QUESTIONS_POSITION)
        # # dada_name_text = []
        # # for n in questions_first_position_check:
        # #     text_name_question = n.text
        # #     dada_name_text.append(text_name_question)
        # # print(dada_name_text)
        # # assert dada_name_text[0] == "Edit question"
        #
        time.sleep(1)
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        time.sleep(6)
        self.element_is_visible(self.Locators.EDIT_ARTICLE).click()
        time.sleep(1)
        # self.element_is_visible(self.Locators.EDIT_ARTICLE).click()
        # self.element_is_visible(self.Locators.INPUT_NAME_STEP).send_keys("Edit")

        try:
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT).click()
        except TimeoutException:
            time.sleep(2)
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT).click()
        """go tu test tab"""
        # self.element_is_visible(self.Locators.TEXTAREA_ALERT).click()
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys("One More" + text_alert)


        """-----------------BUG---------------------------"""


        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).click()
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).clear()
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).send_keys("edit answer")
        self.element_is_visible(self.Locators.BUTTON_EDIT_QUESTION_SAVE).click()
        self.element_is_visible(self.Locators.BUTTON_GO_BACK).click()
        self.element_is_visible(self.Locators.TEXT_GET_TESTED).click()
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
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.EDIT_ARTICLE).click()
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.BUTTON_JUST_NOTIFY).click()
        self.element_is_visible(self.Locators.TEXT_CONFIRM_READ).click()
        """text test tab check"""
        list_tabs_test = self.elements_are_visible(self.Locators.LIST_TABS)
        data_tabs = []
        for n in list_tabs_test:
            value_text = n.text
            data_tabs.append(value_text)
        assert ['поиск', 'версионность', 'тест'] == data_tabs
        self.element_is_visible(self.Locators.RADIOBUTTON_SMALL_CORRECT_CONTENT).click()
        """check tab text"""
        list_tabs = self.elements_are_visible(self.Locators.LIST_TABS)
        data_tabs = []
        for n in list_tabs:
            value_text = n.text
            data_tabs.append(value_text)
        assert ['поиск', 'версионность'] == data_tabs
        self.element_is_visible(self.Locators.RADIOBUTTON_BIG_CORRECT_CONTENT).click()
        """text test tab check"""
        list_tabs_test = self.elements_are_visible(self.Locators.LIST_TABS)
        data_tabs = []
        for n in list_tabs_test:
            value_text = n.text
            data_tabs.append(value_text)
        assert ['поиск', 'версионность', 'тест'] == data_tabs
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
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
        self.element_is_visible(self.Locators.SVG_DEL_FIRST_QUESTION).click()
        self.element_is_visible(self.Locators.CONFIRM_BUTTON_DELETE).click()
        # del2
        self.element_is_visible(self.Locators.SVG_DEL_FIRST_QUESTION).click()
        self.element_is_visible(self.Locators.CONFIRM_BUTTON_DELETE).click()

    def add_edit_question_template(self):
        person = generated_person()
        first_name = person.first_name
        text = "Hello"
        self.input_in_my_project(driver)
        try:
            self.element_is_visible(self.Locators.CREATE_BUTTON).click()
        except StaleElementReferenceException:
            time.sleep(2)
            self.element_is_visible(self.Locators.CREATE_BUTTON).click()
        self.element_is_visible(self.Locators.CREATE_TEMPLATES).click()
        """create new template"""
        self.element_is_visible(self.Locators.NEW_TEMPLATE).click()
        self.element_is_visible(self.Locators.ADD_FIELD_BUTTON).click()
        self.element_is_visible(self.Locators.LIST_OF_FIELDS_1).click()
        self.element_is_visible(self.Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(self.Locators.SAVE_TEMPLATES).click()
        name_templates = "for download file testing" + str(random.randint(999, 99999))
        self.element_is_visible(self.Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name_templates)
        self.element_is_visible(self.Locators.SAVE_TEMPLATES_CHANGE).click()
        self.element_is_visible(self.Locators.FINISH_BUTTON_SCRIPT).click()
        time.sleep(2)
        templates_download = self.driver.find_element(By.XPATH, f"//div[text()='{name_templates}']")
        templates_download.click()
        try:
            self.element_is_visible(self.Locators.TEXT_AREA_ARTICLE).click()
        except TimeoutException:
            time.sleep(10)
            self.element_is_visible(self.Locators.TEXT_AREA_ARTICLE).click()
        self.element_is_visible(self.Locators.DROPDOWN).click()
        frame = self.elements_is_present(self.Locators.FRAME)
        self.switch_to_frame(frame)
        self.element_is_visible(self.Locators.DROP_DOWN_FILES).click()
        self.switch_out_frame()
        self.download_files_is_visible()
        self.check_add_question_func()
        # time.sleep(1)
        # self.element_is_visible(self.Locators.INPUT_INVISIBLE).send_keys(path)

    def add_edit_question_script(self):
        self.input_in_my_project(self.driver)
        try:
            self.element_is_visible(self.Locators.CREATE_BUTTON).click()
        except StaleElementReferenceException:
            time.sleep(3)
            self.element_is_visible(self.Locators.CREATE_BUTTON).click()
        self.element_is_visible(self.Locators.CREATE_SCRIPT).click()
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
        self.element_is_visible(self.Locators.ADD_STEP).click()
        self.element_is_visible(self.Locators.INPUT_NAME_STEP).send_keys("name_step-"+str(random.randint(99, 999)))
        self.element_is_visible(self.Locators.DROPDOWN_STEP).send_keys("Сценарий завершён")
        try:
            self.element_is_visible(self.Locators.TEXT_AREA).click()
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(self.Locators.TEXT_AREA).click()
        self.element_is_visible(self.Locators.DROPDOWN).click()
        frame = self.elements_is_present(self.Locators.FRAME)
        self.switch_to_frame(frame)
        self.element_is_visible(self.Locators.DROP_DOWN_FILES).click()
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
            self.element_is_visible(self.Locators.INPUT_SELECTED).click()
        except ElementClickInterceptedException:
            time.sleep(2)
            self.element_is_visible(self.Locators.INPUT_SELECTED).click()
        typography_for_click = self.elements_is_present(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        action = ActionChains(self.driver)
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
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        # self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """change testing"""
        self.element_is_visible(self.Locators.BUTTON_JUST_NOTIFY).click()
        self.element_is_visible(self.Locators.TEXT_CONFIRM_READ).click()
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nдоступ\nверсионность\nтест'
        text_alert = "ALERT-" + str(random.randint(99, 999))
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert)
        self.element_is_visible(self.Locators.BUTTON_SUBMIT).click()
        """add question"""
        self.element_is_visible(self.Locators.BUTTON_ADD_QUESTION).click()
        """check text and checkboxes"""
        text_choose_question_for_test = self.element_is_visible(self.Locators.TEXT_CHOOSE_QUESTION_FOR_TEST).text
        assert text_choose_question_for_test == "Выберите вопросы для теста"
        list_checkboxes = self.elements_are_visible(self.Locators.LIST_CHECKBOXES)
        for n in list_checkboxes:
            attribute_class = n.get_attribute("class")
            assert attribute_class == "m-switch-box lms-question-bar__switch"
        self.element_is_visible(self.Locators.ON_CHECKBOX_ALL_QUESTIONS).click()
        time.sleep(1)
        self.element_is_visible(self.Locators.SVG_CLOSE_DELETED_WINDOW).click()
        """check first position by index xpath dom and active tab"""
        tab_active = self.element_is_visible(self.Locators.TAB_ACTIVE).text
        assert tab_active == 'тест'
        try:
            questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        except TimeoutException:
            time.sleep(2)
            questions_first_position_check = self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).text
        assert questions_first_position_check == "Edit question"
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.EDIT_ARTICLE).click()
        self.element_is_visible(self.Locators.INPUT_NAME_STEP).send_keys("Edit")
        try:
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT).click()
        except TimeoutException:
            time.sleep(2)
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT).click()
        """go tu test tab"""
        self.element_is_visible(self.Locators.INPUT_TEXTAREA_ALERT).send_keys("Alert")
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        # self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        """check position"""
        try:
            self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).click()
        except StaleElementReferenceException:
            time.sleep(3)
            self.element_is_visible(self.Locators.QUESTIONS_FIRST_POSITION_CHECK).click()
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).clear()
        self.element_is_visible(self.Locators.ANSWER_AND_CHECKBOX).send_keys("edit answer")
        self.element_is_visible(self.Locators.BUTTON_EDIT_QUESTION_SAVE).click()
        self.element_is_visible(self.Locators.BUTTON_GO_BACK).click()
        self.element_is_visible(self.Locators.TEXT_GET_TESTED).click()
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nдоступ\nверсионность'
        self.element_is_visible(self.Locators.TEXTAREA_ALERT).send_keys(text_alert + " new")
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.EDIT_ARTICLE).click()
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY_SCRIPT).click()
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.BUTTON_JUST_NOTIFY).click()
        self.element_is_visible(self.Locators.TEXT_CONFIRM_READ).click()
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nдоступ\nверсионность\nтест'
        self.element_is_visible(self.Locators.RADIOBUTTON_SMALL_CORRECT_CONTENT).click()
        """check tab text"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nдоступ\nверсионность'
        self.element_is_visible(self.Locators.RADIOBUTTON_BIG_CORRECT_CONTENT).click()
        """text test tab check"""
        tabs_check = self.element_is_visible(self.Locators.TABS_CHECK_TEXT_ALL).text
        assert tabs_check == 'поиск\nдоступ\nверсионность\nтест'
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        """check position"""
        """del question from test"""
        # del1
        self.element_is_visible(self.Locators.SVG_DEL_FIRST_QUESTION).click()
        self.element_is_visible(self.Locators.CONFIRM_BUTTON_DELETE).click()
        # del2
        self.element_is_visible(self.Locators.SVG_DEL_FIRST_QUESTION).click()
        self.element_is_visible(self.Locators.CONFIRM_BUTTON_DELETE).click()
        # """del all question"""
        # self.element_is_visible(self.Locators.BUTTON_ADD_QUESTION).click()
        # list_delete = self.elements_are_visible(self.Locators.SVG_DEL_QUESTION)
        # for n in list_delete:
        #     time.sleep(0.5)
        #     n.click()
        #     self.element_is_visible(self.Locators.SVG_DEL_QUESTION_CONFIRM).click()


















































        time.sleep(5)




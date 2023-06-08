import time

from conftest import driver
from locators.topic_database_locators import CreateTopicDatabaseLocators
from pages.base_page import BasePage
from pages.data_login_password import url


class CreateTopicDatabase(BasePage):
    Locators = CreateTopicDatabaseLocators

    def add_topic_database(self, driver):
        self.input_in_my_project(driver)
        self.element_is_visible(self.Locators.LEARNING_BUTTON).click()
        self.element_is_visible(self.Locators.TAB_ALL_COURSES).click()
        self.element_is_visible(self.Locators.DATABASE_OF_QUESTIONS).click()
        """check text open form"""
        text_database_of_questions = self.element_is_visible(self.Locators.TEXT_DATABASE_OF_QUESTIONS).text
        assert text_database_of_questions == "База вопросов"
        text_not_questions_now = self.element_is_visible(self.Locators.TEXT_NOT_QUESTIONS_NOW).text
        assert text_not_questions_now == "В этом проекте пока нет вопросов. Создайте структуру тем для его размещения"
        button_add_topic = self.element_is_visible(self.Locators.BUTTON_ADD_TOPIC).text
        assert button_add_topic == 'Создать темы'
        self.element_is_visible(self.Locators.BUTTON_ADD_TOPIC).click()
        """input name topic and check len"""
        element = self.element_is_visible(self.Locators.INPUT_NAME_TOPIC)
        name_content = self.check_len_name_content(driver, element, n=65, attribute="maxlength")

        self.element_is_visible(self.Locators.INPUT_NAME_TOPIC).send_keys(name_content)




        time.sleep(5)




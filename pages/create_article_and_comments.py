import random
import time

from selenium.common import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By

from pages.creating_panel import CreatingPanel
from locators.all_locators import CreateTopicDatabaseLocators as locators_topic_database
from pages.authorisation_page import Authorisation
import locators.all_locators as locators
from pages.CKE_redactor_and_public_wizard import CKERedactor, PublicWizard
from pages.base_class import MainPage
from pages.users import minervakms


class ContentOptions(MainPage):
    """Редактирование, избранное, комментарии и т.д."""

    def redaction(self):
        """Кнопка Редактировать"""
        self.click_to_element(locators.FormPagesLocators.EDIT_ARTICLE)

    def three_dots_button(self):
        """Кнопка Троеточие"""
        self.click_to_element(locators.SearchRuEnLocators.MEATBALL_ARTICLE)

    def delete_button(self):
        """Кнопка Троеточие"""
        self.click_to_element(locators.SearchRuEnLocators.SVG_DEL)

    def restore_button(self):
        """Кнопка 'восстановить'"""
        self.click_to_element(locators.OpenArticle.BOTTOM_BANNER_BUTTON)


class BaseArticleEditor(CreatingPanel, CKERedactor, PublicWizard, ContentOptions):
    """Создание и наполнение Базовой статьи"""
    BASE_ARTICLE_TITLE = 'Название статьи ' + str(random.randint(999, 9999))

    def title_article(self):
        """Заголовок статьи"""
        self.element_is_visible(locators_topic_database.NAME_OF_ARTICLE).send_keys(self.BASE_ARTICLE_TITLE)

    def change_folder(self):
        """Выбор папки сохранения"""
        self.element_is_visible(locators_topic_database.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")

    def text_area_article(self):
        """Наполнение тела статьи"""
        self.element_is_visible(locators_topic_database.TEXT_AREA_ARTICLE).send_keys('Hello')
        self.input_files()

    def save_data_in_file(self):
        """Метод сохранения ссылки и названия статьи, данные перезаписываются при каждом вызове"""
        with open(r'data.txt', 'w', encoding='utf8') as file:
            file.write(self.get_actual_url() + '\n')
            file.write(self.BASE_ARTICLE_TITLE)

    def creating_base_article(self):
        """Создание обычной статьи с наполнением"""
        self.get_authorisation_in_selen()
        self.create_button()
        self.create_base_article_button()
        self.title_article()
        self.change_folder()
        self.text_area_article()
        self.save_base_article()
        self.save_data_in_file()

    def minor_edit_base_article(self, url):
        """Редактирование статьи и минорное сохранение"""
        self.get_authorisation_in_url(url)
        self.redaction()
        self.element_is_visible(locators_topic_database.TEXT_AREA_ARTICLE).send_keys('HeyHey')
        self.save_minor_edit()

    def major_edit_base_article(self, url):
        """Редактирование статьи и мажорное сохранение"""
        self.get_authorisation_in_url(url)
        self.redaction()
        self.element_is_visible(locators_topic_database.TEXT_AREA_ARTICLE).send_keys('Rick and Morty was here')
        self.save_major_edit()

    def delete_base_article(self, url):
        """Удаление статьи"""
        self.get_authorisation_in_url(url)
        self.three_dots_button()
        self.delete_button()
        self.notification_text_area('Удаление')
        self.execute_button_click()
        time.sleep(1)

    def restore_base_article(self, url):
        """Восстановление статьи"""
        self.get_authorisation_in_url(url)
        self.restore_button()
        self.save_major_edit('Восстановление')


class DataParser:
    """Класс получения данных из файла"""

    @staticmethod
    def get_url_from_data_file():
        """Метод парсит ссылку на статью из файла"""
        with open(r'data.txt', 'r', encoding='utf8') as file:
            url = file.readline()
        return url

    @staticmethod
    def get_article_name_from_data_file():
        """Метод парсит название статьи из файла"""
        with open(r'data.txt', 'r', encoding='utf8') as file:
            name = file.readlines()[1]
        return name


class Comments(Authorisation):
    """Добавление комментария в существующую статью"""

    def comment_text_area(self, text='Максимально понятный коммент'):
        """Заполнение поля комментария, можно передать текст для заполнения"""
        self.element_is_visible(locators.Comments.ADD_COMMENT).send_keys(text)

    def send_comment(self):
        """Подтверждение отправки комментария"""
        self.click_to_element(locators.Comments.SEND_COMMENT)

    def disable_the_question_to_the_expert_option(self):
        """Отключение галочки 'с вопросом к эксперту'"""
        self.click_to_element(locators.Comments.EXPERT_QUESTION)

    @staticmethod
    def create_comments(driver, url):
        """Создание тестового набора комментариев в статье по переданной ссылке, с прохождением авторизации"""
        page = Comments(driver)

        page.get_authorisation_in_url(url)

        for i in range(4):
            page.comment_text_area(f'Тестовый комментарий {i + 1}')
            page.send_comment()

        page.disable_the_question_to_the_expert_option()
        page.comment_text_area('Серый комментарий')
        page.send_comment()
            # проверка создания 5 комментариев
            # try:
            #     time.sleep(1)
            #     check_count_comment = driver.find_element(By.XPATH, "//p[text()='5 комментариев']").text
            #     # check_count_comment = MainPage.element_is_visible(locators.Comments.CHECK_COUNT_COMMENT).text
            #     assert check_count_comment == "5 комментариев"
            # except AssertionError:
            #     continue
            # break

    @staticmethod
    def close_first_comment(driver, url):
        """Закрытие первого комментария"""
        page = Comments(driver)
        page.get_authorisation_in_url(url)
        page.click_to_element(locators.Comments.TO_ANSWER_COMMENT_1)
        page.element_is_visible(locators.Comments.COMMENT_BOX).send_keys('Закрытие 1')
        page.click_to_element(locators.Comments.CHECK_BOX_TICK_SOLVED)
        page.click_to_element(locators.Comments.CLOSE_COMMENT)

    @staticmethod
    def close_second_comment(driver, url):
        """Закрытие первого комментария"""
        page = Comments(driver)
        page.get_authorisation_in_url(url)
        page.click_to_element(locators.Comments.TO_ANSWER_COMMENT_2)
        page.element_is_visible(locators.Comments.COMMENT_BOX).send_keys('Закрытие 2')
        page.click_to_element(locators.Comments.CHECK_BOX_TICK_SOLVED)
        page.click_to_element(locators.Comments.CLOSE_COMMENT)

    @staticmethod
    def close_third_comment(driver, url):
        """Закрытие первого комментария"""
        page = Comments(driver)
        page.get_authorisation_in_url(url)
        page.click_to_element(locators.Comments.TO_ANSWER_COMMENT_3)
        page.element_is_visible(locators.Comments.COMMENT_BOX).send_keys('Закрытие 3')
        page.click_to_element(locators.Comments.CHECK_BOX_TICK_SOLVED)
        page.click_to_element(locators.Comments.CLOSE_COMMENT)

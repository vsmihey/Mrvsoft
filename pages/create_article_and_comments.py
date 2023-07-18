import random
import time
from pages.creating_panel import CreatingPanel
from locators.all_locators import CreateTopicDatabaseLocators as locators_topic_database
from pages.authorisation_page import Authorisation
import locators.all_locators as locators
from pages.CKE_redactor_and_public_wizard import CKERedactor, PublicWizard
from pages.users import minervakms


class BaseArticleEditor(CreatingPanel, CKERedactor, PublicWizard):
    """Создание и наполнение Базовой статьи"""
    BASE_ARTICLE_TITLE = 'Максимально подробное название статьи ' + str(random.randint(999, 9999))

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

    @staticmethod
    def get_url_from_data_file():
        """Метод парсит ссылку на статью из файла"""
        with open(r'data.txt', 'r', encoding='utf8') as file:
            url = file.readline()
        return url

    def creating_base_article(self):
        """Создание обычной статьи с наполнением"""
        self.get_authorisation_in_selen(minervakms)
        time.sleep(5)
        self.create_button()
        self.create_base_article_button()
        time.sleep(1)
        self.title_article()
        self.change_folder()
        self.text_area_article()
        self.save_base_article()
        time.sleep(0.5)
        self.save_data_in_file()




class Comments(Authorisation):
    """Добавление комментария в существующую статью"""

    def comment_text_area(self, text='Максимально понятный коммент'):
        """Заполнение поля комментария, можно передать текст для заполнения"""
        self.element_is_visible(locators.Comments.ADD_COMMENT).send_keys(text)

    def send_comment(self):
        """Подтверждение отправки комментария"""
        self.element_is_visible(locators.Comments.SEND_COMMENT).click()

    def disable_the_question_to_the_expert_option(self):
        """Отключение галочки 'с вопросом к эксперту'"""
        self.element_is_visible(locators.Comments.EXPERT_QUESTION).click()

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

    @staticmethod
    def close_first_comment(driver, url):
        """Закрытие первого комментария"""
        page = Comments(driver)
        page.get_authorisation_in_url(url)
        page.element_is_visible(locators.Comments.TO_ANSWER_COMMENT_1).click()
        page.element_is_visible(locators.Comments.COMMENT_BOX).send_keys('Тест')
        page.element_is_visible(locators.Comments.CHECK_BOX_TICK_SOLVED).click()
        page.send_comment()


if __name__ == '__main__':
    test = BaseArticleEditor()
    test.creating_base_article()
    test.browser.delete_all_cookies()

    Comments.create_comments(BaseArticleEditor.get_url_from_data_file())

    # Comments.close_first_comment(BaseArticleEditor.get_url_from_data_file())

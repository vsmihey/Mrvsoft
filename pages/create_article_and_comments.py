import time
from creating_panel import CreatingPanel
from locators.all_locators import CreateTopicDatabaseLocators as locators_topic_database
from authorisation_page import Authorisation
import locators.all_locators as locators
from CKE_redactor_and_public_vizard import CKERedactor, PublicVizard


class BaseArticleEditor(CreatingPanel, CKERedactor, PublicVizard):
    """Создание и наполнение Базовой статьи"""
    BASE_ARCTICLE_URL = ''
    BASE_ARCTICLE_TITLE = 'Максимально подробное название статьи'

    def title_arcticle(self):
        """Заголовок статьи"""
        self.element_is_visible(locators_topic_database.NAME_OF_ARTICLE).send_keys(self.BASE_ARCTICLE_TITLE)

    def change_folder(self):
        """Выбор папки сохранения"""
        self.element_is_visible(locators_topic_database.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")

    def text_area_article(self):
        """Наполнение тела статьи"""
        self.element_is_visible(locators_topic_database.TEXT_AREA_ARTICLE).send_keys('Hello')
        self.input_files()

    @staticmethod
    def creating_base_article():
        try:
            page = BaseArticleEditor()
            page.get_authorisation_in_selen()
            page.create_button()
            page.create_base_article_button()
            page.title_arcticle()
            page.change_folder()
            page.text_area_article()

        except Exception:
            raise Exception


class Comments(Authorisation):
    """Добавление комментария в существующую статью"""

    def comment_text_area(self, text='Максимально понятный коммент'):
        """Заполнение поля комментария, можно передать текст для заполнения"""
        self.element_is_visible(locators.LocatorsCheckNewsHistory.ADD_COMMENT).send_keys(text)

    def send_comment(self):
        """Подтверждение отправки комментария"""
        self.element_is_visible(locators.LocatorsCheckNewsHistory.SEND_COMMENT).click()

    def disable_the_question_to_the_expert_option(self):
        """Отключение галочки 'с вопросом к эксперту'"""
        self.element_is_visible(locators.Comments.EXPERT_QUESTION).click()

    @staticmethod
    def create_comments(url):
        """Создание тестового набора комментариев в статье по переданной ссылке, с прохождением авторизации"""
        page = Comments()
        page.get_authorisation_in_url(url)

        for i in range(4):
            page.comment_text_area(f'Тестовый комментарий {i + 1}')
            page.send_comment()

        page.disable_the_question_to_the_expert_option()
        page.comment_text_area('Серый комментарий')
        page.send_comment()


if __name__ == '__main__':
    test = BaseArticleEditor()
    test.creating_base_article()
    print(test.BASE_ARCTICLE_URL)
    test.browser.delete_all_cookies()

    # Comments.create_comments('https://test6.minervasoft.ru/news/space/1/article/3389')

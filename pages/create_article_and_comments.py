import time
from creating_panel import CreatingPanel
from locators.all_locators import CreateTopicDatabaseLocators as locators_topic_database
from authorisation_page import Authorisation
import locators.all_locators as locators
from CKE_redactor_and_public_wizard import CKERedactor, PublicWizard


class BaseArticleEditor(CreatingPanel, CKERedactor, PublicWizard):
    """Создание и наполнение Базовой статьи"""
    BASE_ARCTICLE_TITLE = 'Максимально подробное название статьи'

    def __init__(self):
        super().__init__()
        self.url = None

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

    def creating_base_article(self):
        try:
            self.get_authorisation_in_selen()
            self.create_button()
            self.create_base_article_button()
            self.title_arcticle()
            self.change_folder()
            self.text_area_article()
            self.save_base_article()
            time.sleep(1)
            self.url = self.get_actual_url()

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
    print(test.url)
    test.browser.delete_all_cookies()

    Comments.create_comments(test.url)

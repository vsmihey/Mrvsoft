import pathlib
from pathlib import Path
import time
from creating_panel import CreatingPanel
from locators.locators_topic_database import CreateTopicDatabaseLocators as locators_topic_database


class BaseArticleEditor(CreatingPanel):
    """Cоздание и наполнение Базовой статьи"""
    BASE_ARCTICLE_URL = ''

    def title_arcticle(self):
        self.element_is_visible(locators_topic_database.NAME_OF_ARTICLE).send_keys(
            'Максимально подробное название статьи')

    def change_folder(self):
        """Выбор папки сохранения"""
        self.element_is_visible(locators_topic_database.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")

    def text_area_article(self):
        """Наполнение тела статьи"""

        path1 = r'D:\проекты\Mrvsoft\tests\files\mp3.mp3'
        path2 = r'D:\проекты\Mrvsoft\tests\files\avi.avi'

        self.element_is_visible(locators_topic_database.TEXT_AREA_ARTICLE).send_keys('Hello')
        self.elements_is_present(locators_topic_database.UPLOAD_MEDIA).click()

        self.browser.execute_script(
            """document.querySelector(".popup__footer.file-manager__foot.file-manager--hidden").removeAttribute('class')""")
        self.browser.execute_script(
            """document.querySelector("form[enctype='multipart/form-data']").removeAttribute('style')""")


        self.element_is_visible(locators_topic_database.INPUT_INVISIBLE).send_keys(path1)
        self.element_is_visible(locators_topic_database.INPUT_INVISIBLE).send_keys(path2)
        time.sleep(5)

        checkbox_insert_files = self.elements_are_visible(locators_topic_database.CHECKBOX_INSERT_FILES)

        for n in checkbox_insert_files:
            time.sleep(0.5)
            n.click()

        self.element_is_visible(locators_topic_database.INPUT_SELECTED).click()

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

            if not BaseArticleEditor.BASE_ARCTICLE_URL:
                BaseArticleEditor.BASE_ARCTICLE_URL = page.get_actual_url()

        except Exception:
            raise Exception


if __name__ == '__main__':
    BaseArticleEditor.creating_base_article()
    print(BaseArticleEditor.BASE_ARCTICLE_URL)


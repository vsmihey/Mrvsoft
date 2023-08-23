import random
import time

import allure
import pytest
from pages.checking_after_update import CheckingArticleAfterUpdatePage
from pages.create_article_and_comments import BaseArticleEditor
from pages.data_login_password import base_article, article_by_template
from pages.users import minervakms
from pages.users import andrey

user_for_test = andrey


@allure.suite("Проверка обычной статьи, статьи по шаблону, пошагового сценария после установки обновления")
@pytest.mark.order(8)
class TestCheckingAfterUpdate:

    # @allure.feature("Проверка обычной статьи после установки обновления")
    # class TestCheckingArticleAfterUpdate:
    TEXT = "Новая версия" + str(random.randint(999, 9999))

    def check_all_content_in_article(self, driver):
        """Проверка контента в статье"""
        checking_after_updating = BaseArticleEditor(driver)
        checking_after_updating.check_name_in_article()
        checking_after_updating.check_text_artile_heading(driver)
        checking_after_updating.check_text_artile_links()
        checking_after_updating.check_images_in_article()
        checking_after_updating.check_videos_in_article()
        checking_after_updating.check_audio_in_article()
        checking_after_updating.check_table_in_article()
        checking_after_updating.check_h_text_in_article()
        checking_after_updating.paragraph_color_check()
        checking_after_updating.check_styles_text_in_article()
        checking_after_updating.check_color_text_in_article()
        checking_after_updating.important_block_red()
        checking_after_updating.check_spoiler()
        checking_after_updating.check_align_text_in_article()
        checking_after_updating.check_link_href()
        # checking_after_updating.major_edit_in_article(self.TEXT)

    def check_all_content_in_template(self, driver):
        checking_after_updating = BaseArticleEditor(driver)
        checking_after_updating.check_name_article_by_template()
        checking_after_updating.check_image_in_template1()
        checking_after_updating.check_video_in_template()

    @allure.title("Проверка обычной статьи после установки обновления")
    def test_check_article_after_updating(self, driver):
        checking_after_updating = BaseArticleEditor(driver)
        checking_after_updating.get_authorisation_in_url(base_article, user_for_test)
        self.check_all_content_in_article(driver)
        checking_after_updating.major_edit_in_article(self.TEXT)
        checking_after_updating.check_version()
        self.check_all_content_in_article(driver)
        time.sleep(5)

    @allure.title("Проверка статьи по шаблону после установки обновления")
    def test_check_template_after_updating(self, driver):
        checking_after_updating = BaseArticleEditor(driver)
        checking_after_updating.get_authorisation_in_url(article_by_template, user_for_test)
        self.check_all_content_in_template(driver)




    @allure.title("Проверка пошагового сценария после установки обновления")
    def test_check_script_after_updating(self, driver):
        pass







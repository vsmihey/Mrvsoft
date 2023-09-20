import random
import time

import allure
import pytest
from pages.create_article_and_comments import BaseArticleEditor, ArticleByTemplate, ArticleByScript
from pages.data_login_password import base_article, article_by_script
from pages.users import ricksanchez, minervakms
from pages.data_login_password import base_article, article_by_template
from pages.users import leela
from pages.users import andrey

# user_for_test = leela
user_for_test = minervakms
# user_for_test = andrey


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
        checking_after_updating.list_in_article()
        checking_after_updating.check_styles_text_in_article()
        checking_after_updating.important_block_red()
        checking_after_updating.check_spoiler()
        checking_after_updating.check_align_text_in_article()
        checking_after_updating.check_link_href()
        # checking_after_updating.major_edit_in_article(self.TEXT)

    def check_all_content_in_template(self, driver):
        checking_updating_template = ArticleByTemplate(driver)
        checking_updating_template.check_name_article_by_template()
        checking_updating_template.tabs_1()
        checking_updating_template.check_image_in_template1()
        checking_updating_template.check_video_in_template()
        checking_updating_template.check_text_links()
        checking_updating_template.check_text_li_template()
        checking_updating_template.check_text_template()
        checking_updating_template.check_number_template()
        checking_updating_template.check_contents_link_template()
        checking_updating_template.check_color_text_bg_template()
        checking_updating_template.check_smiles_template()
        checking_updating_template.tabs_2_click()
        checking_updating_template.check_table_tab2_in_template()
        checking_updating_template.check_audio_tab2_in_template()
        checking_updating_template.check_link_tab2_template()
        checking_updating_template.tabs_3_click()
        checking_updating_template.check_video_tab3_in_template()
        checking_updating_template.check_file_download_tab3_in_template()
        checking_updating_template.tabs_4_click()
        checking_updating_template.check_href_tab4_in_template()
        checking_updating_template.check_li_tab4_in_template()

    def check_all_content_in_script(self, driver):
        checking_updating_script = ArticleByScript(driver)
        checking_updating_script.check_name_article_by_template()
        checking_updating_script.answer_yes_part1()
        checking_updating_script.check_script_part2()
        checking_updating_script.answer_no_part2()
        checking_updating_script.check_script_part3()
        checking_updating_script.answer_yes_part3()
        checking_updating_script.check_script_part4()
        checking_updating_script.answer_no_part4()
        checking_updating_script.check_script_end()
        checking_updating_script.check_script_button_restart()

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
        checking_after_updating = ArticleByTemplate(driver)
        checking_after_updating.get_authorisation_in_url(article_by_template, user_for_test)
        self.check_all_content_in_template(driver)
        checking_after_updating.major_edit_in_article(self.TEXT)
        checking_after_updating.check_version()
        checking_after_updating.tabs_1_click()
        self.check_all_content_in_template(driver)

    @allure.title("Проверка пошагового сценария после установки обновления")
    def test_check_script_after_updating(self, driver):
        checking_after_updating = ArticleByScript(driver)
        checking_after_updating.get_authorisation_in_url(article_by_script, user_for_test)
        self.check_all_content_in_script(driver)
        checking_after_updating.edit_and_public_article(self.TEXT)
        checking_after_updating.check_version_script()
        self.check_all_content_in_script(driver)








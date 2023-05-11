import time
import pytest
from selenium.common import TimeoutException
from pages import base_page
from pages.form_page import FormPage
from pages.data_login_password import *
from pages.article_page import ArticlePage


class TestFormPage:

    def test_logo(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.logo_head()
        form_page.screenshot()
        self.login = login
        self.password = password_incorrect
        form_page.authorization(self.login, self.password)
        form_page.restore_incorrect()
        form_page.logo_head()
        form_page.screenshot()
        form_page.full_authorization(driver)
        form_page.logo_head()
        form_page.screenshot()
        form_page.title_find(driver)
        time.sleep(1)

    def test_form_1(self, driver):
        """tests incorrect data"""
        form_page = FormPage(driver, url)
        form_page.open()
        self.login = login_incorrect
        self.password = password
        form_page.fill_fields(self.login, self.password)
        self.login = login_incorrect
        self.password = password_incorrect
        form_page.fill_fields(self.login, self.password)
        self.login = login
        self.password = password_incorrect
        form_page.fill_fields(self.login, self.password)
        form_page.check_auth_text()
        form_page.restore_incorrect()
        form_page.check_restore_text()

    def test_title(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.authorization(login, password)
        form_page.input_project()
        # driver.get_screenshot_as_file("scr.png")
        print("input project")
        form_page.all_title(driver)

    @pytest.mark.skip('restore password')
    def test_form_restore(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        password = password_incorrect
        form_page.authorization(login, password)
        form_page.restore_correct()

    def test_add_new_person(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.add_new_person(driver)

    def test_add_new_role(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.add_new_role(driver)
        time.sleep(1)

    def test_folder_create_del_recovery(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.create_del_recovery_folder_content(driver)
        form_page.delete_some_folder(count_folders=8)

    def test_folder1_folder2(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.folder1_folder2(driver)
        form_page.check_folder1_folder2(driver)
        form_page.delete_some_folder(count_folders=3)

    # def test_check_folder1_folder2(self, driver):
    #     form_page = FormPage(driver, url)
    #     form_page.open()
    #     form_page.input_in_my_project(driver)
    #     form_page.check_folder1_folder2(driver)

    @pytest.mark.skip('delete folders')
    def test_del_some_folders(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.delete_some_folder(count_folders=10)  # ставить на 1 папку больше

    def test_favourites(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.favourites(driver)

    def test_add_to_favourites(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.add_to_favourites(driver)

    def test_add_normal_article(self, driver):
        article_page = ArticlePage(driver, url)
        article_page.open()
        article_page.input_in_my_project(driver)
        article_page.add_normal_article(driver)

    def test_fixing_article(self, driver):
        article_page = ArticlePage(driver, url)
        article_page.open()
        article_page.input_in_my_project(driver)
        article_page.fixing_article(driver)
        time.sleep(1)

    def test_add_article_by_templates(self, driver):
        article_page = ArticlePage(driver, url)
        article_page.open()
        article_page.input_in_my_project(driver)
        time.sleep(3)
        article_page.add_article_by_templates(driver)






        # def test_test(self, driver):
        #     # url ='https://test1.minervasoft.ru/content/space/59?popup=article-editor&chosenSpaceId=59&articleId=new&article-type=ARTICLE'
        #     article_page = ArticlePage(driver, url)
        #     article_page.open()
        #     article_page.input_in_my_project(driver)
        #     driver.get("https://test1.minervasoft.ru/content/space/59?popup=article-editor&chosenSpaceId=59&articleId=new&article-type=ARTICLE")
        #     article_page.mytest(driver)

































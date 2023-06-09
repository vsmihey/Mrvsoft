import time
import pytest
from pages.form_page import FormPage
from pages.data_login_password import *
from pages.article_page import ArticlePage, CopyPastePage, CreateDraftPage, FilesPages
from pages.article_page import StepByScriptPage
from pages import base_class


@pytest.mark.order(1)
class TestFormPage:

    def test_logo(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.logo_head()
        # form_page.screenshot()
        self.login = login
        self.password = password_incorrect
        form_page.authorization(self.login, self.password)
        form_page.restore_incorrect()
        form_page.logo_head()
        # form_page.screenshot()
        form_page.full_authorization(driver)
        form_page.logo_head()
        # form_page.screenshot()
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

    def test_title(self):
        form_page = FormPage()
        #form_page.open()
        form_page.get_authorisation_in_superbank()
        #form_page.input_in_my_project(driver)
        # print("input project")
        form_page.all_title(base_class.driver)

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
        # time.sleep(1)

    def test_folder_create_del_recovery(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.create_del_recovery_folder_content(driver)
        form_page.delete_some_folder(driver, count_folders=8)

    # @pytest.mark.skip('test_folder1_folder2')
    def test_folder1_folder2(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.folder1_folder2(driver)
        form_page.check_folder1_folder2(driver)
        form_page.delete_some_folder(driver, count_folders=5)

    # def test_check_folder1_folder2(self, driver):
    #     form_page = FormPage(driver, url)
    #     form_page.open()
    #     form_page.input_in_my_project(driver)
    #     form_page.check_folder1_folder2(driver)

    # @pytest.mark.skip('delete folders')
    def test_del_some_folders(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        form_page.input_in_my_project(driver)
        form_page.delete_some_folder(driver, count_folders=15)  # ставить на 1 папку больше

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
        # article_page.input_in_my_project(driver)
        article_page.add_normal_article(driver)

    def test_fixing_article(self, driver):
        article_page = ArticlePage(driver, url)
        article_page.open()
        article_page.input_in_my_project(driver)
        article_page.fixing_article(driver)
        time.sleep(1)

    # @pytest.mark.skip('add_article_by_templates')
    def test_add_article_by_templates(self, driver):
        article_page = ArticlePage(driver, url)
        article_page.open()
        article_page.input_in_my_project(driver)
        # time.sleep(3)
        article_page.add_article_by_templates(driver)

    @pytest.mark.skip('check_text_link')
    def test_check_text_link(self, driver):
        article_page = ArticlePage(driver, url)
        article_page.open()
        article_page.input_in_my_project(driver)
        article_page.check_text_link(driver)

    # @pytest.mark.skip('delete folders')
    class TestStepByScriptPage:

        def test_step_by_script(self, driver):
            article_page = StepByScriptPage(driver, url)
            article_page.open()
            article_page.input_in_my_project(driver)
            article_page.add_script()
            article_page.check_opened_added_script(driver)
            article_page.check_len_name_content(driver)
            article_page.add_new_step(driver)
            article_page.delete_all()
            article_page.new_step(driver)

        def test_fixing_script(self, driver):
            article_page = StepByScriptPage(driver, url)
            article_page.open()
            article_page.input_in_my_project(driver)
            article_page.add_script()
            article_page.check_step_fixing(driver)

    @pytest.mark.skip('copy_paste')
    class TestCopyPastePage:

        def test_copy_paste(self, driver):
            copy_paste_page = CopyPastePage(driver, url)
            copy_paste_page.open()
            copy_paste_page.input_in_my_project(driver)
            copy_paste_page.add_text_in_article(driver)

    # @pytest.mark.skip('create_draft')
    class TestCreateDraft:

        def test_create_draft(self, driver):
            create_draft_page = CreateDraftPage(driver, url)
            create_draft_page.open()
            create_draft_page.input_in_my_project(driver)
            create_draft_page.open_4_tab(driver)

    class TestFilesPage:

        def test_create_data_files(self, driver):
            article_pages = FilesPages(driver, url)
            article_pages.open()
            article_pages.input_in_my_project(driver)
            article_pages.create_data_files(driver)

        def test_check_size_file(self, driver):
            article_pages = FilesPages(driver, url)
            article_pages.open()
            article_pages.input_in_my_project(driver)
            article_pages.generated_big_file_jpg()
            article_pages.add_big_file(driver)

        def test_check_template_download(self, driver):
            article_pages = FilesPages(driver, url)
            article_pages.open()
            article_pages.input_in_my_project(driver)
            article_pages.check_template_download(driver)

        def test_check_template_download_bigfile(self, driver):
            article_pages = FilesPages(driver, url)
            article_pages.open()
            article_pages.input_in_my_project(driver)
            article_pages.generated_big_file_exe()
            article_pages.template_download_bigfile(driver)

        # @pytest.mark.skip('download_files_from_files')
        def test_download_files_from_files(self, driver):
            article_pages = FilesPages(driver, url)
            article_pages.open()
            article_pages.input_in_my_project(driver)
            article_pages.download_files_from_files()

        def test_script_download_bigfile(self, driver):
            article_pages = FilesPages(driver, url)
            article_pages.open()
            article_pages.input_in_my_project(driver)
            article_pages.generated_big_file_csv()
            article_pages.check_script_download_bigfile()

        def test_script_download(self, driver):
            article_pages = FilesPages(driver, url)
            article_pages.open()
            article_pages.input_in_my_project(driver)
            article_pages.check_script_download()




































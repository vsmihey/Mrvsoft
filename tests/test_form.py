import time
import allure
import pytest
from pages.form_page import FormPage
from pages.data_login_password import *
from pages.article_page import ArticlePage, CopyPastePage, CreateDraftPage, FilesPages
from pages.article_page import StepByScriptPage
from pages.users import DataLoginPassword, jerry

user_for_test = jerry


@pytest.mark.order(1)
@allure.suite("Тест лого, тайтлы, авторизация, статья, пользователи")
class TestFormPage:

    @allure.title("Проверка логотипа")
    def test_logo(self, driver):
        form_page = FormPage(driver)
        form_page.open()
        form_page.logo_head()
        # self.login = login
        login, password = DataLoginPassword.correct_data()
        # self.password = password_incorrect
        login_incorrect, password_incorrect = DataLoginPassword.incorrect_data()
        # form_page.authorization(self.login, self.password)
        form_page.authorization(login, password_incorrect)
        form_page.restore_incorrect()
        form_page.logo_head()
        form_page.full_authorization(driver)
        form_page.logo_head()
        form_page.title_find(driver)

    @allure.title("Проверка авторизации в системе")
    def test_form_1(self, driver):
        """Тест авторизации"""
        form_page = FormPage(driver, url)
        form_page.browser.delete_all_cookies()
        form_page.open()
        # self.login = login_incorrect
        with allure.step("Неверный логин, верный пароль"):
            login_incorrect, password_incorrect = DataLoginPassword.incorrect_data()
            # print(login_incorrect)
            # self.password = password
            login, password = DataLoginPassword.correct_data()
            form_page.fill_fields(login_incorrect, password)
        # self.login = login_incorrect
        # self.password = password_incorrect
        with allure.step("Неверный логин, неверный пароль"):
            login_incorrect, password_incorrect = DataLoginPassword.incorrect_data()
            form_page.fill_fields(login_incorrect, password_incorrect)
        with allure.step("Верный логин, неверный пароль"):
            login, password = DataLoginPassword.correct_data()
            login_incorrect, password_incorrect = DataLoginPassword.incorrect_data()
            form_page.fill_fields(login, password_incorrect)
        form_page.check_auth_text()
        form_page.restore_incorrect()
        form_page.check_restore_text()
        with allure.step("Верный логин, Верный пароль"):
            login = user_for_test.login
            password = user_for_test.password
            form_page.fill_fields_(login, password)
        time.sleep(1)
        check_text_input_in_system = form_page.check_input_text()
        assert check_text_input_in_system == "Выберите проект"

    @allure.title("Тест тайтлы")
    def test_title(self, driver):
        form_page = FormPage(driver)
        # form_page.open()
        form_page.get_authorisation_in_selen(user_for_test)
        # form_page.input_in_my_project(driver)
        # print("input project")
        form_page.all_title(driver)
        # form_page.browser.quit()

    @pytest.mark.skip("Тест восстановление пароля")
    @allure.title("Тест восстановление пароля")
    def test_form_restore(self, driver):
        form_page = FormPage(driver, url)
        form_page.open()
        login_incorrect, password_incorrect = DataLoginPassword.incorrect_data()
        password = password_incorrect
        form_page.authorization(login, password)
        form_page.restore_correct()

    @allure.title("Добавление нового пользователя")
    def test_add_new_person(self, driver):
        form_page = FormPage(driver)
        # form_page.open()
        form_page.get_authorisation_in_selen(user_for_test)
        # form_page.input_in_my_project(driver)
        form_page.add_new_person(driver)

    @allure.title("Добавление новой роли")
    def test_add_new_role(self, driver):
        form_page = FormPage(driver)
        # form_page.open()
        form_page.get_authorisation_in_selen(user_for_test)
        form_page.add_new_role(driver)

    @allure.title("Создание, удаление, восстановление папки в Контенте")
    def test_folder_create_del_recovery(self, driver):
        form_page = FormPage(driver)
        # form_page.open()
        form_page.get_authorisation_in_selen(user_for_test)
        form_page.create_del_recovery_folder_content(driver)
        form_page.delete_some_folder(count_folders=8)

    # @pytest.mark.skip('test_folder1_folder2')
    @allure.title("Создание папка 1 и папка 2")
    def test_folder1_folder2(self, driver):
        form_page = FormPage(driver)
        # form_page.open()
        form_page.get_authorisation_in_selen(user_for_test)
        form_page.folder1_folder2(driver)
        form_page.check_folder1_folder2(driver)
        form_page.delete_some_folder(count_folders=5)

    # def test_check_folder1_folder2(self, driver):
    #     form_page = FormPage(driver, url)
    #     form_page.open()
    #     form_page.input_in_my_project(driver)
    #     form_page.check_folder1_folder2(driver)

    # @pytest.mark.skip('delete folders')
    @allure.title("Удаление папок")
    def test_del_some_folders(self, driver):
        form_page = FormPage(driver)
        # form_page.open()
        form_page.get_authorisation_in_selen(user_for_test)
        form_page.delete_some_folder(count_folders=15)  # ставить на 1 папку больше

    @allure.title("Избранное")
    def test_favourites(self, driver):
        form_page = FormPage(driver)
        # form_page.open()
        form_page.get_authorisation_in_selen(user_for_test)
        form_page.favourites(driver)

    @allure.title("Добавление в Избранное")
    def test_add_to_favourites(self, driver):
        form_page = FormPage(driver)
        # form_page.open()
        form_page.get_authorisation_in_selen(user_for_test)
        form_page.add_to_favourites(driver)

    @allure.title("Добавление обычной статьи")
    def test_add_normal_article(self, driver):
        # article_page = BaseArticleEditor(driver)
        article_page = ArticlePage(driver)
        # article_page.creating_base_article()
        article_page.get_authorisation_in_selen(user_for_test)
        article_page.add_normal_article(driver)

    @allure.title("Способ закрепления для обычной статьи")
    def test_fixing_article(self, driver):
        article_page = ArticlePage(driver)
        # article_page.open()
        article_page.get_authorisation_in_selen(user_for_test)
        article_page.fixing_article(driver)

    @allure.title("Добавление статьи по шаблону")
    # @pytest.mark.skip('add_article_by_templates')
    def test_add_article_by_templates(self, driver):
        article_page = ArticlePage(driver)
        # article_page.open()
        article_page.get_authorisation_in_selen(user_for_test)
        # time.sleep(3)
        article_page.add_article_by_templates(driver)

    @pytest.mark.skip('Проверка добавления ссылки')
    @allure.title("Проверка добавления ссылки")
    def test_check_text_link(self, driver):
        article_page = ArticlePage(driver, url)
        article_page.open()
        article_page.input_in_my_project(driver)
        article_page.check_text_link(driver)

    # @pytest.mark.skip('delete folders')
    class TestStepByScriptPage:

        @allure.title("Добавление и валидация пошагового сценария")
        def test_step_by_script(self, driver):
            article_page = StepByScriptPage(driver)
            # article_page.open()
            article_page.get_authorisation_in_selen(user_for_test)
            article_page.add_script()
            article_page.check_opened_added_script(driver)
            article_page.check_len_name_content(driver)
            article_page.add_new_step(driver)
            article_page.delete_all()
            article_page.new_step(driver)

        @allure.title("Способ закрепления для пошагового сценария")
        def test_fixing_script(self, driver):
            article_page = StepByScriptPage(driver)
            # article_page.open()
            article_page.get_authorisation_in_selen(user_for_test)
            article_page.add_script()
            article_page.check_step_fixing(driver)

    @pytest.mark.skip('Тест copy paste')
    class TestCopyPastePage:

        @allure.title("Тест copy paste")
        def test_copy_paste(self, driver):
            copy_paste_page = CopyPastePage(driver, url)
            copy_paste_page.open()
            copy_paste_page.input_in_my_project(driver)
            copy_paste_page.add_text_in_article(driver)

    # @pytest.mark.skip('create_draft')
    class TestCreateDraft:

        @allure.title("Создание черновика")
        def test_create_draft(self, driver):
            create_draft_page = CreateDraftPage(driver)
            # create_draft_page.open()
            create_draft_page.get_authorisation_in_selen(user_for_test)
            create_draft_page.open_4_tab(driver)

    class TestFilesPage:

        @allure.title("Добавление файлов через файловый менеджер Статья")
        def test_create_data_files(self, driver):
            article_pages = FilesPages(driver)
            # article_pages.open()
            article_pages.get_authorisation_in_selen(user_for_test)
            article_pages.create_data_files(driver)

        @allure.title("Размер файлов добавленных через файловый менеджер Статья")
        def test_check_size_file(self, driver):
            article_pages = FilesPages(driver)
            # article_pages.open()
            article_pages.get_authorisation_in_selen(user_for_test)
            article_pages.generated_big_file_jpg()
            article_pages.add_big_file(driver)

        @allure.title("Добавление файлов через файловый менеджер Шаблон")
        def test_check_template_download(self, driver):
            article_pages = FilesPages(driver)
            # article_pages.open()
            article_pages.get_authorisation_in_selen(user_for_test)
            article_pages.check_template_download(driver)

        @allure.title("Размер файлов добавленных через файловый менеджер Шаблон")
        def test_check_template_download_bigfile(self, driver):
            article_pages = FilesPages(driver)
            # article_pages.open()
            article_pages.get_authorisation_in_selen(user_for_test)
            article_pages.generated_big_file_exe()
            article_pages.template_download_bigfile(driver)

        # @pytest.mark.skip('download_files_from_files')
        @allure.title("Загрузка файлов в Файлы")
        def test_download_files_from_files(self, driver):
            article_pages = FilesPages(driver)
            # article_pages.open()
            article_pages.get_authorisation_in_selen(user_for_test)
            article_pages.download_files_from_files()

        @allure.title("Размер файлов добавленных через файловый менеджер Сценарий")
        def test_script_download_bigfile(self, driver):
            article_pages = FilesPages(driver)
            # article_pages.open()
            article_pages.get_authorisation_in_selen(user_for_test)
            article_pages.generated_big_file_csv()
            article_pages.check_script_download_bigfile()

        @allure.title("Добавление файлов через файловый менеджер Сценарий")
        def test_script_download(self, driver):
            article_pages = FilesPages(driver)
            # article_pages.open()
            article_pages.get_authorisation_in_selen(user_for_test)
            article_pages.check_script_download(driver)

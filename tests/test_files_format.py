import allure
import pytest
from pages.files_format_page import FilesFormatPage, UnformatFilePage
from pages.users import summer

user_for_test = summer


@pytest.mark.order(2)
@allure.suite("Проверка и загрузка разных форматов")
class TestFilesFormat:

    # @allure.feature("Проверка и загрузка разных форматов")
    class TestCheckFormat:

        @allure.title("Проверка загрузки изображения")
        def test_add_pic_files(self, driver):
            files_format_page = FilesFormatPage(driver)
            # files_format_page.open()
            files_format_page.get_authorisation_in_selen(user_for_test)
            files_format_page.add_files_pict(driver)

        @allure.title("Проверка загрузки аудио")
        def test_audio_files(self, driver):
            files_format_page = FilesFormatPage(driver)
            # files_format_page.open()
            files_format_page.get_authorisation_in_selen(user_for_test)
            files_format_page.check_audio_files(driver)

        @allure.title("Проверка загрузки видео")
        def test_video_files(self, driver):
            files_format_page = FilesFormatPage(driver)
            # files_format_page.open()
            files_format_page.get_authorisation_in_selen(user_for_test)
            files_format_page.check_video_files(driver)

        @allure.title("Подготовка фалов для загрузки ")
        def test_create_pic_video_audio_files(self, driver):
            files_format_page = FilesFormatPage(driver)
            # files_format_page.open()
            files_format_page.get_authorisation_in_selen(user_for_test)
            files_format_page.create_pic_video_audio_files(driver)

        @allure.title("Замена в тип контента Файл - видео")
        def test_file_check_replacement_video(self, driver):
            files_format_page = FilesFormatPage(driver)
            # files_format_page.open()
            files_format_page.get_authorisation_in_selen(user_for_test)
            files_format_page.check_replacement_files_video(driver)

        @allure.title("Замена в тип контента Файл - аудио")
        def test_file_check_replacement_audio(self, driver):
            files_format_page = FilesFormatPage(driver)
            # files_format_page.open()
            files_format_page.get_authorisation_in_selen(user_for_test)
            files_format_page.file_check_replacement_audio(driver)

        @allure.title("Замена в тип контента Файл - картинка")
        def test_file_check_replacement_pic(self, driver):
            files_format_page = FilesFormatPage(driver)
            # files_format_page.open()
            files_format_page.get_authorisation_in_selen(user_for_test)
            files_format_page.file_check_replacement_pic(driver)

    # @allure.step("Тест неформатного файла")
    class TestUnformatFile:

        @allure.title("Добавление неформатного файла в тип контента Файл")
        def test_add_unformat_file(self, driver):
            files_format_page = UnformatFilePage(driver)
            # files_format_page.open()
            files_format_page.get_authorisation_in_selen(user_for_test)
            files_format_page.add_unformat_file_rar_zip(driver)
            files_format_page.add_unformat_file_exel()
            files_format_page.add_unformat_file_other()














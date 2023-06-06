import os
import pathlib
import time
from pathlib import Path
from selenium.common import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException, \
    JavascriptException
from selenium.webdriver.common.by import By
from generator.generator import generated_person, generated_files_audio, generated_files_video
from locators.files_format_locators import FilesFormatPageLocators
from pages.base_page import BasePage


class FilesFormatPage(BasePage):
    Locators = FilesFormatPageLocators()

    def add_all_files(self, path):
        """ADD AFF FILES FUNCTION
        before using put to send keys path"""
        person = generated_person()
        text_area_alert = person.first_name + "-Alert"
        try:
            self.element_is_visible(self.Locators.CREATE_BUTTON).click()
        except StaleElementReferenceException:
            time.sleep(5)
            self.element_is_visible(self.Locators.CREATE_BUTTON).click()
        self.element_is_visible(self.Locators.BUTTON_FILE).click()
        self.element_is_visible(self.Locators.DIRECT_FOLDER).send_keys("Контент 1")
        """del hidden class input file"""
        self.remove_class_script()
        self.element_is_visible(self.Locators.INPUT_FIELD_SELECT_FILE).send_keys(path)
        time.sleep(2)
        """typography"""
        try:
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        except ElementClickInterceptedException:
            time.sleep(5)  # waiting for download file
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_CONTINUE).click()
        self.element_is_visible(self.Locators.BUTTON_CONTINUE).click()
        self.element_is_visible(self.Locators.TEXTAREA_INPUT_TEXT).send_keys(text_area_alert)
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        self.element_is_visible(self.Locators.SVG_CLOSE_ARTICLE).click()

    def add_files_pict(self, driver):
        person = generated_person()
        text_area_alert = person.first_name+"-Alert"
        self.implicitly_wait()
        self.input_in_my_project(driver)
        path1 = str(Path(pathlib.Path.cwd(), "files", "png_g.png"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        path3 = str(Path(pathlib.Path.cwd(), "files", "animal.jpeg"))
        path4 = str(Path(pathlib.Path.cwd(), "files", "gomer.gif"))
        data_pictures = [path1, path2, path3, path4]
        for n in data_pictures:
            i = "png_g"
            if n == path2:
                i = "media"
            elif n == path3:
                i = "animal"
            elif n == path4:
                i = "gomer"
            """input file"""
            try:
                self.element_is_visible(self.Locators.CREATE_BUTTON).click()
            except StaleElementReferenceException:
                time.sleep(5)
                self.element_is_visible(self.Locators.CREATE_BUTTON).click()
            self.element_is_visible(self.Locators.BUTTON_FILE).click()
            self.element_is_visible(self.Locators.DIRECT_FOLDER).send_keys("Контент 1")
            """del hidden class input file"""
            self.remove_class_script()
            self.element_is_visible(self.Locators.INPUT_FIELD_SELECT_FILE).send_keys(n)
            time.sleep(2)
            """check file picture"""
            check_file_pictures = driver.find_element(By.CSS_SELECTOR, f"img[alt='{i}']")
            check_file_pictures.is_displayed()
            """typography"""
            self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
            self.element_is_visible(self.Locators.BUTTON_CONTINUE).click()
            self.element_is_visible(self.Locators.BUTTON_CONTINUE).click()
            self.element_is_visible(self.Locators.TEXTAREA_INPUT_TEXT).send_keys(text_area_alert)
            self.element_is_visible(self.Locators.BUTTON_FINISH).click()
            """check file picture"""
            check_file_pictures = driver.find_element(By.CSS_SELECTOR, f"img[alt='{i}']")
            check_file_pictures.is_displayed()
            self.element_is_visible(self.Locators.SVG_CLOSE_ARTICLE).click()

    def check_audio_files(self, driver):
        self.input_in_my_project(driver)
        audio_files = generated_files_audio()
        for n in audio_files:
            file_audio = Path(pathlib.Path.cwd(), f"{n}")
            path = str(file_audio)
            self.add_all_files(path)
        for n in audio_files:
            file_audio = Path(pathlib.Path.cwd(), f"{n}")
            path = str(file_audio)
            os.remove(path)

    def check_video_files(self, driver):
        self.input_in_my_project(driver)
        video_files = generated_files_video()
        for n in video_files:
            file_audio = Path(pathlib.Path.cwd(), f"{n}")
            path = str(file_audio)
            self.add_all_files(path)
        for n in video_files:
            file_audio = Path(pathlib.Path.cwd(), f"{n}")
            path = str(file_audio)
            os.remove(path)

    def create_pic_video_audio_files(self, driver):
        self.input_in_my_project(driver)
        """create pic, video, audio files"""
        path1 = str(Path(pathlib.Path.cwd(), "files", "png_g.png"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        path3 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path4 = str(Path(pathlib.Path.cwd(), "files", "aac.aac"))
        path5 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        path6 = str(Path(pathlib.Path.cwd(), "files", "mp4.mp4"))
        data_all_files = [path1, path2, path3, path4, path5, path6]
        for n in data_all_files:
            self.add_all_files(path=n)
        return path1, path2, path3, path4, path5, path6

    def check_replacement_files_text(self):
        self.element_is_visible(self.Locators.CHANGE_FILE).click()
        try:
            self.elements_is_present(self.Locators.DELETE_DRAFT, timeout=2).click()
        except TimeoutException:
            print("черновик не сохранен")
        try:
            self.remove_class_script()
        except JavascriptException:
            time.sleep(5)
            self.remove_class_script()
        """check text tooltip format"""
        check_text_type_file = self.element_is_visible(self.Locators.CHECK_TEXT_TYPE_FILE).text
        assert check_text_type_file == "Тип файла:"
        check_text_replacement_alert = self.element_is_visible(self.Locators.CHECK_TEXT_REPLACEMENT_ALERT).text
        assert check_text_replacement_alert == "При замене необходимо использовать тот же тип файла"
        element = self.element_is_visible(self.Locators.SVG_INFORMATION_FOR_TOOLTIP)
        self.action_move_to_element(element)
        """text of tooltip"""
        try:
            list_tooltip = self.element_is_visible(self.Locators.LIST_TOOLTIP).text
        except TimeoutException:
            time.sleep(5)
            list_tooltip = self.element_is_visible(self.Locators.LIST_TOOLTIP).text
        print(list_tooltip)

    def check_replacement_files_video(self, driver):
        path1 = str(Path(pathlib.Path.cwd(), "files", "png_g.png"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        path3 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path4 = str(Path(pathlib.Path.cwd(), "files", "aac.aac"))
        path5 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        path6 = str(Path(pathlib.Path.cwd(), "files", "mp4.mp4"))
        self.input_in_my_project(driver)
        """edit avi file"""
        self.elements_is_present(self.Locators.AVI_FILE_CREATED).click()
        self.check_replacement_files_text()
        """change files """
        self.element_is_visible(self.Locators.INPUT_FIELD_SELECT_FILE).send_keys(path5)
        self.element_is_visible(self.Locators.INPUT_FIELD_SELECT_FILE).send_keys(path4)
        check_text_incorrect_format_replacement = self.element_is_visible(self.Locators.CHECK_TEXT_INCORRECT_FORMAT_REPLACEMENT).text
        assert check_text_incorrect_format_replacement == "Неверный формат файла для замены"
        self.element_is_visible(self.Locators.SVG_TEXT_INCORRECT_FORMAT_CLOSE).click()
        # time.sleep(5)
        # assert list_tooltip == "«Аудио» - файлы форматов: mp3, aac, ac3, aiff, au, dts, flac, m4a, m4p, m4r, mp2, ogg, opus, ra, tta, voc, vox, wav, wma.\n"
        #                        "«Видео» - файлы форматов: mp4, avi, flv, mov, 3gp, m4v, asf, m2ts, m4v, mkv, mts, swf, vob, wmv, webm.\n"
        #                        "«Изображение» - файлы форматов: jpg, jpeg, png, gif.\n"
        #                        "«Документ» - все остальные файлы."

        # check_tooltip_format_support_audio = self.element_is_visible(self.Locators.CHECK_TOOLTIP_FORMAT_SUPPORT_AUDIO)
        # check_tooltip_format_support_audio_value = check_tooltip_format_support_audio.text
        # assert check_tooltip_format_support_audio_value == "- файлы форматов: mp3, aac, ac3, aiff, au, dts, flac, m4a, m4p, m4r, mp2, ogg, opus, ra, tta, voc, vox, wav, wma."
        #
        # check_tooltip_format_support_video = self.element_is_visible(
        #     self.Locators.CHECK_TOOLTIP_FORMAT_SUPPORT_VIDEO).text
        # assert check_tooltip_format_support_video == "- файлы форматов: mp4, avi, flv, mov, 3gp, m4v, asf, m2ts, m4v, mkv, mts, swf, vob, wmv, webm."
        #
        # check_tooltip_format_support_pict = self.element_is_visible(
        #     self.Locators.CHECK_TOOLTIP_FORMAT_SUPPORT_PICT).text
        # assert check_tooltip_format_support_pict == "- файлы форматов: jpg, jpeg, png, gif."
        #
        # check_tooltip_format_support_other = self.element_is_visible(
        #     self.Locators.CHECK_TOOLTIP_FORMAT_SUPPORT_OTHER).text
        # assert check_tooltip_format_support_other == "- все остальные файлы."

    def file_check_replacement_audio(self, driver):
        path1 = str(Path(pathlib.Path.cwd(), "files", "png_g.png"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        path3 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path4 = str(Path(pathlib.Path.cwd(), "files", "aac.aac"))
        path5 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        path6 = str(Path(pathlib.Path.cwd(), "files", "mp4.mp4"))
        self.input_in_my_project(driver)
        """edit avi file"""
        self.elements_is_present(self.Locators.MP3_FILE_CREATED).click()
        self.check_replacement_files_text()
        """replacement check"""
        self.element_is_visible(self.Locators.INPUT_FIELD_SELECT_FILE).send_keys(path4)
        self.element_is_visible(self.Locators.INPUT_FIELD_SELECT_FILE).send_keys(path2)
        time.sleep(3)
        check_text_incorrect_format_replacement = self.element_is_visible(
            self.Locators.CHECK_TEXT_INCORRECT_FORMAT_REPLACEMENT).text
        assert check_text_incorrect_format_replacement == "Неверный формат файла для замены"
        self.element_is_visible(self.Locators.SVG_TEXT_INCORRECT_FORMAT_CLOSE).click()

    def file_check_replacement_pic(self, driver):
        path1 = str(Path(pathlib.Path.cwd(), "files", "png_g.png"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        path3 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path4 = str(Path(pathlib.Path.cwd(), "files", "aac.aac"))
        path5 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        path6 = str(Path(pathlib.Path.cwd(), "files", "mp4.mp4"))
        self.input_in_my_project(driver)
        """edit pic file"""
        try:
            self.elements_is_present(self.Locators.JPEG_FILE_CREATED).click()
        except:
            time.sleep(5)
            self.elements_is_present(self.Locators.JPEG_FILE_CREATED).click()
        self.check_replacement_files_text()
        """replacement check"""
        self.element_is_visible(self.Locators.INPUT_FIELD_SELECT_FILE).send_keys(path1)
        self.element_is_visible(self.Locators.INPUT_FIELD_SELECT_FILE).send_keys(path3)
        time.sleep(3)
        check_text_incorrect_format_replacement = self.element_is_visible(
            self.Locators.CHECK_TEXT_INCORRECT_FORMAT_REPLACEMENT).text
        assert check_text_incorrect_format_replacement == "Неверный формат файла для замены"
        self.element_is_visible(self.Locators.SVG_TEXT_INCORRECT_FORMAT_CLOSE).click()




















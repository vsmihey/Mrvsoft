import os
import pathlib
import time
from pathlib import Path
from selenium.common import StaleElementReferenceException
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
        # for n in audio_files:
        #     file_audio = Path(pathlib.Path.cwd(), f"{n}")
        #     path = str(file_audio)
        #     try:
        #         self.element_is_visible(self.Locators.CREATE_BUTTON).click()
        #     except StaleElementReferenceException:
        #         time.sleep(5)
        #         self.element_is_visible(self.Locators.CREATE_BUTTON).click()
        #     self.element_is_visible(self.Locators.BUTTON_FILE).click()
        #     self.element_is_visible(self.Locators.DIRECT_FOLDER).send_keys("Контент 1")
        #     """del hidden class input file"""
        #     self.remove_class_script()
        #     time.sleep(1)
        #     self.element_is_visible(self.Locators.INPUT_FIELD_SELECT_FILE).send_keys(path)
        #     time.sleep(1)
        #     """typography"""
        #     self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        #     self.element_is_visible(self.Locators.BUTTON_CONTINUE).click()
        #     self.element_is_visible(self.Locators.BUTTON_CONTINUE).click()
        #     self.element_is_visible(self.Locators.TEXTAREA_INPUT_TEXT).send_keys(text_area_alert)
        #     self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        #     self.element_is_visible(self.Locators.SVG_CLOSE_ARTICLE).click()

        # for n in audio_files:
        #     file_audio = Path(pathlib.Path.cwd(), f"{n}")
        #     path = str(file_audio)
        #     os.remove(path)
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









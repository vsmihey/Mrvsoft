import pathlib
import time
from pathlib import Path

from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.files_format_locators import FilesFormatPageLocators
from pages.base_page import BasePage


class FilesFormatPage(BasePage):
    Locators = FilesFormatPageLocators()

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
        """input file"""
        self.element_is_visible(self.Locators.CREATE_BUTTON).click()
        self.element_is_visible(self.Locators.BUTTON_FILE).click()
        self.element_is_visible(self.Locators.DIRECT_FOLDER).send_keys("Контент 1")
        """del hidden class input file"""
        self.remove_class_script()
        self.element_is_visible(self.Locators.INPUT_FIELD_SELECT_FILE).send_keys(path1)
        """check file picture"""
        check_file_pictures = driver.find_element(By.CSS_SELECTOR, "img[alt='png_g']")
        check_file_pictures.is_displayed()
        """typography"""
        self.element_is_visible(self.Locators.BUTTON_TYPOGRAPHY).click()
        self.element_is_visible(self.Locators.BUTTON_CONTINUE).click()
        self.element_is_visible(self.Locators.BUTTON_CONTINUE).click()
        self.element_is_visible(self.Locators.TEXTAREA_INPUT_TEXT).send_keys(text_area_alert)
        self.element_is_visible(self.Locators.BUTTON_FINISH).click()
        """check file picture"""
        check_file_pictures = driver.find_element(By.CSS_SELECTOR, "img[alt='png_g']")
        check_file_pictures.is_displayed()
        self.element_is_visible(self.Locators.SVG_CLOSE_ARTICLE).click()




        time.sleep(5)







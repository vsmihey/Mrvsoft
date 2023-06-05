import datetime
import pathlib
import pickle
import time
from pathlib import Path

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from locators.form_pages_locators import *

from pages.data_login_password import *


# from locators.form_pages_locators import FormPagesLocators as Locators
# from pages.data_login_password import *

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def implicitly_wait(self, time=10):
        self.implicitly_wait(time)

    def element_is_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    """поиск по тексту в DOM дереве даже если элемент не виден"""
    def elements_is_present(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def elements_is_not_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=2):
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def input_in_my_project(self, driver):
        """INPUT IN MY PROJECT"""
        Locators = FormPagesLocators
        self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.INPUT_BUTTON).click()
        try:
            time.sleep(1)
            self.element_is_visible(Locators.TEST_PROJECT).click()
        except TimeoutException:
            self.element_is_visible(Locators.ADD).click()
            self.element_is_visible(Locators.ADD_NAMES_PROJECT).send_keys("selen")
            self.element_is_visible(Locators.ADD_DESCRIPTION_PROJECT).send_keys("test_selenium")
            self.element_is_visible(Locators.ADD_PROJECT_BUTTON).click()
            self.element_is_visible(Locators.TEST_PROJECT).click()
            self.element_is_visible(Locators.CONTENT).click()
            time.sleep(12)
            self.element_is_visible(Locators.CREATE_FOLDER_BUTTON).click()
            self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys("Контент 1")
            self.element_is_visible(Locators.CREATE_FOLDER_BUTTON).click()
        except ElementClickInterceptedException:
            self.element_is_visible(Locators.ADD).click()
            self.element_is_visible(Locators.ADD_NAMES_PROJECT).send_keys("selen")
            self.element_is_visible(Locators.ADD_DESCRIPTION_PROJECT).send_keys("test_selenium")
            self.element_is_visible(Locators.ADD_PROJECT_BUTTON).click()
            self.element_is_visible(Locators.TEST_PROJECT).click()
            self.element_is_visible(Locators.CONTENT).click()
            time.sleep(12)
            self.element_is_visible(Locators.CREATE_FOLDER_BUTTON).click()
            self.element_is_visible(Locators.CREATE_NAME_NEW_FOLDER).send_keys("Контент 1")
            self.element_is_visible(Locators.CREATE_FOLDER_BUTTON).click()

    def screenshot(self):
        offset = datetime.timezone(datetime.timedelta(hours=3))  # timezone (+3)
        now_date = datetime.datetime.now(offset)
        now_date = now_date.strftime('%Y.%m.%d.%H.%M.%S')
        # now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        path = Path(pathlib.Path.cwd(), "screenshots", name_screenshot)
        path = str(path)
        self.driver.save_screenshot(path)

    def implicitly_wait(self):
        self.driver.implicitly_wait(10)

    def remove_class_script(self):
        self.driver.execute_script("""document.querySelector("input[type='file']").removeAttribute('class')""")

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_new_tab(self, driver):
        """open new tab"""
        driver.execute_script("window.open('https://google.com')")

    def get_cookies(self, driver):
        """COOKIES GET"""
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    def insert_cookies(self, driver):
        """COOKIES INSERT"""
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def switch_to_frame(self, frame):
        """input frame"""
        self.driver.switch_to.frame(frame)

    def switch_out_frame(self):
        """out frame"""
        self.driver.switch_to.default_content()

    def download_files_is_visible(self):
        """input is visible for load files"""
        self.driver.execute_script(
            """document.querySelector(".popup__footer.file-manager__foot.file-manager--hidden").removeAttribute('class')""")
        self.driver.execute_script(
            """document.querySelector("form[enctype='multipart/form-data']").removeAttribute('style')""")




    # def element_is_visibility(self, element):
    #     element = driver.find_element_by_css_selector("input")
    #     self.driver.execute_script("arguments[0].style.visibility = 'visible';", element)




import datetime
import pathlib
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
# from locators.form_pages_locators import FormPagesLocators as Locators
# from pages.data_login_password import *


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

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

    # def input_in_my_project(self, driver):
    #     """INPUT IN MY PROJECT"""
    #     self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
    #     self.element_is_visible(Locators.LOGIN).send_keys(login)
    #     self.element_is_visible(Locators.PASSWORD).send_keys(password)
    #     self.element_is_visible(Locators.INPUT_BUTTON).click()
    #     self.element_is_visible(Locators.TEST_PROJECT).click()

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

    # def element_is_visibility(self, element):
    #     element = element.find_element_by_css_selector("input")
    #     self.driver.execute_script("arguments[0].style.visibility = 'visible';", element)




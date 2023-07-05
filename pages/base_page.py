import datetime
import pathlib
import pickle
import random
import time
from pathlib import Path
from random import choice
from string import ascii_uppercase

from selenium.common import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException, \
    ElementNotInteractableException, JavascriptException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from generator.generator import generated_person
from locators.locators_checking_filter_changes import AddFilterChangesLocators
from locators.locators_files_format import FilesFormatPageLocators
from locators.locators_form_pages import *
from locators.locators_topic_database import CreateTopicDatabaseLocators

from pages.data_login_password import *


# from locators.form_pages_locators import FormPagesLocators as Locators
# from pages.data_login_password import *

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def implicitly_wait(self):
        self.implicitly_wait()

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

    def check_button_not_click(self, element):
        """put element is visible or is present"""
        # Locators = AddFilterChangesLocators()
        try:
            element.click()
            click = "True"
        except ElementClickInterceptedException:
            click = "False"
        assert click == "False"
        return click

    def input_in_my_project(self, driver):
        """INPUT IN MY PROJECT"""
        Locators = FormPagesLocators
        try:
            self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        except TimeoutException:
            time.sleep(2)
            self.element_is_visible(Locators.TYPE_AUTHOR).send_keys('Встроенный')
        self.element_is_visible(Locators.LOGIN).send_keys(login)
        self.element_is_visible(Locators.PASSWORD).send_keys(password)
        self.element_is_visible(Locators.INPUT_BUTTON).click()
        try:
            time.sleep(0.5)
            self.element_is_visible(Locators.TEST_PROJECT, timeout=3).click()
        except TimeoutException:
            self.element_is_visible(Locators.ADD).click()
            self.element_is_visible(Locators.ADD_NAMES_PROJECT).send_keys("selen")
            self.element_is_visible(Locators.ADD_DESCRIPTION_PROJECT).send_keys("test_selenium")
            self.element_is_visible(Locators.ADD_PROJECT_BUTTON).click()
            self.element_is_visible(Locators.TEST_PROJECT).click()
            self.element_is_visible(Locators.CONTENT).click()
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
        except StaleElementReferenceException:
            time.sleep(2)
            self.element_is_visible(Locators.TEST_PROJECT).click()

    def screenshot(self):
        offset = datetime.timezone(datetime.timedelta(hours=3))  # timezone (+3)
        now_date = datetime.datetime.now(offset)
        now_date = now_date.strftime('%Y.%m.%d.%H.%M.%S')
        # now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot' + now_date + '.png'
        path = Path(pathlib.Path.cwd(), "screenshots", name_screenshot)
        path = str(path)
        self.driver.save_screenshot(path)

    # def implicitly_wait(self):
    #     self.driver.implicitly_wait(10)

    def remove_class_script(self):
        self.driver.execute_script("""document.querySelector("input[type='file']").removeAttribute('class')""")

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_down_page(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

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

    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
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

    def create_and_open_new_template(self, driver):
        """CREATE AND OPEN NEW TEMPLATE"""
        Locators = FormPagesLocators
        self.element_is_visible(Locators.NEW_TEMPLATE).click()
        self.element_is_visible(Locators.ADD_FIELD_BUTTON).click()
        self.element_is_visible(Locators.LIST_OF_FIELDS_1).click()
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(Locators.SAVE_TEMPLATES).click()
        name_templates = "for download file testing" + str(random.randint(999, 99999))
        self.element_is_visible(Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name_templates)
        self.element_is_visible(Locators.SAVE_TEMPLATES_CHANGE).click()
        self.element_is_visible(Locators.FINISH_BUTTON_SCRIPT).click()
        time.sleep(2)
        templates_download = driver.find_element(By.XPATH, f"//div[text()='{name_templates}']")
        templates_download.click()

    def check_len_name(self, driver, element, n: int = 256):
        # для цифр заменить ascii_uppercase на digits
        """генерация имени по n количеству символов"""
        name_content = ''.join(choice(ascii_uppercase) for i in range(n)) # + str(7)
        """вставка сгенерированного имени в поле ввода"""
        element.send_keys(name_content)
        """получение втсавленного имени"""
        get_name = element.get_attribute("value")
        """возвращение имени которое сгенерировали и имени которое вставилось по ограничениям"""
        return name_content, get_name

    def input_random_symbols(self, element, n: int = 25):
        # для цифр заменить ascii_uppercase на digits
        """генерация имени по n количеству символов"""
        name_content = ''.join(choice(ascii_uppercase) for i in range(n)) # + str(7)
        """вставка сгенерированного имени в поле ввода"""
        element.send_keys(name_content)
        return name_content

    def data_sort(self, data):
        """SORT LIST False сортировка по алфавиту, True - наоборот """
        data_sort = sorted(data, reverse=False)
        return data_sort

    def create_article_base(self):
        """CREATE AND OPEN NEW ARTICLE"""
        # self.input_in_my_project(self.driver)
        Locators = CreateTopicDatabaseLocators
        person = generated_person()
        first_name = person.first_name + str(random.randint(999, 9999))
        text = "Hello"
        name_request = "request " + str(random.randint(999, 9999))
        text_alert = "Alert " + str(random.randint(999, 9999))
        """upload media"""
        try:
            self.element_is_visible(Locators.CREATE_BUTTON, timeout=5).click()
        except (StaleElementReferenceException, TimeoutException):
            time.sleep(3)
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        self.element_is_visible(Locators.CREATE_ARTICLE).click()
        """input name and text an folder direct"""
        self.element_is_visible(Locators.NAME_OF_ARTICLE).send_keys(first_name)
        try:
            self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE, timeout=2).send_keys("Контент 1")
        except ElementNotInteractableException:
            time.sleep(2)
            self.element_is_visible(Locators.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")
        try:
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE, timeout=3).send_keys(text)
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(Locators.TEXT_AREA_ARTICLE).send_keys(text)
        try:
            self.elements_is_present(Locators.UPLOAD_MEDIA, timeout=2).click()
        except TimeoutException:
            time.sleep(5)
            self.elements_is_present(Locators.UPLOAD_MEDIA).click()
        """input is visible for load files"""
        self.driver.execute_script(
            """document.querySelector(".popup__footer.file-manager__foot.file-manager--hidden").removeAttribute('class')""")
        self.driver.execute_script(
            """document.querySelector("form[enctype='multipart/form-data']").removeAttribute('style')""")
        path1 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        data_path = [path1, path2]
        for n in data_path:
            self.element_is_visible(Locators.INPUT_INVISIBLE).send_keys(n)
        time.sleep(5)
        checkbox_insert_files = self.elements_are_visible(Locators.CHECKBOX_INSERT_FILES)
        for n in checkbox_insert_files:
            time.sleep(0.5)
            n.click()
        try:
            self.element_is_visible(Locators.INPUT_SELECTED, timeout=2).click()
        except ElementClickInterceptedException:
            time.sleep(2)
            self.element_is_visible(Locators.INPUT_SELECTED).click()
        # self.element_is_visible(Locators.BUTTON_TYPOGRAPHY).click()
        # self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        # self.element_is_visible(Locators.INPUT_NAME_REQUEST).send_keys(name_request)
        # self.element_is_visible(Locators.BUTTON_ADD).click()
        # self.element_is_visible(Locators.RADIOBUTTON_INCLUDED_CONTENT).click()
        # self.element_is_visible(Locators.BUTTON_FINISH_1).click()
        # self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        # self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        # self.element_is_visible(Locators.INPUT_TEXTAREA_FIELD).send_keys(text_alert)
        # self.element_is_visible(Locators.BUTTON_SUBMIT).click()
        # self.element_is_visible(Locators.GO_TO_CONTENT).click()
        return first_name, name_request, text_alert

    def create_article_by_template_base(self, driver):
        # self.input_in_my_project(self.driver)
        Locators = FormPagesLocators
        actions = ActionChains(driver)
        driver.implicitly_wait(10)
        person = generated_person()
        name = "Templates" + str(random.randint(999, 99999))
        name_content = "Content" + str(random.randint(999, 99999))
        name_request = "как помыть крота" + str(random.randint(999, 99999))
        try:
            self.element_is_visible(Locators.CREATE_BUTTON_ON_HEAD_PAGE).click()
        except StaleElementReferenceException:
            time.sleep(2)
            self.element_is_visible(Locators.CREATE_BUTTON_ON_HEAD_PAGE).click()
        self.element_is_visible(Locators.CREATE_TEMPLATES).click()
        self.element_is_visible(Locators.CREATE_TEMPLATES_NEW).click()
        for i in range(1, 6):
            time.sleep(1)
            self.element_is_visible(Locators.ADD_FIELD_BUTTON).click()
            list_of_fields = driver.find_element(By.XPATH,
                                                 f"//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[{i}]")
            list_of_fields.click()
            self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys(
                "Name" + str(random.randint(999, 99999)))
            self.element_is_visible(Locators.SAVE_TEMPLATES).click()
        self.element_is_visible(Locators.ADD_FIELD_BUTTON).click()
        list_of_fields = driver.find_element(By.XPATH,
                                             f"//div[@class='popuper__dialog m-template-editor__popuper-dialog popuper__dialog--opened']//div[6]")
        list_of_fields.click()
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(Locators.ANSWER).send_keys("answer 1")
        self.element_is_visible(Locators.ADD_ANSWER).click()
        self.element_is_visible(Locators.SAVE_BUTTON).click()
        """step 5"""
        self.element_is_visible(Locators.ADD_FIELD_BUTTON).click()
        self.element_is_visible(Locators.LIST_OF_FIELDS_2).click()
        self.element_is_visible(Locators.INPUT_NAME_OF_FIELD).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(Locators.CHECKBOX_VALUE).click()
        self.element_is_visible(Locators.INPUT_VALUE).send_keys("Name" + str(random.randint(999, 99999)))
        self.element_is_visible(Locators.SAVE_TEMPLATES).click()
        """step 6"""
        self.element_is_visible(Locators.INPUT_NAME_OF_TEMPLATES).send_keys(name)
        # print(name)
        self.element_is_visible(Locators.SAVE_CREATED_TEMPLATES).click()
        self.element_is_visible(Locators.SUBMIT_TEMPLATES).click()
        name_of_templates = driver.find_element(By.XPATH, f"//div[contains(text(),'{name}')]")
        name_of_templates.click()
        self.element_is_visible(Locators.check_name_input).send_keys(name_content)
        # print(name_content)
        time.sleep(3)
        self.element_is_visible(Locators.FOLDER_SAVE).send_keys("Контент 1")
        try:
            field_input = self.element_is_visible(Locators.EDIT_TEMPLATES)
        except TimeoutException:
            time.sleep(1)
            field_input = self.element_is_visible(Locators.EDIT_TEMPLATES)
        field_input_1 = self.element_is_visible(Locators.EDIT_TEMPLATES_1)
        field_input_2 = self.element_is_visible(Locators.EDIT_TEMPLATES_2)
        field_input_3 = self.element_is_visible(Locators.EDIT_TEMPLATES_3)
        field_input_4 = self.element_is_visible(Locators.EDIT_TEMPLATES_4)
        field_input_5 = self.element_is_visible(Locators.EDIT_TEMPLATES_5)
        # field_input_6 = self.element_is_visible(Locators.CHOSE_ANSWER)
        """add and check text correct link"""
        actions.click(field_input_1)
        actions.send_keys("some text")
        actions.click(field_input_2)
        actions.click(field_input_2)
        actions.send_keys("one more some text")
        actions.click(field_input_3)
        actions.click(field_input_3)
        actions.send_keys("777")
        actions.click(field_input_4)
        actions.click(field_input_4)
        actions.send_keys("https://www.something.com")
        actions.click(field_input_5)
        actions.click(field_input_5)
        mail = person.email
        actions.send_keys(mail)
        actions.click(field_input)
        actions.perform()
        time.sleep(1)
        # check_name_of_templates = driver.find_element(By.XPATH, f"//h1[normalize-space()='{name}']")
        # check_name_of_templates.is_displayed()
        # self.element_is_visible(Locators.CHANGE_TEMPLATES_BUTTON).is_displayed()
        # time.sleep(1)
        # self.element_is_visible(Locators.TYPOGRAPHY_TEMPLATE).click()
        # self.element_is_visible(Locators.SUBMIT_TEMPLATES).click()
        # input_request = self.element_is_visible(Locators.INPUT_REQUEST)
        # input_request.send_keys(name_request)
        # self.element_is_visible(Locators.ADD_SEARCH_BUTTON).click()
        # self.element_is_visible(Locators.FIELD_OF_CONTENT_RADIO).click()
        # """fixing_all_fields"""
        # select_field_for_fixing = self.element_is_visible(Locators.SELECT_FIELD_FOR_FIXING)
        # for i in range(6):
        #     time.sleep(0.5)
        #     select_field_for_fixing.click()
        #     select_field_for_fixing.send_keys(Keys.DOWN)
        #     select_field_for_fixing.send_keys(Keys.RETURN)
        # self.element_is_visible(Locators.FINISH_BUTTON).click()
        # self.element_is_visible(Locators.SUBMIT_TEMPLATES).click()
        # self.element_is_visible(Locators.TEXT_AREA_ALERT).send_keys("Name" + str(random.randint(999, 99999)))
        # self.element_is_visible(Locators.SUBMIT_TEMPLATES).click()
        # print(name, name_content, name_of_templates, name_request)
        return name, name_content, name_of_templates, name_request

    def create_script_base(self):
        # self.input_in_my_project(self.driver)
        action = ActionChains(self.driver)
        Locators = CreateTopicDatabaseLocators
        name_request_script = "request_script " + str(random.randint(999, 9999))
        name_script = "NAME_SCRIPT-" + str(random.randint(99, 999))
        try:
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        except StaleElementReferenceException:
            time.sleep(3)
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        self.element_is_visible(Locators.CREATE_SCRIPT).click()
        self.element_is_visible(Locators.NAME_OF_STEP_SCRIPT).send_keys(name_script)
        self.element_is_visible(Locators.DIRECT_FOLDER_NAME).send_keys("Контент 1")
        self.element_is_visible(Locators.ADD_STEP).click()
        self.element_is_visible(Locators.INPUT_NAME_STEP).send_keys("name_step-" + str(random.randint(99, 999)))
        self.element_is_visible(Locators.DROPDOWN_STEP).send_keys("Сценарий завершён")
        try:
            self.element_is_visible(Locators.TEXT_AREA).click()
        except TimeoutException:
            time.sleep(5)
            self.element_is_visible(Locators.TEXT_AREA).click()
        self.element_is_visible(Locators.DROPDOWN).click()
        frame = self.elements_is_present(Locators.FRAME)
        self.switch_to_frame(frame)
        self.element_is_visible(Locators.DROP_DOWN_FILES).click()
        self.switch_out_frame()
        time.sleep(1)
        """for visible"""
        self.download_files_is_visible()
        path1 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        data_path = [path1, path2]
        for n in data_path:
            self.element_is_visible(Locators.INPUT_INVISIBLE).send_keys(n)
        time.sleep(5)
        checkbox_insert_files = self.elements_are_visible(Locators.CHECKBOX_INSERT_FILES)
        for n in checkbox_insert_files:
            time.sleep(0.5)
            n.click()
        try:
            self.element_is_visible(Locators.INPUT_SELECTED).click()
        except ElementClickInterceptedException:
            time.sleep(2)
            self.element_is_visible(Locators.INPUT_SELECTED).click()
        # button_typography = self.elements_is_present(Locators.BUTTON_TYPOGRAPHY_SCRIPT)
        # action.click(button_typography).perform()
        # self.element_is_visible(Locators.INPUT_NAME_REQUEST).send_keys(name_request_script)
        # self.element_is_visible(Locators.BUTTON_ADD).click()
        # self.element_is_visible(Locators.BUTTON_FINISH).click()
        # self.element_is_visible(Locators.BUTTON_FINISH_CONFIRM).click()
        # self.element_is_visible(Locators.BUTTON_FINISH_CONFIRM).click()
        # self.element_is_visible(Locators.INPUT_TEXTAREA_FIELD).send_keys("Alert " + str(random.randint(999, 9999)))
        # self.element_is_visible(Locators.BUTTON_FINISH).click()
        return name_request_script, name_script

    def add_files_base(self, path):
        """ADD AFF FILES FUNCTION
        before using put to send keys path"""
        # example:
        # path2 = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))
        # path5 = str(Path(pathlib.Path.cwd(), "files", "avi.avi"))
        # path3 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        Locators = FilesFormatPageLocators()
        person = generated_person()
        text_area_alert = person.first_name + "-Alert"
        name_script = person.first_name + str(random.randint(999, 9999))
        time.sleep(2)
        try:
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        except StaleElementReferenceException:
            # self.screenshot()
            time.sleep(5)
            self.element_is_visible(Locators.CREATE_BUTTON).click()
        self.element_is_visible(Locators.BUTTON_FILE).click()
        self.element_is_visible(Locators.INPUT_NAME_FILE).send_keys(name_script)
        time.sleep(1)
        self.element_is_visible(Locators.DIRECT_FOLDER).send_keys("Контент 1")
        """del hidden class input file"""
        try:
            self.remove_class_script()
        except JavascriptException:
            time.sleep(5)
        time.sleep(1)
        try:
            self.element_is_visible(Locators.INPUT_FIELD_SELECT_FILE).send_keys(path)
        except TimeoutException:
            # self.screenshot()
            time.sleep(5)
            self.element_is_visible(Locators.INPUT_FIELD_SELECT_FILE).send_keys(path)
        """typography"""
        time.sleep(1)
        # try:
        #     self.element_is_visible(Locators.BUTTON_TYPOGRAPHY).click()
        # except ElementClickInterceptedException:
        #     # self.screenshot()
        #     time.sleep(30)
        #     self.element_is_visible(Locators.BUTTON_TYPOGRAPHY).click()
        # self.element_is_visible(Locators.BUTTON_CONTINUE).click()
        # self.element_is_visible(Locators.BUTTON_CONTINUE).click()
        # self.element_is_visible(Locators.TEXTAREA_INPUT_TEXT).send_keys(text_area_alert)
        # self.element_is_visible(Locators.BUTTON_FINISH).click()
        # self.element_is_visible(Locators.SVG_CLOSE_ARTICLE).click()
        return name_script

    def add_new_person_base(self, driver):
        """ADD NEW PERSON"""
        Locators = FormPagesLocators()
        driver.implicitly_wait(10)
        person = generated_person()
        last_name = person.last_name + str(random.randint(999, 9999))
        first_name = person.first_name
        login = "login" + str(random.randint(999, 9999))
        email = person.email
        self.element_is_visible(Locators.SETTINGS).click()
        self.element_is_visible(Locators.PERSONS).click()
        self.element_is_visible(Locators.NEW_PERSON).click()
        self.element_is_visible(Locators.CHANGE_ADMIN).send_keys('Пользователь')
        time.sleep(1)
        self.remove_class_script()
        """add avatar"""
        avatar = Path(pathlib.Path.cwd(), "animal.jpeg")
        path = str(avatar)
        time.sleep(1)
        self.element_is_visible(Locators.UPLOAD_FILE).send_keys(path)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LOGIN_NEW_PERSON).send_keys(login)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.SAVE_PERSON).click()
        self.element_is_visible(Locators.FRAME_PERSON_CLOSE).click()

        return login





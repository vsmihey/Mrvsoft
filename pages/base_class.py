from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from pages import data_login_password
import pathlib
# Настройки браузера
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--window-size=1920,1080")
# # chrome_options.add_argument("--no-sandbox")
# # chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)
# driver.implicitly_wait(12)


class MainPage:

    def __init__(self, browser, url=data_login_password.url):
        self.browser = browser
        self.url = url

    def open(self, url=None):
        if url is None:
            self.browser.get(self.url)
        else:
            self.browser.get(url)

    def get_actual_url(self):
        return self.browser.current_url

    # def element_is_visible(self, locator, timeout=10):
    #     return Wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
    #
    # def elements_is_present(self, locator, timeout=10):
    #     return Wait(self.browser, timeout).until(EC.presence_of_element_located(locator))
    #
    # def elements_are_visible(self, locator, timeout=10):
    #     return Wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_visible(self, locator, timeout=10):
        """Ожидает появления элемента"""
        return Wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        """Работа с несколькоми элементами (например: список элементов)"""
        return Wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    """поиск по тексту в DOM дереве даже если элемент не виден"""

    def elements_is_present(self, locator, timeout=10):
        """Поиск элемента даже если он не виден"""
        return Wait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=2):
        """Элемент кликабельный"""
        return Wait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def remove_class_script(self):
        """Удаление класса элемента, что бы он стал видимым и с ним можно совершить действие"""
        self.browser.execute_script("""document.querySelector("input[type='file']").removeAttribute('class')""")

    def download_files_is_visible(self):
        """Делает элемент видимым (пример: загрузка файлов)"""
        self.browser.execute_script(
            """document.querySelector(".popup__footer.file-manager__foot.file-manager--hidden").removeAttribute('class')""")
        self.browser.execute_script(
            """document.querySelector("form[enctype='multipart/form-data']").removeAttribute('style')""")

    def switch_to_frame(self, frame):
        """Переход в модалбное окно, на вход принимает модальное окно (пример: работа с виджетами)"""
        self.browser.switch_to.frame(frame)

    def switch_out_frame(self):
        """Выход из модального окна, на вход принимает модальное окно (пример: работа с виджетами)"""
        self.browser.switch_to.default_content()


    def screenshot(self):
        # offset = datetime.timezone(datetime.timedelta(hours=3))  # timezone (+3)
        # now_date = datetime.datetime.now(offset)
        # now_date = now_date.strftime('%Y.%m.%d.%H.%M.%S')
        # now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot'+'.png'
        path = pathlib.Path(pathlib.Path.cwd(), "screenshots", name_screenshot)
        path = str(path)
        self.browser.save_screenshot(path)


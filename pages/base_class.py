import time

from selenium.common import InvalidSelectorException, NoSuchElementException, StaleElementReferenceException, \
    TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from locators.all_locators import FormPagesLocators, FilesFormatPageLocators
from pages import data_login_password
import pathlib


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

    def element_is_visible(self, locator, timeout=10):
        """Ожидает появления элемента"""
        return Wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def element_is_invisible(self, locator, timeout=1):
        """Проверяет, что элемент не появился"""
        return Wait(self.browser, timeout).until(EC.invisibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        """Работа с несколькоми элементами (например: список элементов)"""
        return Wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))

    """поиск по тексту в DOM дереве даже если элемент не виден"""

    def elements_is_present(self, locator, timeout=10):
        """Поиск элемента даже если он не виден"""
        return Wait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=10):
        """Поиск элементов (спика элементов) даже если они не видны"""
        return Wait(self.browser, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        """Элемент кликабельный"""
        return Wait(self.browser, timeout).until(EC.element_to_be_clickable(locator))

    def click_to_element(self, locator, timeout=10):
        """Клик по элементу и обработка возможных ошибок"""
        time.sleep(0.2)
        try:
            return Wait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()
        except StaleElementReferenceException:
            # print('Поймал StaleElementReferenceException')
            return Wait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()
        # except TimeoutException:
        #     # print('Поймал TimeoutException')
        #     self.browser.refresh()
        #     return Wait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()
        # except Exception as e:
        #     print(f'Поймал  {e}')
        #     return Wait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()

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

    def action_move_to_element(self, element, driver):
        """Переход к элементу которого не видно"""
        action = ActionChains(driver)
        action.move_to_element(element).perform()
        # action.perform()

    def go_to_element(self, element):
        """Переход к нужному едлементу (на вход принимает необходимый элемент)"""
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_wizard_template(self, name, driver):
        """Скролл визарда шаблонов на величину в пикселях (x, y),
        name - название шаблона, которое ищем"""
        Locators = FormPagesLocators()
        action = ActionChains(driver)
        n = 0
        while True:
            if n == 10:
                break
            try:
                name_of_templates = driver.find_element(By.XPATH,
                                                        f"//div[@class='m-lms-action-tooltip__text']//span[text()='{name}']")
                name_of_templates.click()
                break
            except (InvalidSelectorException, NoSuchElementException):
                locator_scroller = self.element_is_visible(Locators.MODAL_WINDOW_SCROLLER, timeout=3)  # ползунок
                action.drag_and_drop_by_offset(locator_scroller, "0", "200").perform()
                action.drag_and_drop_by_offset(locator_scroller, "0", "-20").perform()
                # action.perform()

    def delete_draft(self):
        """Нажимает 'Удалить черновик', если всплывает оповещение о наличии черновика"""
        locators = FilesFormatPageLocators
        self.element_is_visible(locators.DELETE_DRAFT).click()

    def screenshot(self):
        # offset = datetime.timezone(datetime.timedelta(hours=3))  # timezone (+3)
        # now_date = datetime.datetime.now(offset)
        # now_date = now_date.strftime('%Y.%m.%d.%H.%M.%S')
        # now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot'+'.png'
        path = pathlib.Path(pathlib.Path.cwd(), 'avatars', name_screenshot)
        path = str(path)
        self.browser.save_screenshot(path)


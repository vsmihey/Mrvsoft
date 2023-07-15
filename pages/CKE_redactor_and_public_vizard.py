import time
from base_class import MainPage
import pathlib
from pathlib import Path
import locators.all_locators as locators

class CKERedactor(MainPage):
    """Виджеты CKE редактора"""

    def input_files(self):
        """Добавление файлов через файловый менеджер"""

        path1 = str(Path(pathlib.Path.cwd(), "files", "mp3.mp3"))
        path2 = str(Path(pathlib.Path.cwd(), "files", "media.jpg"))

        self.elements_is_present(locators.CKERedactor.UPLOAD_MEDIA).click()

        self.browser.execute_script(
            """document.querySelector(".popup__footer.file-manager__foot.file-manager--hidden").removeAttribute(
            'class')""")
        self.browser.execute_script(
            """document.querySelector("form[enctype='multipart/form-data']").removeAttribute('style')""")

        self.element_is_visible(locators.CKERedactor.INPUT_INVISIBLE).send_keys(path1)
        self.element_is_visible(locators.CKERedactor.INPUT_INVISIBLE).send_keys(path2)
        time.sleep(5)

        checkbox_insert_files = self.elements_are_visible(locators.CKERedactor.CHECKBOX_INSERT_FILES)

        for n in checkbox_insert_files:
            time.sleep(0.5)
            n.click()

        self.element_is_visible(locators.CKERedactor.INPUT_SELECTED).click()


class PublicVizard(MainPage):
    """Визард публикации"""

    def publish_button_click(self):
        """Кнопка 'опубликовать' в редакторе"""
        #self.browser.find_element(By.CLASS_NAME, 'm-button.m-button--default.m-button--small').click()

    def next_button_click(self):
        """Кнопка 'продолжить' в визадре"""
        pass

    def finish_button_click(self):
        """Кнопка 'завершить' в визадре"""
        pass

    def notification_text_area(self):
        """Заполнение поля уведомления"""
        pass

    def notification_type(self):
        """Настройка типа оповещения для ранее созданных ролей"""
        pass

import time
import pathlib
from pathlib import Path
from pages.base_class import MainPage
import locators.all_locators as locators
from selenium.webdriver import Keys, ActionChains


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
        time.sleep(3)

        checkbox_insert_files = self.elements_are_visible(locators.CKERedactor.CHECKBOX_INSERT_FILES)

        for n in checkbox_insert_files:
            time.sleep(0.5)
            n.click()

        self.element_is_visible(locators.CKERedactor.INPUT_SELECTED).click()

    def text_area_article(self):
        """Наполнение тела статьи"""
        self.bold_text('Жирный текст')
        self.italic_text('Курсивный текст')
        self.underline_text('Подчеркнутый текст')
        self.superscript_text('Надстрочный текст')
        self.cit('23')

        # self.input_files()
        time.sleep(10)

    def bold_text(self, text):
        """Текст выделяется жирным"""
        self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(f'\n{text}')
        self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(
            Keys.LEFT_CONTROL + Keys.LEFT_SHIFT + Keys.ARROW_UP)
        self.click_to_element(locators.CKERedactor.TEXT_BOLD_FORMAT)
        self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(
            Keys.ARROW_RIGHT)
        self.click_to_element(locators.CKERedactor.TEXT_BOLD_FORMAT)

    def italic_text(self, text):
        """Текст выделяется курсивом"""
        self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(f'\n{text}')
        self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(
            Keys.LEFT_CONTROL + Keys.LEFT_SHIFT + Keys.ARROW_UP)
        self.click_to_element(locators.CKERedactor.TEXT_ITALIC_FORMAT)
        self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(
            Keys.ARROW_RIGHT)
        self.click_to_element(locators.CKERedactor.TEXT_ITALIC_FORMAT)

    def underline_text(self, text):
        """Текст выделяется нижним подчеркиванием"""
        self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(f'\n{text}')
        self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(
            Keys.LEFT_CONTROL + Keys.LEFT_SHIFT + Keys.ARROW_UP)
        self.click_to_element(locators.CKERedactor.TEXT_UNDERLINE_FORMAT)
        self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(
            Keys.ARROW_RIGHT)
        self.click_to_element(locators.CKERedactor.TEXT_UNDERLINE_FORMAT)

    def superscript_text(self, text):
        """Текст выделяется нижним подчеркиванием"""
        self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(f'\n{text}')
        self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(
            Keys.LEFT_CONTROL + Keys.LEFT_SHIFT + Keys.ARROW_UP)
        self.click_to_element(locators.CKERedactor.THREE_DOTS_DOP)
        time.sleep(1)
        ActionChains(self.browser).send_keys(Keys.ARROW_UP).perform()
        time.sleep(1)
        ActionChains(self.browser).send_keys(Keys.ARROW_UP).perform()
        time.sleep(1)
        ActionChains(self.browser).send_keys(Keys.ARROW_UP).perform()
        time.sleep(1)
        ActionChains(self.browser).send_keys(Keys.ENTER).perform()

    def cit(self, text):
        """Текст выделяется нижним подчеркиванием"""
        # self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(f'\n{text}')
        # self.element_is_visible(locators.CreateTopicDatabaseLocators.TEXT_AREA_ARTICLE).send_keys(
        #     Keys.LEFT_CONTROL + Keys.LEFT_SHIFT + Keys.ARROW_UP)
        self.click_to_element(locators.CKERedactor.THREE_DOTS_INSERT)
        time.sleep(1)
        ActionChains(self.browser).send_keys(Keys.ARROW_UP).perform()
        time.sleep(1)
        ActionChains(self.browser).send_keys(Keys.ARROW_UP).perform()
        time.sleep(1)
        ActionChains(self.browser).send_keys(Keys.ARROW_UP).perform()
        time.sleep(1)
        ActionChains(self.browser).send_keys(Keys.ENTER).perform()


class PublicWizard(MainPage):
    """Визард публикации"""

    def publish_button_click(self):
        """Кнопка 'опубликовать' в редакторе"""
        self.click_to_element(locators.WizardPublic.BUTTON_TYPOGRAPHY)

    def save_button_click(self):
        """Кнопка 'сохранить' в редакторе"""
        self.click_to_element(locators.WizardPublic.BUTTON_TYPOGRAPHY)

    def next_and_finish_button_click(self):
        """Кнопка 'продолжить' и 'завершить' в визадре"""
        self.click_to_element(locators.WizardPublic.BUTTON_FINISH)

    def execute_button_click(self):
        """Кнопка 'выполнить' при удалении статьи в визадре"""
        self.click_to_element(locators.WizardPublic.BUTTON_EXECUTE)

    def notification_text_area(self, text='Создание статьи'):
        """Заполнение поля уведомления"""
        self.element_is_visible(locators.WizardPublic.INPUT_TEXT_TEXTAREA).send_keys(text)

    def notification_type(self):
        """Настройка типа оповещения для ранее созданных ролей"""
        self.click_to_element(locators.WizardPublic.ROLE_3_NOTIFICATION)
        self.click_to_element(locators.WizardPublic.ROLE_4)

    def role_access(self):
        """Доступ к статье"""
        self.click_to_element(locators.WizardPublic.CHECKBOX_ALL_ROLES)

    def minor_type(self):
        """Выбор минорных изменений"""
        self.click_to_element(locators.WizardPublic.CHECKBOX_MINOR_EDIT)

    def save_base_article(self):
        """Сохранение статьи"""
        self.publish_button_click()
        self.next_and_finish_button_click()
        self.next_and_finish_button_click()
        self.role_access()
        self.click_to_element(locators.WizardPublic.ROLE_1)
        self.next_and_finish_button_click()
        self.notification_text_area()
        self.notification_type()
        self.next_and_finish_button_click()
        time.sleep(1)

    def save_minor_edit(self):
        """Сохранение статьи с незначительными изменениями"""
        self.publish_button_click()
        self.minor_type()
        self.notification_text_area('Минорное редактирование')
        self.next_and_finish_button_click()
        time.sleep(1)

    def save_major_edit(self, text='Мажорное редактирование'):
        """Сохранение статьи со значительными изменениями"""
        self.publish_button_click()
        self.notification_text_area(text)
        self.next_and_finish_button_click()
        time.sleep(1)

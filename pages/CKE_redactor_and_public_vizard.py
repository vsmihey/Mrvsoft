from base_class import MainPage


class CKERedactor:
    """Виджеты CKE редактора"""
    pass


class PublicVizard(MainPage):
    """Визард публикации"""

    def publish_button_click(self):
        """Кнопка 'опубликовать' в редакторе"""
        self.browser.find_element(By.CLASS_NAME, 'm-button.m-button--default.m-button--small').click()

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

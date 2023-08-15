import random
from pages.creating_panel import CreatingPanel
import locators.all_locators as locators


class Test(CreatingPanel):
    TEST_STRING = ''.join([str(random.randint(1, 9)) for _ in range(1, 515)])

    def input_test_name(self):
        """Ввод имени теста"""
        self.element_is_visible(locators.Test.TEST_NAME).send_keys(self.TEST_STRING)

    def check_test_name_length(self):
        """ Метод проверки корректности названия теста, длина не должна превышать 128 символов, название должно
        соответствовать первым 128 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Test.TEST_NAME).get_attribute('value'))) == 128
        assert self.element_is_visible(locators.Test.TEST_NAME).get_attribute('value') == self.TEST_STRING[:128]

    def input_test_description(self):
        """Ввод описания теста"""
        self.element_is_visible(locators.Test.TEST_DESCRIPTION).send_keys(self.TEST_STRING)

    def check_test_description_length(self):
        """ Метод проверки корректности описания теста, длина не должна превышать 512 символов, название должно
        соответствовать первым 512 символам из тестовой строки"""
        assert len(str(self.element_is_visible(locators.Test.TEST_DESCRIPTION).get_attribute('value'))) == 512
        assert self.element_is_visible(locators.Test.TEST_DESCRIPTION).get_attribute('value') == self.TEST_STRING[:512]

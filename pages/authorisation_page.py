import base_class
import data_login_password
from locators.locators_form_pages import FormPagesLocators
import users


class Authorisation(base_class.MainPage):
    """Класс авторизации в системе"""

    def select_authorisation_type(self):
        """Выбирается "встроенный" тип авторизации"""
        self.browser.find_element(*FormPagesLocators.TYPE_AUTHOR).send_keys('Встроенный')

    def input_login(self, login=data_login_password.user_login_pogodin):
        """Заполняем поле для ввода логина, если не передаем логин по дефолту вводит логин админа"""
        self.browser.find_element(*FormPagesLocators.LOGIN).send_keys(login)

    def input_password(self, password=data_login_password.user_password_pogodin):
        """Заполняем поле для ввода пароля, если не передаем пароль по дефолту вводит пароль админа"""
        self.browser.find_element(*FormPagesLocators.PASSWORD).send_keys(password)

    def confirm_button(self):
        """Нажимаем кнопку войти"""
        self.element_is_visible(FormPagesLocators.INPUT_BUTTON).click()

    def select_project_superbank(self):
        """Выбор проекта СуперБанка"""
        self.element_is_visible(FormPagesLocators.SUPER_BANK_PROJECT).click()

    @staticmethod
    def get_authorisation_in_superbank(user=users.admin, url=None):
        """Метод для прохождения авторизации в проект СуперБанка"""
        # TODO: вынести авторизацию по переданной ссылке в отдельный метод
        try:
            page = Authorisation(url=url)
            page.open()
            page.select_authorisation_type()
            page.input_login(user.login)
            page.input_password(user.password)
            page.confirm_button()
            page.select_project_superbank()
            # time.sleep(0.5)
            assert page.get_actual_url() == f'{data_login_password.url}/news/space/1'
            print('Авторизация - Passed')
        except Exception:
            print('Авторизация - Failed')
            raise Exception


if __name__ == '__main__':
    Authorisation.get_authorisation_in_superbank()
    base_class.driver.delete_all_cookies()
    Authorisation.get_authorisation_in_superbank(users.jerry,
                                                 url='https://test6.minervasoft.ru/content/space/54/folder/236/article/4363')
    base_class.driver.quit()

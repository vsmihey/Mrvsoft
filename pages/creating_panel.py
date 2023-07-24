
from pages.authorisation_page import Authorisation
from locators.locators_form_pages import FormPagesLocators


class CreatingPanel(Authorisation):
    """Класс панели создания статей"""

    def create_button(self):
        """Кнопка для перехода в панель создания статей"""
        self.screenshot()
        self.element_is_visible(FormPagesLocators.CREATE_BUTTON).click()

    def create_base_article_button(self):
        """Кнопка для создания обычной статьи"""
        self.element_is_visible(FormPagesLocators.CREATE_ARTICLE).click()

    def create_sample_article_button(self):
        """Кнопка для создания шаблонной статьи"""
        pass

    def create_stepping_article_button(self):
        """Кнопка для создания пошагового сценария"""
        pass


# if __name__ == '__main__':
#     try:
#         page = CreatingPanel()
#         page.get_authorisation_in_superbank()
#         page.create_button()
#         page.create_base_article_button()
#     except Exception as e:
#         print(e)

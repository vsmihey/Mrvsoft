from pages.base_page import BasePage
from locators.form_pages_locators import FormPagesLocators as Locators



class FavouritesPage(BasePage):

    def favourites(self):
        self.element_is_visible(Locators.CONTENT).click()

    def favourites_add(self):
        pass


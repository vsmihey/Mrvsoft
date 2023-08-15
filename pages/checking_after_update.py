from pages.authorisation_page import Authorisation
from pages.users import minervakms


class CheckingArticleAfterUpdatePage(Authorisation):

    def open_project_superbank(self, driver):
        self.get_authorisation_in_superbank(user=minervakms)

    def open_article_superbank(self):
        pass






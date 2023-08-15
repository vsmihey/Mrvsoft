import time

import allure
import pytest
from pages.checking_after_update import CheckingArticleAfterUpdatePage


@allure.suite("Проверка обычной статьи, статьи по шаблону, пошагового сценария после установки обновления")
@pytest.mark.order(8)
class TestCheckingAfterUpdate:

    @allure.feature("Проверка обычной статьи после установки обновления")
    class TestCheckingArticleAfterUpdate:

        @allure.title("Открытие и проверка содержимого статьи")
        def test_open_created_article(self, driver):
            checking_after_updating = CheckingArticleAfterUpdatePage(driver)
            checking_after_updating.open_project_superbank(driver)
            time.sleep(5)













    @allure.feature("Проверка статьи по шаблону после установки обновления")
    class CheckingTemplateAfterUpdate:
        pass

    @allure.feature("Проверка пошагового сценария после установки обновления")
    class CheckingScriptAfterUpdate:
        pass


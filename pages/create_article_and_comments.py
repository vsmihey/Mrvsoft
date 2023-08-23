import random
import time

from selenium.webdriver.common.by import By

from pages.creating_panel import CreatingPanel
from locators.all_locators import CreateTopicDatabaseLocators as locators_topic_database
from pages.authorisation_page import Authorisation
import locators.all_locators as locators
from pages.CKE_redactor_and_public_wizard import CKERedactor, PublicWizard
from pages.base_class import MainPage
from pages.data_login_password import url
from pages.users import minervakms


class ContentOptions(MainPage):
    """Редактирование, избранное, комментарии и т.д."""

    def redaction(self):
        """Кнопка Редактировать"""
        self.click_to_element(locators.FormPagesLocators.EDIT_ARTICLE)

    def three_dots_button(self):
        """Кнопка Троеточие"""
        self.click_to_element(locators.SearchRuEnLocators.MEATBALL_ARTICLE)

    def delete_button(self):
        """Кнопка Троеточие"""
        self.click_to_element(locators.SearchRuEnLocators.SVG_DEL)

    def restore_button(self):
        """Кнопка 'восстановить'"""
        self.click_to_element(locators.OpenArticle.BOTTOM_BANNER_BUTTON)


class BaseArticleEditor(CreatingPanel, CKERedactor, PublicWizard, ContentOptions):
    """Создание и наполнение Базовой статьи"""
    BASE_ARTICLE_TITLE = 'Название статьи ' + str(random.randint(999, 9999))

    def save_data_in_file(self):
        """Метод сохранения ссылки и названия статьи, данные перезаписываются при каждом вызове"""
        with open(r'data.txt', 'w', encoding='utf8') as file:
            file.write(self.get_actual_url() + '\n')
            file.write(self.BASE_ARTICLE_TITLE)

    def creating_base_article(self, user=minervakms):
        """Создание обычной статьи с наполнением"""
        self.get_authorisation_in_selen(user)
        self.create_button()
        self.create_base_article_button()
        self.title_article()
        self.change_folder()
        self.text_area_article()
        self.save_base_article()
        self.save_data_in_file()

    def title_article(self):
        """Заголовок статьи"""
        self.element_is_visible(locators_topic_database.NAME_OF_ARTICLE).send_keys(self.BASE_ARTICLE_TITLE)

    def change_folder(self):
        """Выбор папки сохранения"""
        self.element_is_visible(locators_topic_database.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")

    def minor_edit_base_article(self, url, user=minervakms):
        """Редактирование статьи и минорное сохранение"""
        self.get_authorisation_in_url(url, user)
        self.redaction()
        self.element_is_visible(locators_topic_database.TEXT_AREA_ARTICLE).send_keys('HeyHey')
        self.save_minor_edit()

    def major_edit_base_article(self, url, user=minervakms):
        """Редактирование статьи и мажорное сохранение"""
        self.get_authorisation_in_url(url, user)
        self.redaction()
        self.element_is_visible(locators_topic_database.TEXT_AREA_ARTICLE).send_keys('Rick and Morty was here')
        self.save_major_edit()

    def major_edit_in_article(self, text="123"):
        """Редактирование в статье и мажорное сохранение"""
        self.redaction()
        time.sleep(5)
        # self.element_is_visible(locators_topic_database.TEXT_AREA_ARTICLE).send_keys('Rick and Morty was here')
        self.save_major_edit(text)

    def delete_base_article(self, url, user=minervakms):
        """Удаление статьи"""
        self.get_authorisation_in_url(url, user)
        self.three_dots_button()
        self.delete_button()
        self.notification_text_area('Удаление')
        self.execute_button_click()
        time.sleep(1)

    def restore_base_article(self, url, user=minervakms):
        """Восстановление статьи"""
        self.get_authorisation_in_url(url, user)
        self.restore_button()
        self.save_major_edit('Восстановление')

    def check_name_in_article(self):
        """Проверка двух изображений в статье"""
        locator = locators.CheckAfterUpdating()
        self.element_is_displayed(locator.CHECK_NAME_ARTICLE)

    def check_version(self):
        """Проверка версии статьи после редактирования"""
        locator = locators.CheckAfterUpdating()
        self.click_to_element(locator.VERSION_CHECK)
        "Проверка что версия статьи заканчивается на '0' "
        number_version_check = self.element_is_visible(locator.NUMBER_VERSION_CHECK).text
        number_version = list(number_version_check)
        assert number_version[-1] == "0"
        self.click_to_element(locator.SVG_VERSION_WINDOW_CLOSE)

    def check_text_artile_heading(self):
        """Проверка оглавления"""
        locator = locators.CheckAfterUpdating()
        heading = self.element_is_displayed(locator.HEADING).text
        assert heading == "Оглавление"

    def check_text_artile_links(self):
        """Проверка вкладки с сылкой"""
        locator = locators.CheckAfterUpdating()
        link1 = self.element_is_displayed(locator.LINK1).text
        assert link1 == "1 Ссылка"
        self.click_to_element(locator.LINK1)
        task = self.element_is_displayed(locator.TASK).get_attribute("src")
        'Иконка'
        assert task == "https://pantheonteam.atlassian.net/favicon.ico"


    def check_images_in_article(self):
        """Проверка двух изображений в статье"""
        locator = locators.CheckAfterUpdating()
        time.sleep(1)
        self.element_is_displayed(locator.IMG1_IN_ARTICLE)
        self.element_is_displayed(locator.IMG2_IN_ARTICLE)

    def check_videos_in_article(self):
        """"Проверка двух видео в статье"""
        locator = locators.CheckAfterUpdating()
        self.element_is_visible(locator.VIDEO1_IN_ARTICLE).is_displayed()
        self.element_is_visible(locator.VIDEO2_IN_ARTICLE).is_displayed()

    def check_audio_in_article(self):
        """Проверка аудио в статье"""
        locator = locators.CheckAfterUpdating()
        self.element_is_visible(locator.AUDIO_IN_ARTICLE).is_displayed()

    def check_table_in_article(self):
        """Проверка таблицы в статье"""
        locator = locators.CheckAfterUpdating()
        self.element_is_visible(locator.TABLE_IN_ARTICLE).is_displayed()
        "Проверка текста в таблице"
        check_text_in_table = self.element_is_visible(locator.CHECK_TEXT_IN_TABLE).text
        assert check_text_in_table == "Строка"

    def check_h_text_in_article(self):
        """Проверка заголовков в статье"""
        locator = locators.CheckAfterUpdating()
        "Проверка h1"
        check_h1_text = self.element_is_visible(locator.CHECK_H1_TEXT).tag_name
        assert check_h1_text == "h1"
        "Проверка h2"
        check_h2_text = self.element_is_visible(locator.CHECK_H2_TEXT).tag_name
        assert check_h2_text == "h2"
        "Проверка h3"
        check_h3_text = self.element_is_visible(locator.CHECK_H3_TEXT).tag_name
        assert check_h3_text == "h3"
        "Проверка обычного текста"
        check_p_text = self.element_is_visible(locator.CHECK_P_TEXT).tag_name
        assert check_p_text == "p"

    def check_styles_text_in_article(self):
        """Проверка стилей текста в статье"""
        locator = locators.CheckAfterUpdating()
        "Проверка strong"
        check_strong_text = self.element_is_visible(locator.CHECK_STRONG_TEXT).tag_name
        assert check_strong_text == "strong"
        "Проверка курсив"
        check_italics_text = self.element_is_visible(locator.CHECK_ITALICS_TEXT).tag_name
        assert check_italics_text == "em"
        "Подчеркнутый"
        check_underlined_text = self.element_is_visible(locator.CHECK_UNDERLINED_TEXT).tag_name
        assert check_underlined_text == "u"
        "Надстрочный"
        check_superscript_text = self.element_is_visible(locator.CHECK_SUPERSCRIPT_TEXT).tag_name
        assert check_superscript_text == "sup"
        "Подстрочный"
        check_superscript_text = self.element_is_visible(locator.CHECK_SUBSCRIPT_TEXT).tag_name
        assert check_superscript_text == "sub"
        "Перечеркнутый"
        check_crossed_out_text = self.element_is_visible(locator.CHECK_CROSSED_OUT_TEXT).tag_name
        assert check_crossed_out_text == "s"

    def check_align_text_in_article(self):
        """Проверка выравнивания текста в статье"""
        locator = locators.CheckAfterUpdating()
        "Выравнивание по центру"
        check_align_center_text = self.element_is_visible(locator.CHECK_ALIGN_CENTER_TEXT).get_attribute("style")
        assert check_align_center_text == "text-align: center;"
        "Выравнивание справа"
        check_align_center_text = self.element_is_visible(locator.CHECK_ALIGN_RIGHT_TEXT).get_attribute("style")
        assert check_align_center_text == "text-align: right;"
        "Выравнивание по центру"
        check_align_center_text = self.element_is_visible(locator.CHECK_ALIGN_JUSTIFY_TEXT).get_attribute("style")
        assert check_align_center_text == "text-align: justify;"

    def check_color_text_in_article(self):
        """Проверка цвета текста в статье"""
        locator = locators.CheckAfterUpdating()
        check_color_text = self.element_is_visible(locator.CHECK_COLOR_TEXT).get_attribute("style")
        assert check_color_text == "color: rgb(235, 51, 35);"
        """Проверка выделения цветом текста в статье"""
        check_highlight_color_text = self.element_is_visible(locator.CHECK_HIGHLIGHT_COLOR_TEXT).get_attribute("style")
        assert check_highlight_color_text == "background-color: rgb(255, 254, 85);"

    def important_block_red(self):
        """Проверка Важное! на красном фоне в статье"""
        locator = locators.CheckAfterUpdating()
        # check_important_block_red = self.element_is_visible(locator.CHECK_IMPORTANT_BLOCK_RED).get_attribute("style")
        self.element_is_visible(locator.CHECK_IMPORTANT_BLOCK_RED).is_displayed()
        # assert check_important_block_red == '--color: #eb3323; --icon: url("/assets/images/icons/important-info.svg"); background-color: rgba(235, 51, 35, 0.15);'

    def check_spoiler(self):
        """Проверка спойлера в статье"""
        locator = locators.CheckAfterUpdating()
        spoiler = self.element_is_visible(locator.CHECK_SPOILER).text
        assert spoiler == "Спойлер"
        self.click_to_element(locator.CHECK_SPOILER)
        spoiler_show = self.element_is_visible(locator.CHECK_SPOILER_SHOW).get_attribute("class")
        assert spoiler_show == "m-spoiler m-spoiler--show"

    def check_link_href(self):
        """Проверка ссылок в статье"""
        locator = locators.CheckAfterUpdating()
        link_href_1 = self.element_is_visible(locator.LINK_HREF).get_attribute("href")
        assert link_href_1 == "https://pantheonteam.atlassian.net/browse/QA-1619"
        link_href_2 = self.element_is_visible(locator.LINK_HREF_ZRJHM).get_attribute("href")
        assert link_href_2 == url + "/content/space/54/article/1938#zrjhm"
        link_href_3 = self.element_is_visible(locator.LINK_HREF_PHONE).get_attribute("href")
        assert link_href_3 == "tel:89367776777"
        # link_href_4 = self.element_is_visible(locator.LINK_HREF_MAIL).get_attribute("href")
        # assert link_href_4 == "mailto:admin@minervakms.ru?subject=%D0%9F%D0%BE%D0%B4%D1%82%D0%B2%D0%B5%D1%80%D0%B4%D0%B8%D1%82%D0%B5"

    def check_name_article_by_template(self):
        """Проверка ссылок в статье"""
        locator = locators.CheckAfterUpdating()
        template_text = self.element_is_visible(locator.TEXT_TEMPLATE).text
        assert template_text == "Шаблонная статья"

    def check_image_in_template1(self):
        """Проверка изображения в статье по шаблону"""
        locator = locators.CheckAfterUpdating()
        time.sleep(1)
        # IMG1_IN_TEMPLATE = (By.XPATH, "// img[@ alt='Germany_Winter_Trains_Brocken_Railway_Rails_Snow_609681_1280x853'])[1]")
        self.element_is_displayed(locator.IMG1_IN_TEMPLATE)

    def check_video_in_template(self):
        """"Проверка видео в статье по шаблону"""
        locator = locators.CheckAfterUpdating()
        self.element_is_displayed(locator.VIDEO_IN_TEMPLATE)



    def check_text_links(self):
        """Проверка вкладки с сылками"""
        locator = locators.CheckAfterUpdating()
        link3 = self.element_is_displayed(locator.LINK3).text
        assert link3 == "3 Ссылки"


class DataParser:
    """Класс получения данных из файла"""

    @staticmethod
    def get_url_from_data_file():
        """Метод парсит ссылку на статью из файла"""
        with open(r'data.txt', 'r', encoding='utf8') as file:
            url = file.readline()
        return url

    @staticmethod
    def get_article_name_from_data_file():
        """Метод парсит название статьи из файла"""
        with open(r'data.txt', 'r', encoding='utf8') as file:
            name = file.readlines()[1]
        return name


class Comments(Authorisation):
    """Добавление комментария в существующую статью"""

    def comment_text_area(self, text='Максимально понятный коммент'):
        """Заполнение поля комментария, можно передать текст для заполнения"""
        self.element_is_visible(locators.Comments.ADD_COMMENT).send_keys(text)

    def send_comment(self):
        """Подтверждение отправки комментария"""
        self.click_to_element(locators.Comments.SEND_COMMENT)

    def disable_the_question_to_the_expert_option(self):
        """Отключение галочки 'с вопросом к эксперту'"""
        self.click_to_element(locators.Comments.EXPERT_QUESTION)

    @staticmethod
    def create_comments(driver, url, user=minervakms):
        """Создание тестового набора комментариев в статье по переданной ссылке, с прохождением авторизации"""
        page = Comments(driver)

        page.get_authorisation_in_url(url, user)

        for i in range(4):
            page.comment_text_area(f'Тестовый комментарий {i + 1}')
            page.send_comment()

        page.disable_the_question_to_the_expert_option()
        page.comment_text_area('Серый комментарий')
        page.send_comment()

        # проверка создания 5 комментариев
        try:
            time.sleep(1)
            check_count_comment = driver.find_element(By.XPATH, "//p[text()='5 комментариев']").text
            # check_count_comment = MainPage.element_is_visible(locators.Comments.CHECK_COUNT_COMMENT).text
            assert check_count_comment == "5 комментариев"
        except AssertionError:
            driver.refresh()
            for i in range(4):
                page.comment_text_area(f'Тестовый комментарий {i + 1}')
                page.send_comment()

            page.disable_the_question_to_the_expert_option()
            page.comment_text_area('Серый комментарий')
            page.send_comment()

    @staticmethod
    def close_first_comment(driver, url, user=minervakms):
        """Закрытие первого комментария"""
        page = Comments(driver)
        page.get_authorisation_in_url(url, user)
        page.click_to_element(locators.Comments.TO_ANSWER_COMMENT_1)
        page.element_is_visible(locators.Comments.COMMENT_BOX).send_keys('Закрытие 1')
        page.click_to_element(locators.Comments.CHECK_BOX_TICK_SOLVED)
        page.click_to_element(locators.Comments.CLOSE_COMMENT)

    @staticmethod
    def close_second_comment(driver, url, user=minervakms):
        """Закрытие первого комментария"""
        page = Comments(driver)
        page.get_authorisation_in_url(url, user)
        page.click_to_element(locators.Comments.TO_ANSWER_COMMENT_2)
        page.element_is_visible(locators.Comments.COMMENT_BOX).send_keys('Закрытие 2')
        page.click_to_element(locators.Comments.CHECK_BOX_TICK_SOLVED)
        page.click_to_element(locators.Comments.CLOSE_COMMENT)

    @staticmethod
    def close_third_comment(driver, url, user=minervakms):
        """Закрытие первого комментария"""
        page = Comments(driver)
        page.get_authorisation_in_url(url, user)
        page.click_to_element(locators.Comments.TO_ANSWER_COMMENT_3)
        page.element_is_visible(locators.Comments.COMMENT_BOX).send_keys('Закрытие 3')
        page.click_to_element(locators.Comments.CHECK_BOX_TICK_SOLVED)
        page.click_to_element(locators.Comments.CLOSE_COMMENT)

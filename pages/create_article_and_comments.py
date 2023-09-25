import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.creating_panel import CreatingPanel
from locators.all_locators import CreateTopicDatabaseLocators as locators_topic_database
from pages.authorisation_page import Authorisation
import locators.all_locators as locators
from pages.CKE_redactor_and_public_wizard import CKERedactor, PublicWizard
from pages.base_class import MainPage
from pages.users import ricksanchez
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
        """Кнопка Удаление"""
        self.click_to_element(locators.SearchRuEnLocators.SVG_DEL)

    def restore_button(self):
        """Кнопка 'восстановить'"""
        self.click_to_element(locators.OpenArticle.BOTTOM_BANNER_BUTTON)


class BaseArticleEditor(CreatingPanel, CKERedactor, PublicWizard, ContentOptions):
    """Создание и наполнение Базовой статьи"""
    BASE_ARTICLE_TITLE = 'Название статьи ' + str(random.randint(999, 9999))
    LINK = ''

    def creating_base_article(self, user=ricksanchez):
        """Создание обычной статьи с наполнением"""
        self.get_authorisation_in_selen(user)
        self.create_button()
        self.create_base_article_button()
        self.title_article()
        self.change_folder()
        self.full_text_area_article()
        self.save_base_article()
        self.LINK = self.get_actual_url()

    def creating_base_article_for_other_content(self, user=ricksanchez):
        """Создание обычной статьи с наполнением"""
        self.get_authorisation_in_selen(user)
        self.create_button()
        self.create_base_article_button()
        self.title_article('Другой контент')
        self.change_folder()
        self.min_text_area_article()
        self.save_base_article()

    def title_article(self, title=BASE_ARTICLE_TITLE):
        """Заголовок статьи"""
        self.element_is_visible(locators_topic_database.NAME_OF_ARTICLE).send_keys(title)

    def change_folder(self):
        """Выбор папки сохранения"""
        self.element_is_visible(locators_topic_database.FOLDER_SAVE_ARTICLE).send_keys("Контент 1")

    def minor_edit_base_article(self, url, user=ricksanchez):
        """Редактирование статьи и минорное сохранение"""
        self.get_authorisation_in_url(url, user)
        self.redaction()
        self.delete_draft()
        self.element_is_visible(locators_topic_database.TEXT_AREA_ARTICLE).send_keys('HeyHey\n')
        self.anchor_widget()
        self.save_minor_edit()

    def major_edit_base_article(self, url, user=ricksanchez):
        """Редактирование статьи и мажорное сохранение"""
        self.get_authorisation_in_url(url, user)
        self.redaction()
        self.delete_draft()
        self.element_is_visible(locators_topic_database.TEXT_AREA_ARTICLE).send_keys('Rick and Morty was here')
        self.save_major_edit()

    def major_edit_in_article(self, text="123"):
        """Редактирование в статье и мажорное сохранение"""
        self.redaction()
        time.sleep(5)
        # self.element_is_visible(locators_topic_database.TEXT_AREA_ARTICLE).send_keys('Rick and Morty was here')
        self.save_major_edit(text)

    def delete_base_article(self, url, user=ricksanchez):
        """Удаление статьи"""
        self.get_authorisation_in_url(url, user)
        time.sleep(3)
        self.three_dots_button()
        try:
            self.delete_button()
        except:
            self.browser.refresh()
            self.three_dots_button()
            self.delete_button()
        self.notification_text_area('Удаление')
        self.execute_button_click()
        time.sleep(3)

    def restore_base_article(self, url, user=ricksanchez):
        """Восстановление статьи"""
        self.get_authorisation_in_url(url, user)
        self.restore_button()
        self.save_major_edit('Восстановление')

    def check_name_in_article(self):
        """Проверка имени в статье"""
        check_name_article = self.element_is_visible(locators.CheckAfterUpdating.CHECK_NAME_ARTICLE).text
        assert check_name_article == "Обычная статья"

    def check_version(self):
        """Проверка версии статьи после редактирования"""
        locator = locators.CheckAfterUpdating()
        self.click_to_element(locator.VERSION_CHECK)
        "Проверка что версия статьи заканчивается на '0' "
        number_version_check = self.element_is_visible(locator.NUMBER_VERSION_CHECK).text
        number_version = list(number_version_check)
        assert number_version[-1] == "0"
        self.click_to_element(locator.SVG_VERSION_WINDOW_CLOSE)

    def check_text_artile_heading(self, driver):
        """Проверка оглавления"""
        locator = locators.CheckAfterUpdating()
        heading = self.element_is_visible(locator.HEADING).text
        assert heading == "Оглавление"
        self.click_to_element(locator.HEADING)
        element1 = self.element_is_visible(locator.HEADING1)
        self.action_move_to_element(element1, driver)
        element2 = self.element_is_visible(locator.HEADING2)
        time.sleep(1)
        self.action_move_to_element(element2, driver)
        self.element_is_displayed(locator.HEADING3)

    def check_text_artile_links(self):
        """Проверка вкладки с сылкой"""
        locator = locators.CheckAfterUpdating()
        link1 = self.element_is_visible(locator.LINK1).text
        assert link1 == "1 Ссылка"
        # self.click_to_element(locator.LINK1)
        for i in range(3):
            try:
                self.click_to_element(locator.LINK1)
                task = self.element_is_visible(locator.TASK).text
                assert task == "Задача"
                break
            except TimeoutException:
                self.browser.refresh()
                time.sleep(2)
                if i == 3:
                    assert 1 == 2, "Должно быть 'Задача' во вкладке 'Ссылка'"
        task = self.element_is_visible(locator.TASK_INTO).get_attribute("src")
        'Проверка конки'
        assert task == "https://pantheonteam.atlassian.net/favicon.ico"
        self.status_code200_check("https://pantheonteam.atlassian.net/favicon.ico")

    def check_images_in_article(self):
        """Проверка двух изображений в статье"""
        locator = locators.CheckAfterUpdating()
        time.sleep(1)
        assert self.element_is_displayed(locator.IMG1_IN_ARTICLE)
        assert self.element_is_displayed(locator.IMG2_IN_ARTICLE)

    def check_videos_in_article(self):
        """"Проверка двух видео в статье"""
        locator = locators.CheckAfterUpdating()
        assert self.element_is_displayed(locator.VIDEO1_IN_ARTICLE)
        assert self.element_is_displayed(locator.VIDEO2_IN_ARTICLE)

    def check_audio_in_article(self):
        """Проверка аудио в статье"""
        locator = locators.CheckAfterUpdating()
        assert self.element_is_displayed(locator.AUDIO_IN_ARTICLE)

    def check_table_in_article(self):
        """Проверка таблицы в статье"""
        locator = locators.CheckAfterUpdating()
        assert self.element_is_displayed(locator.TABLE_IN_ARTICLE)
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

    def paragraph_color_check(self):
        """Проверка цвета Абзацев"""
        locator = locators.CheckAfterUpdating()
        "1"
        paragraph_color_red = self.element_is_visible(locator.PARAGRAPH_COLOR_RED).get_attribute("style")
        assert paragraph_color_red == "color: rgb(235, 51, 35);"
        paragraph_color_bg_yellow = self.element_is_visible(locator.PARAGRAPH_COLOR_BG_YELLOW).get_attribute("style")
        assert paragraph_color_bg_yellow == "background-color: rgb(255, 254, 85);"
        "2"
        paragraph_color_purple = self.element_is_visible(locator.PARAGRAPH_COLOR_PURPLE).get_attribute("style")
        assert paragraph_color_purple == "color: rgb(104, 55, 154);"
        paragraph_color_bg_green = self.element_is_visible(locator.PARAGRAPH_COLOR_BG_GREEN).get_attribute("style")
        assert paragraph_color_bg_green == "background-color: rgb(160, 205, 99);"
        "3"
        paragraph_color_green = self.element_is_visible(locator.PARAGRAPH_COLOR_GREEN).get_attribute("style")
        assert paragraph_color_green == "color: rgb(78, 172, 91);"
        paragraph_color_bg_orange = self.element_is_visible(locator.PARAGRAPH_COLOR_BG_ORANGE).get_attribute("style")
        assert paragraph_color_bg_orange == "background-color: rgb(249, 217, 119);"

    def list_in_article(self):
        self.element_is_displayed(locators.CheckAfterUpdating.LIST_NUMB)
        self.element_is_displayed(locators.CheckAfterUpdating.LIST_MARK)

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
        "Выравнивание по левому краю"
        check_align_left_text = self.element_is_visible(locator.CHECK_ALIGN_LEFT_TEXT).get_attribute("style")
        # print("atrribute: " + check_align_left_text)
        # assert check_align_left_text is None
        "Выравнивание по центру"
        check_align_center_text = self.element_is_visible(locator.CHECK_ALIGN_CENTER_TEXT).get_attribute("style")
        assert check_align_center_text == "text-align: center;"
        "Выравнивание справа"
        check_align_center_text = self.element_is_visible(locator.CHECK_ALIGN_RIGHT_TEXT).get_attribute("style")
        assert check_align_center_text == "text-align: right;"
        "Выравнивание по центру"
        check_align_center_text = self.element_is_visible(locator.CHECK_ALIGN_JUSTIFY_TEXT).get_attribute("style")
        assert check_align_center_text == "text-align: justify;"

    def important_block_red(self):
        """Проверка Важное! на красном фоне в статье"""
        # check_important_block_red = self.element_is_visible(locator.CHECK_IMPORTANT_BLOCK_RED).get_attribute("style")
        self.element_is_displayed(locators.CheckAfterUpdating.CHECK_IMPORTANT_BLOCK_RED)
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
        self.status_code200_check("https://pantheonteam.atlassian.net/browse/QA-1619")
        link_href_2 = self.element_is_visible(locator.LINK_HREF_ZRJHM).get_attribute("href")
        assert link_href_2 == url + "/content/space/54/article/1938#zrjhm"
        self.status_code200_check(url + "/content/space/54/article/1938#zrjhm")
        link_href_3 = self.element_is_visible(locator.LINK_HREF_PHONE).get_attribute("href")
        assert link_href_3 == "tel:89367776777"
        link_href_4 = self.element_is_visible(locator.LINK_HREF_MAIL).get_attribute("href")
        result_link_4 = link_href_4.split("?")
        assert result_link_4[0] == "mailto:admin@minervakms.ru"


class ArticleByTemplate(BaseArticleEditor):
    def check_name_article_by_template(self):
        """Проверка имени статьи"""
        locator = locators.CheckAfterUpdating()
        template_text = self.element_is_visible(locator.TEXT_TEMPLATE).text
        assert template_text == "Шаблонная статья"

    def check_image_in_template1(self):
        """Проверка изображения в статье по шаблону"""
        locator = locators.CheckAfterUpdating()
        time.sleep(1)
        # IMG1_IN_TEMPLATE = (By.XPATH, "// img[@ alt='Germany_Winter_Trains_Brocken_Railway_Rails_Snow_609681_1280x853'])[1]")
        assert self.element_is_displayed(locator.TABS_1_IMG)

    def check_video_in_template(self):
        """"Проверка видео в статье по шаблону"""
        assert self.element_is_displayed(locators.CheckAfterUpdating.VIDEO_IN_TEMPLATE)

    def check_text_links(self):
        """Проверка вкладки с сылками"""
        locator = locators.CheckAfterUpdating()
        link3 = self.element_is_visible(locator.LINK3).text
        assert link3 == "3 Ссылки"
        self.click_to_element(locator.LINK3)
        self.element_is_displayed(locator.TEXT_CONTENT_GOOGLE)
        google_linc_ico = self.element_is_visible(locator.GOOGLE_LINC_ICO).get_attribute("src")
        assert google_linc_ico == "http://google.com/favicon.ico"
        self.status_code200_check("http://google.com/favicon.ico")

    def tabs_1(self):
        """Первая вкладка"""
        assert self.element_is_displayed(locators.CheckAfterUpdating.TABS_1)

    def tabs_1_click(self):
        """Клик Первая вкладка"""
        self.click_to_element(locators.CheckAfterUpdating.TABS_1)

    def tabs_2_click(self):
        """Клик Вторая вкладка"""
        self.click_to_element(locators.CheckAfterUpdating.TABS_2)

    def tabs_3_click(self):
        """Клик Третья вкладка"""
        self.click_to_element(locators.CheckAfterUpdating.TABS_3)

    def tabs_4_click(self):
        """Клик Четвертая вкладка"""
        self.click_to_element(locators.CheckAfterUpdating.TABS_4)

    def check_text_li_template(self):
        """Проверка текста в статье по шаблону список
        текст содержится в самом локаторе"""
        self.element_is_displayed(locators.CheckAfterUpdating.TABS_1_LI_TEXT)

    def check_text_template(self):
        """Проверка текста в статье по шаблону
        текст содержится в самом локаторе"""
        self.element_is_displayed(locators.CheckAfterUpdating.TABS_1_TEXT)

    def check_number_template(self):
        """Проверка числовых значений в статье по шаблону
        текст содержится в самом локаторе"""
        self.element_is_displayed(locators.CheckAfterUpdating.TABS_1_ONLY_NUMBERS)

    def check_contents_link_template(self):
        """Проверка ссылки на контент в статье по шаблону"""
        tabs_1_contents_link = self.element_is_visible(locators.CheckAfterUpdating.TABS_1_CONTENTS_LINK).get_attribute(
            "href")
        assert tabs_1_contents_link == "https://pantheonteam.atlassian.net/browse/QA-1619"

    def check_color_text_bg_template(self):
        """Проверка цвета текста в статье по шаблону"""
        assert self.element_is_visible(locators.CheckAfterUpdating.TABS_1_COLOR).get_attribute(
            "style") == "background-color: rgb(255, 254, 85);"

    def check_smiles_template(self):
        """Проверка смайлов в статье по шаблону"""
        assert self.element_is_displayed(locators.CheckAfterUpdating.TABS_1_SMILES)

    def check_link_tab2_template(self):
        """Проверка ссылки на внешний ресурс в статье по шаблону"""
        tabs_2_link = self.element_is_visible(locators.CheckAfterUpdating.TABS_2_LINK).get_attribute("href")
        assert tabs_2_link == "https://dev3.minervakms.ru/content/space/54/folder/234"

    def check_table_tab2_in_template(self):
        """Проверка таблицы в статье по шаблону"""
        assert self.element_is_displayed(locators.CheckAfterUpdating.TABS_2_TABLE_IN_ARTICLE_TEMPLATE)

    def check_audio_tab2_in_template(self):
        """Проверка аудио в статье по шаблону"""
        assert self.element_is_displayed(locators.CheckAfterUpdating.TABS_2_AUDIO_IN_ARTICLE_TEMPLATE)

    def check_video_tab3_in_template(self):
        """Проверка видео в статье по шаблону"""
        assert self.element_is_displayed(locators.CheckAfterUpdating.TABS_3_VIDEO_IN_ARTICLE_TEMPLATE)

    def check_file_download_tab3_in_template(self):
        """Проверка загрузки файлов в статье по шаблону"""
        tabs_3_file_in_article_template = self.element_is_visible(
            locators.CheckAfterUpdating.TABS_3_FILE_IN_ARTICLE_TEMPLATE).get_attribute("href")
        assert tabs_3_file_in_article_template == url + "/api/storage/space/54/file/4439"

    def check_href_tab4_in_template(self):
        """Проверка ссылки в статье по шаблону"""
        tabs_4_href_template = self.element_is_visible(
            locators.CheckAfterUpdating.TABS_4_HREF_IN_ARTICLE_TEMPLATE).get_attribute("href")
        print(tabs_4_href_template)
        assert tabs_4_href_template == "http://google.com/"

    def check_li_tab4_in_template(self):
        """Проверка списка в статье по шаблону"""
        assert self.element_is_displayed(locators.CheckAfterUpdating.TABS_4_LI_IN_ARTICLE_TEMPLATE)


class ArticleByScript(BaseArticleEditor):

    def check_name_article_by_template(self):
        """Проверка имени статьи по скрипту"""
        template_text = self.element_is_visible(locators.CheckAfterUpdating.CHECK_NAME_IN_ARTICLE_SCRIPT).text
        assert template_text == "Запрос на выпуск кредитной карты (БОТ)"

    def check_script_part1(self):
        """Текст в первой части скрипта"""
        assert self.element_is_visible(
            locators.CheckAfterUpdating.TABS_4_LI_IN_ARTICLE_TEMPLATE).text == "Есть ли у вас постоянное место работы ?"

    def answer_yes_part1(self):
        """Клик по кнопке Да"""
        self.click_to_element(locators.CheckAfterUpdating.BUTTON_PART1)

    def answer_no_part2(self):
        """Клик по кнопке нет"""
        self.click_to_element(locators.CheckAfterUpdating.BUTTON_PART2)

    def check_script_part2(self):
        """Проверка текста во 2 скрипте"""
        assert self.element_is_visible(
            locators.CheckAfterUpdating.CHECK_TEXT_SCRIPT_PAST2).text == "Меняли ли вы место работы за последние 6 месяцев?"

    def answer_yes_part3(self):
        """Клик по кнопке Да"""
        self.click_to_element(locators.CheckAfterUpdating.BUTTON_PART3)

    def check_script_part3(self):
        """Проверка текста в 3 скрипте"""
        assert self.element_is_visible(
            locators.CheckAfterUpdating.CHECK_TEXT_SCRIPT_PAST3).text == "Можете ли вы предоставить банку справку о доходах?"

    def check_script_part4(self):
        """Проверка текста в 4 скрипте"""
        check_text_script_past4 = self.element_is_visible(locators.CheckAfterUpdating.CHECK_TEXT_SCRIPT_PAST4).text
        assert check_text_script_past4 == "Есть ли у вас кредиты в других банках?"

    def answer_no_part4(self):
        """Клик по кнопке нет"""
        self.click_to_element(locators.CheckAfterUpdating.BUTTON_PART4)

    def check_script_end(self):
        """Проверка текста в конце скрипта """
        assert self.element_is_visible(
            locators.CheckAfterUpdating.CHECK_TEXT_ANSWER_END).text == "Сценарий завершен"

    def check_script_button_restart(self):
        """Клик по кнопке начать заново"""
        self.click_to_element(locators.CheckAfterUpdating.CHECK_TEXT_ANSWER_RESTART)

    def edit_and_public_article(self, text="123"):
        """Редактирование и публикация статьи"""
        self.redaction()
        self.click_to_element(locators.CheckAfterUpdating.PUBLISH_BUTTON)
        self.notification_text_area(text)
        self.next_and_finish_button_click()

    def check_version_script(self):
        """Проверка версии статьи после редактирования"""
        self.click_to_element(locators.CheckAfterUpdating.VERSION_CHECK)
        "Проверка что версия статьи заканчивается на '0' "
        number_version_check = self.element_is_visible(locators.CheckAfterUpdating.NUMBER_VERSION_CHECK_SCRIPT).text
        number_version = list(number_version_check)
        assert number_version[-1] == "0"
        self.click_to_element(locators.CheckAfterUpdating.CLOSE_SVG_WINDOW_VERSION_SCRIPT)


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

    def comments_for_creation(self):
        """Создание тестового набора комментариев"""
        for i in range(4):
            time.sleep(0.3)
            self.comment_text_area(f'Тестовый комментарий {i + 1}')
            self.send_comment()

        self.disable_the_question_to_the_expert_option()
        self.comment_text_area('Серый комментарий')
        self.send_comment()

    def create_comments(self):
        """Создание тестового набора комментариев в статье по переданной ссылке"""
        for i in range(3):
            try:
                self.comments_for_creation()
                self.browser.refresh()
                self.check_creating_comments('5 комментариев')
                break
            except AssertionError:
                print('Поймал AssertionError')
                if i == 3:
                    raise AssertionError

    def check_creating_comments(self, text):
        """Проверка, создались ли комментарии в статье"""
        assert self.element_is_visible(locators.Comments.AVAILABLE_COMMENTS_MESSAGE).text == text

    def close_first_comment(self):
        """Закрытие первого комментария"""
        for i in range(3):
            try:
                self.check_creating_comments('5 комментариев')
                self.click_to_element(locators.Comments.TO_ANSWER_COMMENT_1)
                self.element_is_visible(locators.Comments.COMMENT_BOX).send_keys('Закрытие 1')
                self.click_to_element(locators.Comments.CHECK_BOX_TICK_SOLVED)
                self.click_to_element(locators.Comments.CLOSE_COMMENT)
                break
            except AssertionError:
                print('Поймал AssertionError')
                self.browser.refresh()
                if i == 3:
                    raise AssertionError

    def close_second_comment(self):
        """Закрытие второго комментария"""
        for i in range(3):
            try:
                self.check_creating_comments('4 комментария')
                self.click_to_element(locators.Comments.TO_ANSWER_COMMENT_2)
                self.element_is_visible(locators.Comments.COMMENT_BOX).send_keys('Закрытие 2')
                self.click_to_element(locators.Comments.CHECK_BOX_TICK_SOLVED)
                self.click_to_element(locators.Comments.CLOSE_COMMENT)
                break
            except AssertionError:
                print('Поймал AssertionError')
                self.browser.refresh()
                if i == 3:
                    raise AssertionError

    def close_third_comment(self):
        """Закрытие третьего комментария"""
        for i in range(3):
            try:
                self.check_creating_comments('3 комментария')
                self.click_to_element(locators.Comments.TO_ANSWER_COMMENT_3)
                self.element_is_visible(locators.Comments.COMMENT_BOX).send_keys('Закрытие 3')
                self.click_to_element(locators.Comments.CHECK_BOX_TICK_SOLVED)
                self.click_to_element(locators.Comments.CLOSE_COMMENT)
                break
            except AssertionError:
                print('Поймал AssertionError')
                self.browser.refresh()
                if i == 3:
                    raise AssertionError

from selenium.webdriver.common.by import By


class FilesFormatPageLocators:
    CREATE_BUTTON = (By.XPATH, "//div[text()='Создать']")
    BUTTON_FILE = (By.XPATH, "//div[contains(text(),'Файл')]")
    DIRECT_FOLDER = (By.XPATH, "//div[@class='m-ui-select m-ui-input-wrapper-2']//select[@class='m-ui-select__select']")
    INPUT_FIELD_SELECT_FILE = (By.CSS_SELECTOR, "input[type='file']")
    """check picture"""
    CHECK_FILE_PICTURES = (By.CSS_SELECTOR, "img[alt='animal1']")
    """typography"""
    BUTTON_TYPOGRAPHY = (By.XPATH, "//p[text()='Опубликовать файл']")
    BUTTON_CONTINUE = (By.XPATH, "//p[contains(text(),'Продолжить')]")
    TEXTAREA_INPUT_TEXT = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    BUTTON_FINISH = (By.XPATH, "//p[contains(text(),'Завершить')]")
    SVG_CLOSE_ARTICLE = (By.XPATH, "(//*[local-name()='svg'][@class='article-modal__close article-modal__close--white'])[1]")
    """check audio"""
    CHECK_AUDIO = (By.XPATH, "//div[@class='article-modal__container article-modal__container--type-file']//audio[@class='article-modal__content-file']")
    """replacement"""
    CHECK_TEXT_TYPE_FILE = (By.XPATH, "//div[text()='Тип файла:']")
    CHECK_TEXT_TYPE_DOWNLOAD_FILE_VIDEO = (By.XPATH, "//div[text()='Видео']")
    SVG_INFORMATION_FOR_TOOLTIP = (By.XPATH, "//div[@class='article-editor-container-document__sidebar-file-type']//*[local-name()='svg']")
    CHANGE_FILE = (By.XPATH, "//div[contains(text(),'изменить')]")
    CHECK_TEXT_REPLACEMENT_ALERT = (By.XPATH, "//p[text()='При замене необходимо использовать тот же тип файла']")
    CHECK_TOOLTIP_TEXT_AUDIO = (By.XPATH, "//b[text()='Аудио']")
    LIST_TOOLTIP = (By.XPATH, "//div[@class='scroller__content m-role-tooltip__scroller-content']")
    CHECK_TOOLTIP_FORMAT_SUPPORT_AUDIO = (By.XPATH, "//p[text()='- файлы форматов: mp3, aac, ac3, aiff, au, dts, flac, m4a, m4p, m4r, mp2, ogg, opus, ra, tta, voc, vox, wav, wma.']")
    CHECK_TOOLTIP_FORMAT_SUPPORT_VIDEO = (By.XPATH, "//p[text()='- файлы форматов: mp4, avi, flv, mov, 3gp, m4v, asf, m2ts, m4v, mkv, mts, swf, vob, wmv, webm.']")
    CHECK_TOOLTIP_FORMAT_SUPPORT_PICT = (By.XPATH, "//p[text()='- файлы форматов: jpg, jpeg, png, gif.']")
    CHECK_TOOLTIP_FORMAT_SUPPORT_OTHER = (By.XPATH, "//p[text()='- все остальные файлы.']")
    CHECK_TEXT_INCORRECT_FORMAT_REPLACEMENT = (By.XPATH, "//div[text()='Неверный формат файла для замены']")
    SVG_TEXT_INCORRECT_FORMAT_CLOSE = (By.XPATH, "//div[@class='m-popup__close']")
    AVI_FILE_CREATED = (By.XPATH, "//p[text()='avi.avi']")
    MP3_FILE_CREATED = (By.XPATH, "//p[text()='mp3.mp3']")
    JPEG_FILE_CREATED = (By.XPATH, "//p[text()='media.jpg']")
    DELETE_DRAFT = (By.XPATH, "//p[contains(text(),'Удалить черновик')]")
    TEXT_FILE_DOWNLOADS = (By.XPATH, "//h2[contains(text(),'Файл загружается')]")

class UnformatFilePageLocators:
    """check add unformat files"""
    CHECK_TEXT_ONLY_DOWNLOAD_ALERT = (By.XPATH, "//h2[contains(text(),'Файл будет доступен только для скачивания')]")
    CHECK_TEXT_NOT_PREVIEW = (By.XPATH, "//h3[contains(text(),'Для этого формата не доступен предпросмотр')]")
    BUTTON_DOWNLOAD_FILE = (By.XPATH, "//p[contains(text(),'Скачать файл')]")
    BUTTON_TYPOGRAPHY = (By.XPATH, "//p[text()='Опубликовать файл']")
    # BUTTON_TYPOGRAPHY = (By.XPATH, "article-editor-container-document__publish-button-wrapper")
    BUTTON_CONTINUE = (By.XPATH, "//p[contains(text(),'Продолжить')]")
    TEXTAREA_INPUT_TEXT_ALERT = (By.XPATH, "//textarea[@placeholder='Введите текст сообщения']")
    BUTTON_FINISH = (By.XPATH, "//p[contains(text(),'Завершить')]")
    """check after typography"""
    TEXT_CHECK_AFTER_TYPOGRAPHY = (By.XPATH, "(//h2[@class='article-modal__view-unavailable-title'][contains(text(),'Просмотр файла недоступен')])[1]")
    BUTTON_DOWNLOAD_CHECK_AFTER_TYPOGRAPHY = (By.XPATH, "(//p[text()='Скачать файл'])[1]")
    """input file"""
    CREATE_BUTTON = (By.XPATH, "//div[text()='Создать']")
    BUTTON_FILE = (By.XPATH, "//div[contains(text(),'Файл')]")
    DIRECT_FOLDER = (By.XPATH, "(//select[@class='m-ui-select__select'])[3]")
    INPUT_FIELD_SELECT_FILE = (By.CSS_SELECTOR, "input[type='file']")
    SVG_CLOSE_DOWNLOADED_FILE = (By.XPATH, "(//*[local-name()='svg'][@class='article-modal__close article-modal__close--white'])[1]")
    """check text convert files"""
    CHECK_TEXT_NOT_PREVIEW_1 = (By.XPATH, "//h2[text()='Просмотр файла недоступен']")
    TEXT_FILE_DOWNLOADS = (By.XPATH, "//h2[contains(text(),'Файл загружается')]")











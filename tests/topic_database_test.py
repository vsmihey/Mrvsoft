import pytest

from pages.data_login_password import url
from pages.topic_database_page import CreateTopicDatabase


@pytest.mark.order(1)
class TestTopicDatabase:

    class TestCreateTopicDatabase:

        def test_add_topic_database(self, driver):
            topic_database_page = CreateTopicDatabase(driver, url)
            topic_database_page.open()
            topic_database_page.add_topic_database(driver)
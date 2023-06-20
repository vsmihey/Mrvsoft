import random
import sys
import time

from selenium.common import TimeoutException, StaleElementReferenceException

from locators.locators_checking_filter_changes import AddFilterChangesLocators
from pages.base_page import BasePage


class AddFilterChanges(BasePage):

    Locators = AddFilterChangesLocators()

    def add_filters_changes(self, count_filters=3):
        """ADD 3 FILTERS"""
        self.input_in_my_project(self.driver)
        self.screenshot()
        self.element_is_visible(self.Locators.SETTINGS).click()
        self.element_is_visible(self.Locators.FILTERS_FOR_SEARCHING).click()
        try:
            self.element_is_visible(self.Locators.BUTTON_CREATE_GROUP_FILTER, timeout=2).click()
        except TimeoutException:
            """del 3 filters and group"""
            self.element_is_visible(self.Locators.SVG_DEL_1).click()
            self.element_is_visible(self.Locators.SVG_DEL_LIST_CONFIRM).click()
            self.element_is_visible(self.Locators.SVG_DEL_2).click()
            self.element_is_visible(self.Locators.SVG_DEL_LIST_CONFIRM).click()
            self.element_is_visible(self.Locators.SVG_DEL_3).click()
            self.element_is_visible(self.Locators.SVG_DEL_LIST_CONFIRM).click()
            # time.sleep(1)
            # svg_del_list = self.elements_are_visible(self.Locators.SVG_DEL_LIST)
            # for n in svg_del_list:
            #     time.sleep(1)
            #     n.click()
            #     time.sleep(1)
            #     self.element_is_visible(self.Locators.SVG_DEL_LIST_CONFIRM).click()
            self.element_is_visible(self.Locators.CHANGE_NAME_GROUP).click()
            self.element_is_visible(self.Locators.BUTTON_DEL_GROUP).click()
            self.element_is_visible(self.Locators.BUTTON_DEL_GROUP_CONFIRM).click()
            self.element_is_visible(self.Locators.BUTTON_CREATE_GROUP_FILTER).click()
        self.element_is_visible(self.Locators.INPUT_NAME_GROUP).send_keys("Groupname_1")
        self.element_is_visible(self.Locators.BUTTON_GROUP_ADD).click()
        """add filters"""
        for n in range(count_filters):
            self.element_is_visible(self.Locators.BUTTON_ADD_FILTER).click()
            self.element_is_visible(self.Locators.INPUT_NAME_FILTER).send_keys("Filtername"+str(random.randint(999, 9999)))
            self.element_is_visible(self.Locators.BUTTON_ADD_FILTER_ADD).click()


        time.sleep(5)









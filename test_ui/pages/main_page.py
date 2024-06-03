from typing import Tuple

from test_ui.locators.main_page_locators import CURR_INFO, IN_SEARCH_FIELD, IFRAME, \
    LI_SEARCH_RESULT, OF_COUNT, SORT_OFFERS, SORTING_OFFERS, LOWEST_PRiCE, GO_TO_CART
from test_ui.pages.base_page import BasePage
from selenium.webdriver.support.ui import Select


class MainPage(BasePage):

    @property
    def currency_button(self):
        return self.driver.find_element(*CURR_INFO)

    @property
    def search_field(self):
        return self.driver.find_element(*IN_SEARCH_FIELD)

    @property
    def search_result(self):
        return self.driver.find_element(*LI_SEARCH_RESULT)

    def input_into_search_field(self, text: str):
        self.search_field.send_keys(text)

    def chose_from_iframe_by_index(self):
        iframe = self.wait_for(IFRAME)
        self.driver.switch_to.frame(iframe)
        self.wait_for(LI_SEARCH_RESULT)
        self.click(LI_SEARCH_RESULT)
        self.driver.switch_to.default_content()

    def list_of_offers(self):
        self.click(OF_COUNT)

    def sort_offers(self):
        self.click(SORT_OFFERS)

    def sorting_offers(self):
        Select(self.driver.find_element(*SORTING_OFFERS)).select_by_visible_text('по возрастанию цены')

    def choice_by_lowest_price(self):
        self.click(LOWEST_PRiCE)


    def go_to_cart(self):
        self.click(GO_TO_CART)


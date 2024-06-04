from selenium.webdriver.support.select import Select

from test_ui.locators.item_page_locators import BN_SELECT_BY_NAME, BN_SORT_OFFERS, BN_CHOOSING_ITEM, BN_OFFERS, \
    BN_SORT_PRICE, BN_ADD_TO_CART, BN_GO_TO_CART
from test_ui.pages.base_page import BasePage


class ItemPage(BasePage):
    def select_by_name(self):
        Select(self.driver.find_element(*BN_SELECT_BY_NAME)).select_by_visible_text("Apple")

    def sort_by_lowest_price(self):
        Select(self.driver.find_element(*BN_SORT_OFFERS)).select_by_visible_text("Дешевые")

    def choosing_item(self):
        self.click(BN_CHOOSING_ITEM)

    def select_offers(self):
        self.click(BN_OFFERS)

    def choice_at_the_lowest_price(self):
        Select(self.driver.find_element(*BN_SORT_PRICE)).select_by_visible_text("по возрастанию цены")

    def add_to_cart(self):
        self.click(BN_ADD_TO_CART)

    def go_to_cart(self):
        self.click(BN_GO_TO_CART)

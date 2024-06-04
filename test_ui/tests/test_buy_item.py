import time

import pytest

from test_ui.pages.cart_page import CartPage
from test_ui.pages.catalog_page import CatalogPage
from test_ui.pages.item_page import ItemPage



@pytest.fixture(autouse=True)
def catalog_page(driver):
    yield CatalogPage(driver)


@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)


class TestAppleLaptop:

    def test_buy_apple_laptop(self, item_page, catalog_page, cart_page, driver):
        catalog_page.click_catalog()
        catalog_page.computers()
        catalog_page.choosing_laptop()
        time.sleep(1)
        item_page.select_by_name()
        # item_page.sort_by_lowest_price()
        # item_page.choosing_item()
        # item_page.select_offers()
        # item_page.choice_at_the_lowest_price()
        # item_page.add_to_cart()
        # item_page.go_to_cart()

    # def test_play_station(self, main_page, driver):
    #     main_page.input_into_search_field("PlayStation 5")
    #     main_page.chose_from_iframe_by_index()
    #
    # def test_list_of_offers(self, main_page, driver):
    #     self.test_play_station(main_page, driver)
    #     main_page.list_of_offers()
    #
    # def test_sorting(self, main_page, driver):
    #     self.test_list_of_offers(main_page, driver)
    #     main_page.sort_offers()
    #
    # def test_sort_by_price(self, main_page, driver):
    #     self.test_sorting(main_page, driver)
    #     main_page.sorting_offers()
    #
    # def test_choice_by_lowest_price(self, main_page, driver):
    #     self.test_sort_by_price(main_page, driver)
    #     main_page.choice_by_lowest_price()
    #
    # def test_go_to_cart(self, main_page, driver):
    #     self.test_choice_by_lowest_price(main_page, driver)
    #     main_page.go_to_cart()

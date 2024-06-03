import pytest
from test_ui.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


class TestPlayStation:

    def test_play_station(self, main_page, driver):
        main_page.input_into_search_field("PlayStation 5")
        main_page.chose_from_iframe_by_index()

    def test_list_of_offers(self, main_page, driver):
        self.test_play_station(main_page, driver)
        main_page.list_of_offers()

    def test_sorting(self, main_page, driver):
        self.test_list_of_offers(main_page, driver)
        main_page.sort_offers()


    def test_sort_by_price(self, main_page, driver):
        self.test_sorting(main_page, driver)
        main_page.sorting_offers()


    def test_choice_by_lowest_price(self, main_page, driver):
        self.test_sort_by_price(main_page, driver)
        main_page.choice_by_lowest_price()


    def test_go_to_cart(self, main_page, driver):
        self.test_choice_by_lowest_price(main_page, driver)
        main_page.go_to_cart()




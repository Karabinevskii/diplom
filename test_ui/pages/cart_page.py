import allure
import pytest
from test_ui.locators.cart_page_locators import BN_GO_TO_CHECKOUT, TXT_COUNT
from test_ui.pages.base_page import BasePage


class CartPage(BasePage):

    def check_cart_title(self):
        page_title = self.driver.title
        assert page_title == "Корзина заказов onliner.by", f"Navigation wrong. {page_title=} != 'Корзина заказов onliner.by'"

    def check_button_is_clickable(self):
        self.wait_for_element_to_be_clickable(BN_GO_TO_CHECKOUT)

    @allure.step("Check cart count: {num_items}")
    @pytest.mark.parametrize("num_items", [1, 2, 3])
    def check_cart_count(self, num_items: int):
        cart_count = self.text(TXT_COUNT)
        expected_count = f" {num_items}"
        assert expected_count in cart_count, f"Counts are equal, {expected_count=} = {cart_count=}"


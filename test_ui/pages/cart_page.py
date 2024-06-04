from test_ui.pages.base_page import BasePage


class CartPage(BasePage):

    def check_cart_title(self):
        page_title = self.driver.title
        assert page_title == "Корзина заказов onliner.by", f"Navigation wrong. {page_title=} != 'Корзина заказов onliner.by'"
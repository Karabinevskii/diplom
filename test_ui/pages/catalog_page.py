from test_ui.locators.catalog_page_locators import BN_CATALOG, BN_COMPUTERS, BN_LAPTOP
from test_ui.pages.base_page import BasePage


class CatalogPage(BasePage):
    def click_catalog(self):
        self.click(BN_CATALOG)

    def computers(self):
        self.click(BN_COMPUTERS)

    def choosing_laptop(self):
        self.click(BN_LAPTOP)

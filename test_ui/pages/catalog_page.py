import allure
import pytest

from test_ui.locators.catalog_page_locators import BN_CATALOG, BN_COMPUTERS, BN_LAPTOP
from test_ui.pages.base_page import BasePage


@allure.feature("Catalog Page Tests")
class CatalogPage(BasePage):
    @allure.title("Test clicking on catalog")
    def click_catalog(self):
        self.click(BN_CATALOG)

    @allure.title("Test selecting computers")
    def computers(self):
        self.click(BN_COMPUTERS)

    @allure.title("Test choosing a laptop")
    def choosing_laptop(self):
        self.click(BN_LAPTOP)

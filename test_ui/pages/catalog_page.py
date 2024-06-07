import allure
from test_ui.locators.catalog_page_locators import BN_CATALOG, BN_COMPUTERS, BN_LAPTOP
from test_ui.pages.base_page import BasePage


@allure.feature("Catalog Page Tests")
class CatalogPage(BasePage):

    def click_catalog(self):
        with allure.step("Select catalog"):
            self.click(BN_CATALOG)


    def computers(self):
        with allure.step("Select category"):
            self.click(BN_COMPUTERS)

    @allure.title("Test choosing a laptop")
    def choosing_laptop(self):
        with allure.step("Select laptop"):
            self.click(BN_LAPTOP)

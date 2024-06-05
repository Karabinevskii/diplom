from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from test_ui.locators.item_page_locators import BN_SELECT_BY_NAME, BN_SORT_OFFERS, BN_CHOOSING_ITEM, BN_OFFERS, \
    BN_SORT_PRICE, BN_ADD_TO_CART, BN_GO_TO_CART, Apple
from test_ui.pages.base_page import BasePage


class ItemPage(BasePage):

    def select_by_name(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*BN_SELECT_BY_NAME))
        self.click(BN_SELECT_BY_NAME)
        # action.move_to_element(qwer).click()
        # apple_button = self.driver.find_element(*Apple)
        # self.click(Apple)
        # action.move_to_element(apple_button).click()
        # self.wait_for(BN_SELECT_BY_NAME).is_selected()
        # action.scroll_to_element(self.driver.find_element(*BN_SELECT_BY_NAME)).click()
        # time.sleep(2)
        # action.scroll_to_element(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[2]/div[2]/div[11]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div')).select_by_visible_text('Apple')
        # action.move_to_element(self.driver.find_element(Apple)).perform()




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

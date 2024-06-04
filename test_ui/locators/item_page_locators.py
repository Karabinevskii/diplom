from selenium.webdriver.common.by import By

BN_SELECT_BY_NAME = By.XPATH, '(//*[@class="input-style__faux"])[1]'
BN_SORT_OFFERS = By.XPATH, '//*[@class="input-style input-style_more input-style_small input-style_arrow_top-bottom catalog-form__input catalog-form__input_width_full"]'
BN_CHOOSING_ITEM = By.XPATH, '//*[@class="catalog-form__offers-unit catalog-form__offers-unit_primary"][1]'
BN_OFFERS = By.XPATH, '//*[@itemprop="offerCount"]'
BN_SORT_PRICE = By.XPATH, '//*[@class="input-style__real"]'
BN_ADD_TO_CART = By.XPATH, '//*[@class="offers-list__part offers-list__part_action"]'
BN_GO_TO_CART = By.XPATH, '//*[@class="button-style button-style_another button-style_base-alter product-recommended__button"]'

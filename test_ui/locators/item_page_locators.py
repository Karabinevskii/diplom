from selenium.webdriver.common.by import By

BN_SUPER = By.XPATH, '//*[contains(text(), "Суперцена")]'
BN_CHOICE_BRANDS = By.XPATH, '(//div[@class="input-style__wrapper catalog-form__input-wrapper catalog-form__input-wrapper_width_full"])[1]'
BN_CHOICE_APPLE = By.XPATH, '(//div[@class="dropdown-style__checkbox-sign"])[contains(text(), "Apple")]'
BN_SORTING_BY_PRICE = By.XPATH, '(//*[@class="input-style__real"])[26]'
BN_CHOOSING_ITEM = By.XPATH, '(//*[@class="catalog-form__description catalog-form__description_primary catalog-form__description_base-additional catalog-form__description_font-weight_semibold catalog-form__description_condensed-other"])[1]'
BN_OFFERS = By.XPATH, '//*[@itemprop="offerCount"]'
BN_SORT_PRICE = By.XPATH, '//*[@class="input-style__real"]'
BN_VISION = By.XPATH, '//*[@class="offers-description-filter-control__item"]'
BN_ADD_TO_CART = By.XPATH, '(//*[@class="button-style button-style_base-alter offers-list__button offers-list__button_cart button-style_expletive"])[2]'
BN_GO_TO_CART = By.XPATH, '//*[@class="button-style button-style_another button-style_base-alter product-recommended__button"]'
BN_SELECT_BY_NAME = By.XPATH, '//*[@id="container"]/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[2]/div[2]/div[11]/div/div/div[2]/div[2]/div/div[1]/div[1]'
TXT_LAPTOP_PRICE = By.XPATH, 'class="catalog-form__link catalog-form__link_nodecor catalog-form__link_primary-additional catalog-form__link_huge-additional catalog-form__link_font-weight_bold"'

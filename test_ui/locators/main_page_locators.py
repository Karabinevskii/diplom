from selenium.webdriver.common.by import By

CURR_INFO = By.XPATH, '//span[@class="_u js-currency-amount"]'
IN_SEARCH_FIELD = By.XPATH, '//input[@class="fast-search__input"]'

IFRAME = By.XPATH, '//iframe[@class="modal-iframe"]'

LI_SEARCH_RESULT = By.XPATH, '//li[@class="search__result"]'

OF_COUNT = By.XPATH, '//*[@class="button button_orange button_big offers-description__button js-product-prices-count-link"]'

OFFERS_RESULT = By.XPATH, '//*[@class="offers-list"]'
SORT_OFFERS = By.XPATH, ('//*[@class="input-style input-style_more input-style_arrow_top-bottom input-style_base-alter '
                         'offers-list__input offers-list__input_width_auto offers-list__input_max-width_s"]')
SORTING_OFFERS = By.XPATH, '//*[@class="input-style__real"]'

LOWEST_PRiCE = By.XPATH, '//*[@id="container"]/div/div/div/div/div[2]/div[1]/main/div/div/div[2]/div[1]/div/div[3]/div/div[4]/div[1]/div/div/div[2]/div[1]/a[2]'

GO_TO_CART = By.XPATH, '//*[@id="container"]/div/div/div/div/div[2]/div[1]/main/div/div/div[2]/div[1]/div/div[3]/div/div[4]/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/a[2]'


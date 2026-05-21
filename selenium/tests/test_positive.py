import allure
import time

from config.config import BASE_URL
from pages.cart_page import CartPage
from utils.driver_factory import get_driver
from utils.excel_reader import ExcelReader
from utils.logger import get_logger
from utils.allure_utils import screenshot

from pages.home_page import HomePage
from pages.moisturizer_page import MoisturizerPage
from pages.product_page import ProductPage


@allure.feature("Nykaa Positive Tests")
@allure.story("PT_1 - Multiple Product Cart Flow")
def test_multiple_product_cart():
    logger = get_logger()
    driver = get_driver()

    home = HomePage(driver)
    moisturizer = MoisturizerPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    try:
        logger.info("PT_1 | Open Nykaa")
        home.open(BASE_URL)
        time.sleep(5)

        # =========================
        # Navigate to Moisturizer
        # =========================
        logger.info("PT_1 | Navigate to moisturizer")

        home.hover_on_skin()
        home.click_moisturizer()

        time.sleep(5)

        driver.switch_to.window(driver.window_handles[-1])

        # =========================
        # Select Product
        # =========================
        logger.info("PT_1 | Select first product")

        moisturizer.select_first_product()

        time.sleep(5)

        driver.switch_to.window(driver.window_handles[-1])

        # =========================
        # Add Same Product Twice
        # =========================
        logger.info("PT_1 | Add same product first time")

        product.add_to_bag()

        time.sleep(3)

        logger.info("PT_1 | Add same product second time")

        product.add_to_bag()

        time.sleep(3)

        # =========================
        # Open Cart
        # =========================
        logger.info("PT_1 | Open cart")

        product.open_cart()

        time.sleep(5)

        # =========================
        # ASSERTION
        # =========================
        cart_items = cart.get_cart_items()

        assert len(cart_items) >= 1, "Product not added in cart"

        logger.info("ASSERT PASSED | Multiple quantity product added in cart")

        # =========================
        # FINAL SCREENSHOT
        # =========================
        screenshot(driver, "PT_1")

    finally:
        logger.info("PT_1 | Closing browser")
        driver.quit()








@allure.feature("Nykaa Positive Tests")
@allure.story("PT_2 - Remove Product From Cart")
def test_remove_product_from_cart():

    logger = get_logger()
    driver = get_driver()

    home = HomePage(driver)
    moisturizer = MoisturizerPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    try:

        logger.info("PT_2 | Open Nykaa")
        home.open(BASE_URL)

        logger.info("PT_2 | Navigate to moisturizer page")
        home.hover_on_skin()
        home.click_moisturizer()

        driver.switch_to.window(driver.window_handles[-1])

        logger.info("PT_2 | Select first product")
        moisturizer.select_first_product()

        driver.switch_to.window(driver.window_handles[-1])

        logger.info("PT_2 | Add product to cart")
        product.add_to_bag()

        logger.info("PT_2 | Open cart")
        product.open_cart()

        logger.info("PT_2 | Delete product from cart")

        cart.delete_cart_items()

        logger.info("PT_2 | Product removed successfully")

        # =========================
        # ASSERTION
        # =========================

        remaining_products = cart.verify_product_removed()

        assert remaining_products == 0, "Product still present in cart"

        logger.info("ASSERT PASSED | Product removed successfully")


        screenshot(driver, "PT_2")

    finally:
        logger.info("Closing browser")
        driver.quit()


# =====================================================
# PT_3 - Verify Search Bar Is Working
# =====================================================
@allure.feature("Nykaa Positive Tests")
@allure.story("PT_3 - Search Bar Validation")
def test_search_bar():
    excel = ExcelReader("data/test_data.xlsx")
    test_data = excel.get_data()

    logger = get_logger()
    driver = get_driver()

    home = HomePage(driver)

    search_product = test_data["SEARCH_PRODUCT"]

    try:

        logger.info("PT_3 | Open Nykaa")
        home.open(BASE_URL)

        logger.info("PT_3 | Search product")

        home.search_product(search_product)

        logger.info("PT_3 | Verify search result page")

        results = home.get_search_results()

        assert len(results) > 0, "No search results found"

        logger.info("Search results displayed")

        logger.info("Search bar working properly")

        screenshot(driver, "PT_3")

    finally:
        logger.info("Closing browser")
        driver.quit()

#=====================================================
# NT_4 - Cart Persistence After Refresh
# =====================================================
@allure.feature("Nykaa Positive Tests")
@allure.story("PT_4 - Cart Refresh Validation")
def test_cart_after_refresh():

    logger = get_logger()
    driver = get_driver()

    home = HomePage(driver)
    moisturizer = MoisturizerPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)

    try:

        logger.info("PT_4 | Open Nykaa")
        home.open(BASE_URL)

        logger.info("PT_4 | Add product to cart")
        home.hover_on_skin()
        home.click_moisturizer()

        driver.switch_to.window(driver.window_handles[-1])

        moisturizer.select_first_product()

        driver.switch_to.window(driver.window_handles[-1])

        product.add_to_bag()

        product.open_cart()

        logger.info("PT_4 | Refresh cart page")
        driver.refresh()

        logger.info("PT_4 | Validate cart still has product")

        cart_items = cart.get_cart_items()

        assert len(cart_items) >= 1, \
            "Cart became empty after refresh"

        logger.info("ASSERT PASSED | Cart persistence working correctly")

        screenshot(driver, "PT_4")

    finally:
        logger.info("Closing browser")
        driver.quit()
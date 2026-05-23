import time
import allure

from config.config import BASE_URL
from utils.allure_utils import screenshot

from utils.excel_reader import ExcelReader
from utils.driver_factory import get_driver
from utils.logger import get_logger

from pages.home_page import HomePage
from pages.cart_page import CartPage


# =====================================================
# NT_1 - Search Invalid Product
# =====================================================
@allure.feature("Nykaa Negative Tests")
@allure.story("NT_1 - Invalid Product Search")
def test_invalid_product_search():

    logger = get_logger()
    driver = get_driver()

    home = HomePage(driver)

    logger.info("START TEST: test_negative")

    with allure.step("Load test data from Excel"):

        excel = ExcelReader("data/test_data.xlsx")
        test_data = excel.get_data()

        invalid_brand_name = test_data["INVALID_BRAND_NAME"]

    try:

        logger.info("NT_1 | Open Nykaa")
        home.open(BASE_URL)

        logger.info("NT_1 | Search invalid product")

        home.search_product(invalid_brand_name)

        logger.info("NT_1 | Verify no results message")

        no_result = home.get_no_result_message()

        assert no_result.is_displayed(), \
            "No result message not displayed"

        logger.info(
            "ASSERT PASSED | Invalid search handled properly"
        )

        screenshot(driver, "NT_1")

    finally:
        logger.info("Closing browser")
        driver.quit()


# =====================================================
# NT_3 - Proceed Button not in Empty Cart
# =====================================================
@allure.feature("Nykaa Negative Tests")
@allure.story("NT_2 - Proceed Button Not Visible on Empty Cart")
def test_proceed_not_visible_empty_cart():
    logger = get_logger()
    driver = get_driver()

    home = HomePage(driver)
    cart = CartPage(driver)
    try:

        logger.info("NT_2 | Open Nykaa")
        home.open(BASE_URL)

        logger.info("NT_2 | Open cart directly")

        home.open_cart()

        logger.info("NT_2 | Check Proceed button")

        proceed_buttons = cart.get_proceed_buttons()

        # better assertion
        assert len(proceed_buttons) == 0 or not proceed_buttons[0].is_enabled(), \
            "BUG: Proceed button is active even in empty cart"

        logger.info("Proceed button  restricted")
        screenshot(driver, "NT_2")

    finally:
        logger.info("Closing browser")
        driver.quit()
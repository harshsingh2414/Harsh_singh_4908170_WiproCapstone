import time
import allure

from config.config import BASE_URL
from utils.driver_factory import get_driver
from utils.logger import get_logger
from utils.excel_reader import ExcelReader
from pages.home_page import HomePage
from pages.moisturizer_page import MoisturizerPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.allure_utils import screenshot

@allure.feature("Nykaa E2E")
@allure.story("Ordered Screenshot Flow")
@allure.severity(allure.severity_level.CRITICAL)
def test_nykaa_e2e():

    logger = get_logger()
    logger.info("START TEST: test_nykaa_e2e")

    with allure.step("Load test data from Excel"):

        excel = ExcelReader("data/test_data.xlsx")
        test_data = excel.get_data()

        brand_name = test_data["BRAND_NAME"]

        logger.info("LOAD | Test data loaded from Excel successfully")
        logger.info(f"DATA | BRAND_NAME = {brand_name}")

    driver = get_driver()

    home = HomePage(driver)
    moisturizer = MoisturizerPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    login = LoginPage(driver)

    step = 1  # ✅ screenshot order controller

    try:

        # =====================================================
        # STEP 1 - OPEN WEBSITE
        # =====================================================
        with allure.step("Open Nykaa Website"):
            logger.info("OPEN | Nykaa website launched")
            home.open(BASE_URL)

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{step:02d}_homepage",
                attachment_type=allure.attachment_type.PNG
            )
            screenshot(driver,f"{step:02d}_homepage")
            step += 1

        assert "nykaa" in driver.current_url.lower()
        logger.info("ASSERT | Homepage loaded successfully")
        # =====================================================
        # STEP 2 - LOGIN FLOW
        # =====================================================
        with allure.step("Login Flow - Sign In"):
            logger.info("CLICK | Sign In button clicked")
            login.open_login()

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{step:02d}_login_popup",
                attachment_type=allure.attachment_type.PNG
            )
            screenshot(driver, f"{step:02d}_login_popup")
            step += 1
        logger.info("SELECT | Mobile / Email option selected")
        with allure.step("Select Mobile / Email"):
            login.choose_mobile_email()

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{step:02d}_mobile_email",
                attachment_type=allure.attachment_type.PNG
            )
            screenshot(driver, f"{step:02d}_mobile_email")
            step += 1
        logger.info("CLICK | Skip login clicked")
        with allure.step("Click Skip"):
            login.click_skip()

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{step:02d}_skip",
                attachment_type=allure.attachment_type.PNG
            )
            screenshot(driver, f"{step:02d}_skip")
            step += 1

        # =====================================================
        # STEP 3 - NAVIGATE TO MOISTURIZER
        # =====================================================
        with allure.step("Navigate to Moisturizer"):
            logger.info("HOVER | Hovering on Skin menu")
            home.hover_on_skin()
            logger.info("CLICK | Clicking Moisturizer category")
            home.click_moisturizer()

            driver.switch_to.window(driver.window_handles[-1])

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{step:02d}_moisturizer_page",
                attachment_type=allure.attachment_type.PNG
            )
            screenshot(driver, f"{step:02d}_moisturizer_page")
            step += 1

        assert "moisturizer" in driver.current_url.lower()
        logger.info("ASSERT | Moisturizer page validated")
        # =====================================================
        # STEP 4 - BRAND FILTER
        # =====================================================
        with allure.step(f"Select Brand: {brand_name}"):

            logger.info(f"SELECT | Brand selected from Excel: {brand_name}")

            moisturizer.select_brand(brand_name)

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{step:02d}_brand_selected",
                attachment_type=allure.attachment_type.PNG
            )
            screenshot(driver, f"{step:02d}_brand_selected")
            step += 1

        # =====================================================
        # STEP 5 - SELECT PRODUCT
        # =====================================================
        with allure.step("Select First Product"):
            logger.info("CLICK | First product selected")
            moisturizer.select_first_product()

            driver.switch_to.window(driver.window_handles[-1])

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{step:02d}_product_page",
                attachment_type=allure.attachment_type.PNG
            )
            screenshot(driver, f"{step:02d}_product_page")
            step += 1

        assert "/p/" in driver.current_url.lower()
        logger.info("ASSERT | Product page validated")

        # =====================================================
        # STEP 6 - ADD TO BAG
        # =====================================================
        with allure.step("Add To Bag"):
            logger.info("ACTION | Product added to bag")
            product.add_to_bag()

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{step:02d}_added_to_bag",
                attachment_type=allure.attachment_type.PNG
            )
            screenshot(driver, f"{step:02d}_added_to_bag")
            step += 1

        # =====================================================
        # STEP 7 - OPEN CART
        # =====================================================
        with allure.step("Open Cart"):
            logger.info("NAVIGATE | Cart opened")
            product.open_cart()

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{step:02d}_cart_opened",
                attachment_type=allure.attachment_type.PNG
            )
            screenshot(driver, f"{step:02d}_cart_opened")
            step += 1

        # =====================================================
        # STEP 8 - PROCEED
        # =====================================================
        with allure.step("Click Proceed"):
            logger.info("ACTION | Proceed button clicked")
            cart.click_proceed()

            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{step:02d}_final_step",
                attachment_type=allure.attachment_type.PNG
            )
            screenshot(driver, f"{step:02d}_final_step")

        logger.info("E2E TEST COMPLETED SUCCESSFULLY")

    except Exception as e:

        logger.error(f"TEST FAILED: {e}")

        allure.attach(
            driver.get_screenshot_as_png(),
            name="FAILED_STATE",
            attachment_type=allure.attachment_type.PNG
        )

        raise

    finally:
        logger.info("Closing browser")
        driver.quit()
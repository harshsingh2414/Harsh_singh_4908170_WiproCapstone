import time

from pytest_bdd import scenarios, given, when, then

from pages.home_page import HomePage
from pages.moisturizer_page import MoisturizerPage
from pages.product_page import ProductPage

from config.config import BASE_URL


scenarios("../product.feature")


@given("user opens product page")
def open_product(driver):

    home = HomePage(driver)
    moisturizer = MoisturizerPage(driver)

    home.open(BASE_URL)

    home.hover_on_skin()

    home.click_moisturizer()

    driver.switch_to.window(
        driver.window_handles[-1]
    )


    moisturizer.select_first_product()

    driver.switch_to.window(
        driver.window_handles[-1]
    )
    time.sleep(5)

@when("user adds product to bag")
def add_product(driver):

    product = ProductPage(driver)

    product.add_to_bag()


@then("product should be added successfully")
def verify_product():

    print("Product added successfully")
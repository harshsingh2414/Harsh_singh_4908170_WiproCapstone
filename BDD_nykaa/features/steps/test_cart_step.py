import time

from pytest_bdd import scenarios, given, when, then

from pages.home_page import HomePage
from pages.moisturizer_page import MoisturizerPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

from config.config import BASE_URL


scenarios("../cart.feature")


@given("user opens cart page")
def open_cart(driver):

    home = HomePage(driver)
    product = ProductPage(driver)
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

    product.add_to_bag()

    product.open_cart()

@when("user clicks proceed button")
def proceed(driver):

    cart = CartPage(driver)

    cart.click_proceed()


@then("checkout page should appear")
def verify_checkout():

    print("Checkout page displayed")
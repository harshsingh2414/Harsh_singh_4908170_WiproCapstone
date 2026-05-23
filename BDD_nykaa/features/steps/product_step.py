from behave import when
from pages.product_page import ProductPage
import allure


# -----------------------------
# ADD PRODUCT TO BAG
# -----------------------------
@allure.step("Add Product To Bag")
@when("user adds product to bag")
def step_add_to_bag(context):

    context.logger.info("Adding product to bag")

    context.product_page = ProductPage(context.driver)

    context.logger.info("Product Page initialized")

    context.product_page.add_to_bag()

    context.logger.info("Product added to bag successfully")

    # ASSERT
    cart_count = context.product_page.get_cart_count()

    assert cart_count >= 1, "Product not added to bag"


# -----------------------------
# OPEN CART FROM PRODUCT PAGE
# -----------------------------
@allure.step("Open Cart From Product Page")
@when("user opens cart from product page")
def step_open_cart(context):

    context.logger.info("Opening cart from product page")

    context.product_page = ProductPage(context.driver)

    context.logger.info("Product Page initialized")

    context.product_page.open_cart()

    context.logger.info("Cart opened successfully from product page")

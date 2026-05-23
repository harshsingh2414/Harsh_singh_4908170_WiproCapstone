from behave import given, when, then
from pages.cart_page import CartPage
import allure


# -----------------------------
# INIT CART PAGE (SAFE)
# -----------------------------
def get_cart_page(context):

    if not hasattr(context, "cart_page"):

        context.logger.info("Initializing Cart Page")

        context.cart_page = CartPage(context.driver)

    return context.cart_page


# -----------------------------
# PROCEED BUTTON
# -----------------------------
@allure.step("Click Proceed Button")
@then("user clicks on proceed button")
def step_click_proceed(context):

    context.logger.info("Clicking proceed button")

    get_cart_page(context).click_proceed()

    context.logger.info("Proceed button clicked successfully")


# -----------------------------
# LOGIN BUTTON IN CART
# -----------------------------
@allure.step("Click Login Button From Cart")
@when("user clicks login button from cart")
def step_click_login(context):

    context.logger.info("Clicking login button from cart")

    get_cart_page(context).click_login_button()

    context.logger.info("Login button clicked successfully")


# -----------------------------
# SIGNUP BUTTON IN CART
# -----------------------------
@allure.step("Click Signup Button From Cart")
@when("user clicks signup button from cart")
def step_click_signup(context):

    context.logger.info("Clicking signup button from cart")

    get_cart_page(context).click_signup_button()

    context.logger.info("Signup button clicked successfully")


# -----------------------------
# SKIP BUTTON
# -----------------------------
@allure.step("Click Skip Button From Cart Popup")
@when("user clicks skip button from cart popup")
def step_click_skip(context):

    context.logger.info("Clicking skip button from cart popup")

    get_cart_page(context).click_skip()

    context.logger.info("Skip button clicked successfully")


# -----------------------------
# DELETE PRODUCT FROM CART
# -----------------------------
@allure.step("Delete Product From Cart")
@when("user deletes product from cart")
def step_delete_product(context):

    context.logger.info("Deleting product from cart")

    get_cart_page(context).delete_cart_items()

    context.logger.info("Product deleted successfully")


# -----------------------------
# VERIFY PRODUCT REMOVED
# -----------------------------
@allure.step("Verify Product Removed From Cart")
@then("product should be removed from cart")
def step_verify_removed(context):

    context.logger.info("Verifying product removal from cart")

    remaining = get_cart_page(context).verify_product_removed()

    assert remaining == 0, f"Products still in cart: {remaining}"

    context.logger.info("Product removed successfully")


# -----------------------------
# GET CART ITEMS
# -----------------------------
@allure.step("Verify Cart Contains Items")
@then("cart should contain items")
def step_cart_items(context):

    context.logger.info("Checking cart items")

    items = get_cart_page(context).get_cart_items()

    assert len(items) > 0, "Cart is empty"

    context.logger.info(f"Cart contains {len(items)} item(s)")


# -----------------------------
# VERIFY PROCEED BUTTON EXISTS
# -----------------------------
@allure.step("Verify Proceed Button Visibility")
@then("proceed button should be visible")
def step_verify_proceed(context):

    context.logger.info("Checking proceed button visibility")

    buttons = get_cart_page(context).get_proceed_buttons()

    assert len(buttons) == 0, "BUG: Proceed button is visible in empty cart"

    context.logger.info("Proceed button is visible")

# -----------------------------
# REFRESH CART PAGE
# -----------------------------
@allure.step("Refresh Cart Page")
@when("user refreshes cart page")
def step_refresh_cart(context):

    context.logger.info("Refreshing cart page")

    context.driver.refresh()

    context.logger.info("Cart page refreshed successfully")
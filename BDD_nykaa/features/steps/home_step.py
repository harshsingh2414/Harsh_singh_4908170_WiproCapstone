from behave import given, when, then
from pages.home_page import HomePage
from config import config

import allure



# -----------------------------
# OPEN WEBSITE (MAIN ENTRY POINT)
# -----------------------------
@allure.step("Open Nykaa Website")
@given("user opens Nykaa website")
def step_open_website(context):

    context.logger.info("Opening Nykaa website")

    if not hasattr(context, "home_page"):

        context.logger.info("Initializing Home Page")

        context.home_page = HomePage(context.driver)

    context.home_page.open(config.BASE_URL)

    context.logger.info("Nykaa website opened successfully")


# -----------------------------
# HOVER SKIN MENU
# -----------------------------
@allure.step("Hover On Skin Menu")
@when("user hovers on skin menu")
def step_hover_skin(context):

    context.logger.info("Hovering on skin menu")

    if not hasattr(context, "home_page"):

        context.logger.info("Initializing Home Page")

        context.home_page = HomePage(context.driver)

    context.home_page.hover_on_skin()

    context.logger.info("Hovered on skin menu successfully")


# -----------------------------
# CLICK MOISTURIZER CATEGORY
# -----------------------------
@allure.step("Click Moisturizers Category")
@when("user clicks on moisturizers category")
def step_click_moisturizer(context):

    context.logger.info("Clicking moisturizers category")

    if not hasattr(context, "home_page"):

        context.logger.info("Initializing Home Page")

        context.home_page = HomePage(context.driver)

    context.home_page.click_moisturizer()

    context.logger.info("Switching to moisturizer tab")

    context.driver.switch_to.window(
        context.driver.window_handles[-1]
    )

    context.logger.info("Moisturizer category opened successfully")


# -----------------------------
# SEARCH PRODUCT
# -----------------------------
@allure.step("Search Product")
@when('user searches for "{product_name}"')
def step_search_product(context, product_name):

    context.logger.info(
        f"Searching for product: {product_name}"
    )

    if not hasattr(context, "home_page"):

        context.logger.info("Initializing Home Page")

        context.home_page = HomePage(context.driver)

    context.home_page.search_product(product_name)

    context.logger.info(
        f"Search completed for: {product_name}"
    )


# -----------------------------
# GET SEARCH RESULTS
# -----------------------------
@allure.step("Verify Search Results")
@then("search results should be displayed")
def step_verify_results(context):

    context.logger.info("Verifying search results")

    results = context.home_page.get_search_results()

    assert len(results) > 0, "No search results found"

    context.logger.info(
        f"Search results displayed successfully: {len(results)} item(s)"
    )


# -----------------------------
# NO RESULT MESSAGE
# -----------------------------
@allure.step("Verify No Result Message")
@then("no results message should be shown")
def step_no_results(context):

    context.logger.info("Checking no result message")

    msg = context.home_page.get_no_result_message()

    assert msg.is_displayed(), "No result message not displayed"

    context.logger.info("No result message displayed successfully")


# -----------------------------
# OPEN CART
# -----------------------------
@allure.step("Open Cart")
@when("user opens cart")
def step_open_cart(context):

    context.logger.info("Opening cart")



    context.logger.info("Initializing Home Page")

    context.home_page = HomePage(context.driver)

    context.home_page.open_cart()

    context.logger.info("Cart opened successfully")
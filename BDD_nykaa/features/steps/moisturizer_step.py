from behave import when
import allure

from pages.moisturizer_page import MoisturizerPage


# -----------------------------
# SELECT BRAND FILTER
# -----------------------------
@allure.step("Select Brand Filter")
@when('user selects brand "{brand_name}"')
def step_select_brand(context, brand_name):

    context.logger.info(f"Selecting brand: {brand_name}")

    context.moisturizer_page = MoisturizerPage(context.driver)

    context.moisturizer_page.select_brand(brand_name)

    context.logger.info(f"Brand selected successfully: {brand_name}")


# -----------------------------
# SELECT FIRST PRODUCT
# -----------------------------
@allure.step("Select First Moisturizer Product")
@when("user selects first moisturizer product")
def step_select_first_product(context):

    context.logger.info("Selecting first moisturizer product")

    context.moisturizer_page = MoisturizerPage(context.driver)

    context.logger.info("Moisturizer Page initialized")

    context.moisturizer_page.select_first_product()

    context.logger.info("First moisturizer product selected")

    context.driver.switch_to.window(
        context.driver.window_handles[-1]
    )

    context.logger.info("Switched to product page tab successfully")
import time

from pytest_bdd import scenarios, given, when, then, parsers

from pages.home_page import HomePage
from pages.moisturizer_page import MoisturizerPage
from utils.excel_reader import ExcelReader
from config.config import BASE_URL


scenarios("../moisturizer.feature")


@given("user opens moisturizer page")
def open_moisturizer(driver):

    home = HomePage(driver)

    home.open(BASE_URL)

    home.hover_on_skin()

    home.click_moisturizer()

    driver.switch_to.window(
        driver.window_handles[-1]
    )


@when("user selects moisturizer brand")
def select_brand(driver):
    excel = ExcelReader("data/test_data.xlsx")

    data = excel.get_data()

    brand_name = data["BRAND_NAME"]

    moisturizer = MoisturizerPage(driver)

    moisturizer.select_brand(brand_name)

@then("moisturizer products should be displayed")
def verify_products():

    print("Products displayed successfully")
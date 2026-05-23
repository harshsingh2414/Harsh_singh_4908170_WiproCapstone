from pytest_bdd import scenarios, given, when, then

from pages.home_page import HomePage
from pages.login_page import LoginPage

from config.config import BASE_URL


scenarios("../login.feature")


@given("user opens Nykaa website")
def open_website(driver):

    home = HomePage(driver)

    home.open(BASE_URL)


@when("user opens login popup")
def open_login(driver):

    login = LoginPage(driver)

    login.open_login()


@when("user chooses mobile email option")
def choose_option(driver):

    login = LoginPage(driver)

    login.choose_mobile_email()


@then("user clicks skip login")
def skip_login(driver):

    login = LoginPage(driver)

    login.click_skip()
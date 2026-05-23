from behave import when
from pages.login_page import LoginPage
import allure


# -----------------------------
# OPEN LOGIN POPUP
# -----------------------------
@allure.step("Open Login Popup")
@when("user opens login popup")
def step_open_login(context):

    context.logger.info("Opening login popup")

    context.login_page = LoginPage(context.driver)

    context.logger.info("Login Page initialized")

    context.login_page.open_login()

    context.logger.info("Login popup opened successfully")


# -----------------------------
# SELECT MOBILE OR EMAIL OPTION
# -----------------------------
@allure.step("Select Mobile Or Email Login Option")
@when("user selects mobile or email login option")
def step_choose_mobile_email(context):

    context.logger.info("Selecting mobile or email login option")

    context.logger.info("Initializing Login Page")

    context.login_page = LoginPage(context.driver)



    context.login_page.choose_mobile_email()

    context.logger.info("Mobile or email login option selected successfully")


# -----------------------------
# CLICK SKIP LOGIN BUTTON
# -----------------------------
@allure.step("Click Skip Login Button")
@when("user clicks skip login button")
def step_skip_login(context):

    context.logger.info("Clicking skip login button")

    context.logger.info("Initializing Login Page")

    context.login_page = LoginPage(context.driver)

    context.login_page.click_skip()

    context.logger.info("Skip login button clicked successfully")
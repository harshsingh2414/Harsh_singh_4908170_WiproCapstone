import allure

from utils.driver_factory import get_driver
from utils.logger import get_logger
from utils.allure_utils import screenshot


def before_scenario(context, scenario):

    context.driver = get_driver()

    context.driver.maximize_window()

    context.logger = get_logger()

    context.logger.info(
        f"START SCENARIO: {scenario.name}"
    )


def after_step(context, step):
    safe_name = (
        step.name
        .replace(" ", "_")
        .replace('"', '')
        .replace(":", "")
        .replace("/", "_")
        .replace("\\", "_")
    )

    screenshot(
        context.driver,
        safe_name
    )

    if step.status == "failed":
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="FAILED_STEP",
            attachment_type=allure.attachment_type.PNG
        )

        context.logger.error(
            f"FAILED STEP: {step.name}"
        )


def after_scenario(context, scenario):

    context.logger.info(
        f"END SCENARIO: {scenario.name}"
    )

    context.driver.quit()
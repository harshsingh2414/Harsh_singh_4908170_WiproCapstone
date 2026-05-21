import os
import allure

# global step counter
STEP_COUNTER = 0


def screenshot(driver, name="step"):

    global STEP_COUNTER
    STEP_COUNTER += 1

    # folder
    screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)

    # ONLY STEP BASED NAME (NO TIME)
    file_path = os.path.join(
        screenshot_dir,
        f"{STEP_COUNTER:03d}_{name}.png"
    )

    # save screenshot
    driver.save_screenshot(file_path)

    # attach to allure
    allure.attach.file(
        file_path,
        name=f"{STEP_COUNTER:03d}_{name}",
        attachment_type=allure.attachment_type.PNG
    )

    return file_path
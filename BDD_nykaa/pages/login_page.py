from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):

    SIGN_IN_BTN = (By.XPATH, "//button[contains(text(),'Sign')]")

    MOBILE_EMAIL_BTN = (By.XPATH, "//button[contains(text(),'Mobile') or contains(text(),'Email')]")

    SKIP_BTN = (By.XPATH, "//*[contains(text(),'Skip')]")

    # =====================================================
    @allure.step("Open Login Popup")
    def open_login(self):

        btn = self.wait.until(
            EC.element_to_be_clickable(self.SIGN_IN_BTN)
        )

        self.driver.execute_script("arguments[0].click();", btn)

    # =====================================================
    @allure.step("Choose Mobile Email Option")
    def choose_mobile_email(self):

        btn = self.wait.until(
            EC.element_to_be_clickable(self.MOBILE_EMAIL_BTN)
        )

        self.driver.execute_script("arguments[0].click();", btn)

    # =====================================================
    @allure.step("Click Skip Login")
    def click_skip(self):

        btn = self.wait.until(
            EC.element_to_be_clickable(self.SKIP_BTN)
        )

        self.driver.execute_script("arguments[0].click();", btn)
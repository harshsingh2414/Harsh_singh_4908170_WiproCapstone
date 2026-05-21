from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
import allure


class CartPage(BasePage):

    PROCEED_BTN = (By.XPATH, "//button[contains(.,'Proceed')]")

    SIGNUP_BTN = (By.XPATH, "//button[contains(.,'Sign up')]")

    SKIP_BTN = (By.XPATH, "//button[contains(.,'Skip')]")

    REMOVE_BTN = (By.XPATH, "//button[contains(.,'Remove')]")

    CART_ITEMS = (By.XPATH, "//*[@id='header-bag-icon']/span")

    DELETE_BTN = (By.XPATH, "//button[@data-test-id='product-remove']")

    YES_BTN = (By.XPATH, "//button[contains(.,'Yes')]")



    # -----------------------------
    @allure.step("Click Proceed Button")
    def click_proceed(self):

        btn = self.wait.until(
            EC.element_to_be_clickable(self.PROCEED_BTN)
        )

        self.driver.execute_script("arguments[0].click();", btn)

    # -----------------------------
    @allure.step("Click Login Button")
    def click_login_button(self):

        btn = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(.,'Login')]")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        self.driver.execute_script("arguments[0].click();", btn)

    # -----------------------------
    @allure.step("Click Signup Button")
    def click_signup_button(self):

        btn = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(.,'Sign up') or contains(.,'Signup')]")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        try:
            btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", btn)

    # -----------------------------
    @allure.step("Click Skip Button")
    def click_skip(self):

        btn = self.wait.until(
            EC.element_to_be_clickable(self.SKIP_BTN)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            btn
        )

        self.driver.execute_script("arguments[0].click();", btn)

    def get_cart_items(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.CART_ITEMS)
        )

    @allure.step("Delete product from cart")
    def delete_cart_items(self):

        delete_btn = self.wait.until(
            EC.element_to_be_clickable(self.DELETE_BTN)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            delete_btn
        )

        yes_btn = self.wait.until(
            EC.element_to_be_clickable(self.YES_BTN)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            yes_btn
        )

    @allure.step("Verify product removed from cart")
    def verify_product_removed(self):

        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(self.DELETE_BTN)
        )

        remaining_products = self.driver.find_elements(*self.DELETE_BTN)

        return len(remaining_products)

    @allure.step("Get Proceed Buttons")
    def get_proceed_buttons(self):

        return self.driver.find_elements(
            *self.PROCEED_BTN
        )
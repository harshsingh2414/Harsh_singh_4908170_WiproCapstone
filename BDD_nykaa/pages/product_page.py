from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class ProductPage(BasePage):

    ADD_TO_BAG = (By.XPATH, "//button[contains(.,'Add to Bag')]")

    CART_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'css-g4vs13')] | //span[contains(@class,'cart-count')]"
    )

    @allure.step("Add Product To Bag")
    def add_to_bag(self):

        add_btn = self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_BAG)
        )

        self.driver.execute_script("arguments[0].click();", add_btn)

    @allure.step("Open Cart")
    def open_cart(self):

        cart_btn = self.wait.until(
            EC.element_to_be_clickable(self.CART_BUTTON)
        )

        self.driver.execute_script("arguments[0].click();", cart_btn)
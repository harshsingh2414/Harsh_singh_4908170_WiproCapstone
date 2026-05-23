from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class MoisturizerPage(BasePage):

    BRAND_FILTER = (By.XPATH, "//span[contains(text(),'Brand')]")

    FIRST_PRODUCT = (By.XPATH, "(//a[contains(@href,'/p/')])[1]")

    @allure.step("Select Brand: {brand_name}")
    def select_brand(self, brand_name):

        brand_filter = self.wait.until(
            EC.visibility_of_element_located(self.BRAND_FILTER)
        )

        self.driver.execute_script("arguments[0].click();", brand_filter)

        brand_locator = (By.XPATH, f"//label[contains(.,'{brand_name}')]")

        brand = self.wait.until(
            EC.visibility_of_element_located(brand_locator)
        )

        self.driver.execute_script("arguments[0].click();", brand)

    @allure.step("Select First Product")
    def select_first_product(self):

        product = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_PRODUCT)
        )

        self.driver.execute_script("arguments[0].click();", product)
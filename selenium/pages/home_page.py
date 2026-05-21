from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class HomePage(BasePage):

    SKIN_MENU = (By.XPATH, "//*[@id='my-menu']/ul/li[2]")

    MOISTURIZERS = (By.XPATH, "//a[contains(text(),'Moisturizers')]")

    SEARCH_BOX = (
        By.XPATH,
        "//input[contains(@placeholder,'Search')]"
    )

    PRODUCT_RESULTS = (
        By.XPATH,
        "//a[contains(@href,'/p/')]"
    )

    NO_RESULT_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'we couldn’t find any matches') or contains(text(),'No products found')]"
    )

    CART_ICON = (By.XPATH, "//*[@id='header-bag-icon']")

    @allure.step("Open Nykaa Website")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Hover On Skin Menu")
    def hover_on_skin(self):
        skin_menu = self.wait.until(
            EC.visibility_of_element_located(self.SKIN_MENU)
        )

        ActionChains(self.driver).move_to_element(skin_menu).perform()

    @allure.step("Click Moisturizer Category")
    def click_moisturizer(self):
        moisturizer = self.wait.until(
            EC.element_to_be_clickable(self.MOISTURIZERS)
        )

        self.driver.execute_script("arguments[0].click();", moisturizer)

    @allure.step("Search Product")
    def search_product(self, product_name):
        search = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BOX)
        )

        search.clear()
        search.send_keys(product_name)
        search.submit()

    @allure.step("Get Search Results")
    def get_search_results(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCT_RESULTS
            )
        )

    @allure.step("Get no result message")
    def get_no_result_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.NO_RESULT_MESSAGE
            )
        )



    def open_cart(self):
        cart_btn = self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        )

        self.driver.execute_script("arguments[0].click();", cart_btn)
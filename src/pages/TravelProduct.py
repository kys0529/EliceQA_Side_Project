from appium.webdriver.webdriver import WebDriver
from src.utils.locators.TravelProductLocator import TravelProductListLocator
from src.pages.BasePage import BasePage

class TravelProduct(BasePage):
    def __init__(self, driver, page_name = "TravelProduct"):
        super().__init__(driver, page_name)
        self.list_locators = TravelProductListLocator

    def travelproduct_navi_click(self):
        self.click_element(self.list_locators.PAGE_NAVI)
    
    def travelproduct_list_search(self, text):
        self.click_element(self.list_locators.SEARCH_ICON)
        search_text = self.send_keys(self.list_locators.SEARCH_BAR, text).text
        self.driver.press_keycode(66)
        return search_text
    
    def travelproduct_filter_select(self, text):
        self.click_element(self.list_locators.FILTER_ICON)
        self.click_element(self.list_locators.filter_dropdown(text))

    def get_package_item(self):
        packages = self.driver.find_elements(self.list_locators.PACKAGE_IMAGE)
        package_items = []
        for package in packages:
            package_items.append(package.get_attribute("content-desc"))
        return package_items

        
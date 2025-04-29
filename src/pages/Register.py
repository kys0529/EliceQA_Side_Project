from src.pages.BasePage import BasePage
from src.utils.locators import RegisterLocator

class Register(BasePage):
    def __init__(self, driver, page_name="Register"):
        super().__init__(driver, page_name)

    def navigate_to_register(self, driver):
        try:
            register = Register(driver)
            register.click_element(RegisterLocator.REGISTER_BTN)
        except Exception as e:
            register.logger.error(f"테스트 실패 - navigate_to_register")
            register.save_screenshot("failed_to_navigate_to_register")
            raise
    
    def find_by_hint(self, locator, hint):
        try:
            for element in self.driver.find_elements(*locator): # *locator = 언패킹을 해야한다
                if element.get_attribute("hint") == hint:
                    self.logger.info(f"{hint} 힌트 확인")
                    return element
        except Exception as e:
            self.logger.error(f"테스트 실패 - find_by_hint")
            self.save_screenshot("failed_to_navigate_to_register")            

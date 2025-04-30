from src.pages.BasePage import BasePage

class Login(BasePage):
    def __init__(self, driver, page_name="Login"):
        super().__init__(driver, page_name)
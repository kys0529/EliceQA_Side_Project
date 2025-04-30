from src.pages.BasePage import BasePage

class MyPage(BasePage):
    def __init__(self, driver, page_name="MyPage"):
        super().__init__(driver, page_name)
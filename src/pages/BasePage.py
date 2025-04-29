import os
import time
import logging
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class BasePage:
    def __init__(self, driver: WebDriver, page_name = "BasePage"):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.page_name = page_name
        self.logger = self.setup_logger()

    # Logger 설정
    def setup_logger(self):
        log_dir = f"reports/logs/{self.page_name}"
        os.makedirs(log_dir, exist_ok=True)
        
        logger = logging.getLogger(self.page_name)
        logger.handlers.clear()
        logger.setLevel(logging.INFO)

        # 로그 파일 출력
        file_handler = logging.FileHandler(f"{log_dir}/{self.page_name}.log", encoding="utf-8")
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"))
        logger.addHandler(file_handler)

        # 터미널 출력
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"))
        logger.addHandler(stream_handler)

        return logger

    # 스크린샷 촬영
    def save_screenshot(self, func_name):
        screenshot_dir = f"reports/screenshots/{self.page_name}"
        os.makedirs(screenshot_dir, exist_ok=True)
    
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_file = os.path.join(screenshot_dir, f"{timestamp}_{func_name}.png")
        self.driver.save_screenshot(screenshot_file)

    # 요소 클릭 (클릭 가능할 때까지 대기 후 클릭)
    def click_element(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"✔ {locator} 요소 클릭 확인")
            return element
        
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"✖ {locator} 요소를 찾지 못하거나 대기 시간 초과: {e}")
            self.save_screenshot("click_element_fail")
            raise

    # 요소 존재 확인 (화면에 존재할 때까지 대기)
    def find_element(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            self.logger.info(f"✔ {locator} 요소 존재 확인")
            return element
        
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"✖ {locator} 요소를 찾지 못하거나 대기 시간 초과: {e}")
            self.save_screenshot("find_element_fail")
            raise

    # 요소 입력
    def send_keys(self, locator, text):
        try:
            element = self.click_element(locator)
            element.send_keys(text)
            self.logger.info(f"✔ {locator} 요소 입력 확인")
            return element
        
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"✖ {locator} 요소를 찾지 못하거나 대기 시간 초과: {e}")
            self.save_screenshot("send_keys_fail")
            raise
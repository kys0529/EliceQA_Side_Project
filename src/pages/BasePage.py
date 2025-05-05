import os
import time
import logging
import cv2  # 스크린샷 비교를 위한 OpenCV import (pip install opencv-python 로 설치하시면 됩니다!)
import re   # 요소 좌표 계산 시 정규식 활용을 위해 import
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
        return screenshot_file

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

    # 요소들 존재 확인 (화면에 존재할 때까지 대기)
    def find_elements(self, locator):
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located(locator))
            self.logger.info(f"✔ {locator} 요소들 존재 확인")
            return elements
        
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"✖ {locator} 요소들을 찾지 못하거나 대기 시간 초과: {e}")
            self.save_screenshot("find_elements_fail")
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

    # 요소 attribute 확인
    def get_attribute(self, locator, attribute):
        try:
            element = self.find_element(locator)
            value = element.get_attribute(attribute)
            value_log = value.replace("\n", "")
            self.logger.info(f"✔ {locator} 요소의 {attribute} 속성 값 확인: {value_log}")
            return value
        
        except (NoSuchElementException, TimeoutException) as e:
            self.logger.error(f"✖ {locator} 요소를 찾지 못하거나 대기 시간 초과: {e}")
            self.save_screenshot("get_attribute_fail")
            raise
    
    # 스크롤 업
    def scroll_up(self):
        size = self.driver.get_window_size()
        start_y = size["height"] * 0.2
        end_y = size["height"] * 0.8
        x = size["width"] * 0.5
        self.driver.swipe(start_x=x, start_y=start_y, end_x=x, end_y=end_y, duration=800)
    
    # 스크롤 다운
    def scroll_down(self):
        size = self.driver.get_window_size()
        start_y = size["height"] * 0.8
        end_y = size["height"] * 0.2
        x = size["width"] * 0.5
        self.driver.swipe(start_x=x, start_y=start_y, end_x=x, end_y=end_y, duration=800)

    # 스크린샷 비교를 위한 특정 좌표 색상값 추출
    def get_coordinate_color(self, status, bounds, x_offset, y_offset):
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_file = self.save_screenshot(f"ForColorCheck - {status}")
        
        x_y_values = re.findall(r"\d+", bounds)
        x1, y1, x2, y2 = map(int, x_y_values)
        
        center_x = (x1+x2)//2
        center_y = (y1+y2)//2
        
        img = cv2.imread(screenshot_file)

        coordinate = (center_x + x_offset, center_y + y_offset)

        h, w, _ = img.shape

        circle_color = (0, 0, 255)
        radius = 5
        thickness = -1

        confirm_coordinate_img = img.copy()

        save_dir = f"reports/screenshots/{self.page_name}"
        os.makedirs(save_dir, exist_ok=True)

        if 0 <= coordinate[0] < w and 0 <= coordinate[1] < h:
            b, g, r = img[coordinate[1], coordinate[0]]
            pixel_rgb = tuple(map(int,(r, g, b)))
            
            file_name = f"{timestamp}_ColorIsChecked - {status}.png"
            save_path = os.path.join(save_dir, file_name)


            cv2.circle(confirm_coordinate_img,coordinate, radius, circle_color, thickness)
            cv2.imwrite(save_path, confirm_coordinate_img)

            self.logger.info("✔ 입력된 좌표값이 이미지 범위 내입니다.")
            self.logger.info("✔ 색상 추출 영역 표시 및 추출 색상 정보가 포함된 이미지가 스크린샷 폴더에 저장되었습니다.")
            return pixel_rgb

        else:
            file_name = f"{timestamp}_ColorNotChecked - {status}.png"
            save_path = os.path.join(save_dir, file_name)
            cv2.imwrite(save_path, confirm_coordinate_img)
            self.logger.error("✖ 입력된 좌표값이 이미지 범위 밖입니다.")
            self.logger.error("✖ 이미지에 색상 추출 영역 및 추출 색상 정보가 포함되지 않습니다.")
            return None

from selenium.webdriver.support import expected_conditions as EC

from src.pages.BasePage import BasePage
from src.utils.locators import HomeLocator

class Home(BasePage):
    def __init__(self, driver, page_name = "Home"):
        super().__init__(driver, page_name)

    # 홈 탭의 날씨 위젯 요소(온도, 풍속) 로딩 완료까지 대기
    def wait_until_weather_widget_loaded(self):
        try:
            self.find_element(HomeLocator.WEATHER_WIDGET_TEMP)
            self.find_element(HomeLocator.WEATHER_WIDGET_WIND)
            self.logger.info("✔ 날씨 위젯 API 로딩 완료")
        except Exception as e:
            self.logger.error(f"✖ 날씨 위젯 API 로딩 실패: {e}")
            self.save_screenshot("wait_until_home_loaded_fail")
            raise

    # 스크롤 요소를 기준으로 특정 방향으로 지정한 비율만큼 스와이프
    def swipe_element(self, scroll_element, direction, percent):
        if direction not in ["left", "right", "up", "down"]:
            self.logger.warning(f"✖ 잘못된 direction 값: {direction}")
            return
        if not (0.0 < percent <= 1.0):
            self.logger.warning(f"✖ percent 값 범위 초과: {percent}")
            return

        try:
            self.driver.execute_script("mobile: swipeGesture", {
                "elementId": scroll_element.id,
                "direction": direction,
                "percent": percent
            })
            self.logger.info(f"✔ 스와이프 성공")
        except Exception as e:
            self.logger.error(f"✖ 스와이프 실패: {e}")
            self.save_screenshot(f"swipe_element_fail")

    # 특정 요소가 나타날 때까지 스크롤 요소를 스와이프
    def swipe_until_element_visible(self, scroll_element, target_element, direction, percent, max_attempts=10):
        for _ in range(max_attempts):
            try:
                self.driver.find_element(*target_element)
                self.logger.info(f"✔ 최대 시도 횟수 {max_attempts}회 내에 대상 요소 발견")
                break
            except:
                self.swipe_element(scroll_element, direction, percent)
        else:
            self.logger.error(f"✖ 최대 시도 횟수 {max_attempts}회 내에 대상 요소를 찾지 못함")
            self.save_screenshot(f"swipe_until_element_visible_fail")

    def get_post_info(self, locator):
        try:
            element = self.find_element(locator)
            content_desc = element.get_attribute("content-desc")
            author, region, content = content_desc.split("\n")[0], content_desc.split("\n")[1], content_desc.split("\n")[3]
            self.logger.info(f"✔ 정보 추출 성공: {author}, {region}, {content}")
            return author, region, content
        except Exception as e:
            self.logger.error(f"✖ 정보 추출 실패: {e}")
            self.save_screenshot("get_like_count_fail")
            raise

    # 게시글 요소의 content-desc에서 '좋아요 N개' 정보를 추출하여 정수로 반환
    def get_like_count(self, locator):
        try:
            content_desc = self.get_attribute(locator, "content-desc")
            split_by_likes = content_desc.split("좋아요")
            if len(split_by_likes) > 1:
                likes_text = split_by_likes[1].split("개")[0].strip()
                like_count = int(likes_text)
                self.logger.info(f"✔ 좋아요 수 추출 성공: {like_count}")
                return like_count
            else:
                self.logger.warning(f"❗ 좋아요 정보가 포함되지 않은 content-desc: {content_desc}")
                return None
        except Exception as e:
            self.logger.error(f"✖ 좋아요 수 추출 실패: {e}")
            self.save_screenshot("get_like_count_fail")
            raise

    def wait_until_element_disappears(self, locator):
        try:
            self.wait.until_not(EC.presence_of_element_located(locator))
            self.logger.info(f"✔ {locator} 요소가 사라짐")
            return True
        except Exception as e:
            self.logger.warning(f"✖ {locator} 요소가 여전히 존재함")
            return False
from src.pages.BasePage import BasePage

class Home(BasePage):
    def __init__(self, driver, page_name = "Home"):
        super().__init__(driver, page_name)

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
    def swipe_until_element_visible(self, scroll_element, target_element, direction, percent, max_attempts=5):
        for _ in range(max_attempts):
            try:
                self.driver.find_element(*target_element)
                break
            except:
                self.swipe_element(scroll_element, direction, percent)
        else:
            self.logger.error(f"✖ 최대 시도 횟수 {max_attempts}회 내에 대상 요소를 찾지 못함")
            self.save_screenshot(f"swipe_until_element_visible_fail")
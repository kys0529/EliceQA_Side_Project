import pytest
from appium.webdriver.webdriver import WebDriver

from src.pages.Home import Home
from src.utils.locators import HomeLocator

@pytest.mark.skip
@pytest.mark.usefixtures("login_driver")
class TestHP01:
    def test_hp_01_01(self, login_driver: WebDriver, request): # 로그인 시, 홈 탭 정상 진입 및 주요 UI 노출 확인
        try:
            home = Home(login_driver) 

            for element in HomeLocator.HOME_TAB_KEY_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info("로그인 시, 홈 탭 정상 진입 및 주요 UI 요소 정상 노출 확인")
        except Exception as e:
            home.logger.info(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.skip
@pytest.mark.usefixtures("login_driver")
class TestHP02:
    def test_hp_02_01(self, login_driver: WebDriver, request): # 홈 탭 진입 상태에서 홈 탭 버튼 선택 시, 홈 탭 진입 상태 유지 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.HOME_TAB)
            for element in HomeLocator.HOME_TAB_KEY_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"홈 탭 -> 홈 탭, 홈 탭 진입 상태 유지 확인")
        except Exception as e:
            home.logger.info(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_02_02(self, login_driver: WebDriver, request): # 여행상품 탭 진입 상태에서 홈 탭 버튼 선택 시, 홈 탭 정상 진입 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_PRODUCT_TAB)
            home.click_element(HomeLocator.HOME_TAB)
            for element in HomeLocator.HOME_TAB_KEY_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"여행상품 탭 -> 홈 탭, 홈 탭 진입 상태 유지 확인")
        except Exception as e:
            home.logger.info(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_02_03(self, login_driver: WebDriver, request): # 채팅 탭 진입 상태에서 홈 탭 버튼 선택 시, 홈 탭 정상 진입 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.CHATTING_TAB)
            home.click_element(HomeLocator.HOME_TAB)
            for element in HomeLocator.HOME_TAB_KEY_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"채팅 탭 -> 홈 탭, 홈 탭 진입 상태 유지 확인")
        except Exception as e:
            home.logger.info(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise
    
    def test_hp_02_04(self, login_driver: WebDriver, request): # 마이페이지 탭 진입 상태에서 홈 탭 버튼 선택 시, 홈 탭 정상 진입 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.MYPAGE_TAB)
            home.click_element(HomeLocator.HOME_TAB)
            for element in HomeLocator.HOME_TAB_KEY_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"마이페이지 탭 -> 홈 탭, 홈 탭 진입 상태 유지 확인")
        except Exception as e:
            home.logger.info(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

# TODO: TestHP03, TestHP04는 추후 구현 (우선순위 하)

@pytest.mark.usefixtures("login_driver")
class TestHP05:
    def test_hp_05_01(self, login_driver: WebDriver, request): # 인기 관광지 혼잡도의 지역 가로 스크롤 확인
        try:
            home = Home(login_driver) 

            scroll_element = home.find_element(HomeLocator.CONGESTION_REGIONS_BAR)
            home.swipe_until_element_visible(scroll_element, HomeLocator.CONGESTION_JEJU_BTN, "left", 0.5)

            assert home.find_element(HomeLocator.CONGESTION_JEJU_BTN).is_displayed()

            home.logger.info("인기 관광지 혼잡도의 지역 가로 스크롤 확인")
        except Exception as e:
            home.logger.info(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_05_02(self, login_driver: WebDriver, request): # 인기 관광지 혼잡도의 관광지 가로 스크롤 확인
        try:
            home = Home(login_driver) 

            first_result = home.find_element(HomeLocator.CONGESTION_FIRST_RESULT)
            before_swipe = first_result.get_attribute("content-desc")

            results_bar = home.find_element(HomeLocator.CONGESTION_RESULTS_BAR)
            home.swipe_element(results_bar, "left", 1.0)

            first_result = home.find_element(HomeLocator.CONGESTION_FIRST_RESULT)
            after_swipe = first_result.get_attribute("content-desc")
            assert before_swipe != after_swipe

            home.logger.info("인기 관광지 혼잡도의 지역 가로 스크롤 확인")
        except Exception as e:
            home.logger.info(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    # TODO: 아직 TestHP05 미완성
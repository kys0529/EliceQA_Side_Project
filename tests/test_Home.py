import pytest
from appium.webdriver.webdriver import WebDriver

from src.pages.Home import Home
from src.utils.locators import HomeLocator
from src.utils.locators.TravelProductLocator import TravelProductListLocator

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
            home.logger.error(f"테스트 실패: {e}")
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
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_02_02(self, login_driver: WebDriver, request): # 여행상품 탭 진입 상태에서 홈 탭 버튼 선택 시, 홈 탭 정상 진입 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_PRODUCT_TAB)
            home.click_element(HomeLocator.HOME_TAB)
            for element in HomeLocator.HOME_TAB_KEY_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"여행상품 탭 -> 홈 탭, 홈 탭 정상 진입 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_02_03(self, login_driver: WebDriver, request): # 채팅 탭 진입 상태에서 홈 탭 버튼 선택 시, 홈 탭 정상 진입 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.CHATTING_TAB)
            home.click_element(HomeLocator.HOME_TAB)
            for element in HomeLocator.HOME_TAB_KEY_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"채팅 탭 -> 홈 탭, 홈 탭 정상 진입 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise
    
    def test_hp_02_04(self, login_driver: WebDriver, request): # 마이페이지 탭 진입 상태에서 홈 탭 버튼 선택 시, 홈 탭 정상 진입 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.MYPAGE_TAB)
            home.click_element(HomeLocator.HOME_TAB)
            for element in HomeLocator.HOME_TAB_KEY_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"마이페이지 탭 -> 홈 탭, 홈 탭 정상 진입 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

# TODO: TestHP03(예약 패키지 D-day 위젯), TestHP04(전국 날씨 위젯)는 추후 구현

@pytest.mark.skip
@pytest.mark.usefixtures("login_driver")
class TestHP05:
    # def test_hp_05_01(self, login_driver: WebDriver, request): # 인기 관광지 혼잡도의 지역 가로 스크롤 확인
    #     try:
    #         home = Home(login_driver) 

    #         scroll_element = home.find_element(HomeLocator.CONGESTION_REGIONS_BAR)
    #         home.swipe_until_element_visible(scroll_element, HomeLocator.CONGESTION_JEJU_BTN, "left", 0.5)

    #         assert home.find_element(HomeLocator.CONGESTION_JEJU_BTN).is_displayed()

    #         home.logger.info("인기 관광지 혼잡도의 지역 가로 스크롤 확인")
    #     except Exception as e:
    #         home.logger.error(f"테스트 실패: {e}")
    #         home.save_screenshot(request.node.name)
    #         raise

    # def test_hp_05_02(self, login_driver: WebDriver, request): # 인기 관광지 혼잡도의 관광지 가로 스크롤 확인
    #     try:
    #         home = Home(login_driver) 

    #         first_result = home.find_element(HomeLocator.CONGESTION_FIRST_RESULT)
    #         before_swipe = first_result.get_attribute("content-desc")

    #         results_bar = home.find_element(HomeLocator.CONGESTION_RESULTS_BAR)
    #         home.swipe_element(results_bar, "left", 1.0)

    #         first_result = home.find_element(HomeLocator.CONGESTION_FIRST_RESULT)
    #         after_swipe = first_result.get_attribute("content-desc")
    #         assert before_swipe != after_swipe

    #         home.logger.info("인기 관광지 혼잡도의 지역 가로 스크롤 확인")
    #     except Exception as e:
    #         home.logger.error(f"테스트 실패: {e}")
    #         home.save_screenshot(request.node.name)
    #         raise

    # TODO: test_hp_05_03(인기 관광지 혼잡도 새로고침)은 추후 구현

    # TODO: test_hp_05_04 ~ 14는 "데이터를 불러오는데 실패했습니다" 오류로 잠시 중단
    def test_hp_05_04(self, login_driver: WebDriver, request): # 인기 관광지 혼잡도의 지역 필터 중 '전체' 필터 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.CONGESTION_ALL_BTN)
            # TODO: 전체 필터 결과는 어떻게 검증하면 좋을까?
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise
    
    # test_hp_05_05 ~ test_hp_05_14
    @pytest.mark.parametrize("locator, region_name", [
        (HomeLocator.CONGESTION_SEOUL_BTN, "서울"),
        (HomeLocator.CONGESTION_BUSAN_BTN, "부산"),
        (HomeLocator.CONGESTION_DAEGU_BTN, "대구"),
        (HomeLocator.CONGESTION_INCHEON_BTN, "인천"),
        (HomeLocator.CONGESTION_GWANGJU_BTN, "광주"),
        (HomeLocator.CONGESTION_DAEJEON_BTN, "대전"),
        (HomeLocator.CONGESTION_ULSAN_BTN, "울산"),
        (HomeLocator.CONGESTION_GYEONGGI_BTN, "경기"),
        (HomeLocator.CONGESTION_GANGWON_BTN, "강원"),
        (HomeLocator.CONGESTION_JEJU_BTN, "제주")
    ])
    def test_hp_05_05(self, login_driver: WebDriver, locator, region_name, request): # 인기 관광지 혼잡도의 지역 필터 중 '서울/부산/대구/인천/광주/대전/울산/경기/강원/제주' 필터 확인
        try:
            home = Home(login_driver)

            scroll_element = home.find_element(HomeLocator.CONGESTION_REGIONS_BAR)
            home.swipe_until_element_visible(scroll_element, locator, "left", 0.2)

            home.click_element(locator)

            first_result = home.find_element(HomeLocator.CONGESTION_FIRST_RESULT)

            assert region_name in first_result.get_attribute("content-desc")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.skip
@pytest.mark.usefixtures("login_driver")
class TestHP06:
    def test_hp_06_01(self, login_driver: WebDriver, request): # '지금 인기있는 여행코스는?'의 더보기 버튼 클릭 시, 여행상품 탭 정상 진입 확인
        try:
            home = Home(login_driver)
            list_locators = TravelProductListLocator()

            home.click_element(HomeLocator.POPULAR_COURSE_MORE)
            for element in list_locators.UI_CHECK_ELEMENT:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"'지금 인기있는 여행코스는?'의 [더보기] 버튼 클릭 시, 여행상품 탭 정상 진입 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

# TODO: TestHP07(알림 기능)은 추후 구현

@pytest.mark.skip
@pytest.mark.usefixtures("login_driver")
class TestHP08:
    def test_hp_08_01(self, login_driver: WebDriver, request): # [여행추천] 버튼 클릭 시, 맞춤 여행 추천 페이지 정상 진입 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_RECOMM_BTN)
            for element in HomeLocator.TRAVEL_RECOMM_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"[여행추천] 버튼 클릭 시, 맞춤 여행 추천 페이지 정상 진입 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

# TODO: TestHP09는 추후 구현 (패키지 상세 페이지 요소 정의 X)

@pytest.mark.skip
@pytest.mark.usefixtures("login_driver")
class TestHP10: 
    def test_hp_10_01(self, login_driver: WebDriver, request): # [가이드랭킹] 버튼 클릭 시, 가이드 랭킹 페이지 정상 진입 확인
        try:
            home = Home(login_driver)
            
            home.click_element(HomeLocator.GUIDE_RANK_BTN)
            for element in HomeLocator.GUIDE_RANK_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"[가이드랭킹] 버튼 클릭 시, 가이드 랭킹 페이지 정상 진입 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.usefixtures("login_driver")
class TestHP11:
    pass
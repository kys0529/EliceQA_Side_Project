import pytest
from appium.webdriver.webdriver import WebDriver

from src.pages.Home import Home
from src.utils.locators import HomeLocator
from src.utils.locators.TravelProductLocator import TravelProductListLocator, TravelProductDetailLocator
from src.utils.locators.MyPageLocator import MypageProfile

@pytest.mark.done
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

@pytest.mark.done
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

@pytest.mark.done
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
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_05_02(self, login_driver: WebDriver, request): # 인기 관광지 혼잡도의 관광지 가로 스크롤 확인
        try:
            home = Home(login_driver) 

            before_swipe = home.get_attribute(HomeLocator.CONGESTION_FIRST_RESULT, "content-desc")
            scroll_element = home.find_element(HomeLocator.CONGESTION_RESULTS_BAR)
            home.swipe_element(scroll_element, "left", 1.0)
            after_swipe = home.get_attribute(HomeLocator.CONGESTION_FIRST_RESULT, "content-desc")

            assert before_swipe != after_swipe

            home.logger.info("인기 관광지 혼잡도의 지역 가로 스크롤 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    # TODO: test_hp_05_03(인기 관광지 혼잡도 새로고침)은 추후 구현

    @pytest.mark.parametrize("expected_regions", [
        ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "경기", "강원", "제주"]
    ])
    def test_hp_05_04(self, login_driver: WebDriver, expected_regions, request): # 인기 관광지 혼잡도의 지역 필터 중 '전체' 필터 확인
        try:
            home = Home(login_driver)
            home.wait_until_weather_widget_loaded()

            scroll_element = home.find_element(HomeLocator.CONGESTION_RESULTS_BAR)
            for i in range(3):
                first_result_desc = home.get_attribute(HomeLocator.CONGESTION_FIRST_RESULT, "content-desc")
                home.swipe_element(scroll_element, "left", 0.3)
                assert any(region in first_result_desc for region in expected_regions)

            home.logger.info("인기 관광지 혼잡도의 지역 필터 중 '전체' 필터 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    @pytest.mark.parametrize("locator, region_name", [ 
        (HomeLocator.CONGESTION_SEOUL_BTN, "서울"), # test_hp_05_05
        (HomeLocator.CONGESTION_BUSAN_BTN, "부산"), # test_hp_05_06
        (HomeLocator.CONGESTION_DAEGU_BTN, "대구"), # test_hp_05_07
        (HomeLocator.CONGESTION_INCHEON_BTN, "인천"), # test_hp_05_08
        (HomeLocator.CONGESTION_GWANGJU_BTN, "광주"), # test_hp_05_09
        (HomeLocator.CONGESTION_DAEJEON_BTN, "대전"), # test_hp_05_10
        (HomeLocator.CONGESTION_ULSAN_BTN, "울산"), # test_hp_05_11
        (HomeLocator.CONGESTION_GYEONGGI_BTN, "경기"), # test_hp_05_12
        (HomeLocator.CONGESTION_GANGWON_BTN, "강원"), # test_hp_05_13
        (HomeLocator.CONGESTION_JEJU_BTN, "제주") # test_hp_05_14
    ])
    def test_hp_05_05(self, login_driver: WebDriver, locator, region_name, request): # 인기 관광지 혼잡도의 지역 필터 중 '서울/부산/대구/인천/광주/대전/울산/경기/강원/제주' 필터 확인
        try:
            home = Home(login_driver)
            home.wait_until_weather_widget_loaded()

            scroll_element = home.find_element(HomeLocator.CONGESTION_REGIONS_BAR)
            home.swipe_until_element_visible(scroll_element, locator, "left", 0.2, 50)
            home.click_element(locator)

            if (region_name != "강원"): # 강원은 인기 관광지 혼잡도 결과가 존재 X
                assert region_name in home.get_attribute(HomeLocator.CONGESTION_FIRST_RESULT, "content-desc")

            home.logger.info(f"인기 관광지 혼잡도의 지역 필터 중 {region_name} 필터 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP06:
    def test_hp_06_01(self, login_driver: WebDriver, request): # '지금 인기있는 여행코스는?'의 더보기 버튼 클릭 시, 여행상품 탭 정상 진입 확인 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)
            list_locators = TravelProductListLocator()

            home.click_element(HomeLocator.POPULAR_COURSE_MORE)
            for element in list_locators.UI_CHECK_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"'지금 인기있는 여행코스는?'의 [더보기] 버튼 클릭 시, 여행상품 탭 정상 진입 확인 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP08:
    def test_hp_08_01(self, login_driver: WebDriver, request): # [여행추천] 버튼 클릭 시, 맞춤 여행 추천 페이지 정상 진입 확인 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_RECOMM_BTN)
            for element in HomeLocator.TRAVEL_RECOMM_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"[여행추천] 버튼 클릭 시, 맞춤 여행 추천 페이지 정상 진입 확인 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP09:
    def test_hp_09_01(self, login_driver: WebDriver, request): # 패키지 클릭 시, 선택된 패키지의 상세 페이지 정상 진입 확인 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)
            list_locators = TravelProductDetailLocator()

            home.click_element(HomeLocator.TRAVEL_RECOMM_BTN)
            home.click_element(HomeLocator.TRAVEL_RECOMM_FIRST_RESULT)
            for element in list_locators.UI_CHECK_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"패키지 클릭 시, 선택된 패키지의 상세 페이지 정상 진입 확인 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP10: 
    def test_hp_10_01(self, login_driver: WebDriver, request): # [가이드랭킹] 버튼 클릭 시, 가이드 랭킹 페이지 정상 진입 확인 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)
            
            home.click_element(HomeLocator.GUIDE_RANK_BTN)
            for element in HomeLocator.GUIDE_RANK_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"[가이드랭킹] 버튼 클릭 시, 가이드 랭킹 페이지 정상 진입 확인 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP11:
    def test_hp_11_01(self, login_driver: WebDriver, request): # 가이드 선택 시, 가이드 프로필 페이지 정상 진입 확인 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)
            myPageProfile = MypageProfile()

            home.click_element(HomeLocator.GUIDE_RANK_BTN)
            home.click_element(HomeLocator.GUIDE_RANK_FIRST_RESULT)
            
            assert home.find_element(myPageProfile.PROFILE_MORE).is_displayed()
            assert home.find_element(myPageProfile.PROFILE_GUIDE_PAKAGE_TITLE).is_displayed()
            assert home.find_element(myPageProfile.PROFILE_GUIDE_PAKAGE_SECTION).is_displayed()

            home.logger.info(f"가이드 선택 시, 가이드 프로필 페이지 정상 진입 확인 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP12:
    def test_hp_12_01(self, login_driver: WebDriver, request): # [지역탐방] 버튼 클릭 시, 지역탐방 페이지 정상 진입 확인 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.REGION_TOUR_BTN)
            for element in HomeLocator.REGION_TOUR_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"[지역탐방] 버튼 클릭 시, 지역탐방 페이지 정상 진입 확인 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP13:
    @pytest.mark.parametrize("city, district, filter, expected_city, expected_district, expected_filter", [
        (HomeLocator.REGION_TOUR_CITY_DAEGU, HomeLocator.REGION_TOUR_DISTRICT_BUKGU, HomeLocator.REGION_TOUR_ALL_BTN, "대구", "북구", "전체"), # test_hp_13_02
        (HomeLocator.REGION_TOUR_CITY_DAEGU, HomeLocator.REGION_TOUR_DISTRICT_BUKGU, HomeLocator.REGION_TOUR_ATTRACTION_BTN, "대구", "북구", "관광지"), # test_hp_13_03
        (HomeLocator.REGION_TOUR_CITY_DAEGU, HomeLocator.REGION_TOUR_DISTRICT_BUKGU, HomeLocator.REGION_TOUR_FOOD_BTN, "대구", "북구", "음식"), # test_hp_13_04
        (HomeLocator.REGION_TOUR_CITY_DAEGU, HomeLocator.REGION_TOUR_DISTRICT_BUKGU, HomeLocator.REGION_TOUR_STAY_BTN, "대구", "북구", "숙박") # test_hp_13_05
    ])
    def test_hp_13_02(self, login_driver: WebDriver, city, district, filter, expected_city, expected_district, expected_filter, request): # 선택된 시/도, 시/군/구, 장소 유형과 관련된 장소 리스트 노출 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.REGION_TOUR_BTN)
            home.click_element(HomeLocator.REGION_TOUR_CITY_DROPDOWN)
            home.click_element(city)
            home.click_element(HomeLocator.REGION_TOUR_DISTRICT_DROPDOWN)
            home.click_element(district)
            home.click_element(filter)

            if expected_filter != "전체":
                location, type = home.get_region_tour_result_info(HomeLocator.REGION_TOUR_FIRST_RESULT)
                assert expected_city in location and expected_district in location and type in expected_filter
            else:
                expected_types = ["관광지", "음식", "숙박"]
                scroll_element = home.find_element(HomeLocator.REGION_TOUR_RESULTS)
                for i in range(3):
                    location, type = home.get_region_tour_result_info(HomeLocator.REGION_TOUR_FIRST_RESULT)
                    home.swipe_element(scroll_element, "up", 0.3)
                    assert expected_city in location and expected_district in location and any(expected_type in type for expected_type in expected_types)

            home.logger.info(f"{expected_city}, {expected_district}, {expected_filter}와 관련된 장소 리스트 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP14:
    @pytest.mark.parametrize("city, district, filter", [
        (HomeLocator.REGION_TOUR_CITY_DAEGU, HomeLocator.REGION_TOUR_DISTRICT_BUKGU, HomeLocator.REGION_TOUR_ALL_BTN), 
    ])
    def test_hp_14_01(self, login_driver: WebDriver, city, district, filter, request): # 장소 리스트 중 가장 상단에 위치한 장소 선택 시, 네이버 지도로 이동
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.REGION_TOUR_BTN)
            home.click_element(HomeLocator.REGION_TOUR_CITY_DROPDOWN)
            home.click_element(city)
            home.click_element(HomeLocator.REGION_TOUR_DISTRICT_DROPDOWN)
            home.click_element(district)
            home.click_element(filter)
            home.click_element(HomeLocator.REGION_TOUR_FIRST_RESULT)

            assert home.find_element(HomeLocator.REGION_TOUR_NAVER_MAP_TITLE).is_displayed()

            home.logger.info(f"장소 리스트 중 가장 상단에 위치한 장소 선택 시, 네이버 지도로 이동")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP15:
    def test_hp_15_01(self, login_driver: WebDriver, request): # [여행갤러리] 버튼 클릭 시, 여행갤러리 페이지 정상 진입 확인 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            for element in HomeLocator.TRAVEL_GALLERY_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"[여행갤러리] 버튼 클릭 시, 여행갤러리 페이지 정상 진입 확인 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP16:
    def test_hp_16_01(self, login_driver: WebDriver, request): # [좋아요] 버튼 클릭 시, 좋아요 수 1 증가 확인 (사전 조건: 좋아요가 눌려있지 않은 상태)
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)

            before_like = home.get_like_count(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT)
            home.click_element(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT_LIKE_BTN)
            after_like = home.get_like_count(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT)

            assert before_like + 1 == after_like

            home.logger.info(f"[좋아요] 버튼 클릭 시, 좋아요 수 1 증가 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_16_02(self, login_driver: WebDriver, request): # [좋아요] 버튼 클릭 시, 좋아요 수 1 감소 확인 (사전 조건: 좋아요가 이미 눌려있는 상태)
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)

            before_like = home.get_like_count(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT)
            home.click_element(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT_LIKE_BTN)
            after_like = home.get_like_count(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT)

            assert before_like - 1 == after_like

            home.logger.info(f"[좋아요] 버튼 클릭 시, 좋아요 수 1 감소 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_16_03(self, login_driver: WebDriver, request): # [댓글] 버튼 클릭 시, 댓글 창 열림 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)

            home.click_element(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT_COMMENT_BTN)
            for element in HomeLocator.TRAVEL_GALLERY_COMMENT_AREA_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"[댓글] 버튼 클릭 시, 댓글 창 열림 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_16_04(self, login_driver: WebDriver, request): # [댓글 모두 보기] 버튼 클릭 시, 댓글 창 열림 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)

            home.click_element(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT_COMMENT_BTN)
            for element in HomeLocator.TRAVEL_GALLERY_COMMENT_AREA_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"[댓글 모두 보기] 버튼 클릭 시, 댓글 창 열림 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise
    
    @pytest.mark.parametrize("comment", ["이것은 댓글 테스트", "댓글 작성 테스트"])
    def test_hp_16_05(self, login_driver: WebDriver, comment, request): # 입력한 댓글이 댓글 리스트에 정상적으로 추가되는지 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT_COMMENT_BTN)

            home.send_keys(HomeLocator.TRAVEL_GALLERY_COMMENT_INPUT, comment)
            home.click_element(HomeLocator.TRAVEL_GALLERY_COMMENT_SEND_BTN)

            assert comment in home.get_attribute(HomeLocator.TRAVEL_GALLERY_COMMENT_FIRST_RESULT, "content-desc")

            home.logger.info(f"입력한 댓글이 댓글 리스트에 정상적으로 추가")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_16_06(self, login_driver: WebDriver, request): # [X] 버튼 클릭 시, 댓글 창 닫힘 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT_COMMENT_BTN)

            home.click_element(HomeLocator.TRAVEL_GALLERY_COMMENT_AREA_CLOSE_BTN)
            assert home.wait_until_element_disappears(HomeLocator.TRAVEL_GALLERY_COMMENT_AREA)

            home.logger.info(f"[X] 버튼 클릭 시, 댓글 창 닫힘 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_16_07(self, login_driver: WebDriver, request): # [스크랩] 버튼 클릭 시, 스크랩한 게시글 리스트에 정상적으로 추가되는지 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            before_author, before_region, before_content = home.get_post_info(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT)
            home.click_element(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT_BOOKMARK_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_BOOKMARK_BTN)
            after_author, after_region, after_content = home.get_post_info(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT)

            assert before_author == after_author and before_region == after_region and before_content == after_content

            home.logger.info(f"[스크랩] 버튼 클릭 시, 스크랩한 게시글 리스트에 정상적으로 추가되는지 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP17:
    def test_hp_17_01(self, login_driver: WebDriver, request): # [스크랩한 게시글] 버튼 클릭 시, 스크랩한 게시글 페이지 정상 진입 확인 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_BOOKMARK_BTN)

            for element in HomeLocator.TRAVEL_GALLERY_BOOKMARK_LIST_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"[스크랩한 게시글] 버튼 클릭 시, 스크랩한 게시글 페이지 정상 진입 확인 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_17_02(self, login_driver: WebDriver, request): # [스크랩] 버튼 클릭 시, 스크랩한 게시글 리스트에서 정상적으로 삭제되는지 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_BOOKMARK_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT_BOOKMARK_BTN)

            assert home.wait_until_element_disappears(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT)

            home.logger.info(f"[스크랩] 버튼 클릭 시, 스크랩한 게시글 리스트에서 정상적으로 삭제되는지 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP18:
    def test_hp_18_01(self, login_driver: WebDriver, request): # [새 게시물 추가] 버튼 클릭 시, 새 게시물 페이지 정상 진입 확인 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_BTN)
            for element in HomeLocator.TRAVEL_GALLERY_ADD_POST_UI_ELEMENTS:
                assert home.find_element(element).is_displayed()

            home.logger.info(f"[새 게시물 추가] 버튼 클릭 시, 새 게시물 페이지 정상 진입 확인 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    def test_hp_18_02(self, login_driver: WebDriver, request): # 아무 입력 없이 [공유] 버튼 클릭 시, 위치 및 설명 경고 텍스트 UI 노출 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_SHARE_BTN)

            assert home.find_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_LOCATION_WARNING).is_displayed()
            assert home.find_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_DESCRIPTION_WARNING).is_displayed()

            home.logger.info(f"아무 입력 없이 [공유] 버튼 클릭 시, 위치 및 설명 경고 텍스트 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    @pytest.mark.parametrize("location, description", [
        ("대구 찜갈비", "찜갈비 존맛탱") 
    ])
    def test_hp_18_03(self, login_driver: WebDriver, location, description, request): # 이미지도 필수 항목이므로, [공유] 버튼이 정상 동작하지 않음
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_BTN)
            home.send_keys(HomeLocator.TRAVEL_GALLERY_ADD_POST_LOCATION_INPUT, location)
            home.send_keys(HomeLocator.TRAVEL_GALLERY_ADD_POST_DESCRIPTION_INPUT, description)
            home.click_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_SHARE_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_BACK_BTN)

            author, region, content = home.get_post_info(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT)
            assert region != location and content != description

            home.logger.info(f"이미지도 필수 항목이므로, [공유] 버튼이 정상 동작하지 않음")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    @pytest.mark.parametrize("location, description", [
        ("대구 루시드 카페", "푸딩 빙수 존맛탱")
    ])
    def test_hp_18_04(self, login_driver: WebDriver, location, description, request): # 작성한 게시글이 피드 글 리스트에 정상적으로 추가됨
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_BTN)
            home.send_keys(HomeLocator.TRAVEL_GALLERY_ADD_POST_LOCATION_INPUT, location)
            home.send_keys(HomeLocator.TRAVEL_GALLERY_ADD_POST_DESCRIPTION_INPUT, description)
            home.click_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_IMG_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_GALLERY_IMG)
            home.click_element(HomeLocator.TRAVEL_GALLERY_ADD_POST_SHARE_BTN)

            author, region, content = home.get_post_info(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT, True)
            assert region == location and content == description

            home.logger.info(f"작성한 게시글이 피드 글 리스트에 정상적으로 추가됨")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestHP19:
    def test_hp_19_01(self, login_driver: WebDriver, request): # [게시물 검색 버튼] 클릭 시, 피드 글 검색 페이지 정상 진입 및 주요 UI 노출 확인
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_SEARCH_BTN)
            
            assert home.find_element(HomeLocator.TRAVEL_GALLERY_SEARCH_INPUT).is_displayed()
            assert home.find_element(HomeLocator.TRAVEL_GALLERY_SEARCH_INPUT_DELETE_BTN).is_displayed()

            home.logger.info(f"[게시물 검색 버튼] 클릭 시, 피드 글 검색 페이지 정상 진입 및 주요 UI 노출 확인")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise

    @pytest.mark.parametrize("keyword, content", [
        ("위치", "대구 루시드 카페"), # test_hp_19_02
        ("내용", "푸딩 빙수 존맛탱"), # test_hp_19_03
        ("패키지", "알찬") # test_hp_19_04
    ])
    def test_hp_19_02(self, login_driver: WebDriver, keyword, content, request): # 입력한 키워드와 관련된 글이 검색 영역에 정상적으로 노출
        try:
            home = Home(login_driver)

            home.click_element(HomeLocator.TRAVEL_GALLERY_BTN)
            home.click_element(HomeLocator.TRAVEL_GALLERY_SEARCH_BTN)
            home.send_keys(HomeLocator.TRAVEL_GALLERY_SEARCH_INPUT, content)

            assert content in home.get_attribute(HomeLocator.TRAVEL_GALLERY_FIRST_RESULT, "content-desc")

            home.logger.info(f"{keyword}와 관련된 키워드 {content} 입력 시, 관련된 글이 검색 영역에 정상적으로 노출")
        except Exception as e:
            home.logger.error(f"테스트 실패: {e}")
            home.save_screenshot(request.node.name)
            raise
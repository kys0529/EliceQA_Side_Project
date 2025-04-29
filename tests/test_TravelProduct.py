import pytest
from src.pages.TravelProduct import TravelProduct
from src.utils.locators.TravelProductLocator import TravelProductListLocator
from appium.webdriver.webdriver import WebDriver


@pytest.mark.usefixtures("login_driver")
class TestTP01:
    # [TP_01_01] 여행 패키지 페이지 진입 확인
    def test_TP_01_01(self, login_driver: WebDriver, request):
        travelProduct = TravelProduct(login_driver)
        list_locators = TravelProductListLocator()
        
        try:
            travelProduct.travelproduct_navi_click()
            travelProduct.logger.info("여행 패키지 화면 진입")

            assert travelProduct.find_element(list_locators.PAGE_TITLE).is_displayed()
            travelProduct.logger.info("여행 패키지 페이지 진입 확인")

        except Exception as e:
            travelProduct.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travelProduct.save_screenshot(request.node.name)
            raise

        finally:
            travelProduct.logger.info("[TP_01_01] 여행 패키지 페이지 진입 확인 테스트 완료")


    # [TP_01_02] 여행 패키지 페이지 UI요소 노출 확인
    def test_TP_01_02(self, login_driver: WebDriver, request):
        travelProduct = TravelProduct(login_driver)
        list_locators = TravelProductListLocator()

        try:
            travelProduct.travelproduct_navi_click()
            travelProduct.logger.info("여행 패키지 화면 진입")
        
            for ui_check in list_locators.UI_CHECK_ELEMENT:
                assert travelProduct.find_element(ui_check).is_displayed()
            travelProduct.logger.info("여행 패키지 페이지 UI요소 노출 확인")

        except Exception as e:
            travelProduct.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travelProduct.save_screenshot(request.node.name)
            raise

        finally:
            travelProduct.logger.info("[TP_01_02] 여행 패키지 페이지 UI요소 노출 확인 테스트 완료")

        
class TestTP02:
    # [TP_02_01] 여행 패키지 페이지 검색 확인 - 검색 결과 존재하는 케이스
    def test_TP_02_01(self, login_driver: WebDriver, request):
        travelProduct = TravelProduct(login_driver)
        list_locators = TravelProductListLocator()

        search_text = "강원"

        try:
            travelProduct.travelproduct_navi_click()
            travelProduct.logger.info("여행 패키지 화면 진입")
        
            travelProduct.travelproduct_list_search(search_text)
            travelProduct.logger.info(f"{search_text} 여행 패키지 검색")

            assert travelProduct.find_element(list_locators.package_select(search_text)).is_displayed()
            travelProduct.logger.info(f"{search_text} 여행 패키지 페이지 검색 확인 - 검색 결과 존재하는 케이스")

        except Exception as e:
            travelProduct.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travelProduct.save_screenshot(request.node.name)
            raise

        finally:
            travelProduct.logger.info("[TP_02_01] 여행 패키지 페이지 검색 확인 - 검색 결과 존재하는 케이스 테스트 완료")


    # [TP_02_02] 여행 패키지 페이지 검색 확인 - 검색 결과 존재하지 않는 케이스
    def test_TP_02_02(self, login_driver: WebDriver, request):
        travelProduct = TravelProduct(login_driver)
        list_locators = TravelProductListLocator()

        search_text = "프랑스"

        try:
            travelProduct.travelproduct_navi_click()
            travelProduct.logger.info("여행 패키지 화면 진입")
        
            travelProduct.travelproduct_list_search(search_text)
            travelProduct.logger.info(f"{search_text} 여행 패키지 검색")

            for ui_check in list_locators.SEARCH_NONE_RESULT_CHECK:
                assert travelProduct.find_element(ui_check).is_displayed()
            travelProduct.logger.info(f"여행 패키지 페이지 검색 확인 - 검색 결과 존재하지 않는 케이스")

        except Exception as e:
            travelProduct.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travelProduct.save_screenshot(request.node.name)
            raise

        finally:
            travelProduct.logger.info("[TP_02_02] 여행 패키지 페이지 검색 확인 - 검색 결과 존재하지 않는 케이스 테스트 완료")


class TestTP03:
    # [TP_03_01] 여행 패키지 페이지 전체 필터 확인
    def test_TP_03_01(self, login_driver: WebDriver, request):
        travelProduct = TravelProduct(login_driver)
        list_locators = TravelProductListLocator()

        filter_name = "전체"

        try:
            travelProduct.travelproduct_navi_click()
            travelProduct.logger.info("여행 패키지 화면 진입")

            # 비교용으로 패키지 저장 필요
        
            travelProduct.travelproduct_filter_select(filter_name)
            travelProduct.logger.info(f"{filter_name} 필터 선택")
            
            # 비교용으로 패키지 저장 필요

            # assert 문으로 비교 필요
            travelProduct.logger.info(f"{filter_name} 전체 필터 확인")

        except Exception as e:
            travelProduct.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travelProduct.save_screenshot(request.node.name)
            raise

        finally:
            travelProduct.logger.info("[TP_03_01] 여행 패키지 페이지 전체 필터 확인 테스트 완료")


    # [TP_03_02~TP_03_11] 여행 패키지 페이지 필터 확인  
    @pytest.mark.parametrize("filter_name", ["서울", "인천/경기", "강원", "대전/충남", "충북", "광주/전남", "전북", "부산/경남", "대구/경북", "제주도"])
    def test_TP_03_02(self, login_driver: WebDriver, request, filter_name):
        travelProduct = TravelProduct(login_driver)
        list_locators = TravelProductListLocator()

        try:
            travelProduct.travelproduct_navi_click()
            travelProduct.logger.info("여행 패키지 화면 진입")
        
            travelProduct.travelproduct_filter_select(filter_name)
            travelProduct.logger.info(f"{filter_name} 필터 선택")

            assert travelProduct.find_element(list_locators.filter_select(filter_name)).is_displayed()
            travelProduct.logger.info(f"{filter_name} 필터 확인")

            # if문 이용해서 패키지 없으면 등록된 패키지 문구 확인 하는 기능 추가

        except Exception as e:
            travelProduct.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travelProduct.save_screenshot(request.node.name)
            raise

        finally:
            travelProduct.logger.info(f"[TP_03_02~TP_03_11] 여행 패키지 페이지 {filter_name} 필터 확인  테스트 완료")
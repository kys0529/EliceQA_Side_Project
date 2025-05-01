import pytest
from src.pages.TravelProduct import TravelProduct
from appium.webdriver.webdriver import WebDriver


@pytest.mark.usefixtures("login_driver")
class TestTP01:
    # [TP_01_01] 여행 패키지 페이지 진입 확인
    def test_TP_01_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)
        
        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")

            assert travel_product.is_package_title_displayed()
            travel_product.logger.info("여행 패키지 페이지 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_01_01] 여행 패키지 페이지 진입 확인 테스트 완료")

    # [TP_01_02] 여행 패키지 페이지 UI 요소 노출 확인
    def test_TP_01_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")
        
            assert travel_product.check_package_ui_elements()
            travel_product.logger.info("여행 패키지 페이지 UI요소 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_01_02] 여행 패키지 페이지 UI 요소 노출 확인 테스트 완료")


@pytest.mark.usefixtures("login_driver")
class TestTP02:
    # [TP_02_01] 여행 패키지 페이지 검색 확인 - 검색 결과 존재하는 케이스
    def test_TP_02_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        search_text = "강원"

        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")
        
            travel_product.search_package(search_text)
            travel_product.logger.info(f"{search_text} 여행 패키지 검색")

            assert travel_product.is_package_search_result_displayed(search_text)
            travel_product.logger.info(f"{search_text} 여행 패키지 검색 확인 - 검색 결과 존재")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_02_01] 여행 패키지 페이지 검색 확인 - 검색 결과 존재하는 케이스 테스트 완료")

    # [TP_02_02] 여행 패키지 페이지 검색 확인 - 검색 결과 존재하지 않는 케이스
    def test_TP_02_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        search_text = "프랑스"

        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")
        
            travel_product.search_package(search_text)
            travel_product.logger.info(f"{search_text} 여행 패키지 검색")

            assert travel_product.check_no_search_results()
            travel_product.logger.info(f"여행 패키지 검색 확인 - 검색 결과 없음")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_02_02] 여행 패키지 페이지 검색 확인 - 검색 결과 존재하지 않는 케이스 테스트 완료")


@pytest.mark.usefixtures("login_driver")
class TestTP03:
    # [TP_03_01] 여행 패키지 페이지 전체 필터 확인
    def test_TP_03_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        filter_name = "전체"

        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")

            initial_packages = travel_product.save_all_packages_back_top(5)
        
            travel_product.select_package_filter(filter_name)
            travel_product.logger.info(f"{filter_name} 필터 선택")
            
            current_packages = travel_product.save_all_packages(5)

            assert initial_packages == current_packages
            travel_product.logger.info(f"{filter_name} 전체 필터 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_03_01] 여행 패키지 페이지 전체 필터 확인 테스트 완료")

    # [TP_03_02~TP_03_11] 여행 패키지 페이지 지역별 필터 확인 
    @pytest.mark.parametrize("filter_name", ["서울", "인천/경기", "강원", "대전/충남", "충북", "광주/전남", "전북", "부산/경남", "대구/경북", "제주도"])
    def test_TP_03_02(self, login_driver: WebDriver, request, filter_name):
        travel_product = TravelProduct(login_driver)

        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")
        
            travel_product.select_package_filter(filter_name)
            travel_product.logger.info(f"{filter_name} 필터 선택")

            assert travel_product.package_filter_select_check(filter_name)
  
            element = travel_product.check_no_filter_results()
            if element:
                travel_product.logger.info(f"{filter_name} 필터 확인 - 등록된 패키지 없음")
            else:
                travel_product.logger.info(f"{filter_name} 필터 확인")
            
        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info(f"[TP_03_02~TP_03_11] 여행 패키지 페이지 {filter_name} 필터 확인 테스트 완료")
    

@pytest.mark.usefixtures("login_driver")
class TestTP04:
    # [TP_04_02] 여행 패키지 페이지 인기순 정렬 확인 
    def test_TP_04_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        sort_name = "인기순"

        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")

            travel_product.select_package_sort(sort_name)
            travel_product.logger.info(f"{sort_name} 정렬 선택")
            
            assert travel_product.is_sorted_by_popularity()
            travel_product.logger.info(f"{sort_name} 정렬 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info(f"[TP_04_02] 여행 패키지 페이지 인기순 정렬 확인 테스트 완료")
    
    # [TP_04_03] 여행 패키지 페이지 가격 낮은순 정렬 확인 
    def test_TP_04_03(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        sort_name = "가격 낮은순"

        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")

            travel_product.select_package_sort(sort_name)
            travel_product.logger.info(f"{sort_name} 정렬 선택")
            
            assert travel_product.is_sorted_by_lowest_price()
            travel_product.logger.info(f"{sort_name} 정렬 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info(f"[TP_04_03] 여행 패키지 페이지 가격 낮은순 정렬 확인 테스트 완료")
 
    # [TP_04_04] 여행 패키지 페이지 가격 높은순 정렬 확인
    def test_TP_04_04(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        sort_name = "가격 높은순"

        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")

            travel_product.select_package_sort(sort_name)
            travel_product.logger.info(f"{sort_name} 정렬 선택")
            
            assert travel_product.is_sorted_by_highest_price()
            travel_product.logger.info(f"{sort_name} 정렬 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info(f"[TP_04_04] 여행 패키지 페이지 가격 높은순 정렬 확인 테스트 완료")


@pytest.mark.usefixtures("login_driver")
class TestTP05:
    # [TP_05_01] 여행 패키지 페이지 찜 선택 확인
    def test_TP_05_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")

            before, after = travel_product.toggle_wishlist_button()
            travel_product.logger.info(f"찜 버튼 클릭")
            
            assert (before + 1) == after
            travel_product.logger.info(f"찜 선택 확인")
        
        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info(f"[TP_05_01] 여행 패키지 페이지 찜 선택 확인 테스트 완료")

    
    # [TP_05_02] 여행 패키지 페이지 찜 취소 확인
    def test_TP_05_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")

            before, after = travel_product.toggle_wishlist_button()
            travel_product.logger.info(f"찜 버튼 클릭")
            
            assert (before - 1) == after
            travel_product.logger.info(f"찜 취소 확인")
        
        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info(f"[TP_05_02] 여행 패키지 페이지 찜 취소 확인 테스트 완료")


@pytest.mark.usefixtures("login_driver")
class TestTP06:
    # [TP_06_01] 여행 패키지 페이지 무한 스크롤 확인
    def test_TP_06_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        try:
            travel_product.click_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")

            before, after = travel_product.package_infinitescroll_check()
            travel_product.logger.info("무한 스크롤 진행")

            assert len(before) < len(after)
            travel_product.logger.info("무한 스크롤 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info(f"[TP_06_02] 여행 패키지 페이지 무한 스크롤 확인 테스트 완료")
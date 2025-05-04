import pytest
from src.pages.TravelProduct import TravelProduct
from appium.webdriver.webdriver import WebDriver

''' 여행 패키지 화면 '''
@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP01:
    # [TP_01_01] 여행 패키지 화면으로 진입 확인
    def test_TP_01_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)
        
        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("하단 네비게이션 바 [여행상품] 탭 터치")

            assert travel_product.check_package_enter()
            travel_product.logger.info("여행 패키지 화면으로 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_01_01] 여행 패키지 화면으로 진입 확인 테스트 완료")

    # [TP_01_02] 여행 패키지 화면 UI 요소 확인
    def test_TP_01_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("하단 네비게이션 바 [여행상품] 탭 터치")
        
            assert travel_product.check_package_ui_elements()
            travel_product.logger.info("여행 패키지 화면 UI 요소 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_01_02] 여행 패키지 화면 UI 요소 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP02:
    # [TP_02_01] 여행 패키지 화면 검색 확인 - 검색 결과 존재하는 케이스
    def test_TP_02_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        search_text = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입 확인")
        
            travel_product.search_packages(search_text)
            travel_product.logger.info(f"상단 돋보기 아이콘 터치 및 검색어 {search_text} 입력")

            assert travel_product.check_search_packages(search_text)
            travel_product.logger.info(f"제목 또는 설명에 {search_text} 검색어가 포함된 여행 패키지 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_02_01] 여행 패키지 화면 검색 확인 - 검색 결과 존재하는 케이스 테스트 완료")

    # [TP_02_02] 여행 패키지 화면 검색 확인 - 검색 결과 존재하지 않는 케이스
    def test_TP_02_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        search_text = "프랑스"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입 확인")
        
            travel_product.search_packages(search_text)
            travel_product.logger.info(f"상단 돋보기 아이콘 터치 및 검색어 {search_text} 입력")

            assert travel_product.check_no_search_packages()
            travel_product.logger.info(f"{search_text} 검색 결과 없는 경우 안내 문구 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_02_02] 여행 패키지 화면 검색 확인 - 검색 결과 존재하지 않는 케이스 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP03:
    # [TP_03_01] 전체 필터에 맞는 여행 패키지 노출 확인
    def test_TP_03_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        filter_name = "전체"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입 확인")

            initial_packages = travel_product.save_all_packages_back_top(5)
        
            travel_product.select_filter(filter_name)
            travel_product.logger.info(f"상단 필터 아이콘 터치 및 {filter_name} 필터 선택")
            
            current_packages = travel_product.save_all_packages(5)

            assert initial_packages == current_packages
            travel_product.logger.info(f"선택된 {filter_name} 필터에 맞는 여행 패키지 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_03_01] 여행 패키지 화면 전체 필터 확인 테스트 완료")

    # [TP_03_02~TP_03_11] 선택된 필터에 맞는 여행 패키지 노출 확인 
    @pytest.mark.parametrize("filter_name", ["서울", "인천/경기", "강원", "대전/충남", "충북", "광주/전남", "전북", "부산/경남", "대구/경북", "제주도"])
    def test_TP_03_02(self, login_driver: WebDriver, request, filter_name):
        travel_product = TravelProduct(login_driver)

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입 확인")
        
            travel_product.select_filter(filter_name)
            travel_product.logger.info(f"상단 필터 아이콘 터치 및 {filter_name} 필터 선택")

            assert travel_product.check_select_filter(filter_name)
            element = travel_product.check_no_select_filter_packages()

            if element:
                travel_product.logger.info(f"{filter_name} 필터에 맞는 여행 패키지 노출 확인 - 필터 결과 없는 경우 안내 문구 노출 확인")
            else:
                travel_product.logger.info(f"선택된 {filter_name} 필터에 맞는 여행 패키지 노출 확인")
            
        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info(f"[TP_03_02~TP_03_11] 선택된 {filter_name} 필터에 맞는 여행 패키지 노출 확인 테스트 완료")
    

@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP04:
    # [TP_04_02] 여행 패키지 인기순으로 노출 확인
    def test_TP_04_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        sort_name = "인기순"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입 확인")

            travel_product.select_sort(sort_name)
            travel_product.logger.info(f"정렬 드롭박스 터치 터치 및 {sort_name} 정렬 선택")
            
            assert travel_product.check_select_sort_popularity()
            travel_product.logger.info(f"여행 패키지 {sort_name}으로 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_04_02] 여행 패키지 인기순으로 노출 확인 테스트 완료")
    
    # [TP_04_03] 여행 패키지 가격 낮은순으로 노출 확인 
    def test_TP_04_03(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        sort_name = "가격 낮은순"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입 확인")

            travel_product.select_sort(sort_name)
            travel_product.logger.info(f"정렬 드롭박스 터치 터치 및 {sort_name} 정렬 선택")
            
            assert travel_product.check_select_sort_lowest_price()
            travel_product.logger.info(f"여행 패키지 {sort_name}으로 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_04_03] 여행 패키지 가격 낮은순으로 노출 확인 테스트 완료")
 
    # [TP_04_04] 여행 패키지 가격 높은순으로 노출 확인
    def test_TP_04_04(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        sort_name = "가격 높은순"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입 확인")

            travel_product.select_sort(sort_name)
            travel_product.logger.info(f"정렬 드롭박스 터치 터치 및 {sort_name} 정렬 선택")
            
            assert travel_product.check_select_sort_highest_price()
            travel_product.logger.info(f"여행 패키지 {sort_name}으로 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_04_04] 여행 패키지 가격 높은순으로 노출 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP05:
    # [TP_05_01] 하트 아이콘 터치 후 찜 개수 확인
    def test_TP_05_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입 확인")

            before, after = travel_product.touch_wishlist()
            travel_product.logger.info(f"하트 아이콘 터치")
            
            assert (before + 1) == after
            travel_product.logger.info(f"찜 선택 확인")
        
        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_05_01] 하트 아이콘 터치 후 찜 개수 확인 테스트 완료")

    
    # [TP_05_02] 하트 아이콘 터치 취소 후 찜 개수 확인
    def test_TP_05_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입 확인")

            before, after = travel_product.touch_wishlist()
            travel_product.logger.info(f"하트 아이콘 터치")
            
            assert (before - 1) == after
            travel_product.logger.info(f"찜 취소 확인")
        
        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_05_02] 하트 아이콘 터치 취소 후 찜 개수 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP06:
    # [TP_06_01] 무한스크롤 확인
    def test_TP_06_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.logger.info("여행 패키지 화면 진입")

            before, after = travel_product.check_infinitescroll()
            travel_product.logger.info("무한스크롤 진행")

            assert len(before) < len(after)
            travel_product.logger.info("무한스크롤 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_06_01] 무한스크롤 확인 테스트 완료")


''' 여행 패키지 상세 화면 '''
@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP07:
    # [TP_07_01] 여행 패키지의 상세 화면으로 진입 확인
    def test_TP_07_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지 터치")

            assert travel_product.check_detail_enter()
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_07_01] 여행 패키지의 상세 화면으로 진입 확인 테스트 완료")

    # [TP_07_02] 여행 패키지의 상세 화면 화면 UI 요소 확인
    def test_TP_07_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            name, price = travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            element = travel_product.check_detail_image()

            if element:
                travel_product.logger.info("등록된 이미지 존재")
            else:
                travel_product.logger.info("등록된 이미지 없음")

            assert travel_product.check_detail_ui_elements(region, name, price)
            travel_product.logger.info("여행 패키지의 상세 화면 화면 UI 요소 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_07_02] 여행 패키지의 상세 화면 화면 UI 요소 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP08:
    # [TP_08_01] 해당 가이드의 채팅창 화면으로 진입 확인
    def test_TP_08_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            guide_name = travel_product.touch_guide_chatting()
            travel_product.logger.info("가이드 이름 우측 채팅 아이콘 터치")

            assert travel_product.check_guide_chatting_enter(guide_name)
            travel_product.logger.info(f"{guide_name} 가이드의 채팅창 화면으로 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_08_01] 해당 가이드의 채팅창 화면으로 진입 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP09:
    # [TP_09_02] 여행 코스의 여행 장소 바텀 시트 노출 확인
    def test_TP_09_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            name = travel_product.touch_travel_course()
            travel_product.logger.info("여행 코스의 여행 장소 터치")

            assert travel_product.check_travel_course_bottom_sheet(name)
            travel_product.logger.info("여행 코스의 여행 장소 바텀 시트 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_09_02] 여행 코스의 여행 장소 바텀 시트 노출 확인 테스트 완료")


''' 리뷰작성 화면 '''
@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP10:
    # [TP_10_01] 예약 승인된 회원 - 선택한 여행 패키지의 리뷰 화면으로 진입 확인(리뷰 존재하는 케이스)
    def test_TP_10_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 승인 리뷰 존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            name, _ = travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            travel_product.touch_review()
            travel_product.logger.info("여행 패키지의 상세 화면 리뷰/별점 터치")

            assert travel_product.check_review_enter(name)
            travel_product.logger.info("리뷰 화면으로 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_10_01] 예약 승인된 회원 - 선택한 여행 패키지의 리뷰 화면으로 진입 확인(리뷰 존재하는 케이스) 테스트 완료")
            
    # [TP_10_02] 예약 승인된 회원 - 선택한 여행 패키지의 리뷰 화면 UI 요소 확인(리뷰 존재하는 케이스)
    def test_TP_10_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 승인 리뷰 존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            review_count, review_rating = travel_product.touch_review()
            travel_product.logger.info("여행 패키지의 상세 화면 리뷰/별점 터치")

            assert travel_product.check_is_verified_review_visible_ui_elements(review_count, review_rating)
            travel_product.logger.info("리뷰 존재하는 경우 화면 UI 요소 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_10_02] 예약 승인된 회원 - 선택한 여행 패키지의 리뷰 화면 UI 요소 확인(리뷰 존재하는 케이스) 테스트 완료")

    # [TP_10_03] 예약 승인된 회원 - 선택한 여행 패키지의 리뷰 화면으로 진입 확인(리뷰 존재하지 않는 케이스)
    def test_TP_10_03(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 승인 리뷰 미존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            name, _ = travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            travel_product.touch_review()
            travel_product.logger.info("여행 패키지의 상세 화면 리뷰/별점 터치")

            assert travel_product.check_review_enter(name)
            travel_product.logger.info("리뷰 화면으로 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_10_03] 예약 승인된 회원 - 선택한 여행 패키지의 리뷰 화면으로 진입 확인(리뷰 존재하지 않는 케이스) 테스트 완료")

    # [TP_10_04] 예약 승인된 회원 - 선택한 여행 패키지의 리뷰 화면 UI 요소 확인(리뷰 존재하지 않는 케이스)
    def test_TP_10_04(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 승인 리뷰 미존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            review_count, review_rating = travel_product.touch_review()
            travel_product.logger.info("여행 패키지의 상세 화면 리뷰/별점 터치")

            assert travel_product.check_is_verified_no_review_visible_ui_elements(review_count, review_rating)
            travel_product.logger.info("리뷰 존재하지 않는 경우 화면 UI 요소 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_10_04] 예약 승인된 회원 - 선택한 여행 패키지의 리뷰 화면 UI 요소 확인(리뷰 존재하지 않는 케이스) 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP11:
    # [TP_11_01] 예약 승인된 회원 - 리뷰 작성하기 화면으로 진입 확인
    def test_TP_11_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 승인 리뷰 존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            travel_product.touch_package_save_info(region)
            travel_product.touch_review()
            travel_product.logger.info("리뷰 화면으로 진입 확인")

            travel_product.touch_review_write()
            travel_product.logger.info("리뷰 작성하기 터치")

            assert travel_product.check_review_write_enter()
            travel_product.logger.info("리뷰 작성 화면으로 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_11_01] 예약 승인된 회원 - 리뷰 작성하기 화면으로 진입 확인 테스트 완료")

    # [TP_11_02] 예약 승인된 회원 - 리뷰 작성하기 화면 UI 요소 확인
    def test_TP_11_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 승인 리뷰 존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            name, _ = travel_product.touch_package_save_info(region)
            travel_product.touch_review()
            travel_product.logger.info("리뷰 화면으로 진입 확인")

            travel_product.touch_review_write()
            travel_product.logger.info("리뷰 작성하기 터치")

            assert travel_product.check_review_write_ui_elements(name)
            travel_product.logger.info("리뷰 작성 화면 UI 요소 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_11_02] 예약 승인된 회원 - 리뷰 작성하기 화면 UI 요소 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP12:
    # [TP_12_01] 예약 승인된 회원 - 리뷰 별점 선택 시, 선택한 별만큼 별이 채워져 노출 확인
    def test_TP_12_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 승인 리뷰 존재 테스트용"
        count = 4

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            travel_product.touch_package_save_info(region)
            travel_product.touch_review()
            travel_product.touch_review_write()
            travel_product.logger.info("리뷰 작성 화면으로 진입 확인")

            save_path = travel_product.touch_review_star(count)
            travel_product.logger.info("별점 선택")

            ai_result = travel_product.check_review_star(save_path)
            assert ai_result == count
            travel_product.logger.info(f"별점 노출 확인 (선택: {count})")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_12_01] 예약 승인된 회원 - 리뷰 별점 선택 시, 선택한 별만큼 별이 채워져 노출 확인 테스트 완료")

    # [TP_12_02] 예약 승인된 회원 - 정상적으로 리뷰 내용 입력 확인
    def test_TP_12_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 승인 리뷰 존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            travel_product.touch_package_save_info(region)
            travel_product.touch_review()
            travel_product.touch_review_write()
            travel_product.logger.info("리뷰 작성 화면으로 진입 확인")

            text = travel_product.input_review()
            travel_product.logger.info("리뷰 작성 화면 리뷰 내용 입력")

            assert travel_product.check_input_review(text)
            travel_product.logger.info("리뷰 작성 화면 리뷰 내용 입력 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_12_02] 예약 승인된 회원 - 정상적으로 리뷰 내용 입력 확인 테스트 완료")

    # [TP_12_04] 예약 승인된 회원 - 리뷰 내용 미입력 시, 토스트 메시지 확인
    def test_TP_12_04(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 승인 리뷰 존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            travel_product.touch_package_save_info(region)
            travel_product.touch_review()
            travel_product.touch_review_write()
            travel_product.logger.info("리뷰 작성 화면으로 진입 확인")

            travel_product.touch_send_review()
            travel_product.logger.info("리뷰 등록 터치")

            assert travel_product.check_no_input_review()
            travel_product.logger.info("리뷰 미작성 시, 토스트 메시지 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_12_04] 예약 승인된 회원 - 리뷰 내용 미입력 시, 토스트 메시지 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP13:
    # [TP_13_01] 예약 승인되지 않은 회원 - 선택한 여행 패키지의 리뷰 화면으로 진입 확인(리뷰 존재하는 케이스)
    def test_TP_13_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 미승인 리뷰 존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            name, _ = travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            travel_product.touch_review()
            travel_product.logger.info("여행 패키지의 상세 화면 리뷰/별점 터치")

            assert travel_product.check_review_enter(name)
            travel_product.logger.info("리뷰 화면으로 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_13_01] 예약 승인되지 않은 회원 - 선택한 여행 패키지의 리뷰 화면으로 진입 확인(리뷰 존재하는 케이스) 테스트 완료")

    # [TP_13_02] 예약 승인되지 않은 회원 - 선택한 여행 패키지의 리뷰 화면 UI 요소 확인(리뷰 존재하는 케이스)
    def test_TP_13_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 미승인 리뷰 존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            review_count, review_rating = travel_product.touch_review()
            travel_product.logger.info("여행 패키지의 상세 화면 리뷰/별점 터치")

            assert travel_product.check_is_unverified_review_visible_ui_elements(review_count, review_rating)
            travel_product.logger.info("리뷰 존재하는 경우 화면 UI 요소 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_13_02] 예약 승인되지 않은 회원 - 선택한 여행 패키지의 리뷰 화면 UI 요소 확인(리뷰 존재하는 케이스) 테스트 완료")

    # [TP_13_03] 예약 승인되지 않은 회원 - 선택한 여행 패키지의 리뷰 화면으로 진입 확인(리뷰 존재하지 않는 케이스)
    def test_TP_13_03(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 미승인 리뷰 미존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            name, _ = travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            travel_product.touch_review()
            travel_product.logger.info("여행 패키지의 상세 화면 리뷰/별점 터치")

            assert travel_product.check_review_enter(name)
            travel_product.logger.info("리뷰 화면으로 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_13_03] 예약 승인되지 않은 회원 - 선택한 여행 패키지의 리뷰 화면으로 진입 확인(리뷰 존재하지 않는 케이스) 테스트 완료")

    # [TP_13_04] 예약 승인되지 않은 회원 - 선택한 여행 패키지의 리뷰 화면 UI 요소 확인(리뷰 존재하지 않는 케이스)
    def test_TP_13_04(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "예약 미승인 리뷰 미존재 테스트용"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.search_packages(region)
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            review_count, review_rating = travel_product.touch_review()
            travel_product.logger.info("여행 패키지의 상세 화면 리뷰/별점 터치")

            assert travel_product.check_is_unverified_no_review_visible_ui_elements(review_count, review_rating)
            travel_product.logger.info("리뷰 존재하지 않는 경우 화면 UI 요소 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_13_04] 예약 승인되지 않은 회원 - 선택한 여행 패키지의 리뷰 화면 UI 요소 확인(리뷰 존재하지 않는 케이스)테스트 완료")


''' 가이드 프로필 화면 '''
@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP14:
    # [TP_14_01] 가이드 이모지 터치 후 가이드 프로필 화면으로 진입 확인
    def test_TP_14_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            guide_name = travel_product.touch_guide_emoji()
            travel_product.logger.info("여행 패키지의 상세 화면 가이드 이름 좌측 사람 아이콘 터치")

            assert travel_product.check_guide_profile_enter(guide_name)
            travel_product.logger.info("가이드 프로필 화면으로 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_14_01] 가이드 이모지 터치 후 가이드 프로필 화면으로 진입 확인 테스트 완료")

    # [TP_14_02] 가이드 이름 터치 후 가이드 프로필 화면으로 진입 확인
    def test_TP_14_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            guide_name = travel_product.touch_guide_name()
            travel_product.logger.info("여행 패키지의 상세 화면 가이드 이름 터치")

            assert travel_product.check_guide_profile_enter(guide_name)
            travel_product.logger.info("가이드 프로필 화면으로 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_14_02] 가이드 이름 클릭 후 가이드 프로필 화면 진입 확인 테스트 완료")
    
    # [TP_14_03] 가이드 프로필 화면 화면 UI 요소 확인
    def test_TP_14_03(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인")

            guide_name = travel_product.touch_guide_name()
            travel_product.logger.info("여행 패키지의 상세 화면 가이드 이름 터치")

            assert travel_product.check_guide_profile_ui_elements(guide_name)
            travel_product.logger.info("가이드 프로필 화면 UI요소 노출 확인")
            
        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_14_03] 가이드 프로필 화면 화면 UI 요소 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP15:
    # [TP_15_01] 가이드 프로필에서 해당 가이드의 채팅창 화면으로 진입 확인
    def test_TP_15_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            guide_name = travel_product.touch_guide_emoji()
            travel_product.logger.info("가이드 프로필 화면으로 진입 확인")

            travel_product.touch_profile_guide_chatting()
            travel_product.logger.info("가이드 프로필 우측 채팅 아이콘 터치")

            assert travel_product.check_guide_chatting_enter(guide_name)
            travel_product.logger.info(f"{guide_name} 가이드의 채팅창 화면으로 진입 확인")      

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_15_01] 가이드 프로필에서 해당 가이드의 채팅창 화면으로 진입 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP16:
    # [TP_16_01] 이름 텍스트가 선택한 가이드의 이메일 주소로 변경되어 노출 확인
    def test_TP_14_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            guide_name = travel_product.touch_guide_emoji()
            travel_product.logger.info("가이드 프로필 화면으로 진입 확인")

            travel_product.touch_profile_guide_name(guide_name)
            travel_product.logger.info("가이드 프로필 가이드 이름 터치")

            assert travel_product.check_profile_guide_email()
            travel_product.logger.info("이름 텍스트가 선택한 가이드의 이메일 주소로 변경되어 노출 확인")      

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_16_01] 이름 텍스트가 선택한 가이드의 이메일 주소로 변경되어 노출 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP17:
    # [TP_17_01] 가이드의 패키지 목록 화면으로 진입 확인
    def test_TP_17_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            guide_name = travel_product.touch_guide_emoji()
            travel_product.logger.info("가이드 프로필 화면으로 진입 확인")

            travel_product.touch_package_more()
            travel_product.logger.info("가이드 프로필 패키지 더보기 터치")

            assert travel_product.check_guide_packages_enter(guide_name)
            travel_product.logger.info("가이드의 패키지 목록 화면으로 진입 확인")      

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_17_01] 가이드의 패키지 목록 화면으로 진입 확인 테스트 완료")

    # [TP_17_02] 가이드의 패키지 목록 전체 노출 확인
    def test_TP_17_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.touch_guide_emoji()
            travel_product.logger.info("가이드 프로필 화면으로 진입 확인")

            travel_product.touch_package_more()
            travel_product.logger.info("가이드 프로필 패키지 더보기 터치")

            assert travel_product.check_guide_packages()
            travel_product.logger.info("가이드의 패키지 목록 전체 노출 확인")      

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_17_02] 가이드 패키지 목록 화면 UI 요소 노출 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP18:
    # [TP_18_01] 가이드 패키지 목록에서 패키지 상세 화면 진입 확인
    def test_TP_18_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.touch_guide_emoji()
            travel_product.logger.info("가이드 프로필 화면으로 진입 확인")

            travel_product.touch_package_more()
            travel_product.logger.info("가이드 프로필 패키지 더보기 터치")

            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지 터치 및 패키지 정보 저장")

            assert travel_product.check_detail_enter()
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인") 

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_18_01] 가이드 패키지 목록에서 패키지 상세 화면 진입 확인 테스트 완료")

    # [TP_18_02] 가이드 패키지 목록에서 패키지 상세 화면 UI 요소 노출 확인
    def test_TP_18_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.touch_guide_emoji()
            travel_product.logger.info("가이드 프로필 화면으로 진입 확인")

            travel_product.touch_package_more()
            travel_product.logger.info("가이드 프로필 패키지 더보기 터치")

            name, price = travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지 터치 및 패키지 정보 저장")

            element = travel_product.check_detail_image()

            if element:
                travel_product.logger.info("등록된 이미지 존재")
            else:
                travel_product.logger.info("등록된 이미지 없음")

            assert travel_product.check_detail_ui_elements(region, name, price)
            travel_product.logger.info("여행 패키지의 상세 화면 화면 UI 요소 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_18_02] 가이드 패키지 목록에서 패키지 상세 화면 UI 요소 노출 확인 테스트 완료")


''' 예약하기 화면 '''
@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP19:
    # [TP_19_01] 예약 날짜 선택 화면으로 진입 확인
    def test_TP_19_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인") 

            travel_product.touch_reservation()
            travel_product.logger.info("여행 패키지의 상세 화면 하단 [예약하기] 버튼 터치")

            assert travel_product.check_reservation_enter()
            travel_product.logger.info("예약 날짜 선택 화면으로 진입 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_19_01] 예약 날짜 선택 화면으로 진입 확인 테스트 완료")

    # [TP_19_02] 예약하기 화면 화면 UI 요소 확인
    def test_TP_19_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.logger.info("여행 패키지의 상세 화면으로 진입 확인") 

            travel_product.touch_reservation()
            travel_product.logger.info("여행 패키지의 상세 화면 하단 [예약하기] 버튼 터치")
            
            assert travel_product.check_reservation_ui_elements()
            travel_product.logger.info("예약하기 화면 화면 UI 요소 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_19_02] 예약하기 화면 화면 UI 요소 확인 테스트 완료")


@pytest.mark.done
@pytest.mark.usefixtures("login_driver")
class TestTP20:
    # [TP_20_01] 예약하기 화면 캘린더 하단에 인원 선택 가능한 요소 노출 확인
    def test_TP_20_01(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.touch_reservation()
            travel_product.logger.info("예약 날짜 선택 화면으로 진입 확인")

            select_date = travel_product.touch_available_date()
            travel_product.logger.info(f"예약하기 화면 예약 가능한 날짜 {select_date} 터치")

            assert travel_product.check_select_personnel()
            travel_product.logger.info("예약하기 화면 캘린더 하단에 인원 선택 가능한 요소 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_20_01] 예약하기 화면 캘린더 하단에 인원 선택 가능한 요소 노출 확인 테스트 완료")

    # [TP_20_02] 예약하기 화면 캘린더 하단 UI 요소 확인
    def test_TP_20_02(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            travel_product.touch_reservation()
            travel_product.logger.info("예약 날짜 선택 화면으로 진입 확인")

            select_date = travel_product.touch_available_date()
            travel_product.logger.info(f"예약하기 화면 예약 가능한 날짜 {select_date} 터치")
            
            assert travel_product.check_selected_date_ui_elements()
            travel_product.logger.info("예약하기 화면 캘린더 하단 UI 요소 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_20_02] 예약하기 화면 캘린더 하단 UI 요소 확인 테스트 완료")

    # [TP_20_03] 인원 + 아이콘 터치 시, 인원 수 변동되며 인원수에 맞게 가격 변동 확인
    def test_TP_20_03(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            _, price = travel_product.touch_package_save_info(region)
            min_value, max_value = travel_product.touch_reservation()
            travel_product.logger.info("예약 날짜 선택 화면으로 진입 확인")

            select_date = travel_product.touch_available_date()
            travel_product.logger.info(f"예약하기 화면 예약 가능한 날짜 {select_date} 터치")

            add_count = 4

            touch_add_count = travel_product.touch_personner_add(add_count, min_value, max_value)
            travel_product.logger.info("예약하기 화면 인원 + 아이콘 터치")

            assert travel_product.check_personner_count(touch_add_count, min_value, price)
            travel_product.logger.info("인원 수 변동되며 인원수에 맞게 가격 변동 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_20_03] 인원 + 아이콘 터치 시, 인원 수 변동되며 인원수에 맞게 가격 변동 확인 테스트 완료")

    # [TP_20_04] 예약하기 화면 인원 최대 인원 수 달성 시 + 아이콘 비활성화되어 노출 확인
    def test_TP_20_04(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            min_value, max_value = travel_product.touch_reservation()
            travel_product.logger.info("예약 날짜 선택 화면으로 진입 확인")

            select_date = travel_product.touch_available_date()
            travel_product.logger.info(f"예약하기 화면 예약 가능한 날짜 {select_date} 터치")

            touch_add_count = max_value - min_value

            travel_product.touch_personner_add(touch_add_count, min_value, max_value)
            travel_product.logger.info("인원 선택 + 아이콘 터치")

            assert travel_product.check_personner_add_clickable()
            travel_product.logger.info("예약하기 화면 인원 최대 인원 수 달성 시 + 아이콘 비활성화되어 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_20_04] 예약하기 화면 인원 최대 인원 수 달성 시 + 아이콘 비활성화되어 노출 확인 테스트 완료")

    # [TP_20_05] 인원 - 아이콘 터치 시, 인원 수 변동되며 인원수에 맞게 가격 변동 확인
    def test_TP_20_05(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            _, price = travel_product.touch_package_save_info(region)
            min_value, max_value = travel_product.touch_reservation()
            travel_product.logger.info("예약 날짜 선택 화면으로 진입 확인")

            select_date = travel_product.touch_available_date()
            travel_product.logger.info(f"예약하기 화면 예약 가능한 날짜 {select_date} 터치")

            add_count = 20

            touch_add_count = travel_product.touch_personner_add(add_count, min_value, max_value)
            travel_product.logger.info("예약하기 화면 인원 + 아이콘 터치")

            minus_count = 3
            
            touch_minus_count = travel_product.touch_personner_minus(touch_add_count, minus_count)
            travel_product.logger.info("예약하기 화면 인원 - 아이콘 터치")

            assert travel_product.check_personner_count(touch_minus_count, min_value, price)
            travel_product.logger.info("인원 수 변동되며 인원수에 맞게 가격 변동 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_20_05] 인원 - 아이콘 터치 시, 인원 수 변동되며 인원수에 맞게 가격 변동 확인 테스트 완료")

    # [TP_20_06] 예약하기 화면 인원 최소 인원 수 달성 시 - 아이콘 비활성화되어 노출 확인
    def test_TP_20_06(self, login_driver: WebDriver, request):
        travel_product = TravelProduct(login_driver)

        region = "강원"

        try:
            travel_product.touch_travel_product_navigation()
            travel_product.touch_package_save_info(region)
            min_value, max_value = travel_product.touch_reservation()
            travel_product.logger.info("예약 날짜 선택 화면으로 진입 확인")

            select_date = travel_product.touch_available_date()
            travel_product.logger.info(f"예약하기 화면 예약 가능한 날짜 {select_date} 터치")

            add_count = 5

            touch_add_count = travel_product.touch_personner_add(add_count, min_value, max_value)
            travel_product.logger.info("예약하기 화면 인원 + 아이콘 터치")

            minus_count = touch_add_count
            
            travel_product.touch_personner_minus(touch_add_count, minus_count)
            travel_product.logger.info("예약하기 화면 인원 - 아이콘 터치")

            assert travel_product.check_personner_minus_clickable()
            travel_product.logger.info("예약하기 화면 인원 최소 인원 수 달성 시 - 아이콘 비활성화되어 노출 확인")

        except Exception as e:
            travel_product.logger.error(f"✖ 테스트 중 문제 발생: {e}")
            travel_product.save_screenshot(request.node.name)
            raise

        finally:
            travel_product.logger.info("[TP_20_06] 예약하기 화면 인원 최소 인원 수 달성 시 - 아이콘 비활성화되어 노출 확인 테스트 완료")

    




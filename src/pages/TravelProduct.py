import re
import time
import pytz
import os
from datetime import datetime
from src.pages.BasePage import BasePage
from src.utils.locators.TravelProductLocator import (
    TravelProductUtilLocator, 
    TravelProductListLocator, 
    TravelProductDetailLocator, 
    TravelProductReviewLocator,
    GuideProfileLocator, 
    ReservationLocator
)
from src.utils.locators.ChattingLocator import ChatRoomLocator
from src.utils.locators.MyPageLocator import MypageProfile
from src.resources.testdata.TravelProduct.TravelProdouctTestdata import TestItem

class TravelProduct(BasePage):
    def __init__(self, driver, page_name = "TravelProduct"):
        super().__init__(driver, page_name)
        self.util_locator = TravelProductUtilLocator
        self.page_locator = TravelProductListLocator
        self.detail_locator = TravelProductDetailLocator
        self.review_locator = TravelProductReviewLocator
        self.guide_profile_locator = GuideProfileLocator
        self.reservation_locator = ReservationLocator
        self.chat_locator = ChatRoomLocator
        self.mypage_profile_locator = MypageProfile


    ''' 여행 패키지 화면 '''
    # 하단 네비게이션 바 [여행상품] 탭 터치
    def touch_travel_product_navigation(self):
        self.click_element(self.page_locator.PAGE_NAVIGATION)

    # 여행 패키지 화면으로 진입 확인
    def check_package_enter(self):
        return self.find_element(self.page_locator.PAGE_TITLE).is_displayed()

    # 여행 패키지 화면 UI 요소 확인
    def check_package_ui_elements(self):
        return all( 
            self.find_element(ui_element).is_displayed()
            for ui_element in self.page_locator.UI_CHECK_ELEMENTS
        )

    # 상단 돋보기 아이콘 터치 및 검색어 입력
    def search_packages(self, search_text):
        self.click_element(self.page_locator.SEARCH_BUTTON)
        self.send_keys(self.util_locator.INPUT, search_text)
        self.driver.press_keycode(66)
        
    # 제목 또는 설명에 검색어가 포함된 여행 패키지 노출 확인
    def check_search_packages(self, package_name):
        return self.find_element(self.util_locator.get_image(package_name)).is_displayed()

    # 검색 결과 없는 경우 안내 문구 노출 확인
    def check_no_search_packages(self):
        return all(
            self.find_element(ui_element).is_displayed()
            for ui_element in self.page_locator.SEARCH_NO_RESULTS
        )

    # 상단 필터 아이콘 터치 및 필터 선택
    def select_filter(self, filter_name):
        self.click_element(self.page_locator.FILTER_BUTTON)
        self.click_element(self.util_locator.get_accessibility_id(filter_name))

    # 선택된 필터에 맞는 여행 패키지 노출 확인
    def check_select_filter(self, filter_name):
        return self.find_element(self.page_locator.get_selected_filter(filter_name)).is_displayed()

    # 여행 패키지 화면에 노출된 패키지 목록 수집
    def get_visible_packages(self):
        packages = self.driver.find_elements(*self.util_locator.IMAGES)
        package_items = []  
        for package in packages:
            package_items.append(package.get_attribute("content-desc"))
        return package_items

    # 여행 패키지 화면에 노출된 패키지 목록 수집 (스크롤 추가) 
    def save_all_packages(self, max_scroll, return_scroll_count=False):
        scroll_count = 1
        all_packages = []
        while scroll_count < max_scroll:
            current_packages = self.get_visible_packages()
            all_packages.extend(current_packages)     
            self.scroll_down()
            scroll_count += 1
        if return_scroll_count:
            return all_packages, scroll_count
        return all_packages
    
    # 여행 패키지 화면에 노출된 패키지 목록 수집 (스크롤 후 상단으로 이동 추가)
    def save_all_packages_back_top(self, max_scroll):
        all_packages, scroll_count = self.save_all_packages(max_scroll, return_scroll_count=True)
        while scroll_count > 1:
            self.scroll_up()
            scroll_count -= 1
        return all_packages
    
    # 필터 결과 없는 경우 안내 문구 노출 확인
    def check_no_select_filter_packages(self):
        return self.driver.find_elements(*self.page_locator.FILTER_NO_RESULTS)

    # 정렬 드롭박스 터치 터치 및 정렬 선택
    def select_sort(self, sort_name):
        self.click_element(self.util_locator.get_accessibility_id("기본순"))
        self.click_element(self.util_locator.get_button(sort_name))
    
    # 여행 패키지 인기순으로 노출 확인
    def check_select_sort_popularity(self):
        package_items = self.save_all_packages(5)
        popularity_values = []
        for package_item in package_items:
            popularity_values.append(int(package_item[-1]))    
        for i in range(1, len(popularity_values)):
            if popularity_values[i] > popularity_values[i - 1]:
                return False        
        return True

    # 여행 패키지 가격 낮은순으로 노출 확인
    def check_select_sort_lowest_price(self):
        package_items = self.save_all_packages(5)
        prices = []
        for package_item in package_items:
            match = re.search(r"₩([\d,]+)", package_item)
            price = int(match.group(1).replace(",", ""))
            prices.append(price)    
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                return False        
        return True
    
    # 여행 패키지 가격 높은순으로 노출 확인
    def check_select_sort_highest_price(self):
        package_items = self.save_all_packages(5)
        prices = []
        for package_item in package_items:
            match = re.search(r"₩([\d,]+)", package_item)
            price = int(match.group(1).replace(",", ""))
            prices.append(price)    
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                return False        
        return True
    
    # 패키지의 찜 개수 확인
    def get_wishlist_count(self):
        return int(self.get_attribute(self.util_locator.IMAGES, "content-desc")[-1])

    # 하트 아이콘 터치 후 찜 개수 확인
    def touch_wishlist(self):
        before = self.get_wishlist_count()
        package = self.find_element(self.util_locator.IMAGES) 
        wish_btn = package.find_element(*self.util_locator.BUTTON)
        wish_btn.click()
        time.sleep(0.5)   # 찜 클릭 후 개수 변경을 위한 대기
        after = self.get_wishlist_count()
        return before, after
    
    # 무한스크롤 확인
    def check_infinitescroll(self):
        before = self.get_visible_packages()
        after = self.save_all_packages(5)
        return before, after
    

    ''' 여행 패키지 상세 화면 '''
    # 여행 패키지 터치 및 패키지 정보 저장
    def touch_package_save_info(self, region):
        for _ in range(1, 100):
            elements = self.driver.find_elements(*self.util_locator.get_image(region))
            if elements:
                item = self.get_attribute(self.util_locator.get_image(region), "content-desc")
                name = item.split("\n")[0]
                price = re.search(r"₩([\d,]+)", item).group(1)
                self.click_element(self.util_locator.get_image(region))
                return name, price
            self.scroll_down()
    
    # 여행 패키지의 상세 화면으로 진입 확인
    def check_detail_enter(self):
        return self.find_element(self.detail_locator.DETAIL_TITLE).is_displayed()
    
    # 여행 패키지의 상세 화면 이미지 요소 확인
    def check_detail_image(self):
        return self.driver.find_elements(*self.util_locator.IMAGES)
    
    # 여행 패키지의 상세 화면 화면 UI 요소 확인
    def check_detail_ui_elements(self, region, name, price):
        ui_elements_found = False
        DETAIL_UI_ELEMENTS = [
            self.util_locator.get_text(name),
            self.util_locator.get_accessibility_id(region),
            self.util_locator.get_text(price),
            *self.detail_locator.UI_CHECK_ELEMENTS
        ]   
        for ui_element in DETAIL_UI_ELEMENTS:
            self.find_element(ui_element).is_displayed()
        for _ in range(1, 10):
            elements = self.driver.find_elements(*self.detail_locator.TRAVEL_COURSE)
            if elements:
                self.find_element(self.detail_locator.TRAVEL_COURSE).is_displayed()
                ui_elements_found = True
                break
            self.scroll_down()
        return ui_elements_found

    # 여행 패키지의 상세 화면 화면 가이드 이름 확인
    def get_guide_name(self):
        element = self.get_attribute(self.detail_locator.GUIDE_BUTTON, "content-desc")
        guide_name = element[5:]
        return guide_name
    
    # 가이드 이름 우측 채팅 아이콘 터치
    def touch_guide_chatting(self):
        guide_name = self.get_guide_name()
        self.click_element(self.detail_locator.GUIDE_CHATTING_BUTTON)
        return guide_name
     
    # 해당 가이드의 채팅창 화면으로 진입 확인
    def check_guide_chatting_enter(self, guide_name):
        return self.find_element(self.chat_locator.chat_room_title(guide_name)).is_displayed()
    
    # 여행 코스의 여행 장소 터치
    def touch_travel_course(self):
        for _ in range(1, 10):
            elements = self.driver.find_elements(*self.detail_locator.TRAVEL_COURSE_BUTTON)
            if elements:
                element = self.get_attribute(self.detail_locator.TRAVEL_COURSE_BUTTON, "content-desc")
                name = element[3:].split("\n")[0]
                self.click_element(self.detail_locator.TRAVEL_COURSE_BUTTON)
                return name
            self.scroll_down()
    
    # 여행 코스의 여행 장소 바텀 시트 노출 확인
    def check_travel_course_bottom_sheet(self, name):
        name_element = self.find_element(self.util_locator.get_text(name))
        bottom_sheet_element = self.find_element(self.detail_locator.TRAVEL_COURSE_BOTTOM_SHEET)
        return name_element.is_displayed() and bottom_sheet_element.is_displayed()
    

    ''' 리뷰작성 화면 '''
    # 여행 패키지의 상세 화면 리뷰/별점 터치
    def touch_review(self):
        lines = self.get_attribute(self.review_locator.REVIEW, "content-desc").strip().split("\n")
        review_count = int(''.join(filter(str.isdigit, lines[0])))
        review_rating = lines[1]
        self.click_element(self.detail_locator.REVIEW)
        return review_count, review_rating

    # 리뷰 화면으로 진입 확인
    def check_review_enter(self, name):
        return self.find_element(self.util_locator.get_text(name)).is_displayed()
    
    # 리뷰 화면 UI 요소
    def check_review_ui_elements(self, review_count, review_rating):
        REVIEW_UI_ELEMENTS = [
            self.util_locator.get_text(review_rating),
            self.review_locator.get_review_count(review_count)
        ]
        return REVIEW_UI_ELEMENTS
    
    # 리뷰 존재하는 경우 화면 UI 요소 확인 (예약 승인된 회원)
    def check_is_verified_review_visible_ui_elements(self, review_count, review_rating):
        REVIEW_UI_ELEMENTS = self.check_review_ui_elements(review_count, review_rating)
        REVIEW_UI_ELEMENTS.append(self.review_locator.VERIFIED_REVIEW_SECTION_VISIBLE)
        return all(
            self.find_element(ui_element).is_displayed()
            for ui_element in REVIEW_UI_ELEMENTS
        )
    
    # 리뷰 존재하는 경우 화면 UI 요소 확인 (예약 승인되지 않은 회원)
    def check_is_unverified_review_visible_ui_elements(self, review_count, review_rating):
        REVIEW_UI_ELEMENTS = self.check_review_ui_elements(review_count, review_rating)
        REVIEW_UI_ELEMENTS.append(self.review_locator.UNVERIFIED_REVIEW_SECTION_VISIBLE)
        REVIEW_UI_ELEMENTS.append(self.review_locator.UNVERIFIED_REVIEW)
        return all(
            self.find_element(ui_element).is_displayed()
            for ui_element in REVIEW_UI_ELEMENTS
        )
    
    # 리뷰 존재하지 않는 경우 화면 UI 요소 확인 (예약 승인된 회원)
    def check_is_verified_no_review_visible_ui_elements(self, review_count, review_rating):
        REVIEW_UI_ELEMENTS = self.check_review_ui_elements(review_count, review_rating)
        REVIEW_UI_ELEMENTS.append(self.review_locator.INVISIBLE_REVIEW)
        return all(
            self.find_element(ui_element).is_displayed()
            for ui_element in REVIEW_UI_ELEMENTS
        )
    
    # 리뷰 존재하지 않는 경우 화면 UI 요소 확인 (예약 승인되지 않은 회원)
    def check_is_unverified_no_review_visible_ui_elements(self, review_count, review_rating):
        REVIEW_UI_ELEMENTS = self.check_review_ui_elements(review_count, review_rating)
        REVIEW_UI_ELEMENTS.append(self.review_locator.INVISIBLE_REVIEW)
        REVIEW_UI_ELEMENTS.append(self.review_locator.UNVERIFIED_REVIEW)
        return all(
            self.find_element(ui_element).is_displayed()
            for ui_element in REVIEW_UI_ELEMENTS
        ) 
    
    # 리뷰 작성하기 터치
    def touch_review_write(self):
        self.click_element(self.review_locator.TO_WRITE_REVIEW)

    # 리뷰 작성 화면으로 진입 확인
    def check_review_write_enter(self):
        return self.find_element(self.review_locator.REVIEW_WRITE)
    
    # 리뷰 작성 화면 UI 요소 확인
    def check_review_write_ui_elements(self, name):
        REVIEW_WRITE_UI_ELEMENTS = [
            self.util_locator.get_text(name),
            self.util_locator.INPUT,
            self.review_locator.SEND_REVIEW
        ]
        for i in range(1, 6):
            REVIEW_WRITE_UI_ELEMENTS.append(self.review_locator.select_review_star(i))
        return all(
            self.find_element(ui_element).is_displayed()
            for ui_element in REVIEW_WRITE_UI_ELEMENTS
        )
    
    # 별점 선택
    def touch_review_star(self, count):
        for i in range(1, count + 1):
            self.click_element(self.review_locator.select_review_star(i))
        base_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(base_dir, "../resources/testdata/TravelProduct", "selected_review_star.png")
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        self.driver.save_screenshot(save_path)
        return save_path

    # 별점 노출 확인
    def check_review_star(self, save_path):
        ai_result = TestItem.get_star_count_from_api(save_path) # google Ai 사용
        return ai_result
        
    # 리뷰 작성 화면 리뷰 내용 입력
    def input_review(self):
        text = "리뷰 작성 테스트 중입니다"
        review = self.click_element(self.util_locator.INPUT)
        review.send_keys(text) 
        return text
    
    # 리뷰 작성 화면 리뷰 내용 입력 확인
    def check_input_review(self, text):
        return self.find_element(self.util_locator.INPUT).text == text
    
    # 리뷰 등록 터치
    def touch_send_review(self):
        self.click_element(self.review_locator.SEND_REVIEW)
    
    # 리뷰 미작성 시, 토스트 메시지 노출 확인
    def check_no_input_review(self):
        return self.find_element(self.review_locator.NO_INPUT_REVIEW)


    ''' 가이드 프로필 화면 '''
    # 여행 패키지의 상세 화면 가이드 이름 좌측 사람 아이콘 터치
    def touch_guide_emoji(self):
        guide_name = self.get_guide_name()
        self.click_element(self.detail_locator.GUIDE_EMOJI_BUTTON)
        return guide_name
    
    # 여행 패키지의 상세 화면 가이드 이름 터치
    def touch_guide_name(self):
        guide_name = self.get_guide_name()
        self.click_element(self.detail_locator.GUIDE_BUTTON)
        return guide_name

    # 가이드 프로필 화면으로 진입 확인
    def check_guide_profile_enter(self, guide_name):
        return self.find_element(self.mypage_profile_locator.get_profile_title_locator(guide_name))

    # 가이드 프로필 화면 화면 UI 요소 확인
    def check_guide_profile_ui_elements(self, guide_name):
        GUIDE_PROFILE_UI_ELEMENTS = self.guide_profile_locator.UI_CHECK_ELEMENTS
        GUIDE_PROFILE_UI_ELEMENTS.append(self.util_locator.get_accessibility_id(guide_name))
        return all(
            self.find_element(ui_element).is_displayed()
            for ui_element in GUIDE_PROFILE_UI_ELEMENTS
        )

    # 가이드 프로필 우측 채팅 아이콘 터치
    def touch_profile_guide_chatting(self):
        self.click_element(self.guide_profile_locator.GUIDE_CHATTING_BUTTON)

    # 가이드 프로필 가이드 이름 터치
    def touch_profile_guide_name(self, guide_name):
        self.click_element(self.guide_profile_locator.guide_name_to_email(guide_name))

    # 이름 텍스트가 선택한 가이드의 이메일 주소로 변경되어 노출 확인
    def check_profile_guide_email(self):
        elements = self.driver.find_elements(*self.util_locator.TEXT)
        for element in elements:
            desc = element.get_attribute("content-desc")
            if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", desc):
                return True
        return False

    # 가이드 프로필 패키지 더보기 터치
    def touch_package_more(self):
        self.click_element(self.guide_profile_locator.PACKAGE_MORE_BUTTON)
    
    # 가이드의 패키지 목록 화면으로 진입 확인
    def check_guide_packages_enter(self, guide_name):
        return self.find_element(self.guide_profile_locator.guide_package_title(guide_name))
    
    # 가이드의 패키지 목록 전체 노출 확인
    def check_guide_packages(self):
        return self.find_element(self.util_locator.IMAGES).is_displayed()
    

    ''' 예약하기 화면 '''
    # 여행 패키지의 상세 화면 하단 [예약하기] 버튼 터치 및 예약 가능 인원 저장
    def touch_reservation(self):
        element = self.get_attribute(self.detail_locator.PARTICIPANTS, "content-desc")
        min_value = int(''.join(filter(str.isdigit, element.split("~")[0])))
        max_value = int(''.join(filter(str.isdigit, element.split("~")[1])))
        self.click_element(self.detail_locator.RESERVATION_BUTTON)
        return min_value, max_value

    # 예약 날짜 선택 화면으로 진입 확인
    def check_reservation_enter(self):
        return self.find_element(self.reservation_locator.RESERVATION_TITLE).is_displayed()

    # 오늘 날짜 받아오기
    def get_today_date(self, zero_pad=False):
        kst = pytz.timezone('Asia/Seoul')
        now_kst = datetime.now(kst)
        if zero_pad:
            year_month = f"{now_kst.year}년 {now_kst.month:02}월"
            return year_month
        else:
            year_month = f"{now_kst.year}년 {now_kst.month}월"
            return year_month

    # 예약하기 화면 화면 UI 요소 확인
    def check_reservation_ui_elements(self):
        year_month = self.get_today_date()
        year_month_title = self.find_element(self.util_locator.get_text(year_month))
        calendar = self.find_element(self.reservation_locator.CALENDAR)
        return year_month_title.is_displayed and calendar.is_displayed()

    # 예약하기 화면 예약 가능한 날짜 터치
    def touch_available_date(self):
        year_month_touch = self.get_today_date()
        year_month_check = self.get_today_date(zero_pad=True)
        for day in range(1, 32):
            touch_date = f"{year_month_touch} {day}일"
            check_date = f"{year_month_check} {day:02}일"
            self.click_element(self.util_locator.get_text(touch_date))
            elements = self.driver.find_elements(*self.reservation_locator.get_selected_date(check_date))
            if elements:
                select_date = elements[0].get_attribute("content-desc")
                break
        return select_date
                  
    # 예약하기 화면 캘린더 하단에 인원 선택 가능한 요소 노출 확인
    def check_select_personnel(self):
        return self.find_element(self.reservation_locator.SELECT_PERSONNEL).is_displayed()

    # 예약하기 화면 캘린더 하단 UI 요소 확인
    def check_selected_date_ui_elements(self):
        return all (
            self.find_element(ui_element).is_displayed()
            for ui_element in self.reservation_locator.UI_CHECK_ELEMENTS
        )

    # 예약하기 화면 인원 + 아이콘 터치
    def touch_personner_add(self, count, min_value, max_value):
        available_clicks = max_value - min_value
        touch_add_count = min(count, available_clicks)
        for _ in range(touch_add_count):
            is_clickable = self.get_attribute(self.reservation_locator.ADD_PERSONNEL, "clickable")
            if is_clickable == "true":
                self.click_element(self.reservation_locator.ADD_PERSONNEL)
            else:
                break
        return touch_add_count
           
    # 인원 수 변동되며 인원수에 맞게 가격 변동 확인
    def check_personner_count(self, touch_count, min_value, price):
        personner_count = min_value + touch_count
        all_price = personner_count * int(price.replace(",", ""))
        price_text = f"₩{all_price:,}"
        UI_CHECK_ELEMENTS = [personner_count, price_text]
        return all (
            self.find_element(self.util_locator.get_text(ui_element)).is_displayed()
            for ui_element in UI_CHECK_ELEMENTS
        )

    # 예약하기 화면 인원 - 아이콘 터치
    def touch_personner_minus(self, add_count, minus_count):
        touch_minus_count = min(minus_count, add_count)
        for _ in range(touch_minus_count):
            is_clickable = self.get_attribute(self.reservation_locator.MINUS_PERSONNEL, "clickable")
            if is_clickable == "true":
                self.click_element(self.reservation_locator.MINUS_PERSONNEL)
            else:
                break
        return touch_minus_count

    # 예약하기 화면 인원 최대 인원 수 달성 시 + 아이콘 비활성화되어 노출 확인
    def check_personner_add_clickable(self):
        is_clickable = self.get_attribute(self.reservation_locator.ADD_PERSONNEL, "clickable")
        return is_clickable != "true"
        
    # 예약하기 화면 인원 최소 인원 수 달성 시 - 아이콘 비활성화되어 노출 확인
    def check_personner_minus_clickable(self):
        is_clickable = self.get_attribute(self.reservation_locator.MINUS_PERSONNEL, "clickable")
        return is_clickable != "true"




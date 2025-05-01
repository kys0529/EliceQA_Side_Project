import re
import time
from src.utils.locators.TravelProductLocator import TravelProductUtilLocator, TravelProductListLocator, TravelProductDetailLocator
from src.utils.locators.ChattingLocator import ChatRoomLocator
from src.pages.BasePage import BasePage

class TravelProduct(BasePage):
    def __init__(self, driver, page_name = "TravelProduct"):
        super().__init__(driver, page_name)
        self.util_locator = TravelProductUtilLocator
        self.page_locator = TravelProductListLocator
        self.detail_locator = TravelProductDetailLocator
        self.chat_locator = ChatRoomLocator

    # 네비게이션 탭 클릭
    def click_travel_product_navigation(self):
        self.click_element(self.page_locator.PAGE_NAVIGATION)

    # 네비게이션 탭 클릭
    def is_package_title_displayed(self):
        return self.find_element(self.page_locator.PAGE_TITLE).is_displayed()

    # 주요 UI 요소 노출 여부 확인
    def check_package_ui_elements(self):
        return all( 
            self.find_element(ui_element).is_displayed()
            for ui_element in self.page_locator.UI_CHECK_ELEMENTS
        )

    # 패키지 검색
    def search_package(self, search_text):
        self.click_element(self.page_locator.SEARCH_BUTTON)
        self.send_keys(self.util_locator.INPUT, search_text)
        self.driver.press_keycode(66)
        
    # 검색 결과 노출 여부 확인
    def is_package_search_result_displayed(self, package_name):
        return self.find_element(self.util_locator.get_image(package_name)).is_displayed()

    # 검색 결과 없음 문구 확인
    def check_no_search_results(self):
        return all(
            self.find_element(ui_element).is_displayed()
            for ui_element in self.page_locator.SEARCH_NO_RESULTS
        )

    # 필터 선택
    def select_package_filter(self, filter_name):
        self.click_element(self.page_locator.FILTER_BUTTON)
        self.click_element(self.util_locator.get_accessibility_id(filter_name))

    # 선택한 필터가 적용됐는지 확인
    def package_filter_select_check(self, filter_name):
        return self.find_element(self.page_locator.get_selected_filter(filter_name)).is_displayed()

    # 현재 화면에 노출된 패키지 정보 수집
    def get_visible_packages(self):
        packages = self.driver.find_elements(*self.util_locator.IMAGES)
        package_items = []  
        for package in packages:
            package_items.append(package.get_attribute("content-desc"))
        return package_items

    # 스크롤 하면서 패키지 정보 수집
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
    
    # 스크롤 후 수집하고 다시 상단으로 이동
    def save_all_packages_back_top(self, max_scroll):
        all_packages, scroll_count = self.save_all_packages(max_scroll, return_scroll_count=True)
        while scroll_count > 1:
            self.scroll_up()
            scroll_count -= 1
        return all_packages
    
    # 필터 결과 없음 케이스 확인
    def check_no_filter_results(self):
        return self.driver.find_elements(*self.page_locator.FILTER_NO_RESULTS)

    # 정렬 옵션 선택
    def select_package_sort(self, sort_name):
        self.click_element(self.util_locator.get_accessibility_id("기본순"))
        self.click_element(self.util_locator.get_button(sort_name))
    
    # 인기순 정렬 확인
    def is_sorted_by_popularity(self):
        package_items = self.save_all_packages(5)
        popularity_values = []
        for package_item in package_items:
            popularity_values.append(int(package_item[-1]))    
        for i in range(1, len(popularity_values)):
            if popularity_values[i] > popularity_values[i - 1]:
                return False        
        return True

    # 가격 낮은순 정렬 확인
    def is_sorted_by_lowest_price(self):
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
    
    # 가격 높은순 정렬 확인
    def is_sorted_by_highest_price(self):
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
    
    # 첫 번째 패키지의 찜 개수 확인
    def get_wishlist_count(self):
        return int(self.get_attribute(self.util_locator.IMAGES, "content-desc")[-1])

    # 찜 버튼 토글 후 찜 개수 비교
    def toggle_wishlist_button(self):
        before = self.get_wishlist_count()
        package = self.find_element(self.util_locator.IMAGES) 
        wish_btn = package.find_element(*self.util_locator.BUTTON)
        wish_btn.click()
        time.sleep(0.5)   # 찜 클릭 후 개수 변경을 위한 대기
        after = self.get_wishlist_count()
        return before, after
    
    # 무한스크롤 확인
    def package_infinitescroll_check(self):
        before = self.get_visible_packages()
        after = self.save_all_packages(5)
        return before, after
    
    # 패키지 클릭 후 이름/가격 저장
    def click_package_save_info(self, region):
        for _ in range(1, 10):
            elements = self.driver.find_elements(*self.util_locator.get_image(region))
            if elements:
                item = self.get_attribute(self.util_locator.get_image(region), "content-desc")
                name = item.split("\n")[0]
                price = re.search(r"₩([\d,]+)", item).group(1)
                self.click_element(self.util_locator.get_image(region))
                return name, price
            self.scroll_down()
    
    # 상세 타이틀 노출 여부 확인
    def is_detail_title_displayed(self):
        return self.find_element(self.detail_locator.DETAIL_TITLE).is_displayed()
    
    # 상세 이미지 요소 확인
    def check_detail_image_elements(self):
        return self.driver.find_elements(*self.util_locator.IMAGES)
    
    # 상세 화면 UI 요소 노출 여부 확인
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

    # 가이드 채팅 진입
    def click_guide_chatting(self):
        element = self.get_attribute(self.detail_locator.GUIDE, "content-desc")
        guide_name = element[5:]
        self.click_element(self.detail_locator.GUIDE_CHATTING_BUTTON)
        return guide_name
     
    # 가이드 채팅 화면 타이틀 노출 여부 확인
    def is_guide_chatting_title_displayed(self, guide_name):
        return self.find_element(self.chat_locator.chat_room_title(guide_name)).is_displayed()
    
    # 여행 코스 클릭
    def click_travel_course(self):
        for _ in range(1, 10):
            elements = self.driver.find_elements(*self.detail_locator.TRAVEL_COURSE_BUTTON)
            if elements:
                element = self.get_attribute(self.detail_locator.TRAVEL_COURSE_BUTTON, "content-desc")
                name = element[3:].split("\n")[0]
                self.click_element(self.detail_locator.TRAVEL_COURSE_BUTTON)
                return name
            self.scroll_down()
    
    # 여행 코스 클릭 바텀시트 노출 확인
    def is_travel_lane_bottom_sheet_displayed(self, name):
        name_element = self.find_element(self.util_locator.get_text(name))
        bottom_sheet_element = self.find_element(self.detail_locator.TRAVEL_COURSE_BOTTOM_SHEET)
        return name_element.is_displayed() and bottom_sheet_element.is_displayed()



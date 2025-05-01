import re
import time
from src.utils.locators.TravelProductLocator import TravelProductListLocator
from src.pages.BasePage import BasePage

class TravelProduct(BasePage):
    def __init__(self, driver, page_name = "TravelProduct"):
        super().__init__(driver, page_name)
        self.page_locator = TravelProductListLocator

    # 여행 상품 네비게이션 탭 클릭
    def click_travel_product_navigation(self):
        self.click_element(self.page_locator.PAGE_NAVIGATION)

    # 여행 패키지 페이지 타이틀이 노출되는지 확인
    def is_package_title_displayed(self):
        return self.find_element(self.page_locator.PAGE_TITLE).is_displayed()

    # 여행 패키지 페이지의 주요 UI 요소들 노출되는지 확인
    def check_package_ui_elements(self):
        return all( 
            self.find_element(ui_element).is_displayed()
            for ui_element in self.page_locator.UI_CHECK_ELEMENTS
        )

    # 여행 패키지 검색
    def search_package(self, search_text):
        self.click_element(self.page_locator.SEARCH_BUTTON)
        self.send_keys(self.page_locator.SEARCH_INPUT, search_text)
        self.driver.press_keycode(66)
        
    # 검색한 여행 패키지가 노출되는지 확인
    def is_package_search_result_displayed(self, package_name):
        return self.find_element(self.page_locator.get_package_by_text(package_name)).is_displayed()

    # 검색 결과 없는 케이스 안내 문구 노출되는지 확인
    def check_no_search_results(self):
        return all(
            self.find_element(ui_element).is_displayed()
            for ui_element in self.page_locator.SEARCH_NO_RESULTS
        )

    # 여행 패키지 필터 선택
    def select_package_filter(self, filter_name):
        self.click_element(self.page_locator.FILTER_BUTTON)
        self.click_element(self.page_locator.get_filter_option(filter_name))

    # 여행 패키지 필터 적용 확인
    def package_filter_select_check(self, filter_name):
        return self.find_element(self.page_locator.get_selected_filter(filter_name)).is_displayed()

    # 현재 화면에 노출된 패키지 정보를 저장
    def get_visible_packages(self):
        packages = self.driver.find_elements(*self.page_locator.PACKAGE_IMAGES)
        package_items = []  
        for package in packages:
            package_items.append(package.get_attribute("content-desc"))
        return package_items

    # 스크롤하며 모든 패키지 정보를 저장
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
    
    # 스크롤하며 모든 패키지 정보를 저장 후 다시 상단으로 이동
    def save_all_packages_back_top(self, max_scroll):
        all_packages, scroll_count = self.save_all_packages(max_scroll, return_scroll_count=True)
        while scroll_count > 1:
            self.scroll_up()
            scroll_count -= 1
        return all_packages
    
    # 필터 적용 후 등록된 패키지 없는 케이스 확인
    def check_no_filter_results(self):
        return self.driver.find_elements(*self.page_locator.FILTER_NO_RESULTS)

    # 여행 패키지 정렬 옵션 선택
    def select_package_sort(self, sort_name):
        self.click_element(self.page_locator.SORT_BUTTON)
        self.click_element(self.page_locator.get_sort_option(sort_name))
    
    # 여행 패키지가 인기순으로 정렬되었는지 확인
    def is_sorted_by_popularity(self):
        package_items = self.save_all_packages(3)
        popularity_values = []
        for package_item in package_items:
            popularity_values.append(int(package_item[-1]))    
        for i in range(1, len(popularity_values)):
            if popularity_values[i] > popularity_values[i - 1]:
                return False        
        return True

    # 여행 패키지가 가격 낮은순으로 정렬되었는지 확인
    def is_sorted_by_lowest_price(self):
        package_items = self.save_all_packages(3)
        prices = []
        for package_item in package_items:
            match = re.search(r"₩([\d,]+)", package_item)
            price = int(match.group(1).replace(",", ""))
            prices.append(price)    
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                return False        
        return True
    
    # 여행 패키지 정렬 가격 높은순 확인
    def is_sorted_by_highest_price(self):
        package_items = self.save_all_packages(3)
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
        return int(self.get_attribute(self.page_locator.PACKAGE_IMAGES, "content-desc")[-1])

    # 여행 패키지 찜 선택 확인
    def toggle_wishlist_button(self):
        before = self.get_wishlist_count()
        package = self.find_element(self.page_locator.PACKAGE_IMAGES) 
        wish_btn = package.find_element(*self.page_locator.WISHLIST_BUTTON)
        wish_btn.click()
        time.sleep(0.5)   # 찜 클릭 후 개수 변경을 위한 대기
        after = self.get_wishlist_count()
        return before, after
    
    # 여행 패키지 무한 스크롤 확인
    def package_infinitescroll_check(self):
        before = self.get_visible_packages()
        after = self.save_all_packages(3)
        return before, after
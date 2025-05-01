import pytest
from appium.webdriver.webdriver import WebDriver
from src.pages.MyPage import MyPage
from src.utils.locators import MyPageLocator

# class TestMP00:
#     def test_mp_00_00(): # 기능/의도 설명
#         mypage = MyPage() # 클래스에 대한 객체의 변수명은 첫 문자를 소문자로!


@pytest.mark.usefixtures("login_driver")
class TestMP01: # 홈 탭 진입 상태 > 마이페이지 진입 가능 여부 확인
    def test_mp_01_01(self, login_driver:WebDriver, request):
        try:
            mypage = MyPage()
            mypage.driver.find_element(*MyPageLocator.MypageMainLocator.MYPAGE_TAB).click()
            assert mypage.find_element(*MyPageLocator.MypageMainLocator.MYPAGE_TITLE).is_displayed()
            mypage.logger.info("✅ 홈 탭 진입 상태에서 마이페이지 진입 확인")
        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise
import pytest
from appium.webdriver.webdriver import WebDriver
from src.pages.MyPage import MyPage
from src.utils.locators import MyPageLocator
import time

# class TestMP00:
#     def test_mp_00_00(): # 기능/의도 설명
#         mypage = MyPage() # 클래스에 대한 객체의 변수명은 첫 문자를 소문자로!


@pytest.mark.usefixtures("login_driver")
class TestMP01:
    @pytest.mark.done
    def test_mp_01_01(self, login_driver: WebDriver, request):  # 홈 탭 진입 상태 > 마이페이지 탭 진입 가능 여부 확인
        try:
            # Precondition
            mypage = MyPage(login_driver)

            # Steps
            mypage.into_mypage()

            # Expected Result
            assert mypage.find_element(MyPageLocator.MypageMain.MYPAGE_TITLE)
            mypage.logger.info("✅ 홈 탭 진입 상태에서 마이페이지 진입 확인")

        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise

    @pytest.mark.done
    def test_mp_01_02(self, login_driver: WebDriver, request):  # 여행상품 탭 진입 상태 > 마이페이지 탭 진입 가능 여부 확인
        try:
            # Precondition
            mypage = MyPage(login_driver)
            mypage.click_element(MyPageLocator.MypageMain.TRAVEL_PRODUCT_TAB)

            # Steps
            mypage.into_mypage()

            # Expected Result
            assert mypage.find_element(MyPageLocator.MypageMain.MYPAGE_TITLE)
            mypage.logger.info("✅ 여행상품 탭 진입 상태에서 마이페이지 진입 확인")

        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise

    @pytest.mark.done
    def test_mp_01_03(self, login_driver: WebDriver, request):  # 채팅 탭 진입 상태 > 마이페이지 탭 진입 가능 여부 확인
        try:
            # Precondition
            mypage = MyPage(login_driver)
            mypage.click_element(MyPageLocator.MypageMain.CHATTING_TAB)

            # Steps
            mypage.into_mypage()

            # Expected Result
            assert mypage.find_element(MyPageLocator.MypageMain.MYPAGE_TITLE)
            mypage.logger.info("✅ 채팅 탭 진입 상태에서 마이페이지 진입 확인")
        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise

    @pytest.mark.done
    def test_mp_01_04(self, login_driver: WebDriver, request):  # 마이페이지 탭 진입 상태 > 마이페이지 탭 선택 시 진입 상태 유지 확인
        try:
            # Precondition
            mypage = MyPage(login_driver)
            mypage.into_mypage()
            time.sleep(1)  # 마이페이지 진입 후 아주 잠시 대기

            # Steps
            mypage.into_mypage()

            # Expected Result
            assert mypage.find_element(MyPageLocator.MypageMain.MYPAGE_TITLE)
            mypage.logger.info(
                "✅ 마이페이지 탭 진입 상태에서 마이페이지 진입 상태 유지 확인"
            )

        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise


@pytest.mark.skip("스크린샷으로 비교 필요로, 검증 과정 추후 개발 예정")
@pytest.mark.usefixtures("login_driver")
class TestMP02:
    @pytest.mark.wip
    def test_mp_02_01(self, login_driver: WebDriver, request):  # 앱 테마 변경 - 다크 모드
        try:
            # Precondition
            mypage = MyPage(login_driver)
            mypage.into_mypage()

            # Steps
            mypage.click_element(MyPageLocator.MypageMain.THEME_TOGGLE_BTN)

            # Expected Result
            '''assert 추가 필요'''
            mypage.logger.info("✅ 앱 테마 - 다크 모드로 변경 확인")

        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise

    @pytest.mark.wip
    def test_mp_02_02(self, login_driver: WebDriver, request):  # 앱 테마 변경 - 라이트 모드
        try:
            # Precondition
            mypage = MyPage(login_driver)
            mypage.into_mypage()

            # Steps
            mypage.click_element(MyPageLocator.MypageMain.THEME_TOGGLE_BTN)
            mypage.click_element(MyPageLocator.MypageMain.THEME_TOGGLE_BTN)

            # Expected Result
            '''assert 추가 필요'''
            mypage.logger.info("✅ 앱 테마 - 라이트 모드로 변경 확인")

        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise


@pytest.mark.usefixtures("login_driver")
class TestMP03:
    def test_mp_03_01(self, login_driver: WebDriver, request):  # 마이페이지 > 프로필 페이지 진입 여부 확인
        try:
            # Precondition
            mypage = MyPage(login_driver)
            mypage.into_mypage()
            nickname = mypage.get_nickname()  # 현재 로그인 한 유저의 닉네임 받아오기
            mypage.logger.info(f"✅ 현재 로그인 한 유저 닉네임 : {nickname}")

            # Steps
            mypage.click_element(MyPageLocator.MypageMain.PROFILE_PHOTO)

            PROFILE_PAGE_TITLE = MyPageLocator.MypageProfile.get_profile_title_locator(nickname)  # 프로필 페이지 타이틀 로케이터 완성

            profile_title_text = mypage.get_attribute(PROFILE_PAGE_TITLE, "content-desc")

            # Expected Result
            assert profile_title_text == f"{nickname} 님의 프로필"
            mypage.logger.info("✅ 마이페이지에서 프로필 페이지 정상 진입 확인")

        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise

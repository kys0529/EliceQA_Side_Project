import pytest
import time
import os
from appium.webdriver.webdriver import WebDriver
from src.pages.MyPage import MyPage
from src.utils.locators import MyPageLocator

"""
class TestMP00:
    def test_mp_00_00(self, login_driver: WebDriver, request): # 기능/의도 설명
        try:
            # Precondition
            mypage = MyPage(login_driver) # 클래스에 대한 객체의 변수명은 첫 문자를 소문자로!
            
            # Steps

            # Expected Result
        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise
"""


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
            """assert 추가 필요"""
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
            """assert 추가 필요"""
            mypage.logger.info("✅ 앱 테마 - 라이트 모드로 변경 확인")

        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise


@pytest.mark.usefixtures("login_driver")
class TestMP03:
    @pytest.mark.done
    def test_mp_03_01(self, login_driver: WebDriver, request):  # 마이페이지 > 프로필 페이지 진입 여부 확인
        try:
            # Precondition
            mypage = MyPage(login_driver)
            mypage.into_mypage()
            nickname = mypage.get_nickname()  # 현재 로그인 한 유저의 닉네임 받아오기
            mypage.logger.info(f"✅ 현재 로그인 한 유저 닉네임 : {nickname}")

            # Steps
            mypage.into_profile_page()

            PROFILE_PAGE_TITLE = MyPageLocator.MypageProfile.get_profile_title_locator(
                nickname
            )  # 프로필 페이지 타이틀 로케이터 완성

            profile_title_text = mypage.get_attribute(
                PROFILE_PAGE_TITLE, "content-desc"
            )

            # Expected Result
            assert profile_title_text == f"{nickname} 님의 프로필"
            mypage.logger.info("✅ 마이페이지에서 프로필 페이지 정상 진입 확인")

        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise

@pytest.mark.skip("스크린샷으로 비교 필요로, 검증 과정 추후 개발 예정")
class TestMP04:
    @pytest.mark.wip
    def test_mp_04_01(self, login_driver: WebDriver, request): # 프로필 이미지 영역 > 등록 이미지 없을 시 기본 프로필 이미지 제공하는지 확인
        try:
            # Precondition
            mypage = MyPage(login_driver)
            mypage.into_mypage()
            mypage.into_profile_page()

            # Steps
            ''' 프로필 사진 영역 로케이터 검색 불가 > 검증 방법 고민 필요 '''
            # Expected Result

        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise
    @pytest.mark.wip
    def test_mp_04_02(self, login_driver: WebDriver, request): # 프로필 이미지 영역 > 등록 이미지 있을 시 회원 정보에 등록된 프로필 이미지 제공하는지 확인
        try:
            # Precondition
            mypage = MyPage(login_driver)
            mypage.into_mypage()
            mypage.into_profile_page()
            
            # Steps
            ''' 프로필 사진 영역 로케이터 검색 불가 > 검증 방법 고민 필요 '''
            # Expected Result

        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise

class TestMP05:
    @pytest.mark.done
    def test_mp_05_01(self, login_driver: WebDriver, request): # 닉네임 표시 영역 선택 시 이메일로 표시 내용 변경 확인
        try:
            # Precondition
            mypage = MyPage(login_driver)
            nickname = mypage.get_nickname()
            mypage.into_mypage()
            mypage.into_profile_page()
            profile_nickname = mypage.get_attribute(MyPageLocator.MypageProfile.get_profile_nickname(nickname),'content-desc')
            
            # Steps
            mypage.click_element(MyPageLocator.MypageProfile.get_profile_nickname(nickname))

            # Expected Result
            current_user_email = os.getenv("LOGIN_ID")
            PROFILE_EMAIL = MyPageLocator.MypageProfile.get_profile_email(current_user_email)   # 프로필 페이지 내 이메일 요소 로케이터 완성
            mypage.find_element(PROFILE_EMAIL)  # 현재 로그인 된 이메일로 로케이터가 정해져서, 먼저 요소가 있는지 찾기
            current_profile_email = mypage.get_attribute(PROFILE_EMAIL, 'content-desc')
            mypage.logger.info(f"✅ 현재 로그인 유저 이메일 : {current_user_email}")
            assert profile_nickname != current_profile_email    # 이메일 정보로 보여지는 정보가 변경되었는지 확인
            mypage.logger.info(f"✅ 프로필 닉네임 정보가 이메일 정보로 변경되었습니다. : {current_profile_email}")
            assert current_user_email == current_profile_email
            mypage.logger.info(f"✅ 프로필 닉네임 정보가 현재 로그인 한 유저 이메일 정보와 동일합니다.")

        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise

    @pytest.mark.done
    def test_mp_05_02(self, login_driver: WebDriver, request): # 이메일 표시 영역 선택 시 닉네임으로 표시 내용 변경 확인
        try:
            # Precondition
            mypage = MyPage(login_driver)
            current_user_email = os.getenv("LOGIN_ID")
            nickname = mypage.get_nickname()
            mypage.into_mypage()
            mypage.into_profile_page()
            
            # Steps
            mypage.click_element(MyPageLocator.MypageProfile.get_profile_nickname(nickname))
            profile_email = mypage.get_attribute(MyPageLocator.MypageProfile.get_profile_email(current_user_email),'content-desc')
            mypage.click_element(MyPageLocator.MypageProfile.get_profile_email(current_user_email))

            # Expected Result
            after_click_nickname = mypage.get_attribute(MyPageLocator.MypageProfile.get_profile_nickname(nickname),'content-desc')
            assert profile_email != after_click_nickname
            mypage.logger.info(f"✅ 프로필 이메일 정보가 닉네임 정보로 변경되었습니다. : {after_click_nickname}")
            assert nickname == after_click_nickname
            mypage.logger.info(f"✅ 프로필 닉네임 정보가 현재 로그인 한 유저 닉네임 정보와 동일합니다.")
            
        except Exception as e:
            mypage.logger.info(f"❌ 테스트 실패: {e}")
            mypage.save_screenshot(request.node.name)
            raise

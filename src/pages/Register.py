from src.pages.BasePage import BasePage
from src.utils.locators import RegisterLocator
from src.resources.testdata.test_data import not_registered_id, registered_id
import imaplib
import email
import datetime
from email.header import decode_header
import time
from email.utils import parsedate_to_datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from src.utils.helpers import login
from src.utils.locators import MyPageLocator
from appium.webdriver.webdriver import WebDriver as AppiumWebDriver

class Register(BasePage):
    def __init__(self, driver, page_name="Register"):
        super().__init__(driver, page_name)

    def navigate_to_register(self, driver):
        try:
            register = Register(driver)
            register.click_element(RegisterLocator.REGISTER_BTN)
        except Exception as e:
            register.logger.error(f"테스트 실패 - navigate_to_register")
            register.save_screenshot("failed_navigate_to_register")
            raise
    
    def input_register_data(self, driver, id_info):
        try:
            if id_info == "registered_id":
                nickname = registered_id["nickname"]
                email_id = registered_id["email_id"]
                email_domain = registered_id["email_domain"]
                password = registered_id["password"]
            elif id_info == "not_registered_id":
                nickname = not_registered_id["nickname"]
                email_id = not_registered_id["email_id"]
                email_domain = not_registered_id["email_domain"]
                password = not_registered_id["password"]
            register = Register(driver)
            nickname_input = register.find_by_hint(RegisterLocator.TEXT_INPUT, "닉네임")
            register.send_keys(nickname_input, nickname)
            email_id_input = register.find_by_hint(RegisterLocator.TEXT_INPUT, "이메일 아이디")
            register.send_keys(email_id_input, email_id)
            email_dropdown = register.find_element(RegisterLocator.EMAIL_DROPDOWN_BTN)
            register.click_element(email_dropdown)
            if email_domain == "naver":
                register.click_element(RegisterLocator.NAVER_BTN)
            elif email_domain == "gmail":
                register.click_element(RegisterLocator.GMAIL_BTN)
            elif email_domain == "daum":
                register.click_element(RegisterLocator.DAUM_BTN)
            else:
                register.click_element(RegisterLocator.ENTER_MANUALLY_BTN)
            password_input = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호")
            register.send_keys(password_input, password)
            password_confirm_input = register.find_by_hint(RegisterLocator.TEXT_INPUT, "비밀번호 확인")
            register.send_keys(password_confirm_input, password)
            self.hide_keyboard()
            register.click_element(RegisterLocator.REGISTER_BTN)
        except Exception as e:
            register.logger.error(f"테스트 실패 - input_register_data")
            register.save_screenshot("failed_input_register_data")
            

    def find_by_hint(self, locator, hint):
        try:
            for element in self.driver.find_elements(*locator): # *locator = 언패킹을 해야한다
                if element.get_attribute("hint") == hint:
                    self.logger.info(f"{hint} 힌트 확인")
                    return element
        except Exception as e:
            self.logger.error(f"테스트 실패 - find_by_hint")
            self.save_screenshot("failed_to_navigate_to_register")            

    def handle_exception(self, request, e):
        self.logger.error(f"테스트 실패")
        self.save_screenshot(request.node.name)
        assert False, "테스트 실패"

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
            self.logger.info("키보드 숨김")
        except Exception as e:
            self.logger.error(f"키보드 숨기기 실패: {e}")
            self.save_screenshot("hide_keyboard_fail")
    
    def check_email_auth(self, id_info):
        # 1) 로그인 정보 선택
        try:
            if id_info == "registered_id":
                email_id = registered_id["email_id"]
                password = registered_id["app_key"]
            elif id_info == "not_registered_id":
                email_id = not_registered_id["email_id"]
                password = not_registered_id["app_key"]
            else:
                raise ValueError(f"알 수 없는 id_info: {id_info}")
        except Exception as e:
            self.logger.error(f"이메일 정보 불러오기 실패")
            self.save_screenshot("failed_check_email_auth")
            raise

        # 2) IMAP 로그인
        try:
            M = imaplib.IMAP4_SSL('imap.gmail.com', 993)
            M.login(f"{email_id}@gmail.com", password)
            M.select('INBOX')
        except Exception as e:
            self.logger.error(f"IMAP 로그인 실패")
            self.save_screenshot("failed_check_email_auth")
            raise

        # 3) 최대 4회 폴링
        try:
            for attempt in range(1, 5):
                # 3-1) 최신 메일 UID 조회
                result, data = M.uid('search', None, "ALL")
                if result != 'OK' or not data or not data[0]:
                    raise Exception("메일이 없거나 조회 중 오류 발생")
                latest_uid = data[0].split()[-1]

                # 3-2) 메일 원본 가져오기
                result, msg_data = M.uid('fetch', latest_uid, '(RFC822)')
                if result != 'OK':
                    raise Exception("메일 원본을 불러오는 중 오류 발생")
                raw_email = msg_data[0][1]
                msg = email.message_from_bytes(raw_email)

                # 3-3) 제목 디코딩
                subject, encoding = decode_header(msg.get("Subject"))[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding or "utf-8", errors="ignore")

                # 3-4) 수신 시간 파싱 및 delta 계산
                date_str = msg.get("Date")
                email_dt = parsedate_to_datetime(date_str)
                now_utc = datetime.datetime.now(datetime.timezone.utc)
                delta = (now_utc - email_dt).total_seconds()

                # 3-5) 본문(content) 추출
                content = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        ctype = part.get_content_type()
                        disp = str(part.get("Content-Disposition"))
                        if ctype == "text/plain" and "attachment" not in disp:
                            charset = part.get_content_charset() or "utf-8"
                            content = part.get_payload(decode=True).decode(charset, errors="ignore")
                            break
                else:
                    charset = msg.get_content_charset() or "utf-8"
                    content = msg.get_payload(decode=True).decode(charset, errors="ignore")

                # 3-6) 검사 조건
                if "이메일 인증" in subject and delta <= 10:
                    M.logout()
                    return {"subject": subject, "content": content, "delta": delta}

                # 3-7) 아직 아니면 1초 대기 후 재시도
                time.sleep(1)
        except Exception as e:
            self.logger.error(f"메일 인증 확인 중 오류 발생: {e}")
            self.save_screenshot("failed_check_email_auth")
            raise

        # 4) 네 번 모두 실패하면
        M.logout()
        assert False, (
            f"❌ 인증 실패: 제목에 '이메일 인증' 포함={ '이메일 인증' in subject }, "
            f"수신까지 {delta:.1f}초 경과"
        )

    
    def execute_email_verification(self, email_content):
        try:
            chrome_options = Options()
            chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
            driver = webdriver.Chrome(service=Service(), options=chrome_options)
            match = re.search(r'https?://[^\s]+', email_content)
            if not match:
                raise ValueError("❌ 인증 링크를 찾을 수 없습니다.")
            match = match.group(0)
            url = match
            driver.get(url)
            time.sleep(2)
            driver.quit()
        except Exception as e:
            self.logger.error(f"테스트 실패 - execute_email_verification")
            self.save_screenshot("failed_execute_email_verification")
            raise

    def delete_ID(self, driver :AppiumWebDriver, id_info):
        try:
            if id_info == "registered_id":
                id = registered_id["nickname"]
                email_id = registered_id["email_id"]
                password = registered_id["password"]
            elif id_info == "not_registered_id":
                id = not_registered_id["nickname"]
                email_id = not_registered_id["email_id"]
                password = not_registered_id["password"]
            else:
                raise ValueError(f"알 수 없는 id_info: {id_info}")
        except Exception as e:
            self.logger.error(f"이메일 정보 불러오기 실패")
            self.save_screenshot("failed_check_email_auth")
            raise
        try:
            register = Register(driver)
            mypage_tab = MyPageLocator.MypageMain.MYPAGE_TAB
            register.click_element(mypage_tab)
            user_profile = MyPageLocator.MypageMain.get_user_profile_locator(id, f"{email_id}@gmail.com")
            register.click_element(user_profile)
            password_input = register.find_by_hint(RegisterLocator.TEXT_INPUT,"비밀번호를 입력하세요\n비밀번호")
            password_input.send_keys(password)
            confirm_btn = MyPageLocator.MypageMain.POPUP_COMFIRM
            register.click_element(confirm_btn)
            delete_btn = MyPageLocator.MypageModifyPage.MODI_WITHDRAW
            register.click_element(delete_btn)
            password_input_again = register.find_by_hint(RegisterLocator.TEXT_INPUT,"비밀번호를 입력해주세요...")
            register.send_keys(password_input_again, password)
            withdraw_btn = RegisterLocator.WITHDRAW_BTN
            register.click_element(withdraw_btn)
            register.find_element(RegisterLocator.COMPLETE_POPUP)
        except Exception as e:
            self.logger.error(f"테스트 실패 - delete_ID")
            self.save_screenshot("failed_delete_ID")
            raise
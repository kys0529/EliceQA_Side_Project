import re
import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="src/config/.env")

class TestItem:
    @staticmethod
    def get_star_count_from_api(image_path):
        # 이미지 base64로 인코딩
        with open(image_path, "rb") as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

        # 요청 헤더
        headers = {"Content-Type": "application/json"}

        # 요청 URL
        API_KEY = os.getenv("API_KEY")
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

        # 요청 본문
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "inline_data": {
                                "mime_type": "image/png",
                                "data": encoded_image
                            }
                        },
                        {
                            "text": "이 이미지에 완전히 노란색으로 칠해진 별은 몇 개인가요? 반쯤 칠해진 별은 포함하지 마세요. \
                                완전 칠해진 별은 ★ 이런 형식입니다. 숫자만 대답하세요. 예: 5"
                        }
                    ]
                }
            ]
        }

        # 요청 전송
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        # 응답 원문 전체 보기
        result_text = response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
        print("💬 AI 응답 원문:", result_text)

        # 숫자 추출
        match = re.search(r"\d+", result_text)
        return int(match.group()) if match else 0

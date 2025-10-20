from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import pyautogui
import pyperclip

input_id = ""
input_pw = ""

user_home = os.path.expanduser("~")
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chromedriver_path = os.path.join(user_home, "Documents", "chromedriver-win64", "chromedriver.exe")
service = Service(chromedriver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
# 사람이 작업하지 않은 것으로 인식함.
pyperclip.copy(input_id)
pyautogui.hotkey("ctrl", "v")
# id.send_keys(input_id)
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
# pw.send_keys(input_pw)
pyperclip.copy(input_pw)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 로그인 버튼
driver.find_element(By.CSS_SELECTOR, "#log\.login").click()


input("아무 키나 눌러서 종료하세요")
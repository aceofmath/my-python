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

# 메일함 이동
driver.get("https://mail.naver.com/v2/folders/0/all")

# 메일 쓰기 버튼 클릭
driver.find_element(By.CSS_SELECTOR, "#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write").click()
time.sleep(2)

# 받는 사람
driver.find_element(By.CSS_SELECTOR, "#recipient_input_element").send_keys("aceofmath@naver.com")
time.sleep(2)

# 제목
driver.find_element(By.CSS_SELECTOR, "#subject_title").send_keys("자동화 메일 제목입니다")
time.sleep(2)

# 본문
iframe = driver.find_element(By.CSS_SELECTOR, "#content > div.contents_area > div > div.editor_area > div > div.editor_body > iframe") #iframe 안으로 들어가기
driver.switch_to.frame(iframe)
driver.find_element(By.CSS_SELECTOR, "body > div > div.workseditor-body > div.workseditor-content").send_keys("자동화 메일 본문입니다.")
driver.switch_to.default_content() # iframe 밖으로 나오기
time.sleep(2)

# 보내기 버튼
driver.find_element(By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div:nth-child(1) > button").click()
time.sleep(2)

input("아무 키나 눌러서 종료하세요")
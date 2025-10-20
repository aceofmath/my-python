import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ✅ 현재 사용자 홈 디렉토리 가져오기
user_home = os.path.expanduser("~")
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chromedriver_path = os.path.join(user_home, "Documents", "chromedriver-win64", "chromedriver.exe")
service = Service(chromedriver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.naver.com")
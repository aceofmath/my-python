from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time

# 크롬 설정
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service(r"C:\Users\PMG036\Documents\chromedriver-win64\chromedriver.exe")  # 크롬드라이버 경로 수정

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://search-etf.com/month_dividend.php")
time.sleep(2)

while True:
    try:
        # div#load-more-desktop 하위의 버튼
        more_button = driver.find_element(
            By.CSS_SELECTOR,
            "div#load-more-desktop button.btn.btn-primary.load-more-btn"
        )

        # 버튼이 실제로 보이는지 확인
        if not more_button.is_displayed():
            print("더보기 버튼이 더 이상 보이지 않음 → 종료")
            break

        # 스크롤 후 강제 클릭
        driver.execute_script("arguments[0].scrollIntoView(true);", more_button)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", more_button)
        print("✅ 더보기 버튼 클릭!")
        time.sleep(1.5)  # 데이터 로딩 대기

    except NoSuchElementException:
        print("더보기 버튼을 찾을 수 없음 → 종료")
        break

# 테이블 추출
html = driver.page_source
soup = BeautifulSoup(html, "lxml")
table = soup.select_one("div#desktop-table table")

if table:
    df = pd.read_html(str(table))[0]
    df.to_excel("월배당ETF_목록.xlsx", index=False)
    print("💾 엑셀 저장 완료: 월배당ETF_목록.xlsx")
else:
    print("❌ 테이블을 찾지 못했습니다.")

driver.quit()

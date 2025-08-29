# 📁 main_program.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time
import datetime
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials


def connect_to_google_sheet(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("your-credentials.json", scope)
    client = gspread.authorize(creds)
    try:
        sheet = client.open(sheet_name)
    except gspread.SpreadsheetNotFound:
        sheet = client.create(sheet_name)
    return sheet


def crawl_etf_data():
    # ✅ 현재 사용자 홈 디렉토리 가져오기
    user_home = os.path.expanduser("~")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    #service = Service(r"C:\Users\aceof\Documents\chromedriver-win64\chromedriver.exe")  # 수정 필요
    chromedriver_path = os.path.join(user_home, "Documents", "chromedriver-win64", "chromedriver.exe")
    service = Service(chromedriver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://search-etf.com/month_dividend.php")
    time.sleep(2)

    while True:
        try:
            more_button = driver.find_element(
                By.CSS_SELECTOR,
                "div#load-more-desktop button.btn.btn-primary.load-more-btn"
            )
            if not more_button.is_displayed():
                break
            driver.execute_script("arguments[0].scrollIntoView(true);", more_button)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", more_button)
            print("✅ '더보기' 클릭")
            time.sleep(1.5)
        except NoSuchElementException:
            print("⛔ 더보기 버튼 없음 → 종료")
            break

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    table = soup.select_one("div#desktop-table table")

    df = None
    if table:
        df = pd.read_html(str(table))[0]

        for col_index in [3, 5]:
            df.iloc[:, col_index] = (
                df.iloc[:, col_index].astype(str)
                .str.replace("원", "", regex=False)
                .str.replace(",", "", regex=False)
                .str.strip()
            )
            df.iloc[:, col_index] = pd.to_numeric(df.iloc[:, col_index], errors='coerce')

        df.iloc[:, 6] = (
            df.iloc[:, 6].astype(str)
            .str.replace("%", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.strip()
        )
        df.iloc[:, 6] = pd.to_numeric(df.iloc[:, 6], errors='coerce')

        df = df.sort_values(by=df.columns[6], ascending=False).reset_index(drop=True)
        rank_col_name = df.columns[7] if len(df.columns) > 7 else "순위"
        df.insert(7, rank_col_name, df.index + 1)
    else:
        print("❌ 테이블을 찾지 못했습니다.")

    driver.quit()
    return df


def upload_to_google_sheets(df, sheet_name="월배당ETF_목록"):
    if df is None or df.empty:
        print("⚠️ 저장할 데이터프레임이 비어 있습니다.")
        return

    df = df.fillna("").astype(str)
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    sheet = connect_to_google_sheet(sheet_name)

    try:
        worksheet = sheet.worksheet(today)
        sheet.del_worksheet(worksheet)
    except gspread.exceptions.WorksheetNotFound:
        pass

    worksheet = sheet.add_worksheet(title=today, rows=str(len(df) + 10), cols=str(len(df.columns) + 5))

    try:
        data = [df.columns.values.tolist()] + df.values.tolist()
        worksheet.update(data)
        print(f"✅ Google Sheets 저장 완료: [{sheet_name}] → 시트 '{today}'")
    except Exception as e:
        print(f"❌ Google Sheets 업데이트 실패: {e}")


def main():
    df = crawl_etf_data()
    upload_to_google_sheets(df)


if __name__ == "__main__":
    main()

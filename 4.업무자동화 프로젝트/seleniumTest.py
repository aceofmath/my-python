from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
import glob
import shutil
from datetime import datetime

# ===== 설정 =====
download_dir = r"C:\dev\workspace\py_test\result"  # 다운로드 폴더
os.makedirs(download_dir, exist_ok=True)

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

service = Service(r"C:\Users\PMG036\Documents\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 30)

driver.get("https://www.k-etf.com/calendar/dividend")
def short_wait(sec=0.5):
    time.sleep(sec)

# ===== 1) 다음 달 버튼 클릭 =====
try:
    next_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[span[normalize-space()='다음 달']]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
    short_wait()
    driver.execute_script("arguments[0].click();", next_btn)
    print("✅ 다음 달 버튼 클릭 완료")
except Exception as e:
    print("❌ 다음 달 버튼 클릭 실패:", e)

# ===== 2) CSV 버튼 클릭 =====
try:
    short_wait(2)
    csv_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[span[normalize-space()='CSV']]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", csv_btn)
    short_wait()
    driver.execute_script("arguments[0].click();", csv_btn)
    print("✅ CSV 버튼 클릭 완료")
    time.sleep(5)  # 다운로드 대기
except Exception as e:
    print("❌ CSV 버튼 클릭 실패:", e)

# ===== 3) 최신 CSV 파일 이름 변경 =====
try:
    list_of_files = glob.glob(os.path.join(download_dir, "*.csv"))
    if not list_of_files:
        raise FileNotFoundError("다운로드된 CSV 파일이 없습니다.")
    
    latest_file = max(list_of_files, key=os.path.getctime)
    today = datetime.now().strftime("%Y%m%d")
    new_file_path = os.path.join(download_dir, f"배당일정_{today}.csv")
    
    if os.path.exists(new_file_path):
        os.remove(new_file_path)
    
    shutil.move(latest_file, new_file_path)
    print(f"💾 CSV 파일 이름 변경 완료: {new_file_path}")

except Exception as e:
    print("❌ CSV 파일 이름 변경 실패:", e)

driver.quit()
print("✅ 스크립트 실행 완료")

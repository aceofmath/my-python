import requests
from bs4 import BeautifulSoup
import csv

url_base = "https://finance.naver.com/sise/sise_market_sum.naver?&page="

with open("market_summary.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    # 제목 추출
    res = requests.get(url_base + "1")
    soup = BeautifulSoup(res.text, "html.parser")
    titles = [th.get_text().strip() for th in soup.find("table", attrs={"class":"type_2"}).find("thead").find_all("th")]
    writer.writerow(titles)

    # 여러 페이지 순회
    for page in range(1, 46):  # 필요에 따라 페이지 수 조정
        res = requests.get(url_base + str(page))
        soup = BeautifulSoup(res.text, "html.parser")
        rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
        for row in rows:
            cols = [td.get_text().strip() for td in row.find_all("td")]
            if len(cols) <= 1:
                continue
            writer.writerow(cols)

import os
import xml.etree.ElementTree as ET
from openpyxl import Workbook

def extract_books_from_xml(file_path):
    """XML 파일에서 <book> 정보를 추출"""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except Exception as e:
        print(f"[ERROR] XML 파싱 실패: {file_path}, {e}")
        return []

    results = []
    for book in root.findall(".//book"):
        book_id = book.attrib.get("id", "")
        author = book.findtext("author", "")
        title = book.findtext("title", "")
        genre = book.findtext("genre", "")

        # prices 하위 노드들을 하나의 문자열로 합치기 (쉼표 구분)
        prices_node = book.find("prices")
        price_value = ""
        if prices_node is not None:
            values = [p.text for p in prices_node if p.text]
            price_value = ", ".join(values)

        publish_date = book.findtext("publish_date", "")
        description = book.findtext("description", "").strip()

        results.append({
            "file": file_path,
            "id": book_id,
            "author": author,
            "title": title,
            "genre": genre,
            "price": price_value,
            "publish_date": publish_date,
            "description": description
        })
    return results


def scan_xml_files(base_dir):
    """하위 폴더까지 모든 XML 파일 검색 후 데이터 추출"""
    all_results = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".xml"):
                file_path = os.path.join(root, file)
                all_results.extend(extract_books_from_xml(file_path))
    return all_results


def save_to_excel(data, output_file="books.xlsx"):
    """추출한 결과를 엑셀(xlsx) 파일로 저장"""
    wb = Workbook()
    ws = wb.active
    ws.title = "Books"

    headers = ["file", "id", "author", "title", "genre", "price", "publish_date", "description"]
    ws.append(headers)

    for row in data:
        ws.append([
            row["file"],
            row["id"],
            row["author"],
            row["title"],
            row["genre"],
            row["price"],
            row["publish_date"],
            row["description"]
        ])

    wb.save(output_file)
    print(f"엑셀 저장 완료: {output_file}")


if __name__ == "__main__":
    base_directory = r"C:\dev\workspace\py_test\resource\xml\parseXml"  # 탐색 시작 경로 (필요에 따라 변경)
    results = scan_xml_files(base_directory)
    save_to_excel(results, "books.xlsx")

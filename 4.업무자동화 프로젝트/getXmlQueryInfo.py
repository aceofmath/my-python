import os
import re
import csv
import xml.etree.ElementTree as ET

def extract_sql_info_from_xml(file_path):
    """XML 파일에서 SQL 태그와 테이블 정보를 추출"""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except Exception as e:
        print(f"[ERROR] XML 파싱 실패: {file_path}, {e}")
        return []

    results = []

    # MyBatis mapper 안의 SQL 태그들
    for tag in ["select", "insert", "update", "delete"]:
        for elem in root.findall(tag):
            sql_text = "".join(elem.itertext()).strip()  # SQL 구문 추출
            tables = extract_tables_from_sql(sql_text)
            results.append({
                "file": file_path,
                "operation": tag,
                "id": elem.attrib.get("id", ""),  # SQL ID 속성
                "tables": ", ".join(tables),      # 여러 개면 쉼표 구분
                "sql": sql_text.replace("\n", " ").strip()
            })
    return results


def extract_tables_from_sql(sql_text):
    """SQL문에서 테이블명 추출 (간단한 정규식 기반)"""
    tables = set()

    # FROM, UPDATE, INTO, DELETE FROM 뒤의 테이블명 추출
    patterns = [
        r"from\s+([a-zA-Z0-9_]+)",
        r"update\s+([a-zA-Z0-9_]+)",
        r"into\s+([a-zA-Z0-9_]+)",
        r"delete\s+from\s+([a-zA-Z0-9_]+)"
    ]

    sql_lower = sql_text.lower()
    for pattern in patterns:
        matches = re.findall(pattern, sql_lower, re.IGNORECASE)
        for match in matches:
            tables.add(match)

    return list(tables)


def scan_xml_files(base_dir):
    """하위 폴더까지 모든 XML 파일 검색 후 정보 추출"""
    all_results = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".xml"):
                file_path = os.path.join(root, file)
                all_results.extend(extract_sql_info_from_xml(file_path))
    return all_results


def save_to_csv(data, output_file="output.csv"):
    """결과를 CSV 파일로 저장"""
    if not data:
        print("저장할 데이터가 없습니다.")
        return

    fieldnames = ["file", "operation", "id", "tables", "sql"]
    with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"CSV 저장 완료: {output_file}")


if __name__ == "__main__":
    base_directory = r"C:\XMall4\svc\workspace\gnujava\src\main\resources\egovframework\sqlmap\mysql"  # 탐색 시작 경로 (원하는 폴더로 변경)
    results = scan_xml_files(base_directory)

    # 결과 CSV로 저장
    save_to_csv(results, "output.csv")

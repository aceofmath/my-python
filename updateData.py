import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def connect_to_google_sheet(sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("your-credentials.json", scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name)


def to_float(val):
    try:
        return float(val.replace(',', '').strip())
    except:
        return 0.0


def update_possession_columns(sheet_name="월배당ETF_목록"):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    sheet = connect_to_google_sheet(sheet_name)

    try:
        main_ws = sheet.worksheet(today)
        possession_ws = sheet.worksheet("보유ETF")
    except gspread.exceptions.WorksheetNotFound as e:
        print(f"❌ 필요한 시트를 찾을 수 없습니다: {e}")
        return

    main_data = main_ws.get_all_values()
    possession_data = possession_ws.get_all_values()

    if not main_data or not possession_data:
        print("❌ 시트에 데이터가 없습니다.")
        return

    main_header = main_data[0]
    possession_header = possession_data[0]

    try:
        main_code_idx = main_header.index("종목코드")
        possession_code_idx = possession_header.index("종목코드")
    except ValueError:
        print("❌ '종목코드' 열이 존재하지 않습니다.")
        return

    # ✅ 매핑: 보유ETF 열 index → 오늘 시트 열 index
    target_mapping = {
        5: 3,  # F ← D (현재가)
        6: 4,  # G ← E (배당일)
        7: 5,  # H ← F (분배금)
        8: 6,  # I ← G (분배율)
        9: 7   # J ← H (순위)
    }

    code_to_values = {}
    for row in main_data[1:]:
        if len(row) > main_code_idx:
            code = row[main_code_idx]
            values = [row[target_mapping[i]] if target_mapping[i] < len(row) else "" for i in target_mapping]
            code_to_values[code] = values

    # ✅ 헤더 업데이트
    new_header = possession_data[0]
    if len(new_header) < 12:
        new_header += ["구매합계", "분배금합계"]
    updated_rows = [new_header]

    total_purchase = 0
    total_dividend = 0

    for row in possession_data[1:]:
        if len(row) < possession_code_idx + 1:
            continue  # Skip malformed rows

        code = row[possession_code_idx]
        new_values = code_to_values.get(code, [""] * len(target_mapping))

        # 보유ETF 시트의 열 수가 부족할 경우 확장
        while len(row) < 12:
            row.append("")

        for i, val in zip(target_mapping.keys(), new_values):
            row[i] = val

        qty = sum([to_float(row[i]) for i in [2, 3, 4]])  # C, D, E
        current_price = to_float(row[5])  # F
        dividend = to_float(row[7])       # H

        purchase_total = int(qty * current_price)
        dividend_total = int(qty * dividend)

        total_purchase += purchase_total
        total_dividend += dividend_total

        row[10] = purchase_total
        row[11] = dividend_total

        # 합계 행 제거 (혹시 기존에 있던 경우)
        if row[0].strip() != "합계":
            updated_rows.append(row)

    # ✅ 마지막에 합계 행 1개 추가
    total_row = [""] * 12
    total_row[0] = "합계"
    total_row[10] = total_purchase
    total_row[11] = total_dividend
    updated_rows.append(total_row)

    # ✅ 시트 업데이트
    possession_ws.update(updated_rows)
    print("✅ '보유ETF' 시트 데이터 업데이트 완료 (합계 정리 포함)")

    # ✅ 숫자 서식 적용: C, D, E, F, H, K, L → 3,4,5,6,8,11,12 (1-indexed)
    format_columns_as_number(possession_ws, col_indices=[3, 4, 5, 6, 8, 11, 12], row_count=len(updated_rows))


def format_columns_as_number(ws, col_indices, row_count):
    """특정 열에 금액 숫자 포맷 적용: 쉼표 포함, 소수점 없음"""
    sheet_id = ws._properties['sheetId']
    requests = []

    for col in col_indices:
        requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 1,  # 데이터 행부터
                    "endRowIndex": row_count,
                    "startColumnIndex": col - 1,
                    "endColumnIndex": col
                },
                "cell": {
                    "userEnteredFormat": {
                        "numberFormat": {
                            "type": "NUMBER",
                            "pattern": "#,##0"  # 쉼표 포함, 소수점 없음
                        }
                    }
                },
                "fields": "userEnteredFormat.numberFormat"
            }
        })

    ws.spreadsheet.batch_update({"requests": requests})
    print("✅ 숫자 포맷 적용 완료: 쉼표 포함, 소수점 없음")


if __name__ == "__main__":
    update_possession_columns()

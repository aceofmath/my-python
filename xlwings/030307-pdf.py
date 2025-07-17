import win32com.client as win32
import os

# 루트 폴더 지정
root_folder = r"C:\Users\PMG036\Documents\test"  # 원하는 경로로 변경

# Excel 실행 (백그라운드)
excel = win32.Dispatch('Excel.Application')
excel.Visible = False
excel.DisplayAlerts = False

# os.walk로 하위 폴더까지 순회
for current_path, subdirs, files in os.walk(root_folder):
    for filename in files:
        if filename.lower().endswith(('.xlsx', '.xlsm', '.xls')):
            fullpath = os.path.join(current_path, filename)

            # PDF는 root_folder에 저장 (파일명만 사용)
            pdf_name = os.path.splitext(filename)[0] + ".pdf"
            pdf_path = os.path.join(root_folder, pdf_name)

            print(f"[처리중] {fullpath} → {pdf_path}")

            try:
                wb = excel.Workbooks.Open(fullpath)

                wb.ExportAsFixedFormat(
                    Type=0,                   # PDF
                    Filename=pdf_path,
                    Quality=0,                # 표준
                    IncludeDocProperties=True,
                    IgnorePrintAreas=False,
                    OpenAfterPublish=False
                )

                wb.Close(SaveChanges=False)
            except Exception as e:
                print(f"[에러] {fullpath}: {e}")

# Excel 종료
excel.Quit()

print("✅ 모든 Excel을 PDF로 변환하여 root_folder에 저장 완료!")

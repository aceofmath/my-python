import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.load_workbook(r"C:\dev\workspace\py_test\openpyxl_test.xlsx")
ws = wb["Sheet4"]  #활성화 되어있는 시트 설정(시트명 : "업")

for r in ws.rows:
    print("")
    for c in r:
        print(c.value, end=" ")
import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.load_workbook(r"C:\dev\workspace\py_test\openpyxl_test.xlsx")
ws = wb["Sheet1"]  #활성화 되어있는 시트 설정(시트명 : "업")

#1행부터 2개행까지 행을 삭제한다.
ws.delete_rows(1,2)

ws.delete_cols(3,4)

wb.save("openpyxl_test.xlsx")
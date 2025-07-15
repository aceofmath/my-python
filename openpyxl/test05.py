import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.load_workbook(r"C:\dev\workspace\py_test\openpyxl_test.xlsx")
ws = wb["test"]  #활성화 되어있는 시트 설정(시트명 : "업")

#test 시트 삭제
wb.remove(ws)
#test 시트 재생성
wb.create_sheet('test')

wb.save("openpyxl_test.xlsx")
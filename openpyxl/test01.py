import  openpyxl  as  op  #openpyxl 모듈 import
wb = op.load_workbook(r"C:\dev\workspace\py_test\openpyxl_test.xlsx")
ws_list = wb.sheetnames  #해당 Workbook의 시트 목록을 리스트로 저장

for  sht  in  ws_list:
    ws = wb[sht] #Sheet 객체 생성
    print(ws) #객체 출력

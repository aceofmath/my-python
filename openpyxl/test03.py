import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.load_workbook(r"C:\dev\workspace\py_test\openpyxl_test.xlsx")
ws = wb["Sheet3"]  #활성화 되어있는 시트 설정(시트명 : "업")

#"B1" Cell에 입력하기
ws.cell(1, 2).value = "입력테스트2"

#"C1" Cell에 입력하기
ws["C1"].value = "입력테스트2"


ws2 = wb["Sheet2"]
datalist = [2,4,8,16,32,64,128,256] #임의의 숫자 리스트 정의

i=1  # 행값을 바꾸기 위한 인덱스 정의

for  data  in  datalist:
    ws2.cell(row = i, column=1).value = data  #A열(Column=1)에 행을 바꾸면서 입력
    i=i+1  #행값 증가

# wb.save("result.xlsx") #엑셀 파일 저장(파일명 : result.xlsx)
wb.save("openpyxl_test.xlsx")
import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.load_workbook(r"C:\dev\workspace\py_test\resource\xlsx\0301_test.xlsx")
ws = wb["Sheet5"]

ws['M1'].value = "합계"
ws['N1'].value = "=sum(D:D)"

row_max = ws.max_row  #최대 행값 저장

#for문 통해 2행~최대행까지 반복문
#range(a,b+1) : a부터 b까지 반복하는 range 구문
for  row  in  range(2, row_max+1):
    #함수 자동 작성
    ws["F"+str(row)].value = "=D"+str(row)+"*"+"E"+str(row)


wb.save("openpyxl_test.xlsx")
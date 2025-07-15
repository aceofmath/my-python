import  openpyxl  as  op  #openpyxl 모듈 import
import  win32com.client

def  writeFunc():
    wb = op.load_workbook(r"C:\dev\workspace\py_test\openpyxl_test.xlsx") #Workbook 객체 생성
    ws = wb["Sheet5"]

    row_max = ws.max_row  #최대 행값 저장

    #for문 통해 2행~최대행까지 반복문
    #range(a,b+1) : a부터 b까지 반복하는 range 구문
    for  row  in  range(2, row_max+1):
    #함수 자동 작성
        ws["F"+str(row)].value = "=D"+str(row)+"*"+"E"+str(row)

    wb.save(r"openpyxl_test.xlsx") #결과 엑셀파일 저장

def  loadData():
    #엑셀 직접 실행시키고 저장 및 종료
    excel = win32com.client.Dispatch("Excel.Application")
    temp_wb = excel.Workbooks.Open(r"C:\dev\workspace\py_test\openpyxl_test.xlsx")
    temp_wb.Save()
    excel.quit()

    #openpyxl 통해 Workbook 객체 및 WorkSheet 객체 생성
    wb = op.load_workbook(r"openpyxl_test.xlsx", data_only=True)
    ws = wb["Sheet5"]

    #빈 리스트 생성
    data = []

    #ws.rows 속성 활용하여 for문 진행
    for  row  in  ws.rows:
        data.append(row[5].value) #E열 데이터를 리스트에 추가

    print(data) #최종 리스트 출력

if  __name__ == "__main__":
    writeFunc() #writeFunc 실행
    loadData() #loadData 실행
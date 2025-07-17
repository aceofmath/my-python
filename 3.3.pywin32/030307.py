import win32com.client

#excel App 열기(객체 생성)
excel = win32com.client.Dispatch("Excel.Application")

#엑셀 실행과정이 보이게
excel.Visible = True

#Workbook 객체 생성(새로 추가)
wb = excel.Workbooks.Add()

#활성화되어잇는 시트를 객체로 생성
ws = wb.Worksheets("Sheet1") #Worksheet 설정

# 1행 1열에 텍스트 입력
ws.Cells(1,1).Value = "사장님 몰래 하는 파이썬 업무자동화"


# ======================================================
# 1. Save( )
# ======================================================

#Workbook(통합문서) 저장
# wb.Save() 

# ======================================================
# 2. SaveAs( )
# ======================================================

# #path 지정
# path = r"C:\dev\workspace\py_test\3.3.pywin32"

# #저장
# wb.SaveAs(path+"/test1.xlsx")

# ======================================================
# 3. ExportAsFixedFormat( )
# ======================================================

#path 지정
path = r"C:\dev\workspace\py_test\3.3.pywin32"

#저장
wb.ExportAsFixedFormat(Type=0, Filename=path+"/test1.xlsx", From=1, To=1)
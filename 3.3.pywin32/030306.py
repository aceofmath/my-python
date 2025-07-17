import win32com.client

excel = win32com.client.Dispatch("Excel.Application") #엑셀 프로그램을 객체로 생성
excel.Visible = True #실행과정 보이게

#기존 존재하는 data파일을 Workbook 객체로 생성
wb = excel.Workbooks.Open(r"C:\dev\workspace\py_test\3.3.pywin32\030306.xlsx")

#활성화되어잇는 시트를 객체로 생성
ws = wb.Worksheets("Sheet1") #Worksheet 설정

#차트를 새로 추가하고 선택하기
# ws.Shapes.AddChart().Select() 


# 선택 된 차트의 데이터영역을 설정하기
# excel.ActiveChart.SetSourceData(Source=ws.Range("A1:B9"))
chart = ws.Shapes.AddChart(51,300,20,500,400).Select() #막대 차트 200*200 크기 생성
excel.ActiveChart.SetSourceData(Source=ws.Range("A1:B9")) #데이터 범위 설정

#차트 제목 나오게(False면 안보임)
excel.ActiveChart.HasTitle = True

#차트 제목 설정
excel.ActiveChart.ChartTitle.Text = "국어 과목"

#차트 제목 글씨 크기
excel.ActiveChart.ChartTitle.Characters.Font.Size=14

#차트 제목 색상(파란색)
excel.ActiveChart.ChartTitle.Characters.Font.ColorIndex = 5

#제목 굵게 
excel.ActiveChart.ChartTitle.Characters.Font.Bold=True 


#차트 범례 보이게(Fasle면 안보임)
excel.ActiveChart.HasLegend = True

#차트 범례 글씨 크기
excel.ActiveChart.Legend.Font.Size = 15

#차트 범례 굵게
excel.ActiveChart.Legend.Font.Bold = True

#차트 범례색상 설정(파란색)
excel.ActiveChart.Legend.Font.ColorIndex = 5

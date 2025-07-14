import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.load_workbook(r"C:\dev\workspace\py_test\openpyxl_test.xlsx")
ws = wb["Sheet4"]  #활성화 되어있는 시트 설정(시트명 : "업")

#방법 1 : Sheet의 Cell 속성 사용하기
data1 = ws.cell(row=1, column=2).value

#방법 2 : 엑셀 인덱스(Range) 사용하기
data2 = ws["B1"].value

rng = ws["A1:C3"]

#위 결과 출력해보기
print("cell(1,2) : ", data1)
print('Range("B1"):', data2)
# print("Range(a1:c3) : ", rng)
for  rng_data  in  rng: #튜플의 첫번째 차원 : 색깔이 다른 영역 data
    for  cell_data  in  rng_data: #튜플의 두번째 차원을 위한 for문 : 1개의 Cell 요소
        print(cell_data.value) #각 Cell 요소의 값 출력

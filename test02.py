import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.Workbook() #새로운 Workbook 객체 생성

print(wb) #객체를 출력해보기

wb.save("openpyxl_test.xlsx")
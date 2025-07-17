import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.load_workbook(r"C:\dev\workspace\py_test\resource\xlsx\0301_test.xlsx", data_only=True)
ws = wb["Sheet5"]

data = []
for  row  in  ws.rows:    
    data.append(row[5].value)

print(data)    

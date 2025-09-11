import pandas as pd

file_name = r"C:\dev\workspace\py_test\resource\xlsx\E01EXAMPLE.xlsx"


# # 기존 시트 읽기
# df1 = pd.read_excel(file_name, sheet_name=1)
# df2 = pd.read_excel(file_name, sheet_name=2)

# # 병합
# df3 = df1.merge(df2, how="left")

# 시트 읽기 및 병합
df3 = pd.read_excel(file_name, sheet_name=1).merge(
    pd.read_excel(file_name, sheet_name=2), how="left"
)

# 바로 Sheet4에 저장 (기존 Sheet4가 있으면 덮어쓰기)
with pd.ExcelWriter(file_name, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    df3.to_excel(writer, sheet_name="Sheet4", index=False)

print("✅ df3가 Sheet4에 바로 저장되었습니다.")

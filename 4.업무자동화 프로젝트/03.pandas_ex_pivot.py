import pandas as pd

file_name = r"C:\dev\workspace\py_test\resource\xlsx\E03EXAMPLE.xlsx"


# # 기존 시트 읽기
# df1 = pd.read_excel(file_name, sheet_name=1)
# df2 = pd.read_excel(file_name, sheet_name=2)

# # 병합
# df3 = df1.merge(df2, how="left")

# 시트 읽기 및 병합
df3 = pd.read_excel(file_name, sheet_name=1).merge(
    pd.read_excel(file_name, sheet_name=2), how="left"
)

pdf1 = df3.pivot_table("수량", index=["업체","메뉴"], aggfunc="count")
pdf2 = df3.pivot_table("가격", index="업체", aggfunc="sum")

with pd.ExcelWriter(file_name, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    pdf1.to_excel(writer, sheet_name="Sheet4", index=False)

with pd.ExcelWriter(file_name, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    pdf2.to_excel(writer, sheet_name="Sheet5", index=False)

# pdf1.to_clipboard(index=False)
# pdf2.to_clipboard(index=False)
import os
import  openpyxl  as  op
from  openpyxl.styles.fonts  import  Font
from  openpyxl.styles  import  Border, Side
from  openpyxl.styles.colors  import  Color
from  openpyxl.styles  import  Alignment
from  openpyxl.styles  import  PatternFill
from  openpyxl.styles  import  Protection

file_name = "030106.xlsx"

# 파일 삭제
try:
    os.remove(file_name)
    print(f"파일 '{file_name}'이(가) 성공적으로 삭제되었습니다.")
except FileNotFoundError:
    print(f"오류: 파일 '{file_name}'을(를) 찾을 수 없습니다.")
except PermissionError:
    print(f"오류: 파일 '{file_name}'을(를) 삭제할 권한이 없습니다.")
except Exception as e:
    print(f"파일 삭제 중 예상치 못한 오류가 발생했습니다: {e}")

#Workbook 및 Worksheet 객체 설정하기
wb = op.Workbook()
ws = wb.active

# ======================================================
# 1) Font(글꼴)
# ======================================================

#font test1 : 직접 font 설정하기
ws["A1"].value = "Font test1"
ws["A1"].font = Font(size=20, italic = True, bold = True)

#font test2 : format을 정해놓고 font 설정하기
ws["A2"].value = "Font Test2"
font_format = Font(size=12, name='굴림', color = 'FF000000')
ws["A2"].font = font_format

# ======================================================
# 2) Border, Side(테두리)
# ======================================================

#"C3"에 값 입력
ws["C3"].value = "1개 Cell"

#border test1 : 위에는 실선, 아래에는 이중선 적용 예시 코드
ws["C3"].border = Border(top = Side(border_style="thin", color="ff0000"), bottom = Side(border_style="double"))
# ws["C3"].border = Border(bottom = Side(border_style="double"))


# ======================================================
# 3) Alignment(정렬)
# ======================================================

# "C2"와 "C4"에 Text 입력  
ws["C2"].value = "Alignment test1"
ws["C4"].value = "Alignment test2"

# 셀 너비, 높이 설정하기
ws.row_dimensions[2].height = 50 #2행의 높이 50으로
ws.row_dimensions[4].height = 50 #4행의 높이 50으로
ws.column_dimensions['C'].width = 50 #C열의 너비 50으로

#Alignment test1
ws["C2"].alignment = Alignment(horizontal = 'left', vertical='center')

#Alignment test2
format1 = Alignment(horizontal = 'center', vertical='center')
ws["C4"].alignment = format1

# ======================================================
# 4) PatternFill(채우기)
# ======================================================

#PatternFill test1 : green
ws["C5"].fill = PatternFill(fill_type='solid', fgColor="00FF00")
# ws["C3"].fill = green

#PatternFill test2 : Black
ws["C5"].fill = PatternFill(fill_type='solid', fgColor="000000")


# ======================================================
# 5) Protection(셀 숨김, 보호)
# ======================================================

#text 입력하기
ws["D3"].value = "Protection test1 : locked"
ws["D5"].value = "Protection test2 : hidden"

#Protection 속성 설정하기(숨김/잠금)
ws["D3"].protection = Protection(locked = True, hidden = True)
ws["D5"].protection = Protection(locked = False, hidden = False)

#Workbook(엑셀) 저장 및 객체 닫기
wb.save(file_name)
wb.close()
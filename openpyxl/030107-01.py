import os
import  openpyxl  as  op
from  openpyxl.styles.fonts  import  Font

#test 엑셀 파일이 있는 경로 지정
path = r"C:\dev\workspace\py_test"

input_file_name = "030107_test.xlsx"
file_name = r"C:\dev\workspace\py_test\result\030107.xlsx"

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


wb = op.load_workbook(path + "/"+ input_file_name, data_only=True) #Workbook 객체 생성
ws = wb.active #Worksheet 객체 생성

#합/불 판정해주는 함수
def passfail():
    #최대 행값 구하기
    max_row = ws.max_row
    #최대 행값 활용하여 for문 (2행부터~최대행까지)
    for row_index in range(2, max_row+1):
        #평균값 데이터를 average 변수에 저장
        average = ws.cell(row = row_index, column=5).value
        #평균이 70점 이상이면 '합격' 표시
        if average >= 70:
            ws.cell(row=row_index, column=6).value = "합격"
        #평균이 70점 미만이면 '불합격' 표시
        else:
            ws.cell(row=row_index, column=6).value = "불합격"

#조건부 서식 적용 함수
def conditionFormat():
    #합격일 때 format 변수로 설정
    pass_format =  Font(size=12, name='굴림', color = '000000FF') #   000000FF은 파란색
    #불합격일 때 foramt을 변수로 설정
    fail_format =  Font(size=12, name='굴림', color = '00FF0000') #00ff000은 빨간색
    #행 최대값 구하기 
    max_row  = ws.max_row

    #행 최대값 사용하여 for문 사용(반복)
    for row_index in range(2, max_row+1):
        #합격/불합격인지 문자열 읽어오기
        result_str = ws.cell(row = row_index, column=6).value
        #합격일 경우 서식
        if result_str == "합격":
            ws.cell(row=row_index, column=6).font = pass_format

        #불합격일 경우 서식
        else:
            ws.cell(row=row_index, column=6).font = fail_format

#실행부
if __name__ == "__main__":
    # 1) 성적표에 합격/불합격 표시하기
    passfail()
    # 2) 합격/불합격에 대한 조건부 서식 적용하기
    conditionFormat()
    wb.save(file_name)

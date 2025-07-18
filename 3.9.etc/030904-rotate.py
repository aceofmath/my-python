# step1.관련 모듈 import
from PyPDF2 import PdfReader, PdfWriter

# step2.기존 pdf 불러오기
pdfReader = PdfReader(r"C:\dev\workspace\py_test\resource\pdf\a.pdf", "rb")

# step3.새로 만들 pdf 객체 생성
pdfWriter = PdfWriter()

# 페이지 하나씩 받아와서 돌린 후, 붙여넣는 반복문
for pageNum in range(len(pdfReader.pages)):

    # step4.기존 PDF에서 한 페이지씩 가져오기
    page = pdfReader.pages[pageNum]

    # step5.시계 방향으로 90도 회전 (반시계로 90도 회전은 270 입력하면 됨)
    page.rotate(180)

    # step6.회전된 페이지 새로운 PDF에 붙여넣기
    pdfWriter.add_page(page)

# step7.새로운 pdf 파일을 해당 경로('./')에 원하는 이름으로 저장
pdfWriter.write(open(r'./result/030904/a.pdf', 'wb'))

# step1.관련 모듈 import
from PyPDF2 import PdfReader, PdfWriter

# step2.기존 PDF 불러오기
pdfReader = PdfReader(r"C:\dev\workspace\py_test\resource\pdf\a.pdf", "rb")

# 페이지 하나씩 받아와서 저장하는 반복문
for pageNum in range(len(pdfReader.pages)):

    # step3.새로 만들 pdf 객체 생성 (계속 누적되지 않기 위해 for문 안으로 넣음)
    pdfWriter = PdfWriter()

    # step4.기존 PDF에서 한 페이지씩 가져오기
    page = pdfReader.pages[pageNum]

    # step5.위에서 가져온 페이지를 새로 만든 PDF에 붙여넣기
    pdfWriter.add_page(page)

    # step6.새로운 PDF 파일을 해당 경로('./')에 원하는 이름으로 저장
    # (이름을 계속 다르게 해주기 위해서 f 문자열 포매팅 개념을 이용)
    pdfWriter.write(open(f"./result/030904/a{pageNum+1}.pdf", "wb"))

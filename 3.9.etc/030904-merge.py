# step1.관련 모듈 import (Writer 대신 Merger를 사용하는 것에 주의!)
from PyPDF2 import PdfReader, PdfMerger

# step2.기존 pdf 불러오기
pdfReader1 = PdfReader(open(r"C:\dev\workspace\py_test\resource\pdf\a.pdf","rb")) # 3장
pdfReader2 = PdfReader(open(r"C:\dev\workspace\py_test\resource\pdf\b.pdf","rb")) # 2장

# step3.새로 만들 pdf 객체 생성 (병합용)
pdfMerger = PdfMerger()

# step4.PDF 하나씩 가져와서 차례대로 병합
pdfMerger.append(pdfReader1)
pdfMerger.append(pdfReader2)

# step5.새로운 pdf 파일을 해당 경로('./')에 원하는 이름으로 저장
pdfMerger.write("./result/030904/병합한 테스트 PDF 파일.pdf")

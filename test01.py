# step1.필요한 PIL의 모듈 3가지 import
from PIL import  Image, ImageDraw, ImageFont

# step2.워터마크 삽입할 이미지 불러오기
img = Image.open('screen-3.jpg')
width, height = img.size

# step3.그림판에 이미지를 그대로 붙여넣는 느낌의 Draw() 함수 
draw = ImageDraw.Draw(img)

# step4.삽입할 워터마크 문자
text = "H3LAB"

# step5.삽입할 문자의 폰트 설정
font = ImageFont.truetype('C:/Users/PMG036/AppData/Local/Microsoft/Windows/Fonts/경기천년제목_Light.ttf', 50)

# step6.삽입할 문자의 높이, 너비 정보 가져오기
left, top, width_txt, height_txt = draw.textbbox((10,10), text, font)

# step7.워터마크 위치 설정
margin = 10
x = left
# x = width - width_txt - margin
y = top
# y = height - height_txt - margin

# step8.텍스트 적용하기
draw.text((x, y), text, fill='white', font=font)

# step9.이미지 출력
img.show()

# step10.현재작업 경로에 완성 이미지 저장
img.save("screen-3_make.jpg")

#import PIL로 불러올 시, Image 모듈은 안불러와져서 에러가 뜸

from PIL import Image

# 고양이 이미지 불러와서 img라는 변수에 입력
img = Image.open(r'C:\dev\workspace\py_test\resource\img\cat.jpg')

# ======================================================
# 1) Pillow 설치 및 이미지 불러오기
# ======================================================

# 이미지 보여주기
# img.show()

# 이미지 파일명
print(img.filename)
# >>> cat.jpg

# 이미지 형식
print(img.format)
# >>> JPEG

# 이미지 크기
print(img.size)
# >>> (640, 426)

# 이미지 너비
print(img.width)
# >>> 640

# 이미지 높이
print(img.height)
# >>> 426

# 이미지의 색상 모드
print(img.mode)
# >>> RGB

# ======================================================
# 2) 이미지 편집(resize,crop,rotate,flip)
# ======================================================

# (1)이미지 사이즈 변경
# img_resized = img.resize((400,300))

# # 변경한 이미지 출력
# img_resized.show()

# # 비교를 위해 원본 이미지 출력
# img.show()

# # (2)이미지 자르기
# img_cropped = img.crop((0,0,300,300))

# # 잘라낸 이미지 출력
# img_cropped.show()

# # (3) 이미지 회전
# # 이미지 90도 회전
# img_rotated = img.rotate(90)

# # 회전한 이미지 출력
# img_rotated.show()

# # (4)) 이미지 대칭
# # 좌우대칭
# img_flipped_LR = img.transpose(Image.FLIP_LEFT_RIGHT)
# img_flipped_LR.show()

# # 상하대칭
# img_flipped_TB = img.transpose(Image.FLIP_TOP_BOTTOM)
# img_flipped_TB.show()


# (5) 이미지 저장
img_flipped_TB = img.transpose(Image.FLIP_TOP_BOTTOM)
img_flipped_TB.save(r'C:\dev\workspace\py_test\result\cat_flip.jpg')

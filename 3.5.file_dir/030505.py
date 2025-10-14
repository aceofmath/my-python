import shutil
import os

# 방법 1 - 파일과 폴더가 현재 작업경로에 있는 경우만 가능
# shutil.copy('복사할 파일명.확장자', '복사한 파일을 담을 폴더명')

print(os.getcwd())

path = os.getcwd() + '/3.5.file_dir/'

# 예시
shutil.copy(path + '/Test.xlsx', path + '/테스트 폴더')

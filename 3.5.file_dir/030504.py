import glob

list_filepath = glob.glob("*.jpg")

list_filepath = glob.glob('./**/*.jpg', recursive=True)

for filepath in list_filepath:
    print(filepath)


# 경로 관련 라이브러리
# 1. os
# os 모듈은 폴더(디렉토리)를 생성하거나 경로(path)를 다룰 때 사용합니다.

# 2. shutil
# shutil 모듈은 파일을 복사하거나 이동시킬 때 사용합니다.

# 3. glob
# glob 모듈은 패턴을 사용하여 현재 폴더(디렉토리)는 물론 하위 경로의 파일들을 검색할 때 사용합니다.
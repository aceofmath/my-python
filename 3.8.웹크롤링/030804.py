# requests 패키지 가져오기
import requests
# BeautifulSoup 패키지 불러오기
# 주로 bs로 이름을 간단히 만들어서 사용함
from bs4 import BeautifulSoup as bs

# 가져올 url 문자열로 입력
url = 'https://h3lab.netlify.app'

# requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
response = requests.get(url)

# 우리가 얻고자 하는 html 문서가 여기에 담기게 됨
html_text = response.text

# html을 잘 정리된 형태로 변환
soup = bs(html_text, 'html.parser')

searchs = soup.select('.text-white.mb-5')

for i in searchs:
    print(i.get_text())

searchs = soup.select('.portfolio-box')
for i in searchs:
    print(f"■프로젝트명 : {i.attrs['title']}, ■이미지소스 : {i.attrs['href']}")

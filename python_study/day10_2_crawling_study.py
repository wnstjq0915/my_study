# 데이터 수집 단계

# 데이터 수집 -> 데이터 분석/처리 -> 인공지능 모델 학습
# -> 인공지능 모델 평가 -> 사용

# http (hypertext transfer protocol)
# request - response 요청 응답
# client - server
# html (hypertext markup language)
# 웹사이트를 표현하기 위한 언어
# <html></html>
# html 파싱

# import requests # 외부 라이브러리라 터미널에 pip install requests 설치하기

# url = "https://www.naver.com/"
# response = requests.get(url) # 주소로 요청하고 응답 받기
# status = response.status_code # 상태코드
# html = response.text

# print(status)
# print(html)

# http 상태 코드
# 200 : OK
# 요청 성공
# 302 : 리다이렉트
# 다른 페이지로 바로 연결

# 400번대는 클라이언트 리퀘스트, 즉 내 잘못이 대부분
# 400 : Bad REquest 요청이 잘못됨
# 401 : Unauthorized 비인증됨
# 403 : Forbidden 접근 권한 없음
# 404 : Not Found  요청받은 내용이 없음
# 405 : Method Not Allowed 접근 방법이 잘못됨

# 500 : Internal Server Error 서버 에러
# 501 : Not Implemented
# 502 : Bad Gateway 잘못된 응답

# url 구조
# 프로토콜://호스트주소:포트번호/경로?쿼리 # 추가적인 데이터는 쿼리로. 검색 같이 유동적인 값
# http://naver.com/?~~~~~
# 쿼리
# 쿼리이름=값&쿼리이름=값&쿼리이름=값

# search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# response = requests.get(search_url)
# print(response.text)

# search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# keyword = '맥주'
# url = search_url + keyword
# response = requests.get(url)
# print(type(response.text))

# BeautifulSoup # pip install beautifulsoup4
# html 파싱(parsing)
# html을 객체 구조화해서 사용
# import requests
# from bs4 import BeautifulSoup # html을 객체로 볼 수 있게 하는거. 이것도 외부라이브러리
# html 태그
# <태그이름 속성==속성값>내용</태그이름>
# html = "<html><body>Hello</body></html>"
# soup = BeautifulSoup(html, "html.parser")
# print(soup.body.text)
# print(type(soup.body.text))


# search_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# 네이버는 셀레니움 사용하면 크롤링 가능


# 구글에 맥주 검색해서 나오는 이미지들 자동으로 폴더 생성해서 그 안에 다운받기
# import requests
# from bs4 import BeautifulSoup

# search_url = "https://www.google.com/search?tbm=isch&q="
# # 이건 구글
# keyword = '맥주'
# url = search_url + keyword
# response = requests.get(url)

# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# imgs = soup.find_all('img') 
# # (soup.find_all('img')[4]) # img 찾아서 리스트 한개에 다 담아줌. 그렇다보니 인덱싱 가능.

# import os # 폴더 만들기 위해서
# folder_name = "imgs"
# if not os.path.exists(folder_name): # "imgs"라는 폴더명이 없으면
#     os.mkdir(folder_name) # 폴더 생성

# for idx, img in enumerate(imgs[1:]):
#     file_name = f"img_{idx}.jpg"
#     file_path = os.path.join(folder_name, file_name)
#     img_response = requests.get(img['src'])
#     img_data = img_response.content
#     with open(file_path, "wb") as f:
#         f.write(img_data) # wb: 2진수 데이터로 쓰겠다는거



# enumerate(이터러블)
# li1 = ["김연아", "류현진", "손흥민"]
# for name in enumerate(li1):
#     print(name)
# 출력:
# (0, '김연아')
# (1, '류현진')
# (2, '손흥민')



"""
crawling_result 폴더의 headlines.txt 파일에 저장
"""
# 네이버 IT/과학 뉴스 크롤링

import os # 폴더 만들기 위해서
folder_name = "crawling_result"
if not os.path.exists(folder_name): # "imgs"라는 폴더명이 없으면
    os.mkdir(folder_name) # 폴더 생성

import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}) # 크롤링 방지 회피. 네이버에서 프로그램 통한 접속 막아둔거 직접 접속코드 같은걸 적어서 우회함
html = response.text
soup = BeautifulSoup(html, "html.parser")
div = soup.find('div', attrs={'class': 'list_body'}) # attrs가 클래스 접근하는거??
# a태그를 가지고 오고 싶은데 링크가 달린거 다 가져오게 됨.
# 그래서 헤드라인 속 a태그만 가져오기 위해 div 클래스 list_body를 가져옴.
headlines = div.find_all('a', attrs={'class': 'cluster_text_headline'}) # a태그 달린거 기사 저장함. a태그는 링크가 달린거에 대한 태그

for headline in headlines: # a태그 한줄한줄 headline 변수에 할당
    print(headline.text.strip()) # 공백 없앤 기사제목들 한줄프린트
    with open("crawling_result/headlines.txt", "a", encoding="utf-8") as f: # crawling_result 폴더 안에 headlines.txt에 내용 적기.(파일 없으면 만듬.)
        f.write(headline.text.strip()) # 기사내용 공백 없앤 뒤에 적기
        f.write("\n") # 줄바꿈
# 기사내용 가져오기
    article_response = requests.get(headline['href']) # a태그 링크 뒤에 href=링크 식으로 구성돼 있으므로 링크에 접속요청
    article_soup = BeautifulSoup(article_response.text, "html.parser") # 접속요청 반응을 택스트로 바꾼 뒤 파싱하고 article_soup에 할당
    article = article_soup.find('div', attrs={"id": "dic_area"}) # 기사 내에 기사내용의 공간이 id='dic_area'.
    print(article.text) # 따로 저장은 안 하고 프린트만 함.
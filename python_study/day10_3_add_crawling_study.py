import requests
from bs4 import BeautifulSoup

search_url = "https://www.google.com/search?tbm=isch&q=" # 구글 query=검색내용 에서 검색내용만 빼서 가져옴.
keyword = '맥주'
url = search_url + keyword
response = requests.get(url) # url에 접속요청을 했을 때 반응을 response에 저장, 외부라이브러리 requests가 있어야 함.
html = response.text # 접속이 잘 됐을때의 코드인 200에 .text를 붙이면 그 페이지의 html을 긁어옴. 이걸 html 변수에 저장.
soup = BeautifulSoup(html, "html.parser") # html은 그냥 텍스트라 파이썬에서 다룰 수 있게 객체로 바꾸기 위해 BeautifulSoup 사용


imgs = soup.find_all('img') # beutifulsoup해서 .find_all 사용가능
# (soup.find_all('img')[4]) # img 찾아서 리스트 한개에 다 담아줌. 그렇다보니 인덱싱 가능.

import os # 폴더 만들기 위해서
folder_name = "imgs"
if not os.path.exists(folder_name): # "imgs"라는 폴더명이 없으면
    os.mkdir(folder_name) # 폴더 생성

for idx, img in enumerate(imgs[1:]): # 파일이름 겹쳐서 덮어쓰기 되는 것을 방지하기 위해 enumerate를 써서 파일명에 인덱스 할당
    file_name = f"img_{idx}.jpg" # 파일명: 'img_인덱스(ex 0 ~ 10).jpg
    file_path = os.path.join(folder_name, file_name) # 폴더 안에 파일 만들기
    img_response = requests.get(img['src']) # img 태그 내에서 src라는 클래스 비슷한 문구가 들어있는 이미지파일에 접속요청을 보내고 img_response에 받음
    img_data = img_response.content # 경로의 데이터(이미지파일)를 img_data에 할당. 16진수로 할당이 됨.
    with open(file_path, "wb") as f: # wb: 2진수로 데이터를 쓰는거. 파일을 열고 2진수로 된 내용을 적는거 with open -> 파일 open이랑 close 자동으로 해주는거
        f.write(img_data) # 파일을 만들어서 2진수로 된 이미지파일을 적음. 이게 jpg파일로 되면서 이미지화됨.
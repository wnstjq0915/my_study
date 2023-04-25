# 파일 입출력
# 파이썬에서 파일 생성, 수정

# open()
# 파이썬 내장 함수
# 파일을 열고, 파일 객체를 리턴한다.
# open(파일 이름, 파일 열기 모드)

# f = open("C:/users/405/my_study/python_study/새파일.txt", 'w') # 파이썬 스터디 폴더에 '새파일.txt' 파일이 생성됨.
# f.close()


# 파일의 경로
# 절대 경로 : C:/ D:/ 처럼 최상단 경로부터 나타낸 경로
# (누가 길을 물어봤을 때 주소를 알려주는거)
# 상대 경로 : 현재 작업 위치부터 나타낸 경로
# (여기서 앞으로 가서 옆으로 가면 나온다 같이 설명하는식)

# 파일 열기 모드
# r: 읽기 모드, 파일을 읽기만 할 때 사용 # 내용 추가 및 입력 불가능 read
# w: 쓰기 모드, 파일에 내용을 쓸 때 사용 # 내용 쓸 때 사용 write
# a: 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용 add

# f = open("python_study/새파일.txt", 'w', encoding="utf-8")
# for i in range(1, 11):
#     f.write(str(i) + "번째 줄\n") # print가 터미널에 출력되는 것과는 다르게 파일에 데이터 출력
# f.close()
# w모드는 덮어쓰기 된다.(전에 기록한 내용들 사라짐)

f = open("python_study/새파일.txt", 'a', encoding="utf-8")
for i in range(11, 21):
    f.write(str(i) + "번째 줄\n")
f.close() # 새 파일에 잘 추가돼서 입력됨.
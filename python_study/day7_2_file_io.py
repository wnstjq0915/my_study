# 파일 입출력
# 파이썬에서 파일 생성, 수정

# open()
# 파이썬 내장 함수
# 파일을 열고, 파일 객체를 리턴한다.
# open(파일 이름, 파일 열기 모드)

f = open("C:/users/405/my_study/python_study/새파일.txt", 'w') # 파이썬 스터디 폴더에 '새파일.txt' 파일이 생성됨.
f.close()


# 파일의 경로
# 절대 경로 : C:/ D:/ 처럼 최상단 경로부터 나타낸 경로
# (누가 길을 물어봤을 때 주소를 알려주는거)
# 상대 경로 : 현재 작업 위치부터 나타낸 경로
# (여기서 앞으로 가서 옆으로 가면 나온다 같이 설명하는식)

# 파일 열기 모드
# r: 읽기 모드, 파일을 읽기만 할 때 사용 # 내용 추가 및 입력 불가능 read
# w: 쓰기 모드, 파일에 내용을 쓸 때 사용 # 내용 쓸 때 사용 write
# a: 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용 add


# w
f = open("python_study/새파일.txt", 'w', encoding="utf-8")
for i in range(1, 11):
    f.write(str(i) + "번째 줄\n") # print가 터미널에 출력되는 것과는 다르게 파일에 데이터 출력
f.close()
# w모드는 덮어쓰기 된다.(전에 기록한 내용들 사라짐)

# a
f = open("python_study/새파일.txt", 'a', encoding="utf-8")
for i in range(11, 21):
    f.write(str(i) + "번째 줄\n")
f.close() # 새 파일에 잘 추가돼서 입력됨.

# r
# readline() 한줄
# readlines() 리스트형태로 한줄씩 문자열로 전부
# read() 전부 문자열로


# readline() 함수
# 첫번째 줄부터 1줄 읽어온다.
# 커서가 이동하는 것처럼 읽어옴
f = open("python_study/새파일.txt", 'r', encoding="utf-8")
while True:
    line = f.readline()
    if line == "":
        break
    print(line, end = "")
f.close()
# 1번째 줄
# 2번째 줄
# ...


#readlines() 함수
# 파일의 모든 줄을 읽어서 리스트로 반환
f = open("python_study/새파일.txt", 'r', encoding="utf-8")
lines = f.readlines()
print(lines) # '1번째 줄\n', '2번째 줄\n' ... 리스트 형태로 한줄씩 저장
f.close()

f = open("python_study/새파일.txt", 'r', encoding="utf-8")
lines = f.readlines()
for line in lines: # 각 줄을 lines라는 리스트에 담아서
    print(line) # 한줄씩 출력되게
    f.close()


# read() 함수
# 파일 내용 전체를 문자열로 리턴한다.
f = open("python_study/새파일.txt", 'r', encoding="utf-8")
data = f.read()
print(data) # 각 줄을 읽고 다 프린트
print([data]) # 안에 담긴 내용들을 '로 감싸 줄바꿈 \n까지 프린트
f.close()


# # for문으로 읽기
f = open("python_study/새파일.txt", 'r', encoding="utf-8")
for line in f:
    print(line)
f.close()


# with문
# open - close를 자동으로 해준다.
with open("python_study/새파일.txt", "a", encoding="utf-8") as f: # 수동으로 close 넣는 것보다 관리가 쉬움
    f.write("end of file") # 코드블럭을 open과 close로 감쌈


# csv(comma separated values)
# ,로 구분되는 값들을 모아놓은 파일
# 이름, 입실시간, 퇴실시간
# 권오천,09:20,18:10
# 김예진,09:21,18:11

with open("python_study/data.csv", "w", encoding="utf-8") as f:
    f.write("날짜,날씨,기온,\n")
    f.write("20230424,맑음,10\n")
    f.write("20230425,비,9\n")

with open("python_study/data.csv", 'r', encoding="utf-8") as f:
    data = f.readlines()
    print(data)


"""
계산 결과 저장 함수
정수 2개를 입력받고
두 수를 더한 결과를
add_result.txt파일에
저장하는 함수를 정의하세요
함수 이름: add_write
"""
def add_write(n1, n2):
    with open("add_result.txt", 'w', encoding="utf-8") as f: # 현재 위치인 mystudy폴더에 생성
        f.write(str(n1 + n2)) # str값으로 해야 들어감.
add_write(3, 4) # 정상적으로 7 저장됨.


"""
텍스트 파일에 적힌 정수 2개를 읽어와서
더하는 함수를 정의하세요
텍스트 파일 이름: add_number.txt
경로: python_study/add_number.txt
정수 2개를 더한 결과를 print하세요.
함수 이름: read_add_print
"""
def read_add_print():
    with open("python_study/add_number.txt", 'r', encoding="utf-8") as f:
        data = f.read()
        a = int(data[0]) # 파일 내의 문자열을 인덱싱을 통해 저장
        b = int(data[2])
        print(a + b)
read_add_print() # 잘 됨.
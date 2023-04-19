li_1 = ["Hello", "World", "Python"]
# li_1의 원소를 사용하여
# Hello World Python 이라고 출력하세요

# li_1의 원소를 사용하여
# Help라고 출력하세요.

li_2 = [1, 2, 3]
# li_1과 li_2를 사용하여
# ["Hello", "World", "Python", 1, 2, 3]
# 을 출력하세요

# li_1과 li_2를 사용하여
# ["Hello", 1, "World", 2, "Python", 3]
# 을 출력하세요

print(li_1[0], li_1[1], li_1[2]) # li_1[0] + li_1[1] + li_1[2] 이런식으로 했었으나 비효율적
print(li_1[0][:3] + li_1[2][0]) # [0:3]으로 썼으나 0은 생략 가능
print(li_1 + li_2) # 비효율적이지만 li_1.extend(li_2)를 해서 li_1 print할수도 있음
li_1.insert(1, li_2[0])
li_1.insert(3, li_2[1]) # index 주의
li_1.insert(5, li_2[2]) # 마지막은 append 사용가능 ( 코드는 더 짧아지나 가시성 약간 떨어짐 )
print(li_1)

# 첫번째 문제 다른 방법도 있음
# join(리스트)
# 리스트의 문자열을 합친다.
# " ".join(li_1) 이렇게 하면 li_1의 원소 사이사이에 " "가 들어간 뒤에 합쳐짐
# print(" ".join(li_1)) # Hello World Python

scores = []
scores = list() # 비어있는 리스트 생성. 위랑 이거랑 같은 코드

scores.append(int(input("영어 점수:")))
scores.append(int(input("국어 점수:")))
scores.append(int(input("수학 점수:")))

# avg = (scores[0] + scores[1] + scores[2]) / 3 # 이렇게 다 쓰는걸 하드코딩이라 함
#윗방법 대신 sum() 활용

# sum()
# 리스트의 요소를 모두 더한다.
# 리스트에 문자가 있으면 에러
avg = sum(scores) / 3
# 위에 평균 구하는 과정보다 훨씬 단순(전부 더하기에). 이런 과정을 일반화라고 함.

print(f"평균점수: {avg}")

if avg >= 91:
    print("성적: A")
elif avg >= 81:
    print("성적: B")
elif avg >= 71:
    print("성적: C")
elif avg >= 61:
    print("성적: D")
else:
    print("성적: F")


# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건을
# 몇개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 500원이다.


# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건별로 각각 몇 개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은
# 1번 물건 1000원, 2번 물건 50원, 3번 물건 120원이다.

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 내가 한거

# me = []
# me.append(int(input("나이: ")))
# me.append(int(input("돈: ")))

# a = [(me[1] // 500), (me[1]) % 500]
# a1 = [(me[1] // 1000), (me[1]) % 1000]
# a2 = [(me[1] // 50), (me[1]) % 50]
# a3 = [(me[1] // 120), (me[1]) % 120]

# print(f"물건: {a[0]}개, 잔돈: {a[1]}원")
# print(f"물건1: {a1[0]}개, 잔돈: {a1[1]}원")
# print(f"물건2: {a2[0]}개, 잔돈: {a2[1]}원")
# print(f"물건3: {a3[0]}개, 잔돈: {a3[1]}원")

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

age = input("나이")
money = int(input("돈"))
prices = [500, 1000, 50, 120]

print(money // prices[0], "개", money % prices[0], "원")
print("물건1", money // prices[1], "개", money % prices[1], "원")
print("물건2", money // prices[2], "개", money % prices[2], "원")
print("물건3", money // prices[3], "개", money % prices[3], "원")

#논리연산자 요약

age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken:
    print("치킨을 먹는다.")
if money >= beer and age >= 20:
    print("맥주를 먹는다.")
if money >= drink:
    print("음료수를 먹는다.") # 치킨을 먹는다, 음료수를 먹는다 라는 두 출력이 나오나 20000원으로는 둘 다 못 먹음.

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # 방법 1
age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
# 치킨, 맥주, 음료수
# 우선순위: 치킨, 맥주, 음료 순. (맥주나 음료수는 둘 중 하나.)
if money >= chicken:
    if money >= chicken + beer and age >= 20: # 3만원 이상, 성인. if문 가장 위에 가장 빡센 조건 넣기.
        print("치킨과 맥주를 먹는다.")
    elif money >= chicken + drink: # 2만 5천원 이상
        print("치킨과 음료수를 먹는다.")
    else:
        print("치킨을 먹는다.") # 2만원 이상
else:
    print("아무것도 먹지 못 한다.") # 2만원 미만


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # 방법 2
age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
# 치킨, 맥주, 음료수
# 우선순위: 치킨, 맥주, 음료 순. (맥주나 음료수는 둘 중 하나.)
if money >= chicken:
    money -= chicken
    if money >= beer and age >= 20:
        print("치킨과 맥주를 먹는다.")
    elif money >= drink:
        print("치킨과 음료수를 먹는다.")
    else:
        print("치킨을 먹는다.")
else:
    print("아무것도 먹지 못 한다.")


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # 한줄씩 출력
age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken:
    print("치킨을 먹는다.") # 2만원 이상
    if money >= chicken + beer and age >= 20: # 3만원 이상, 성인.
        print("맥주를 먹는다.")
    elif money >= chicken + drink: # 2만 5천원 이상
        print("음료수를 먹는다.")
else:
    print("아무것도 먹지 못 한다.") # 2만원 미만


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # if 하나만 쓰기
age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken + beer and age >= 20:
    print("치킨과 맥주를 먹는다.")
elif money >= chicken + drink:
    print("치킨과 음료수를 먹는다.")
elif money >= chicken:
    print("치킨을 먹는다.")
else:
    print("아무것도 못 먹는다.")


# 내 풀이는 음료만 먹는 것은 적용되지 않음.


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # 강사님 정답 1
age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken:
    print("치킨을 먹는다.")
money -= chicken
if money >= beer and age >= 20:
    print("맥주를 먹는다.")
elif money >= drink:
    print("음료수를 먹는다.")


print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # 강사님 정답 2. 모든 경우 가능하고 보기 편해서 이게 젤 나은 듯?
if money >= chicken + beer + drink and age >= 20:
    print("치킨, 맥주, 음료수 먹는다.")
elif money >= chicken + beer and age >= 20:
    print("치킨, 맥주 먹는다.")
elif money >= chicken + drink:
    print("치킨, 음료수 먹는다.")
elif money >= chicken:
    print("치킨 먹는다.")
elif money >= beer + drink and age >= 20:
    print("맥주, 음료수 먹는다.")
elif money >= drink and age >= 20:
    print("맥주 먹는다.")
elif money >= drink:
    print("음료수 먹는다.")
else:
    print("못 먹는다.")
# dictionary(딕셔너리) 자료형
# 바로바로 찾아쓰기 좋음
# key-value 형태
# key: value
# {"이름": "이름", "나이": 18, "점수": [80, 90, 100], 1: "문자"}  # key값은 숫자도 가능
# # 리스트는 인덱스로 접근하는 반면 얘는 key값으로 찾기에 어떤 정보인지 알아보기 쉬움

person = {
    "이름": "이름",
    "나이": 18,
    "점수": {
        "영어": 80,
        "국어": 90,
        "수학": 100,
    }
}

print(person["나이"]) # 18
print(person["점수"]["영어"]) # 80

dict_1 = {1: 'a'}
dict_1['b'] = 2 # 'b': 2 key-value 쌍 추가
print(dict_1)
dict_1[1] = 'c' # key가 1인 데이터의 value를 c로 수정
print(dict_1)
del dict_1[1] # key가 1인 데이터쌍이 없어짐
print(dict_1)


dict_2 = {1: 'a', 2: 'b', 3: 'c'}
# keys()
# 딕셔너리에서 key 값만 리스트 형태로 돌려준다.
# dict_2.keys()
dict_keys = dict_2.keys()
print(dict_keys)
# values()
dict_values = dict_2.values() # 딕셔너리에서 key 값만 리스트 형태로 돌려준다.
print(dict_values)

# 딕셔너리에서 key-value 쌍을 튜플로 묶은 값을 리스트 형태로 돌려준다.
dict_items = dict_2.items() # 반복문 돌릴 때 유용
print(dict_items)

# get()
# key에 대응되는 value를 돌려준다.
# key값이 존재하지 않으면 None을 돌려준다. 그냥 dict_2["나이"]를 했을 경우 "나이"가 없으면 에러남
dict_2.get("나이") # dict_2에는 나이라는 키가 없음
print(dict_2.get("나이")) # None. 자바스크립트는 같은 의미로 Null값
a = dict_2.get("나이") # None값 또한 변수에 할당 가능
print(a)
print(dict_2.get("나이", "나이 불명")) # 이 경우 "나이"가 없으면 None 대신 뒤에 "나이불명"을 출력
print(dict_2.get(1)) # 1의 value값인 a 출력
# value를 이용해 key값을 찾는 경우도 있지만 딕셔너리 내를 순회한 뒤에 찾기에 비효율적

# clear()
# 딕셔너리 안의 모든 요소를 삭제한다.
dict_2.clear()
print(dict_2)
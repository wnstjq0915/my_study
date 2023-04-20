# if, else 요약

weather = "비" # weather 변수에 "비"값 할당
print("비가 오나요?", weather == "비") # 비가 오나요? + bool값(True)
if weather == "비": # weather가 "비" 일 때(True)
    print("비가 온다.\n우산을 가져간다.")
else: # weather가 "비"가 아닐 때(False)
    print("비가 오지 않는다.\n우산을 가져가지 않는다.")

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ") # 맑을 경우 추가
weather = "맑음"
print("비가 오나요?", weather == "비")
if weather == "비":
    print("비가 온다.\n우산을 가져간다.")
elif weather == "맑음":
    print("날씨가 좋다.")
else:
    print("비가 오지 않는다.\n우산을 가져가지 않는다.")
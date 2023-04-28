"""
거꾸로 배열해도 같은 단어 또는 문장이 되는
회문인지 판별하는 함수를 정의하세요.
함수에 문자열을 입력받고 회면이면 True
아니면 False를 반환하도록 정의하세요.
함수 이름: is_palindrome
반환 값: True or False
ex 기러기, 토마토 등등
""" # 글자 뒤집는게 편함. reversed? [::-1]


# def is_palindrome(input_string):
#     input_string = input_string.replace(" ", "") # 문자열 중간에 있는 공백 제거
#     # length = len(input_string)
#     # for i in range(lenth//2): # 인트값을 내기 위해서 //
#     #     length - 1 # length에 
#     #     if input_string[i] == input_string[length - 1 - i]:
#     #         return False
#     # # return True


# def is_palindrome(input_string):
#     input_string = input_string.replace(" ", "")
#     return input_string == input_string[::-1]

# # reversed("변수 혹은 문자열") # 리턴값 반대로. [::-1]과 같음. reverse는 리스트만.
# a = "안녕하세요"
# # print(reversed(a)) # 리버스한 값이 프린트되지 않음.
# a = reversed(a)
# print(a) # 이것도 안 됨. reversed보단 [::-1] 쓰기

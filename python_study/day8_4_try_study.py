# 예외처리
# li = [1,2,3,4,5]
# li[100]

# 100 / 0

# f = open("없는파일", "r")

# 에러 발생 시 프로그램을 중단하고
# 에러 메세지를 보여준다.
# 예외처리 구문
# try ~ except
# try 블록에는 오류가 발생할 수 있는 코드
# except 블록에는 오류가 발생했을 때 수행할 코드
# 오류가 발생하지 않으면 except 블록의 코드는 실행되지 않는다.
# try:
#     100 / 0
# except ZeroDivisionError as e:
#     print("에러 발생")
# print("에러 발생 후")

# try:
#     100 / 0
# except Exception as e: # 전체에러 예외처리
#     print(e)
# print("에러 발생 후")

# try:
#     100 / 0
# except ZeroDivisionError as e:
#     print(e, "0으로 나눌 수 없습니다.")

try:
    [1, 2, 3, 4, 5][100]
except IndexError as e:
    print(e, "인덱싱 할 수 없습니다.")
except ZeroDivisionError as e:
    print(e, "0으로 나눌 수 없습니다.")


# finally
# 예외 발생 여부와 상관 없이 항상 수행되는 코드

# try:
#     f = open("없는 파일", "r")
# except:
#     print("에러 발생")
# finally:
#     f.close()

# else
# 오류가 발생하지 않으면 실행

try:
    age = int(input("나이: "))
except:
    print("입력이 잘못 되었습니다.")
else:
    if age >= 20:
        print("성인입니다.")
    else:
        print("미성년자입니다.")

class Bird:
    def fly(self):
        raise NotImplementedError
my_bird = Bird()
try:
    my_bird.fly() # NotImplementError가 발생
except:
    print("구현되지 않았습니다.")
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
# 실행하는 곳에서는 __name__이 __main이 되는데
# import로 불러오면 __name__이 파일이름(my_module)이 됨.
    print(add(1, 2))
    print(sub(3, 4))
else:
    print(__name__)
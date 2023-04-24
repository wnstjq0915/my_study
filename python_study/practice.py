'''
구구단문제 다시 해보기
'''

input_a = int(input("양의 정수: "))
for i in range(1, input_a):
    answer = i
    for j in str(i):
        if int(j) % 3 == 0 and j != '0': # j가 0일때도 주의
            answer = "짝"
            break
    print(answer) # answer을 출력해야 되는거 주의
"""브1
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


예제 입력 1 
Mississipi
예제 출력 1 
?

예제 입력 2 
zZa
예제 출력 2 
Z
"""

word = input().upper()
apb = list(set(word))
count_apb = [word.count(i) for i in apb]
count_max = max(count_apb)
print('?' if count_apb.count(count_max) > 1 else apb[count_apb.index(count_max)])

"""
풀이설명
세트를 이용해서 중복을 제거(런타임 줄이기)
[for문]을 통해서 알파벳마다 count해서 리스트로
최대값을 알아낸 뒤에 삼항연산자를 통해 ? 또는 알파벳으로 출력
"""
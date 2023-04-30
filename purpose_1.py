"""
얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다.
예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때,
해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다.
즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열
callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을
1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.
"""

# def solution(players, callings): # 내 답. 리스트로 풀이. 속도가 너무 느려서 실패
#     for i in callings:
#         a = players.index(i)
#         players[a], players[a - 1] = players[a - 1], players[a]
#     return players

# 정답.
def solution(players, callings):
    hashmap = dict()
    for i,v in enumerate(players):
        hashmap[v] = i 
    for call in callings:
        pre,post = hashmap[call] - 1,hashmap[call]
        hashmap[players[pre]] = post
        hashmap[players[post]] = pre
        players[pre],players[post] = players[post],players[pre]
    return players

"""
목표
line 27에서 players의 배열이 어떻게 바꾸는지를 자세히 보기.
dict형을 key를 이용해 오름차순으로 정렬하는 방법과
dict형 key와 value를 바꾸는 방법 공부
dictinary 관련 더 자세히 알아보기

다른사람 답:
https://school.programmers.co.kr/learn/courses/30/lessons/178871/solution_groups?language=python3
"""
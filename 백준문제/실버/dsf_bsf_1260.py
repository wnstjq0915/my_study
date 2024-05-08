"""
예제입력 (수의 범위, 연결 수, 시작)
4 5 1
1 2
1 3
1 4
2 4
3 4

예제출력(dsf, bsf 순)
1 2 4 3
1 2 3 4
"""
def dsf(graph, start_num, nums_kind, used_nums = set()):
    used_nums.add(start_num)
    if len(nums_kind) == len(used_nums):
        return
    for num in graph[start_num]: # set(graph[start_num] - used_num)을 하고 싶지만 이 연산도 O(n)
        if num not in used_nums:
            print(num, end=' ')
            dsf(graph, num, nums_kind, used_nums)
    return used_nums

def bsf(graph, start_num, used_nums):
    if len(nums_kind) == len(used_nums):
        return
    li = list()

    for num in graph[start_num]:
        if num not in used_nums:
            print(num, end=' ')
            li.append(num)
            used_nums.add(num)
    for num in li:
        bsf(graph, num, used_nums)


graph = dict()
nums_kind = set()
li = list()

step, start = list(map(int, input().split()))[1:]
for _ in range(step): li.append(sorted(list(map(int, input().split()))))
for connect in li:
    if connect[0] not in graph: graph[connect[0]] = list()
    if connect[1] not in graph: graph[connect[1]] = list()
    graph[connect[0]].append(connect[1])
    graph[connect[1]].append(connect[0])
for key in graph.keys(): graph[key].sort() # 입력이 중복된 값이 있다면 list(set()) 사용하기

nums_kind.update(set(graph.keys()))

# 재귀함수 호출
print(start, end=' ')
dsf(graph, start, nums_kind)
print()

print(start, end=' ')
bsf(graph, start, {start})
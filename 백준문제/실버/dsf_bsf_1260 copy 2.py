def dfs(graph, start_num, used_nums = set()):
    print(start_num, end=' ')
    used_nums.add(start_num)
    if len(graph.keys()) == len(used_nums): # 조건에서의 에러로 생각됨 모든 그래프가 하나로 이어지진 않은 것 같음
        return
    for num in graph[start_num]:
        if num not in used_nums:
            dfs(graph, num, used_nums)
    return


def bfs(graph, start_num):
    used_nums = {start_num}
    li = [start_num]
    print(start_num, end=' ')
    i = 0
    len_keys = len(graph.keys())
    while len(li) != len_keys: # 조건에서의 에러로 생각됨
        for num in graph[start_num]:
            if num not in used_nums:
                used_nums.add(num)
                li.append(num)
                print(num, end=' ')
        i += 1
        start_num = li[i]


graph = dict()
li = []

rng, step, start = map(int, input().split())
for _ in range(step): li.append(list(map(int, input().split())))
for connect in li:
    if connect[0] not in graph: graph[connect[0]] = []
    if connect[1] not in graph: graph[connect[1]] = []
    graph[connect[0]].append(connect[1])
    graph[connect[1]].append(connect[0])
for key in graph.keys(): graph[key].sort()

dfs(graph, start)
print()
bfs(graph, start)
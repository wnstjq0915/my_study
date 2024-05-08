def dfs(graph, start_num, used_nums = set()):
    if start_num not in used_nums:
        print(start_num, end=' ')
        used_nums.add(start_num)
    if len(graph.keys()) == len(used_nums):
        return
    for num in graph[start_num]:
        if num not in used_nums:
            dfs(graph, num, used_nums)
    return used_nums


# 큐구조로 수정하기
def bfs(graph, start_num, used_nums):
    if len(graph.keys()) == len(used_nums):
        return
    li = list()

    for num in graph[start_num]:
        if num not in used_nums:
            print(num, end=' ')
            li.append(num)
            used_nums.add(num)
    for num in li:
        bfs(graph, num, used_nums)


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
for key in graph.keys(): graph[key].sort()

nums_kind.update(set(graph.keys()))

dfs(graph, start)
print()

print(start, end=' ')
bfs(graph, start, {start})
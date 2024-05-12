def dfs(graph, v, visited=set()):
    print(v, end=' ')
    visited.add(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    queue = [start]
    visited = {start}
    print(start, end=' ')
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(neighbor, end=' ')

graph = {}
rng, step, start = map(int, input().split())
for _ in range(step):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

for key in graph:
    graph[key].sort()

dfs(graph, start)
print()
bfs(graph, start)

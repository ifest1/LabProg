import queue
vertex, origin, destiny = [int(n) for n in input().split()]
graph = {new_list: [] for new_list in range(1, vertex+1)}
edges = []
print(graph)
for i in range(vertex-1):
    v1, v2, weight = [int(n) for n in input().split()]
    edges.append((v1, v2, weight))
    graph[v1].append(v2)
    graph[v2].append(v1)


def BFS():
    q = queue.Queue()
    visiteds = [origin]
    q.put(origin)
    flag = True
    stack = []

    while not q.empty():
        if flag:
            v = q.get()
            stack.append(v)
        if v == destiny:
            return stack

        if v not in graph:
            flag = False
            v = stack.pop()
            continue

        else:
            flag = True

        for w in graph[v]:
            if w not in visiteds:
                visiteds.append(w)
                q.put(w)


print(BFS())

import heapq

vertex, origin, destiny = [int(n) for n in input().split()]
graph = {new_list: [] for new_list in range(1, vertex+1)}

for i in range(vertex-1):
    v1, v2, weight = [int(n) for n in input().split()]
    graph[v1].append((v2, weight))
    graph[v2].append((v1, weight))

def djikstra(graph, source, destiny):
    distances = {ilhas: float("inf") for ilhas in graph}
    distances[source] = 0
    pq = [(source, 0)]

    while pq:
        current, current_distance = heapq.heappop(pq)
        if current_distance > distances[current]: continue

        for i in graph[current]:

            tentative = distances[current] + i[1]

            if tentative < distances[i[0]]:
                distances[i[0]] = tentative
                heapq.heappush(pq, (i[0], tentative))

    return distances[destiny]


print(djikstra(graph, origin, destiny))




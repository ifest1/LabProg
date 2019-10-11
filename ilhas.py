import heapq

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


def main():
    ilhas, fibras = [int(n) for n in input().split()]
    distances = []
    graph = {new_list: [] for new_list in range(1, ilhas + 1)}

    for i in range(fibras):
        v1, v2, ping = [int(n) for n in input().split()]
        graph[v1].append((v2, ping))
        graph[v2].append((v1, ping))

    server = int(input())

    for i in graph:
        if i != server:
            distances.append(djikstra(graph, i, server))
    
    print(max(distances) - min(distances)) 

main()



#!/usr/bin/python
 # -*- coding: utf-8 -*-
map_ = {}
def createMap():
    i = int(input("Quantidade de países: "))
    for i in range(i):
        country = input("Digite o nome do %d país: " %(i+1))
        map_[country] = []
        print("Digite o nome dos países vizinhos: \t(-1 para sair): ")
        while True:
            neighbour = input()
            if neighbour == "-1":
                break
            map_[country].append(neighbour)

def checkNeighbours(nodes, color, colors):
        return all(color != colors.get(n) for n in nodes)

def minColors(map_):
    colors = {}
 
    for country, neighbours in map_.items():
        found_color = False
        for color in range(1, 4):
            if checkNeighbours(neighbours, color, colors):
                found_color = True
                colors[country] = color
                break
 
        if not found_color:
            return None

    return max(colors.values())

createMap()
print(minColors(map_))


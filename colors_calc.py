#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Entrada:
1) QUANTIDADE DE PAÍSES
2) PAÍS E OS VIZINHOS (A PRIMEIRA LETRA É REFERENTE AO PAÍS O RESTO SÃO OS VIZINHOS)

Exemplo de entrada:
6		
A B C D
B A D E F
C A D
D C A B
E B
F B
'''
def createMap():
    graph = {}
    i = int(input())
    for i in range(i):
        temp = input().split(' ')
        country = temp[0]
        del temp[0]
        graph[country] = temp
    return graph

def getGrades(graph):
    grades = {}
    for country in graph:
        grades[country] = len(graph[country])
    return grades

def nextNode(graph, grades, colored, availableColors):
    maxGrade = 0
    adjacentColors = 0
    maxNode = None
    colors = []

    for key, value in grades.items():
        painted = 0
        if maxGrade <= value:
            colors = availableColors.copy()
            painted += getAdjacentColor(graph, key, colored, colors)
            if adjacentColors <= painted:
                maxGrade = value
                maxNode = key

    return [maxNode, colors[0]]

def getAdjacentColor(graph, key, colored, colors):
    painted = 0
    for nb in graph[key]:
        if nb in colored:
            painted += 1
            try:
                index = colors.index(colored[nb])
                del colors[index]
            except:
                pass

    return painted

def color(graph):
    colors = [1, 2, 3, 4]
    colored = {}
    grades = getGrades(graph)
    while grades:
        currentNode, color = nextNode(graph, grades, colored, colors)
        colored[currentNode] = color
        del grades[currentNode]
    return colored

def main():
    graph = createMap() 
    print(color(graph))
    values = color(graph).values()
    print("Número de cores: ")
    print(max(values))

main()


    

import math
import statistics

def getCuts(rets):
    greater = 0
    index = 0
    ordered = sorted(rets)

    for i in range(0, len(ordered)):
        if i > 0 and (greater < ordered[i] - ordered[i-1]):
            greater = ordered[i] - ordered[i-1]
            index = i

    smallers, greaters = ordered[:index], ordered[index:]
    if len(smallers) > 0:
        return (statistics.median(smallers), greaters)
    return None

def cutPaper(height, paper):
    pieces = 2
    mountain = 0
    for i in range(1, len(paper)):
        if (i + 1) <= len(paper):
            if (paper[i] <= height) and (paper[i-1] > height):
                mountain += 1
            if (paper[i] <= height) and (paper[i+1] > height):
                mountain += 1
        if mountain == 2:
            pieces += 1
            mountain = 0

    return pieces

def main():
    n = int(input())
    paper = [int(i) for i in input().split()]
    result = (0, paper)
    best_cut = 0
    while result:
        result = getCuts(result[1])
        if result is not None:
            cut = cutPaper(result[0], paper)
            if cut > best_cut: best_cut = cut
    print(best_cut)
main()


def subsets(remaining, size = 2, current_set = '', sets = []):
    if not size:
        sets.append(current_set)
        return

    elif remaining:
        subsets(remaining[1:], size - 1, current_set + remaining[0])
        subsets(remaining[1:], size, current_set)
    
    return sets

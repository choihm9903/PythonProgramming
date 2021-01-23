def max_score(scorelist):
    max = scorelist[0]
    for score in scorelist:
        if score > max:
            max = score
    return max

def min_score(scorelist):
    min = scorelist[0]
    for score in scorelist:
        if score < min:
            min = score
    return min

def gap_score(scorelist):
    gap = max_score(scorelist) - min_score(scorelist)
    return gap

math_score = [45, 66, 70, 83, 50, 77, 87, 92, 73, 89]
print(gap_score(math_score))

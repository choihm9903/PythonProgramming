def max_score(scorelist):
    max = scorelist[0]
    for score in scorelist:
        if score > max:
            max = score
    return max

math_score = [45, 66, 70, 83, 50, 77, 87, 92, 73, 89]
print(max_score(math_score))

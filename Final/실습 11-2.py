list_fruit = ["apple","banana","tomato"]
list_animal = ["bear","elephant","monkey"]
list_instrument = ["guitar","piano","harmonica"]

def length(wordlist):
    sum = 0
    for word in wordlist:
        sum += len(word)
    return sum

print(length(list_fruit))
print(length(list_animal))
print(length(list_instrument))

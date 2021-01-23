def longest(str1, str2, str3):
    longest = str1
    if (len(longest) < len(str2)):
        longest = str2
    if (len(longest) < len(str3)):
        longest = str3
    return longest

def shortest(str1, str2, str3):
    shortest = str1
    if (len(shortest) > len(str2)):
        shortest = str2
    if (len(shortest) > len(str3)):
        shortest = str3
    return shortest

print(longest("one", "second", "three"))
print(shortest("one", "second", "three"))

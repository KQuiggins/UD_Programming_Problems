""" What are all of the letters that never appear consecutively in an English word? For example, we know that “U” isn’t an answer, because of the word VACUUM, and we know that “A” isn’t an answer, because of “AARDVARK”, but which letters never appear consecutively? """


with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mySet = set()
    result = []
    
    for word in words:
        for x in word:
            if x + x in word:
                mySet.add(x)

    for i in letters:
        if i not in mySet:
            result.append(i)
print(result)


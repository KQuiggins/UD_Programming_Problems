""" What is the longest word that contains no vowels? """

with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    temp = []
    for word in words:
        if 'A' not in word and 'E' not in word and 'I' not in word and 'O' not in word and 'U' not in word:
            temp.append(word)
            found = max(temp, key=len)
    print(found)

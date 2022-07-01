""" What are all of the words with no vowel and not even a Y? """

with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    for word in words:
        if 'A' in word or 'E' in word or 'I' in word or 'O' in word or 'U' in word or 'Y' in word:
            continue
        else:
            print(word)
            
""" What is the shortest word that contains all 5 vowels? """

temp = []


with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    for word in words:
        if 'A' in word and 'E' in word and 'I' in word and 'O' in word and 'U' in word:
            temp.append(word)

    result = min(temp, key=len)
    print(result)

# print(temp)

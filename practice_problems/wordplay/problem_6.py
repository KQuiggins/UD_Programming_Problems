""" What are all of the words that have a B and an X and are less than 5 letters long? """


with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    for word in words:
        if "B" in word and "X" in word and len(word) < 5:
            print(word)
            
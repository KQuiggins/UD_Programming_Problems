# What are all of the words that have no E or A and are at least 15 letters long?

with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    for word in words:
        if 'E' and 'A' not in word and len(word) >= 15:
            print(word)
        
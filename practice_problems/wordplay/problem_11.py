""" Create and print an array containing all of the words that end in "GHTLY" """

found = []

with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    for word in words:
        if word.endswith('GHTLY'):
            found.append(word)

print(found)

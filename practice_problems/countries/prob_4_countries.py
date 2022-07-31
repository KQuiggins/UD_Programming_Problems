""" What is the shortest country name? Make sure your solution can handle ties. """

with open('countries.txt', 'r') as f:
    words = f.read().splitlines()

    shortest_word = words[0]
    ties = []
    #print(shortest_word)
    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word
            ties = []
        elif len(word) == len(shortest_word):
            ties.append(word)
    print(ties)
    print(shortest_word)

""" What are all of the words that both start with a “TH” and end with a “TH”? """

with open('sowpods.txt') as f:
    words = f.read().splitlines()

    for word in words:
        if word.lower().startswith('th') and word.lower().endswith('th'):
            print(word)
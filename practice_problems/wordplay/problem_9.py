""" What are all of the words that have all 5 vowels, in alphabetical order? """

with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    word_list = []
    for word in words:
        if "A" in word and "E" in word and "I" in word and "O" in word and "U" in word:
            word_list.append(word)
    print(sorted(word_list))
            
        
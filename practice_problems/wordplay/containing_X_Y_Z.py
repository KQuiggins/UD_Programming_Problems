# what are all the words containing X, Y, Z?

with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    for word in words:
        if 'X' in word and 'Y' in word and 'Z' in word:
            print(word)
            print('\n')
        else:
            continue

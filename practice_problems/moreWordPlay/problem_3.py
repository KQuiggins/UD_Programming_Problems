""" What are all of the words that have only “E”s for vowels and are at least 15 letters long? """

vowels = ['A', 'U', 'I', 'O']
target = 'E'
temp = []


with open('sowpods.txt', 'r') as f1:
    words = f1.read().splitlines()

    for word in words:
        if target in word and len(word) >= 15:
            temp.append(word)
            #print(temp)
    
    for word in temp:
        flag = False
        for letter in vowels:
            if letter in word:
                flag = True
                break
        if flag == False:
            print(word)

       
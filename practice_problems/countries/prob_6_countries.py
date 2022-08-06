""" There is at least one country name that contains another country name. Find all of these cases. """

with open('countries.txt', 'r') as f:
    words = f.read().splitlines()

    current_word = words[0]
    current_index = 0
    temp = []

    for i in range(1, len(words)):
        #print(words[i])
        if current_word in words[i]:
            #print(words[i])
            temp.append(current_word)
            current_index += 1
            
        else:
            current_index += 1
            current_word = words[current_index]

            
        
    print(temp)
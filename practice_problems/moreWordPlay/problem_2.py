""" What are all of the words that have only “U”s for vowels? """


vowels = ['A', 'E', 'I', 'O']
target = 'U'
temp = []


with open('sowpods.txt', 'r') as f1:
    names = f1.read().splitlines()

    for name in names:
        if target in name:
            temp.append(name)
    
            
    
    for name in temp:
        vowels_in_name = False
        for letter in vowels:
            if letter in name:
                vowels_in_name = True
                break
        if vowels_in_name == False:
            print(name)




                
        

    
""" What is the shortest baby name in the top 40 baby names for 2020? """

with open('bNames2020.txt', 'r') as f:
    names = f.read().splitlines()

    temp = []
    shortest = len(names[0])
    
    for name in names:
        if len(name) < shortest:
            shortest = len(name)
            temp.append(name)
    print(temp)

        
with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mySet = set()
    result = []
    
    for word in words:
        for x in word:
            if x not in mySet and x + x in word:
                mySet.add(x)

    for i in letters:
        if i not in mySet:
            result.append(i)
print(result)



""" What are the longest baby names in the top 40 baby names for 2020? Make sure you can handle if there’s a tie. """

with open('bNames2020.txt', 'r') as f:
    names = f.read().splitlines()

    
    ties = []
    longest = names[0]

    for name in names:
        if len(name) > len(longest):
            longest = name
        elif len(name) == len(longest):
            ties.append(name)

    for tie in ties:
        if len(tie) == len(longest):
            print(tie)

print(longest)
    

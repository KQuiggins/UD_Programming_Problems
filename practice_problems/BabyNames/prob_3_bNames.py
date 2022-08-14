""" There is at least one baby name from the top 40 baby names for 2020 that, when spelled backwards, is a valid Scrabble word. Find and print all such names. """

with open('bNames2020.txt', 'r') as f:
    names = f.read().splitlines()
    
    for i in range(len(names)):
        for j in names
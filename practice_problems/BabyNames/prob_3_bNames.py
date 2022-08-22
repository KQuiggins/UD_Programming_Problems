import requests

""" There is at least one baby name from the top 40 baby names for 2020 that, when spelled backwards, is a valid Scrabble word. Find and print all such names. """

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
r = requests.get(url = URL)

with open('bNames2020.txt', 'r') as f:
    names = f.read().splitlines()
    
    for i in range(len(names)):
        rev = names[i][::-1].lower()
        r = requests.get(url = URL + rev)
        if r.status_code == 200:
            print(names[i], rev)
        
        
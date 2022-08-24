import requests
from time import process_time

""" There is at least one baby name from the top 40 baby names for 2020 that, when spelled backwards, is a valid Scrabble word. Find and print all such names. """

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
r = requests.get(url = URL)
found_words = set()

with open('bNames2020.txt', 'r') as f:
    names = f.read().splitlines()
    
    start = process_time()  # start timer

    for i in range(len(names)):
        rev = names[i][::-1].lower()
        r = requests.get(url = URL + rev)
        if r.status_code == 200:
            found_words.add(rev)
            found_words.add(names[i])
        
    end = process_time() # end timer

    print(end, start) # print start and end times
    print(end-start) # print time difference

    print(found_words)
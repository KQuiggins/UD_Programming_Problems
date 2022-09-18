import requests
from time import process_time

""" There is at least one baby name from the top 40 baby names for 2020 that, when spelled backwards, is a valid Scrabble word. Find and print all such names. """

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
r = requests.get(url=URL)
found_words = []

with open('bNames2020.txt', 'r') as f:
    names = f.read().splitlines()

    start = process_time()  # start timer

    for i in range(len(names)):
        rev = names[i][::-1].lower()
        r = requests.get(url=URL + rev)
        if r.status_code == 200:
            found_words.append(rev)
            found_words.append(names[i])

    end = process_time()  # end timer

    print(f"Time Started: {start}")  # print start and end times
    print(f"Time Ended: {end}")
    total_time = start - end
    print(f"Total time to process request using a list: {total_time}")  # print time difference
    print(f"Names found when spelled backwards that are valid scrabble words: {found_words}")

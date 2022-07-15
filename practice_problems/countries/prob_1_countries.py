""" What are all of the countries that have “United” in the name? """

with open('countries.txt') as f:
    words = f.read().splitlines()
    found = [word for word in words if "United" in word]

print(found)
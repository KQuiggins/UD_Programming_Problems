""" There is at least one country name that contains another country name. Find all of these cases. """

with open('countries.txt', 'r') as f:
    words = f.read().splitlines()
""" What are all of the words that both start and end with a Y? """

with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    print([word for word in words if word.startswith('Y') and word.endswith('Y')])
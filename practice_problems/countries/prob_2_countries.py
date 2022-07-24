""" What countries both begin and end with a vowel? """

vowels = ["A", "E", "I", "O", "U"]

with open('countries.txt', 'r') as f:
    words = f.read().splitlines()

    for word in words:
        if word[0].upper() in vowels and word[-1].upper() in vowels:

            print(word)
        

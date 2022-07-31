""" What countries use only one vowel in their name (the vowel can be used multiple times) """

def vowel_count(word):
    vowels = 'aeiou'
    vowel_set = set()
    for letter in word:
        if letter in vowels:
            vowel_set.add(letter)
    return vowel_set
    
    



with open('countries.txt', 'r') as f:
    words = f.read().splitlines()
    
    
    for word in words:
        lower_word = word.lower()
        if len(vowel_count(lower_word)) == 1:
            print(word)
            
        

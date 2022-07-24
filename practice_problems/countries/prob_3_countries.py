""" What country names are > 50% vowels? """

def vowel_count(word):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    lower_word = word.lower()
    for i in lower_word:
        if i in vowels:
            count += 1
    return count

print(vowel_count("hello"))


temp = []

with open('countries.txt', 'r') as f:
    words = f.read().splitlines()
    for word in words:
        v_count = vowel_count(word)
        if v_count > len(word) / 2:
            temp.append(word)

print(temp)





    
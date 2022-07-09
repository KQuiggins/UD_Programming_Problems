""" What is the longest palindrome? """

with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()

    temp = []
    for word in words:
        if word == word[::-1]:
            temp.append(word)
    longest_palindrome = max(temp, key=len)
    print(f"The longest palindrome is {longest_palindrome}!")

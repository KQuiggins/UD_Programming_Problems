"""  Start of setting up storage to use during a for loop, including counters and arrays """

""" How many words contain the substring "TYPE”? """

with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    count = 0
    for word in words:
        if "TYPE" in word:
            count += 1
            continue
    print(count)
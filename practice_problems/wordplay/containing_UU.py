# What are all of the words containing UU?

with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    print([word for word in words if 'UU' in word])

# what are all the word with Q but not U?

with open('sowpods.txt', 'r') as f:
    words = f.read().splitlines()
    print([word for word in words if "Q" in word and "U" not in word])
    
    
    
""" Which of the letters Q, X, and Z is the least common? """
q_count = 0
y_count = 0
z_count = 0

with open('sowpods.txt', 'r') as f:

    words = f.read().splitlines()
    for word in words:
        if 'Q' in word:
            q_count += 1
        if 'Y' in word:
            y_count += 1
        if 'Z' in word:
            z_count += 1
    if q_count < y_count and q_count < z_count:
        print("'Q' is the least frequent letter.")
    elif y_count < q_count and y_count < z_count:
        print("'Y' is the least frequent letter.")
    else:
        print("'Z' is the least frequent letter.")

    print(f"'Q' count is {q_count}.")
    print(f"'Y' count is {y_count}.")
    print(f"'Z' count is {z_count}.")
        

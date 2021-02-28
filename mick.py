def max_me(lst):
    big = float('-inf')
    for i in lst:
        if i > big:
            big = i
    print(big)

def max_of_three(n, m, t):
    if n >= m and n >= t:
        return n
    elif m > t:
        return m
    else:
        return t


print(max_of_three(3, 10, 15))

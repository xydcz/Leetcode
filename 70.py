def cs(n):
    if n <= 2:
        return n
    a = 1
    b = 2
    for i in range(3, n+1):
        b, a = a+b, b
    return b


print(cs(6))
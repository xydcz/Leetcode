
def trace(num):
    s = 0
    for i in num:
        m = min(i)
        s += m
    print(s)


num = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
trace(num)
def trace(num):
    dp = [[0]*len(num[-1])] * len(num)
    dp[-1] = num[-1]
    for i in range(len(num)-2, -1, -1):
        for j in range(len(num[i])):
            dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + num[i][j]
    return dp[0][0]


num = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
a = trace(num)
print(a)

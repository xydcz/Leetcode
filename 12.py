def uniquePaths(m, n):
    dp = [[1] * m] * n
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            if i >= 0 and j >= 0:
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
    return dp[0][0]



m = 7
n = 3
print(uniquePaths(m, n))
return字符串
def lengthoflongsubstring(s):
    res = ''
    for i in range(1, len(s)):
        dic = {}
        for j in range(i, -1, -1):
            if s[j] not in dic:
                dic[s[j]] = 1
                if len(s[j:i+1]) > len(res):
                    res = s[j:i+1]
            else:
                break
    return res


s = 'aab'
print(lengthoflongsubstring(s))
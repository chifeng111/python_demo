# coding: utf-8
''' 
        给定两个字符串str1 和str2，返回两个字符串的最长公共子串。
    str1="1AB2345CD"，str2="12345EF"，返回"2345"。
'''

def getDp(str1, str2):
    row, col = len(str1), len(str2)
    dp = [[0 for i in range(col)] for j in range(row)]
    for i in range(row):
        if str1[i] == str2[0]:
            dp[i][0] = 1
    for i in range(col):
        if str1[0] == str2[i]:
            dp[0][i] = 1
    for i in range(1, row):
        for j in range(1, col):
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
    return dp

def getLCST(str1, str2, dp):
    end, _max = 0, 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if dp[i][j] > _max:
                _max, end = dp[i][j], i
    return str1[end-_max+1:end+1]
    
    
if __name__ == '__main__':
    str1, str2 = '1AB2345CD', '12345EF'
    dp = getDp(str1, str2)
#     for i in dp:
#         print(i)
    print(getLCST(str1, str2, dp))

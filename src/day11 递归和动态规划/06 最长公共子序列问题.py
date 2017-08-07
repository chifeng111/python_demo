# coding: utf-8
from numpy import array

def getDp(str1, str2):
    row, col = len(str1), len(str2)
    dp = array([[0 for c in range(col)] for r in range(row)])
    for i in range(row):
        if str1[i] == str2[0]:
            dp[i:,0] = 1; break
    for i in range(col):
        if str1[0] == str2[i]:
            dp[0,i:] = 1; break
    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if str1[i] == str2[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
    return dp

def getLCSE(str1, str2, dp):
    row, col = len(str1)-1, len(str2)-1
    res = []
    while row>=0 and col>=0:
        # if row == 0 and col == 0 and dp[row][col] == 1:
        #     res.append(str1[row])
        if dp[row][col] == dp[row-1][col] and row > 0:
            row -= 1
        elif dp[row][col] == dp[row][col-1] and col > 0:
            col -= 1
        else:
            res.append(str1[row]); row -= 1; col -= 1
    return res[::-1]



if __name__ == '__main__':
    # str1, str2 = 'ABCDE', 'BADEF'
    str1, str2 = '1A2C3D4B56', 'B1D23CA45B6A'
    getDp(str1, str2)
    dp = getDp(str1, str2)
    print(getLCSE(str1, str2, dp))


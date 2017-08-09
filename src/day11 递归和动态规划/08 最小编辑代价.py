# coding: utf-8
'''
给定两个字符串str1 和str2，再给定三个整数ic、dc 和rc，分别代表插入、删除和替
换一个字符的代价，返回将str1 编辑成str2 的最小代价。
'''


def minCost(str1, str2, ic, dc, rc):
    row, col = len(str1), len(str2)
    dp = [[0 for i in range(col + 1)] for j in range(row + 1)]
    for i in range(row + 1):
        dp[i][0] = dc * i
    for i in range(col + 1):
        dp[0][i] = ic * i
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if str1[i - 1] != str2[j - 1]:
                dp[i][j] = min(dc + dp[i - 1][j], ic + dp[i]
                               [j - 1], rc + dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dc + dp[i - 1][j], ic + dp[i]
                               [j - 1], dp[i - 1][j - 1])
#     return dp
    return dp[row][col]


if __name__ == '__main__':
    str1, str2 = "ab12cd3", "abcdf"
#     str1, str2 = "abc", "adc"
    ic, dc, rc = 5, 3, 2
    print(minCost(str1, str2, ic, dc, rc))

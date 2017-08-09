# coding: utf-8


def isCross(str1, str2, aim):
    if len(aim) != len(str1) + len(str2):
        return False
    row, col = len(str1), len(str2)
    dp = [[0 for c in range(col + 1)] for r in range(row + 1)]
    dp[0][0] = 1
    for i in range(1, row + 1):
        if str1[i - 1] == aim[i - 1]:
            dp[i][0] = 1
    for i in range(1, col + 1):
        if str2[i - 1] == aim[i - 1]:
            dp[0][i] = 1
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if dp[i][j - 1] and str2[j - 1] == aim[i + j - 1]:
                dp[i][j] = 1
            elif dp[i - 1][j] and str1[i - 1] == aim[i + j - 1]:
                dp[i][j] = 1
#     return dp
    if dp[row][col]:
        return True
    else:
        return False


if __name__ == '__main__':
    str1, str2, aim = "AB", "12", "12BA"
    print(isCross(str1, str2, aim))

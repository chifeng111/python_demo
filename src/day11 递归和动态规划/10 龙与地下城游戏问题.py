# coding: utf-8
'''
    给定一个二维数组map，含义是一张地图，例如，如下矩阵：
    -2 -3 3
    -5 -10 1
    0 30 -5
    游戏的规则如下：
     骑士从左上角出发，每次只能向右或向下走，最后到达右下角见到公主。
     地图中每个位置的值代表骑士要遭遇的事情。如果是负数，说明此处有怪兽，要
    让骑士损失血量。如果是非负数，代表此处有血瓶，能让骑士回血。
     骑士从左上角到右下角的过程中，走到任何一个位置时，血量都不能少于1。
    为了保证骑士能见到公主，初始血量至少是多少？根据map，返回初始血量。
'''


def minHP(m):
    if len(m) == 0:
        return 1
    row, col = len(m), len(m[0])
    dp = [[0 for c in range(col)] for r in range(row)]
    dp[row - 1][col - 1] = max(1, 1 - m[row - 1][col - 1])
    for i in range(row - 1, -1, -1):
        for j in range(col - 1, -1, -1):
            if i == row - 1 and j == col - 1:
                continue
            elif j == col - 1:
                dp[i][j] = max(1, dp[i + 1][j] - m[i][j])
            elif i == row - 1:
                dp[i][j] = max(1, dp[i][j + 1] - m[i][j])
            else:
                dp[i][j] = min(
                    max(1, dp[i][j + 1] - m[i][j]),
                    max(1, dp[i + 1][j] - m[i][j])
                )
    return dp[0][0]


if __name__ == '__main__':
    m = [[-2, -3, 3], [-5, -10, 1], [0, 30, -5]]
    print(minHP(m))

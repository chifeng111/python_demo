# coding: utf-8
'''N 皇后问题是指在NN 的棋盘上要摆N 个皇后，要求任何两个皇后不同行、不同列，
也不在同一条斜线上。给定一个整数n，返回n 皇后的摆法有多少种。'''


def Nqueens(n):
    if n < 1:
        return 0
    record = [-1 for i in range(n)]
    return process(0, record, n)


def process(i, record, n):
    if i == n:
        return 1
    res = 0
    for j in range(n):
        if isValid(record, i, j):
            record[i] = j
            res += process(i + 1, record, n)
    return res


def isValid(record, i, j):
    for k in range(i):
        if j == record[k] or abs(record[k] - j) == abs(i - k):
            return False
    return True


if __name__ == '__main__':
    print(Nqueens(8))
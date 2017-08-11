# coding: utf-8
'''给定一个整型数组arr，代表数值不同的纸牌排成一条线。玩家A 和玩家B 依次拿走
每张纸牌，规定玩家A 先拿，玩家B 后拿，但是每个玩家每次只能拿走最左或最右的纸牌，
玩家A 和玩家B 都绝顶聪明。请返回最后获胜者的分数。'''


def win(arr):
    if len(arr) == "":
        return 0
    return max(f(arr, 0, len(arr) - 1), s(arr, 0, len(arr) - 1))


def f(arr, i, j):
    if i == j:
        return arr[i]
    else:
        return max(arr[i] + s(arr, i + 1, j), arr[j] + s(arr, i, j - 1))


def s(arr, i, j):
    if i == j:
        return 0
    else:
        return min(f(arr, i + 1, j), f(arr, i, j - 1))


if __name__ == '__main__':
    arr = [1, 100, 2]
#     arr = [1, 2, 100, 4]
    print(win(arr))

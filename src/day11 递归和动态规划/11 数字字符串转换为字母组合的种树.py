# coding: utf-8


def fun(s):
    n = len(s)
    p = [0 for i in range(n)]  # p[i]代表以i开头后面数字转换为字母的组合数
    p.append(1)  # 后面加一个1，是为了使倒数第二个元素赋值时不报错，减少elif的使用
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            if s[i] == '0':
                p[i] = 0
            else:
                p[i] = 1
        else:
            if s[i] == '0':
                p[i] = 0
            elif int(s[i:i + 2]) > 26:
                p[i] = p[i + 1]
            else:
                p[i] = p[i + 2] + p[i + 1]
#     return p
    return p[0]


if __name__ == '__main__':
    s = "11"
#     s = "1111"
    print(fun(s))

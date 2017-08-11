# coding: utf-8
'''
给定一个只由0（假）、1(真)、&(逻辑与)、|（逻辑或）和^(异或)五种字符组成的字符
串express，再给定一个布尔值desired。返回express 能有多少种组合方式，可以达到desired
的结果。
'''


def isValid(express):
    if len(express) % 2 == 0:
        return False
    for i in range(len(express)):
        if i % 2 == 0:
            if express[i] not in ['0', '1']:
                return False
        else:
            if express[i] not in ['&', '|', '^']:
                return False
    return True


def fun(express, desired):
    if not isValid(express):
        return 0
    else:
        return p(express, desired, 0, len(express) - 1)


def p(express, desired, l, r):
    if l == r:
        if express[l] == '1' and desired:
            return 1
        elif express[l] == '0' and not desired:
            return 1
        else:
            return 0
    res = 0
    if desired == True:
        for i in range(l + 1, r, 2):
            if express[i] == '&':
                res += p(express, True, l, i - 1) * p(express, True, i + 1, r)
            elif express[i] == '|':
                res += p(express, True, l, i - 1) * p(express, True, i + 1, r)
                res += p(express, True, l, i - 1) * p(express, False, i + 1, r)
                res += p(express, False, l, i - 1) * p(express, True, i + 1, r)
            elif express[i] == '^':
                res += p(express, True, l, i - 1) * p(express, False, i + 1, r)
                res += p(express, False, l, i - 1) * p(express, True, i + 1, r)
    else:
        for i in range(l + 1, r, 2):
            if express[i] == '&':
                res += p(express, False, l, i - 1) * p(express, True, i + 1, r)
                res += p(express, True, l, i - 1) * p(express, False, i + 1, r)
            elif express[i] == '|':
                res += p(express, False, l, i - 1) * \
                    p(express, False, i + 1, r)
            elif express[i] == '^':
                res += p(express, True, l, i - 1) * p(express, True, i + 1, r)
                res += p(express, False, l, i - 1) * \
                    p(express, False, i + 1, r)
    return res


if __name__ == '__main__':
    express, desired = '1^0|0|1', False
#     print(isValid(express))
    print(fun(express, desired))

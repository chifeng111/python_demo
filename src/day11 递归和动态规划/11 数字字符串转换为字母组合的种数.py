# coding: utf-8
'''
    给定一个字符串str，str 全部由数字字符组成，如果str 中某一个或某相邻两个字符组
    成的子串值在1~26 之间，则这个子串可以转换为一个字母。规定"1"转换为"A"，"2"转换
    为"B"，"3"转换为"C"..."26"转换为"Z"。写一个函数，求str 有多少种不同的转换结果，并
    返回种数。
    
    str="1111"。
    能转换出的结果有"AAAA"、"LAA"、"ALA"、"AAL"和"LL"，返回5。
    
    str="01"。
    "0"没有对应的字母，而"01"根据规定不可转换，返回0。
    
    str="10"。
    能转换出的结果是"J"，返回1。
'''


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

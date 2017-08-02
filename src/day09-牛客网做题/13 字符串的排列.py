# coding: utf-8
def pringSubString(s):
    if len(s) == 1:
        print(s)
    for i in divideTwo(s):
        print(i[0]+pringSubString(i[1]))

def divideTwo(s):
    l = []
    for i in range(len(s)):
        ss = list(s)
        ss[0], ss[i] = ss[i], ss[0]
        ss = "".join(ss)
        l.append((ss[0], ss[1:]))
    return list(set(l))

if __name__ == '__main__':
    s = 'abc'
    print(divideTwo(s))


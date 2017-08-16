# coding: utf-8
'''
{0x00, 0x01},
{0x02, 0x03},
{0x03, 0x04},
{0x05, 0x06}
'''
import sys


def AddDependency(m1, m2, _map):
    if m1 not in _map:
        _map[m1] = [m2]
    else:
        _map[m1].append(m2)
    if m2 not in _map:
        _map[m2] = []


def ModulesCycleDependency(m, _map):
    d = _map[m]
    if not d:
        return False
    if m in d:
        return True
    while d:
        v = d.pop()
        if ModulesCycleDependency(v, _map):
            return True
    return False


def myprint(dependencyMap):
    k = dependencyMap.keys()
    k = list(k)
    for i in range(len(k) - 1):
        if dependencyMap[k[i]]:
            print("{" + "{}, {}".format(k[i], 'true') + "},")
        else:
            print("{" + "{}, {}".format(k[i], 'false') + "},")
    if dependencyMap[k[len(k) - 1]]:
        print("{" + "{}, {}".format(k[len(k) - 1], 'true') + "}")
    else:
        print("{" + "{}, {}".format(k[len(k) - 1], 'false') + "}")


if __name__ == '__main__':
    _map = {}
    while True:
        s = sys.stdin.readline().strip()
        if s[-1] != ",":
            m1, m2 = s[1:-1].split(",")[0], s[1:-1].split(",")[1]
            m2 = m2[1:]
            AddDependency(m1, m2, _map)
            break
        else:
            m1, m2 = s[1:-2].split(",")[0], s[1:-2].split(",")[1]
            m2 = m2[1:]
            AddDependency(m1, m2, _map)
    dependencyMap = {}
    for i in _map.keys():
        if ModulesCycleDependency(i, _map):
            dependencyMap[i] = True
        else:
            dependencyMap[i] = False
    myprint(dependencyMap)

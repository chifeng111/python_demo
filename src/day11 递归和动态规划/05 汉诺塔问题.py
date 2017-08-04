# coding: utf-8

def hanoi(n):
    '''
    n=1 时，打印：
    move from left to right
    
    n=2 时，打印：
    move from left to mid
    move from left to right
    move from mid to right
    '''
    if n > 0:
        fun(n, 'left', 'mid', 'right')
        
def fun(n, _from, mid, to):
    if n == 1:
        print("move from {} to {}".format(_from, to))
    else:
        fun(n-1, _from, to, mid)
        fun(1, _from, mid, to)
        fun(n-1, mid, _from, to)
        
if __name__ == '__main__':
    hanoi(2)
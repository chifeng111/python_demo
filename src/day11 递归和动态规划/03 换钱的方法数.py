# coding: utf-8

def coins(arr, aim):
    '''
    arr=[5,10,25,1]，aim=0。
        组成0 元的方法有1 种，就是所有面值的货币都不用。所以返回1。
    
    arr=[5,10,25,1]，aim=15。
        组成15 元的方法有6 种，分别为3 张5 元、1 张10 元+1 张5 元、1 张10 元+5 张1
        元 、10 张1 元+1 张5 元、2 张5 元+5 张1 元和15 张1 元。所以返回6。
    
    arr=[3,5]，aim=2。
        任何方法都无法组成2 元。所以返回0。
    '''
    if len(arr) == 0:
        return -1
    n = len(arr)
    dp = [[0 for i in range(aim+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(aim+1):
        if not i%arr[0]:
            dp[0][i] = 1
    for i in range(1, n):
        for j in range(1, aim+1):
            num, k = 0, 0
            while j-arr[i]*k >= 0:
                num += dp[i-1][j-k*arr[i]]
                k += 1
            dp[i][j] = num
#     return dp
    return dp[n-1][aim]
#     
if __name__ == '__main__':
#     arr, aim = [5,10,25,1], 15
#     arr, aim = [5,10,25,1], 0
    arr, aim = [3,5], 2
    print(coins(arr, aim))
# coding: utf-8

def minCoins(arr, aim):
    '''
    arr=[5,2,3]，aim=20。
    4 张5 元可以组成20 元，其他的找钱方案都要使用更多张的货币，所以返回4。
    
    arr=[5,2,3]，aim=0。
        不用任何货币就可以组成0 元，返回0。
    
    arr=[3,5]，aim=2。
        根本无法组成2 元，钱不能找开的情况下默认返回-1。
    '''
    if len(arr) == 0:
        return -1
    n, MAX = len(arr), 100000
    dp = [[MAX for i in range(aim+1)] for j in range(n)]
    for i in range(n):
        dp[i][0] = 0
    for i in range(aim+1):
        if not i%arr[0]:
            dp[0][i] = int(i/arr[0])
    for i in range(1, n):
        for j in range(1, aim+1):
            dp[i][j] = min(dp[i-1][j], dp[i][j-arr[i]]+1)
#     return dp
    if dp[n-1][aim] == MAX:
        return -1
    else:
        return dp[n-1][aim]

if __name__ == '__main__':
    arr, aim = [2, 3, 5], 20
    print(minCoins(arr, aim))
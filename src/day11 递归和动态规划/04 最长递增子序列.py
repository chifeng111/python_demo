# coding: utf-8
''''arr=[2,1,5,3,6,4,8,9,7]，返回的最长递增子序列为[1,3,4,8,9]。'''


def getDp(arr):
    '''dp[i]表示以arr[i]结尾的最长递增子序列的个数'''
    dp = [1 for i in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp

def generateLIS(arr, dp):
    inx = dp.index(max(dp))
    Len = dp[inx]
    lis_r = []
    lis_r.append(arr[inx])
    for i in range(inx-1, -1, -1):
        if dp[i] == Len -1 and arr[i] < arr[inx]:
            lis_r.append(arr[i])
            inx = i
            Len -= 1
    return lis_r[::-1]

if __name__ == '__main__':
    arr = [1]
#     arr = [2,1,5,3,6,4,8,9,7]
#     arr=[2,1,5,3,6,4,8,9,7,10,1,4,15,1,2,3,4,5,6,6,7,8,9]
    dp = getDp(arr)
    print(generateLIS(arr, dp))
    
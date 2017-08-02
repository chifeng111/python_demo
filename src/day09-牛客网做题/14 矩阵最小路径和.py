# coding: utf-8

def minPathSum(matrix):
    if len(matrix) == 0:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    dp = [[0 for c in range(col)] for r in range(row)]
    dp[0][0] = matrix[0][0]
    for r in range(1, row):
        dp[r][0] = dp[r-1][0] + matrix[r][0]
    for c in range(1, col):
        dp[0][c] = dp[0][c-1] + matrix[0][c]
    for r in range(1, row):
        for c in range(1, col):
            dp[r][c] = min(dp[r-1][c]+matrix[r][c], dp[r][c-1]+matrix[r][c])
    return dp[row-1][col-1]


if __name__ == '__main__':
    m = [[1]]
#     m = [[1,2]]
#     m = [[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
    print(minPathSum(m))
    
    
    
    
class Solution(object):
    def minFallingPathSum(self, A):
        if len(A) == 1:
            return min(A[0])
        
        n  = len(A)
        dp = [ [0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[0][i] = A[0][i]
        for r in range(1,n):
            for c in range(n):
                if c == 0:
                    dp[r][c] = A[r][c] + min(dp[r-1][c],dp[r-1][c+1])
                elif c == n-1:
                    dp[r][c] = A[r][c] + min(dp[r-1][c-1],dp[r-1][c])
                else:
                    dp[r][c] = A[r][c] + min(dp[r-1][c-1],dp[r-1][c],dp[r-1][c+1])
        return min(dp[-1])
        

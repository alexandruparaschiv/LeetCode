class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n_rows = len(obstacleGrid)
        n_cols = len(obstacleGrid[0])
        
        dp = [ [0]*n_cols for _ in range(n_rows)]
        
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        for i in range(n_rows):
            for j in range(n_cols):
                if obstacleGrid[i][j]:
                    continue;
                if i>0:
                    dp[i][j] += dp[i-1][j]
                if j>0:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]

# bottom-up dynamic programming solution
# use an array dp to store the minimum number
# of squares required to add up to the current number N

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        dp = [0]
        highest_square= 1
        
        if n == 1:
            return 1
        
        for i in range(1,n+1):
            if highest_square**2==i:
                squares.append(highest_square**2)
                highest_square += 1
            minsquare = dp[i-1] + 1
            
            for square in squares:
                minsquare = min(minsquare,dp[i-square]+1)
            dp.append(minsquare)
        return dp[-1]

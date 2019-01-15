# Problem 877
# dynamic programming

class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        total_piles = sum(piles)
        no_piles = len(piles)
        max_Alex = 0
        cache = [[ 0 for i in range(no_piles) ] for j in range(no_piles)]
        def helper(curr_piles,i,j):
            if cache[i][j] != 0:
                return cache[i][j]
            if i==j:
                return curr_piles[0]
            else:
                max_Alex = max(curr_piles[0]+helper(curr_piles[1:],i+1,j),curr_piles[-1]+helper(curr_piles[:-1],i,j-1))
                cache[i][j] = max_Alex
                return max_Alex
        max_Alex = helper(piles,0,len(piles)-1)
        if max_Alex > total_piles - max_Alex:
            return True
        else:
            return False

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        choices = [x for x in range(1,n+1)]
        
        if n == 0:
            return [] 
        
        def helper(remaining,temp,index,result):
            if remaining == 0:
                result.append(temp[:])
                return
            if n-index<remaining: #for pruning the search tree
                return
            if not choices:
                return
            for i in range(index,n):
                temp.append(choices[i])
                helper(remaining-1,temp,i+1,result)
                temp.pop()
                    
        helper(k,[],0,result)
        return result

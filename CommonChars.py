class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        no_letters = ord('z') - ord('a') +1
        memo = [ [0]*len(A) for _ in range(no_letters)]
        
        for i,word in enumerate(A):
            for char in word:
                memo[ord(char)-ord('a')][i] += 1
                
        letters = []
        for j in range(len(memo)):
            no_letters = min(memo[j])
            if no_letters:
                for i in range(no_letters):
                    letters.append(chr(j+ord('a')))
        return letters

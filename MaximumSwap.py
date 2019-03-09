class Solution(object):
    
    def swap(self,num,i,j):
        
        num = list(num)
        num[i],num[j] = num[j],num[i]
        return int(''.join(num))
        
        
    def maximumSwap(self, num):
        
        max_num = num
        num = str(num)
        nums = [ [0]*len(num) for _ in num]
        for i in range(len(num)-1):
            for j in range(i+1,len(num)):
                nums[i][j] = self.swap(num,i,j)
        for i in range(len(num)-1):
            for j in range(i+1,len(num)):
                max_num = max(max_num,nums[i][j])
        return max_num

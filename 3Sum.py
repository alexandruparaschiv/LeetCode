# perform a bidirectional search, store solutions in a set to avoid duplicates


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        solutions = set()
        i = 0
        while i < len(nums) - 2:
            j = i+1
            k = len(nums) - 1
            while j < k:
                target = nums[i] + nums[j] +nums[k]
                if target == 0 :
                    solutions.add((nums[i],nums[j],nums[k]))
                    if nums[j+1] == nums[j]:
                        j += 1
                    elif nums[k-1] == nums[k]:
                        k -= 1
                    else:
                        j +=1 
                if target > 0 :
                    k -= 1
                elif target < 0 :
                    j += 1
            i = i+1
        solutions = list(solutions)
        return solutions

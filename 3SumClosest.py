class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        closest = float('inf')
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1         
            while j < k:    
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == target:
                    return target
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                if curr_sum - target > 0:
                    k -= 1
                else:
                    j += 1
        return closest

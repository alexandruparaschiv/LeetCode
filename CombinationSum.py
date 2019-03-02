# simple backtracking solution to combination sum

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        all_solutions = []
        candidate_solution = []
        def helper(candidates,target):
            if target < 0:
                return 0
            elif target == 0:
                if sorted(candidate_solution) not in all_solutions:
                    all_solutions.append(sorted(candidate_solution[:]))
            else:
                for num in candidates:
                    candidate_solution.append(num)
                    helper(candidates,target-num)
                    candidate_solution.pop()
        helper(candidates,target)
        return list(all_solutions)

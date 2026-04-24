class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        solution_map = {}

        for i, j in enumerate(nums):
            diff = target - j
            if diff in solution_map:
                return [solution_map[diff], i]
            
            solution_map[j] = i
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        nums.sort()

        if len(nums) == 1:
            return 1

        for i in range(len(nums)-1):
            count = 0
            for j in range(i, len(nums)):
                if nums[i] + count == nums[j]:
                    count+=1
            
            max_count = max(max_count, count)
        
        return max_count
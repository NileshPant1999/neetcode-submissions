class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_count = 0
        num_set = set(nums)


        for num in nums:
            if (num - 1) not in num_set:
                count = 1
                while (num + count) in num_set:
                    count+=1
            
                max_count = max(max_count, count)
        
        return max_count
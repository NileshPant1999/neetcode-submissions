class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        already_present = set()
        for i in range(len(nums)):
            if nums[i] in already_present:
                return True
    
            already_present.add(nums[i])

        return False

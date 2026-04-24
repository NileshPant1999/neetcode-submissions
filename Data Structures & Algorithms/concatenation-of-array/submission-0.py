class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        final_array =[0] * (2 * n)

        for i, num in enumerate(nums):
            final_array[i] = final_array[i+n] = num
        
        return final_array
    
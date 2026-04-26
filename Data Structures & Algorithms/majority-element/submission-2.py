class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        final_dict = {}
        max_count = -1
        index = -1

        for num in nums:
            if num in final_dict:
                final_dict[num] += 1
            else:
                final_dict[num] = 1
        
        for n in final_dict.keys():
            if final_dict[n] > max_count:
                max_count = final_dict[n]
                index = n
            

        return index
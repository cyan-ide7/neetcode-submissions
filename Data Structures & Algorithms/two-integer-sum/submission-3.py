class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = target - nums[i]
            if j in nums:
                idx = nums.index(j)
                if idx != i:
                
                    if i > idx: 
                     j
                     j = i
                     i = idx 
                     idx = j  
                     
                     return [i, idx]
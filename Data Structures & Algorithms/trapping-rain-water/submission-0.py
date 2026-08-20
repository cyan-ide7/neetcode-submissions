class Solution:
    def trap(self, height: List[int]) -> int:

        left_max = 0
        right_max = 0 
        v = 0
        l= 0
        r=len(height) -1 

        while l < r :
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else :
                    v = (left_max - height[l])+ v

                l += 1

            else :
                if height[r] >= right_max:
                    right_max = height[r]
                else :
                    v = (right_max - height[r])+ v
                r-=1
        return v 
                    

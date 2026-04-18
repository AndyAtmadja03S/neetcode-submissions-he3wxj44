class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
    
        def rob1(arr):
            prev2, prev1 = 0, 0
            for n in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + n)
            return prev1
        
        return max(rob1(nums[:-1]), rob1(nums[1:]))
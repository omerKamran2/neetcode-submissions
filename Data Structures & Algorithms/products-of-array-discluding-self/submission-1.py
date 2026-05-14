class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        for x in range(0, len(nums)):
            for y in range(0, len(nums)):
                if x != y:
                    res[x] *= nums[y]
        
        return res


        
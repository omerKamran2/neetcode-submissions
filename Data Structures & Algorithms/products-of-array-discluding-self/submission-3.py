class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        pre = 1
        for x in range(len(nums)):
            out.append(pre)
            pre *= nums[x]

        post = 1
        for x in range(len(nums) - 1, -1, -1):
            out[x] *= post
            post *= nums[x]
        return out





        
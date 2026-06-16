class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()

        for x in range(0, len(nums)):
            s = target - nums[x]
            if s in h:
                return [h[s], x]
            h[nums[x]] = x
        
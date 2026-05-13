class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()

        for x, n in enumerate(nums):
            diff = target - n
            if diff in h.keys():
                return [h[diff], x]
            else:
                h[n] = x
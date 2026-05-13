class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()

        for x in range(len(nums)):
            h[nums[x]] = x
        
        for y in range(len(nums)):
            diff = target - nums[y]
            if diff in h.keys() and h[diff] != y:
                if h[diff] < y:
                    return [h[diff], y]
                else:
                    return [y, h[diff]]

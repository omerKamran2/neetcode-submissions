class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()

        for x in range(len(nums)):
            h[nums[x]] = x
        
        for y in range(len(nums)):
            target2 = target - nums[y]
            if target2 in h.keys() and h[target2] != y:
                if h[target2] < y:
                    return [h[target2], y]
                else:
                    return [y, h[target2]]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[r] <= nums[mid]:
                # pivot is in the right half
                l = mid + 1
            else:
                #pivot is in the left half
                r = mid
        
        res = self.bin_search(nums, 0, l, target)
        if res != -1:
            return res
        else:
            return self.bin_search(nums, l, len(nums) - 1, target)

        

    def bin_search(self, nums: List[int], l: int, r: int, target: int) -> int:
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1



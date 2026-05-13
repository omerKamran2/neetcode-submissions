class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()

        for x in nums:
            if x in hashmap:
                return True
            else:
                hashmap.add(x)
        
        return False
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        seq = 0

        for n in nums:
            sub_seq = 0
            while n in s:
                sub_seq += 1
                n += 1
            seq = max(sub_seq, seq)

        return seq
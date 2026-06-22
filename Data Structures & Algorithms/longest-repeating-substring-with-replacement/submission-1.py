class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = defaultdict()
        l, r = 0, 0
        maxL = 0
        maxFreq = 0
        while (r < len(s)):
            if s[r] in h.keys():
                h[s[r]] += 1
            else:
                h[s[r]] = 1

            maxFreq = max(maxFreq, h[s[r]])

            rep = (r - l + 1) - maxFreq

            if rep > k:
                h[s[l]] -= 1
                l += 1
            elif rep <= k:
                maxL = max(maxL, r - l + 1)
            
            r += 1  

        return maxL
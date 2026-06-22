class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = defaultdict()
        l, r = 0, 0
        maxL = 0
        maxFreq = 0
        while (r < len(s)):
            h[s[r]] = 1 + h.get(s[r], 0)
            maxFreq = max(maxFreq, h[s[r]])

            rep = (r - l + 1) - maxFreq

            if rep > k:
                h[s[l]] -= 1
                l += 1
            elif rep <= k:
                maxL = max(maxL, r - l + 1)
            
            r += 1  

        return maxL
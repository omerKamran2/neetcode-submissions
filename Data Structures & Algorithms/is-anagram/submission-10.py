class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        h = dict()

        for x in s:
            if x not in h:
                h[x] = 1
            else:
                h[x] += 1
        
        for y in t:
            if y in h.keys():
                if h[y] == 0:
                    return False
                else:
                    h[y] -= 1
            else:
                return False
        
        for val in h.values():
            if val > 0:
                return False

        return True

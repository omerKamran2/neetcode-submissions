class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l, r = 0, (len(s1))

        countS1 = [0] * 26
        for i in range(l, r):
            countS1[ord(s1[i]) - 97] += 1

        while (r <= len(s2)):
            countS2 = [0] * 26
            for i in range(l, r):
                countS2[ord(s2[i]) - 97] += 1
            if countS1 == countS2:
                return True
            else:
                l += 1
                r += 1

        return False
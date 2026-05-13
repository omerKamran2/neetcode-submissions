class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        l = []
        res = dict()
        for x in strs:
            h = [0]*26
            for y in x:
                h[ord(y) - ord('a')] += 1
            if tuple(h) in res.keys():
                res[tuple(h)].append(x)
            else:
                res[tuple(h)] = [x]
        
        for x in res:
            l.append(res[x])
        
        return l
class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        mapping = {')': '(', '}': '{', ']': '['}

        for x in s:
            if x in '([{':
                res.append(x)
            else:
                if len(res) == 0:
                    return False
                elif res[-1] == mapping[x]:
                    res.pop()
                else:
                    return False
        
        return len(res) == 0
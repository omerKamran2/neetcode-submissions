class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for x in s:
            if x in '([{':
                res.append(x)
            else:
                if x == ')':
                    if len(res) == 0:
                        return False
                    elif res[-1] == '(':
                        res.pop()
                    else:
                        return False
                elif x == ']':
                    if len(res) == 0:
                        return False
                    elif res[-1] == '[':
                        res.pop()
                    else:
                        return False
                elif x == '}':
                    if len(res) == 0:
                        return False
                    elif res[-1] == '{':
                        res.pop()
                    else:
                        return False
        return len(res) == 0
        
        
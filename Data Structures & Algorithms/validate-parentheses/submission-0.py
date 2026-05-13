class Solution:
    def isValid(self, s: str) -> bool:
        Map = {'}': '{', ')':'(', ']':'['}
        stack = []

        for x in s:
            if x in Map:
                if stack and stack[-1] == Map[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        
        return not stack

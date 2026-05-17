class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''

        for x in s:
            if x.isalnum():
                newStr += x.lower()

        left = 0
        right = len(newStr) - 1
        while left <= right:
            if newStr[left] != newStr[right]:
                return False
            left += 1
            right -= 1
        
        return True
            
        
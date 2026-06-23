class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [0] * len(height)
        suf = [0] * len(height)

        stack = []

        i = 0
        while i < len(height):
            if stack and stack[-1][0] < height[i]:
                pre[i] = stack[-1][0]
                stack.append([height[i], i])
            elif stack and stack[-1][0] > height[i]:
                pre[i] = stack[-1][0]
            else:    
                stack.append([height[i], i])
            i += 1
        
        i = len(height) - 1
        stack = []
        while i >= 0:
            if stack and stack[-1][0] < height[i]:
                suf[i] = stack[-1][0]
                stack.append([height[i], i])
            elif stack and stack[-1][0] > height[i]:
                suf[i] = stack[-1][0]
            else:
                stack.append([height[i], i])
            i -= 1

        tWater = 0
        for i in range(len(height)):
            water = min(suf[i], pre[i]) - height[i]
            if water > 0:
                tWater += water
        
        return tWater
            
                
            
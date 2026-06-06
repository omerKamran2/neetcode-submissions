class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxH = 0
        stack = [] # pairs of height/index

        for i, h in enumerate(heights):
            if stack and h < stack[-1][0]:
                start = i
                while stack and h < stack[-1][0]:
                    height, index = stack.pop()
                    #max height
                    maxH = max(maxH, height * (i - index))
                    start = index
                stack.append([h, start])
            else:
                stack.append([h, i])

        n = len(heights)
        for i in range(0, len(stack)):
            width = (n - stack[i][1])
            height = stack[i][0]
            maxH = max(maxH, height*width)

        return maxH
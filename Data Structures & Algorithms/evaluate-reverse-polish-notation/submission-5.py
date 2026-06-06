class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                if token == '+':
                    stack.append(stack.pop() + stack.pop())
                elif token == '-':
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif token == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(float(b)/a))
        
        return stack[0]

        
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif i == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(i))
        return stack[-1]
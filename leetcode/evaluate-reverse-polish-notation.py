class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                stack.append(int(num1)+int(num2))
            elif c == '-':
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                stack.append(int(num2)-int(num1))
            elif c == '*':
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                stack.append(int(num1)*int(num2))
            elif c == '/':
                num1 = stack[-1]
                stack.pop()
                num2 = stack[-1]
                stack.pop()
                dv = int(num2)/int(num1)
                if dv >= 0:
                    stack.append(floor(dv))
                else:
                    stack.append(ceil(dv))
            else:
                stack.append(int(c))
        return stack[0]
        
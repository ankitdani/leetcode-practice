class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # num2 / num1 for division. same for subtraction
        hset = []
        hset.append('+')
        hset.append('-')
        hset.append('*')
        hset.append('/')
        stack = []
        for token in tokens:
            if token not in hset:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                res = 0
                if token == '+':
                    res = num1 + num2
                elif token == '*':
                    res = num1 * num2
                elif token == '-':
                    res = num2 - num1
                elif token == '/':
                    res = int(num2 / num1)
                stack.append(res)
        return stack.pop()

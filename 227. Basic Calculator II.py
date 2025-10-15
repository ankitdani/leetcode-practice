class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        num = 0
        prev_opr = '+'
        stack = []

        for i, ch in enumerate(s):

            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in '+-*/' or i == len(s)-1:
                if prev_opr == '+':
                    stack.append(num)
                elif prev_opr == '-':
                    stack.append(-num)
                elif prev_opr == '*':
                    stack.append(num * stack.pop())
                elif prev_opr == '/':
                    stack.append(int(stack.pop() / num))
                
                prev_opr = ch
                num = 0
        return sum(stack)
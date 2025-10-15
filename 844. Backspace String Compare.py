class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for ch in s:
            if stack1 and ch == '#':
                stack1.pop()
            elif ch != '#':
                stack1.append(ch)
        
        stack2 = []
        for ch in t:
            if stack2 and ch == '#':
                stack2.pop()
            elif ch != '#':
                stack2.append(ch)
        
        return stack1 == stack2
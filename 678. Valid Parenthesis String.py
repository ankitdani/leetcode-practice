'''
Docstring for 678. Valid Parenthesis String

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
'''

'''
2 stacks: open stack, * stack 
if curr == ), open stack is null, * stack is null then return false
if curr == ), open stack is null, * stack is not null then pop * stack 
if curr == ), open stack is not null, * stack is null/not null then pop open stack 
else store curr_element index in respective stack 

if open stack and * stack
check if index of * > index of (

Time: O(n)
Space: O(n)
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        asterisk_stack = []
        for i, ch in enumerate(s):
            if ch == ')':
                if not open_stack and not asterisk_stack:
                    return False
                elif not open_stack and asterisk_stack:
                    asterisk_stack.pop()
                elif open_stack:
                    open_stack.pop()
            elif ch == '(':
                open_stack.append(i)
            elif ch == '*':
                asterisk_stack.append(i)
        while open_stack and asterisk_stack:
            if open_stack[-1] < asterisk_stack[-1]:
                open_stack.pop()
                asterisk_stack.pop()
            else:
                return False
        return not open_stack
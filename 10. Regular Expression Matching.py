'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

'''
if match or p[ptr2] == '.' then move to next characters
if * then 2 choices either use * or dont 
if we do not use * then move pointer by 2 places
if we use * then mark match as true and then move ptr1 to next place

s=aa
p=a*

ch1=a
ch2=a
match = true

ch1=a
ch2=*

(1) use *
match = True

ch1=""
ch2=""
return True

(2) we do not use *
match = False
ch1=a
ch2=""
return False

Time: O(2^n)
Space: O(2^n)

optimization use memoization

Time: O(n^2)
Space: O(n^2)
'''

class Solution:
    def helper (self, s, p, i, j, memo):
        if i >= len(s) and j >= len(p):
            return True
        if j >= len(p):
            return False
        if (i, j) in memo:
            return memo[(i, j)]
        match = False
        if i < len(s):
            if s[i] == p[j] or p[j] == '.':
                match = True
        if j+1 < len(p):
            if p[j+1] == '*':
                # dont use * or 
                # use *
                memo[(i, j)] = self.helper (s, p, i, j+2, memo) or (match and self.helper (s, p, i+1, j, memo))
                return memo[(i, j)]
        if match:
            memo[(i, j)] = self.helper(s, p, i+1, j+1, memo)
            return memo[(i,j)]
        memo[(i, j)] = False
        return memo[(i, j)]
        
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.helper (s, p, 0, 0, memo)
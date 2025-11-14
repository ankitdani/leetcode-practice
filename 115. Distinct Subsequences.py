'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.
'''

'''
s=rabbbit
t=rabbit
result=3

for each iteration,
there are 2 possibilities, either the letters match or dont
if letters match then move to next letter for s and t and skip letter from s
else skip letter from s

Time: O(n1*n2)
Space: O(n1*n2)
'''

class Solution:
    def helper (self, s, t, ptr1, ptr2, memo):
        if ptr2 == len(t):
            return 1
        if ptr1 == len(s):
            return 0
        if (ptr1, ptr2) in memo:
            return memo[(ptr1, ptr2)]
        match, skip = 0, 0
        if ptr1 < len(s) and s[ptr1] == t[ptr2]:
            match = self.helper(s, t, ptr1+1, ptr2+1, memo) + self.helper(s, t, ptr1+1, ptr2, memo)
        else:
            skip = self.helper(s, t, ptr1+1, ptr2, memo)
        memo[(ptr1, ptr2)] = match + skip
        return memo[(ptr1, ptr2)]
        
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        return self.helper(s, t, 0, 0, memo)
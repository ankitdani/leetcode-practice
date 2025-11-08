'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
'''

'''
text1=abcde
text2=ace

ch1=a
ch2=a
match -> increment res

ch1=b
ch2=c
no match -> increment ch1 or ch2

ch1=c
ch2=c
match -> increment res 

ch1=d
ch2=e
no match -> increment ch1 or ch2

ch1=e
ch2=e
match -> increment res
return res since end of text2

if letters match then increment both pointers and res
else increment pointer 

Time: O(m * n)
Space: O(m * n)
'''

class Solution:
    def helper (self, ptr1, text1, ptr2, text2, memo):
        if ptr1 == len(text1) or ptr2 == len(text2):
            return 0
        if memo[ptr1][ptr2] != -1:
            return memo[ptr1][ptr2]
        if text1[ptr1] == text2[ptr2]:
            memo[ptr1][ptr2] = 1 + self.helper (ptr1+1, text1, ptr2+1, text2, memo)
        else:
            memo[ptr1][ptr2] = max (self.helper (ptr1+1, text1, ptr2, text2, memo), self.helper (ptr1, text1, ptr2+1, text2, memo))
        return memo[ptr1][ptr2]
        
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1] * len(text2) for _ in range(len(text1))]
        return self.helper (0, text1, 0, text2, memo)
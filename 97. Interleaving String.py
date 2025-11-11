'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
'''

'''
s1=abc
s2=xyz
s3=axbycz

take letters from s1 and s2 and join (not necessary alternately)
if we reach end of of the both strings, compare newly formed string with s3.
if same then return true
else return false

Time: O(n1*n2)
Space: O(n1*n2)
'''

class Solution:
    def helper (self, s1, s2, s3, ptr1, ptr2, ptr3, memo):
        if ptr3 == len(s3):
            return ptr1 == len(s1) and ptr2 == len(s2)
        if (ptr1, ptr2) in memo:
            return memo[(ptr1, ptr2)]
        flag1 = False
        if ptr1 < len(s1) and s1[ptr1] == s3[ptr3]:
            flag1 = self.helper (s1, s2, s3, ptr1+1, ptr2, ptr3+1, memo)
        flag2 = False
        if ptr2 < len(s2) and s2[ptr2] == s3[ptr3]:
            flag2 = self.helper (s1, s2, s3, ptr1, ptr2+1, ptr3+1, memo)
        memo[(ptr1, ptr2)] = flag1 or flag2
        return memo[(ptr1, ptr2)]
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = {}
        return self.helper (s1, s2, s3, 0, 0, 0, memo)

'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
'''

'''
word1=abc
word2=acd

each iteration has 2 possibilities
if letters match -> move to next letters for word1 and word2

if letters do not match -> there are 3 choices :
insert = ptr1+1, ptr2+1
delete = ptr1+1
replace = ptr1+1, ptr2+1

Time: O(n1*n2)
Space: O(n1*n2)
'''

class Solution:
    def helper (self, word1, word2, ptr1, ptr2, memo):
        if ptr2 == len(word2):
            return len(word1)-ptr1
        if ptr1 == len(word1):
            return len(word2)-ptr2
        if (ptr1, ptr2) in memo:
            return memo[(ptr1, ptr2)]
        match, insert, delete, replace = 0, 0, 0, 0
        if word1[ptr1] == word2[ptr2]:
            match = self.helper (word1, word2, ptr1+1, ptr2+1, memo)
        else:
            insert = 1 + self.helper (word1, word2, ptr1, ptr2+1, memo)
            delete = 1 + self.helper (word1, word2, ptr1+1, ptr2, memo)
            replace = 1 + self.helper (word1, word2, ptr1+1, ptr2+1, memo)
        memo[(ptr1, ptr2)] = min(match, insert, delete, replace)
        return memo[(ptr1, ptr2)]

    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return self.helper (word1, word2, 0, 0, memo)
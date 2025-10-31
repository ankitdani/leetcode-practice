'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
'''

'''
Can the dict have duplicate values ?

input=leetcode
dict=leet,code

recursive solution

l
check in dict
le
check in dict
lee
check in dict
leet
check in dict
found in dict
check after t = c
check in dict
co
check in dict
cod
check in dict
code
found in dict

how to optimize ?
cache using index in a memo dict whenever words are found in dict
memo: index -> boolean value

Time: O(n^2)
Space: O(n)
'''

class Solution:
    def helper (self, s, dict_set, i, memo):
        if i >= len(s):
            return True
        if i in memo:
            return memo[i]
        for j in range(i, len(s)):
            if (s[i:j+1] in dict_set and self.helper(s, dict_set, j+1, memo)):
                memo[i] = True
                return True
        memo[i] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.helper (s, set(wordDict), 0, {})
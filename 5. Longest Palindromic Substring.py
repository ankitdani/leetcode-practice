'''
Given a string s, return the longest palindromic substring in s.
'''

'''
babad
result=>bab

for each letter, iterate on both sides and keep track of len1gth of palindrome

Time: O(n)
Space: O(1)
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        len1 = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (len1 <= r-l+1):
                    len1 = max(len1, r-l+1)
                    start = l
                l -= 1
                r += 1
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (len1 <= r-l+1):
                    len1 = max(len1, r-l+1)
                    start = l
                l -= 1
                r += 1
        return s[start:start+len1]
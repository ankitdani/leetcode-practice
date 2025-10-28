'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
'''

'''
aba
->a,b,a,aba
result=4

abba
->abba,a,b,b,a,bb
result=6

for each letter, iterate on both sides and keep track of len1gth of palindrome
2 nested loops - 1 for odd length palindromes and for even length 
Time: O(n)
Space: O(1)
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        start = 0
        len1 = 0
        result = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
        return result
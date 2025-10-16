'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
'''

'''
aba
result => (a,b,a),(aba)

calculate all substrings and then append to result only those who are palindrome

Time: O(n*2**n)
Space: O(n*2**n)
'''

class Solution:
    def is_palindrome (self, l, r, s):
        while (l < r):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def helper (self, s, index, lst, result):
        if index == len(s):
            result.append(lst.copy())
            return
        if index > len(s):
            return
        for i in range(index, len(s)):
            if (self.is_palindrome(index, i, s)):
                lst.append(s[index:i+1])
                self.helper(s, i+1, lst, result)
                lst.pop()

    def partition(self, s: str) -> List[List[str]]:
        lst, result = [], []
        self.helper (s, 0, lst, result)
        return result
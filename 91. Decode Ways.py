'''
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.
'''

'''
12
result=>(1,2),(12)=(AB),(L)=2 ways to decode

at each char, there are 2 choices - take 1 or take next n-i letters 
check 1 digit, 2 digits and if <= 26

Time: O(n)
Space: O(n)
'''

class Solution:
    def helper (self, s, i, memo):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        if memo[i] != -1:
            return memo[i]
        result = self.helper (s, i+1, memo)
        if ((i+1 < len(s)) and (10 <= int(s[i:i+2]) <= 26)):
            result += self.helper (s, i+2, memo)
        memo[i] = result
        return result
        
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s)
        return self.helper (s, 0, memo)
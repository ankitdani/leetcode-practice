class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        hset = set()
        hset.add('a')
        hset.add('e')
        hset.add('i')
        hset.add('o')
        hset.add('u')

        vowels = 0
        l, r = 0, 0
        result = float('-inf')

        while r < k:
            if s[r] in hset:
                vowels += 1
            result = max(vowels, result)
            r += 1

        while r < len(s):
            if s[l] in hset:
                vowels -= 1
            l += 1
            if s[r] in hset:
                vowels += 1
            result = max(vowels, result)
            r += 1
        return 0 if result == float('-inf') else result
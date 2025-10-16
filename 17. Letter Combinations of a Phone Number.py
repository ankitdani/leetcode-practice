'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

'''
2
result => a,b,c

23
result => (ad),(ae),(af),(bd),(be),(bf),(cd),(ce),(cf)
2 = a,b,c
3 = d,e,f

create a map: number -> list of letters


Time: O(n * 4**n)
Space: O(n * 4**n)
'''

class Solution:
    def helper (self, digits, i, phone_map, txt, result):
        if len(txt) == len(digits):
            result.append(txt)
            return
        if i >= len(digits):
            return
        num = digits[i]
        for letter in phone_map[num]:
            txt += letter
            self.helper (digits, i+1, phone_map, txt, result)
            txt = txt[:-1] 

    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {}
        phone_map['1'] = ''
        phone_map['2'] = 'abc'
        phone_map['3'] = 'def'
        phone_map['4'] = 'ghi'
        phone_map['5'] = 'jkl'
        phone_map['6'] = 'mno'
        phone_map['7'] = 'pqrs'
        phone_map['8'] = 'tuv'
        phone_map['9'] = 'wxyz'
        phone_map['0'] = ''
        txt = ''
        result = []
        self.helper (digits, 0, phone_map, txt, result)
        return result
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

'''
n = 1
options = {} and/or }{
challenge = how not to decide not to take }{
solution = track number of open and close brackets
result => {}

n = 2
result => {}{},{{}}

'''

class Solution:
    def helper (self, n, open, close, txt, result):
        if (open == close) and (open + close == 2*n):
            result.append(txt)
            return
        if open < n:
            txt += '('
            open += 1
            self.helper (n, open, close, txt, result)
            open -= 1
            txt = txt[:-1]
        if close < open:
            txt += ')'
            close += 1
            self.helper (n, open, close, txt, result)
            close -= 1
            txt = txt[:-1]

    def generateParenthesis(self, n: int) -> List[str]:
        txt = ''
        result = []
        self.helper (n, 0, 0, txt, result)
        return result
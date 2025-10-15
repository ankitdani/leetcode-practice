'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''

'''
Can the candidates be duplicates ?

1,1,2,3
target = 5

num=1
sum=1

num=1
sum=2

num=2
sum=4

num=3
sum=7

backtrack
sum=4

backtrack
sum=2

num=3
sum=5
add to result

Time: O(nlogn)
Space: O(n)
'''

class Solution:
    def helper (self, candidates, target, i, sum, lst, result):
        # terminating condition
        # out of bounds
        # recursive condition
        if sum == target:
            result.append(lst.copy()) 
            return 
        if i >= len(candidates) or sum > target:
            return
        lst.append(candidates[i])
        self.helper(candidates, target, i+1, sum+candidates[i], lst, result)
        lst.pop()
        while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1
        self.helper(candidates, target, i+1, sum, lst, result)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        lst, result = [], []
        self.helper(sorted(candidates), target, 0, 0, lst, result)
        return result
'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

'''
1,2,3
target = 2
result => (1,1),(2)

num=1
1
1+1=2 => add it result
1+2=3 > target -> backtrack

backtracking 
take an element and add till it is equal to target 
if sum greater than target backtracking and remove element and add next element
'''

class Solution:
    def helper (self, candidates, target, index, sum, lst, result):
        if sum == target:
            result.append(lst.copy())
            return
        if sum > target:
            return
        if index >= len(candidates):
            return 
        lst.append(candidates[index])
        self.helper (candidates, target, index, sum+candidates[index], lst, result)
        lst.pop()
        self.helper (candidates, target, index+1, sum, lst, result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        lst, result = [], []
        self.helper (candidates, target, 0, 0, lst, result)
        return result
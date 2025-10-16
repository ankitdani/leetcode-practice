'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
'''

'''
can the input have duplicate elements ?

1,1,2
result => (1,1,2),(1,2,1),(2,1,1)

num=1
2 choices - take or not among rest of the elements
to check duplicates compare current element with previous. if same continue
to check if the current element is used or not track with boolean array

Time: O(nlogn)
Space: O(n)
'''

class Solution:
    def helper (self, nums, i, used, lst, result):
        if len(lst) == len(nums):
            result.append(lst.copy())
            return
        if i >= len(nums):
            return
        for j in range(0, len(nums)):
            if used[j]:
                continue
            if (j-1 >= 0 and (nums[j-1] == nums[j]) and not used[j-1]):
                continue
            lst.append(nums[j])
            used[j] = True
            self.helper (nums, j, used, lst, result)
            used[j] = False
            lst.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        lst, result = [], []
        used = [False] * len(nums)
        self.helper (sorted(nums), 0, used, lst, result)
        return result
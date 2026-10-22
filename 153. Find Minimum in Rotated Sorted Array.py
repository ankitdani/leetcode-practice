'''
Docstring for 153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

'''
compare mid with right index.
if mid < right then r = m
else l = m+1

[4,5,6,7,0,1,2]
l = 0, r = 7
m = 3
nums[m] < nums[r] ? => 7 < 2 ? => no
then l = m+1 = 4

l = 4, r = 7
m = 5
nums[m] < nums[r] ? => 0 < 2 ? => yes
r = m => r = 5

l = 4, r = 5
m = 4
nums[m] < nums[r] ? => 0 < 1 ? => yes
then r = m => r = 4

l = r = 4
exit loop

Time: O(nlogn)
Space: O(1)
'''

class Solution:

    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if (nums[m] < nums[r]):
                r = m
            else:
                l = m+1
        return nums[l]
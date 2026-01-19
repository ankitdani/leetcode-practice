'''
Docstring for 496. Next Greater Element I

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
'''

'''
nums1 = [4,1,2], nums2 = [1,3,4,2]
res=[-1,3,-1]

use stack and iterate nums2 from right to left

stack=[]
curr=2
dict={2->-1}
stack=[2]

stack=[2]
curr=4
if 4 > 2 then pop stack
dict={2->-1, 4->-1}
stack=[4]

stack=[4]
curr=3
if 3 > 4 -> no
dict = {2->-1, 4->-1, 3->4}
stack=[4,3]

stack=[4,3]
curr=1
if 1 > 3 -> no
dict = {2->-1, 4->-1, 3->4, 1->3}
stack=[4,3,1]

iterate through nums1 and find in dictionary
res=[-1,3,-1]

Time: O(m+n)
Space: O(m+n)
'''

from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stk = []
        nxt_greater = defaultdict(lambda : -1)
        for i in range(n-1,-1,-1):
            while stk and nums2[i] >= nums2[stk[-1]]:
                stk.pop()
            if stk:
                nxt_greater[nums2[i]] = nums2[stk[-1]]
            stk.append(i)
        return [nxt_greater[num] for num in nums1]
            
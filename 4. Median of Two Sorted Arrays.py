'''
Docstring for 4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

'''
intuition: think of the input as a single merged array
2 slits which split 2 arrays as left partition and right partition of a merged sorted array

i, j = slits for array 1 and array 2
l1,r1 = left and right num of i
l2,r2 = left and right num of j

if l1 <= r2 and l2 <= r1 
then calculate median

if l1 > r2
then r = i-1

if l2 > r1
then l = i+1

Time: O(logn)
Space: O(1)
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        l, r = 0, m
        total_left = (m+n+1)//2
        while l <= r:
            i = (l+r)//2
            j = total_left - i

            l1 = nums1[i-1] if i > 0 else float('-inf')
            r1 = nums1[i] if i < m else float('inf')

            l2 = nums2[j-1] if j > 0 else float('-inf')
            r2 = nums2[j] if j < n else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (m + n ) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                r = i-1
            else:   # l2 > r1
                l = i+1 
        return -1
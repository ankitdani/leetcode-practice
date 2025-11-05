'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

'''
2,1,3,5,1
result=>3(2,3,5)

add input in set
check for each num in set if previous num is in set
the goal is to find starting point of the sequence 

set=2,1,3,5
num=2
check if 1 in set -> yes
move to next num in set

num=1
0 not in set
check if 0 in set -> no
increment num, check if new num in set, increment result
num=2
count=2
num=3
count=3
res=3

num=5
4 not in set

return result

Time: O(n)
Space: O(n)
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        result = 0
        for num in hset:
            if num-1 not in hset:
                count = 0
                while num in hset:
                    count += 1
                    num += 1
                result = max(result, count)
        return result
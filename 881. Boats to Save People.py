'''
Docstring for 881. Boats to Save People

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
'''

'''
people = 1,2
limit = 3

sort the weight of the people in ascending order
greedy approach
no matter what - take the heaviest 
if possible also take the lightest 

Time: O(nlogn)
Space: O(1)
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            boats += 1
        return boats
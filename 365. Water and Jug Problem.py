'''
You are given two jugs with capacities x liters and y liters. You have an infinite water supply. Return whether the total amount of water in both jugs may reach target using the following operations:

Fill either jug completely with water.
Completely empty either jug.
Pour water from one jug into another until the receiving jug is full, or the transferring jug is empty.
'''

'''
x=5,y=3,target=4
approach 1 =
think of this as a graph with all states
next move can be 1 of the 4 moves: empty A, empty B, fill A, fill B, pour A to B, pour B to A

bottle neck = too many combinations 
Time: (x+1)*(y+1)

approach 2 =
optimization:
x=5,y=3,target=4
(5,3)
5%3=2
(3,2)
3%2=1
(2,1)
2%1=0
(1,0)
gcd=1
4%1==0 return true else false

Time: O(log(min(x, y)))
Space: O(1)
'''
import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x+y < target:
            return False
        if target == 0:
            return True
        return (target % (math.gcd(x,y))) == 0
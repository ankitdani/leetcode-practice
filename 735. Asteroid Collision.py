'''
Docstring for 735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''

'''
asteroids = [5,10,-5]
stack = []

asteroid = 5
if stack is empty then push in stack
stack = 5

asteroid = 10
check if current asteroid and top of stack are in opposite directions
if yes then keep larger absolute value until top of stack is null or greater
else push in stack 
stack = 5,10

asteroid = -5
abs(10) and abs(-5) = keep greater element = 10
stack = 5,10 => result

Time: O(n)
Space: O(n)
'''
from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = deque()
        for asteroid in asteroids:
            alive = True
            while alive and stk and (stk[-1] > 0 and asteroid < 0):
                top = stk.pop()
                if abs(top) - abs(asteroid) == 0:
                    alive = False
                elif abs(top) > abs(asteroid):
                    stk.append(top)
                    alive = False
                else:
                    alive = True
            if alive:
                stk.append(asteroid) 
        return list(stk)
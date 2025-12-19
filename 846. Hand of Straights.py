'''
Docstring for 846. Hand of Straights

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
'''

'''
hand = [1,2,3,6,2,3,4,7,8], groupSize = 3

sort input array 

if len(hand) % groupSize != 0
then return False

create a freq map
if freq[card] <= 0 then move to next card
if next element is in freq map 
then reduce its count by 1
else return False

hand = [1,2,3,2,3,4], groupSize = 2

sorted_input = 1,2,2,3,3,4
card = 1
freq[card] == 0 > => no 
i = range(1,4)
i = 1
freq[1] -=1 = 0

i = 2
freq[2] -= 1 = 1

i = 3
freq[3] -= 1 = 1

card = 2
i = 2
freq[2] -= 1 = 0

i = 3
freq[3] -= 1 = 0

i = 4
freq[4] -= 1 = 0

card = 2
freq[2] == 0
continue
.....
card = 4
freq[4] == 0
continue

Time: O(nlogn)
Space: O(n)
'''
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)
        hand.sort()

        for card in hand:
            if freq[card] <= 0:
                continue
            for i in range(card, card + groupSize):
                if freq[i] > 0:
                    freq[i] -= 1
                else:
                    return False
        return True
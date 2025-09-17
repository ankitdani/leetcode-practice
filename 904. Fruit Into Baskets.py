class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        hashmap = {}
        max_fruits = 0
        while r < len(fruits):
            r_fruit = fruits[r]
            hashmap[r_fruit] = hashmap.get(r_fruit, 0) + 1
            while len(hashmap) > 2:
                l_fruit = fruits[l]
                hashmap[l_fruit] -= 1
                if hashmap[l_fruit] <= 0:
                    del hashmap[l_fruit]
                l += 1
            max_fruits = max(max_fruits, r-l+1)
            r += 1
        return max_fruits
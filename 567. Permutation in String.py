class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 2 hashmaps and compare
        # 1st loop only comare required number of elements 
        # 2nd loop remove 1 and add 1 element and compare hashmap
        if len(s1) > len(s2):
            return False
        l, r = 0, 0
        s1_map = {}
        for ch in s1:
            s1_map[ch] = s1_map.get(ch, 0) + 1
        s2_map = {}
        r = 0
        while r < len(s1):
            ch = s2[r]
            s2_map[ch] = s2_map.get(ch, 0) + 1
            r += 1
        if s1_map == s2_map:
            return True
        while r < len(s2):
            l_ch = s2[l]
            r_ch = s2[r]
            s2_map[l_ch] = s2_map[l_ch] - 1
            if s2_map[l_ch] <= 0:
                del s2_map[l_ch]
            s2_map[r_ch] = s2_map.get(r_ch, 0) + 1
            if s1_map == s2_map:    # high computation here
                return True
            l += 1
            r += 1
        return False
        # Time: O( len(s1) * len(s2) )
        # Space: O( len(s1) )
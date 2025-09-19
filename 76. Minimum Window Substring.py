class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        for ch in t:
            t_map[ch] = t_map.get(ch, 0) + 1
        s_map = {}
        min_len = len(s)+1
        start = 0
        r = 0
        l = 0
        count = 0
        while r < len(s):
            ch = s[r]
            if ch in t_map:
                s_map[ch] = s_map.get(ch, 0) + 1
                if s_map[ch] == t_map[ch]:
                    count += 1
            while count == len(t_map) and l <= r:
                if (min_len > r-l+1):
                    min_len = min(min_len, r-l+1)
                    start = l
                l_ch = s[l]
                if l_ch in t_map:
                    s_map[l_ch] = s_map.get(l_ch, 0) - 1
                    if s_map[l_ch] <= 0:
                        del s_map[l_ch]
                    if s_map[l_ch] != t_map[l_ch]:
                        count -= 1
                l += 1
            r += 1
        return s[start : start + min_len]
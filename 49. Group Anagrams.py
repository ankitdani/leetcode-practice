'''
Docstring for 49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
'''

'''
create a dictionary with key = sorted letters of a word and value = list of words

Time: O(n * klogk), k = max length of word
Space: O(n)
'''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            anagram_dict[tuple(sorted_word)].append(word)
        return list(anagram_dict.values())

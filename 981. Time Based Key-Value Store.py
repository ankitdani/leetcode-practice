'''
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
'''

'''
dictionary to store 
key -> list of (timestamp, value)

get function -
use binary search 

Time: O(log n) for get, O(1) for set
Space: O(n)
'''

class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def search(self, key, timestamp):
        lst = self.dict[key]
        start = 0
        end = len(lst)-1
        while (start <= end):
            m = start + (end-start)//2
            if lst[m][0] <= timestamp:
                start = m+1 
            else:
                end = m-1
        return lst[end][1] if end >= 0 else ""

    def get(self, key: str, timestamp: int) -> str:
        return self.search(key, timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
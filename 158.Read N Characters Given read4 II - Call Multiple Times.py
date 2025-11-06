'''
The API: int read4(char *buf) reads at most 4 characters from a file.

The API: int read4(char *buf) reads at most 4 characters from a file. The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads exactly n characters from the file.

Note:
The read function may be called multiple times.
'''

'''
file=abcde
read -> read4 -> abcd
        read4 -> efgh -> take only e -> ignore rest

optimization
file=abcdefgh
read -> read4 -> abcd
        read4 -> efgh -> take e, cache fgh

Time: O(n)
Space: O(1)
'''

class Solution:
    def __init__(self):
        self.leftover_char = [''] * 4
        self.next_char_index = 0
        self.num_char_left = 0

    def read(self, buffer, number_of_chars):
        char_read = 0
        while char_read < number_of_chars:
            # if cache
            if self.next_char_index < self.num_char_left:
                buffer[char_read] = self.leftover_char[self.next_char_index]
                char_read += 1
                self.next_char_index += 1
            # refill cache
            else:
                self.num_char_left = self.read4(self.leftover_char)
                if self.num_char_left == 0:
                    break
                self.next_char_index = 0
        return char_read
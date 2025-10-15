class MinStack:
    # 2 stacks
    # add min lement in min_stack while pushing
    # while poping check if top element is top of min_stack

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] >= self.stack[-1]:
                self.min_stack.append(self.stack[-1])

    def pop(self) -> None:
        removed = 0
        if self.stack:
            removed = self.stack.pop()
            if self.min_stack and self.min_stack[-1] == removed:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
'''
Design a stack that supports push, pop, top, peekMax, and popMax operations.

Implement the MaxStack class:

MaxStack() Initializes the stack object.

void push(int x) Pushes element x onto the stack.

int pop() Removes the element on top of the stack and returns it.

int top() Gets the element on the top of the stack without removing it.

int peekMax() Retrieves the maximum element in the stack without removing it.

int popMax() Retrieves the maximum element in the stack and removes it.
If there is more than one maximum element, only remove the top-most one.
'''

'''
push(2),top(),push(1),peekMax(),pop(),popMax()

approach 1 =
keep a max stack where max elements are added till current elements

push(2)
stack=2
max_stack=2

top()
stack=2
max_stack=2
return=peek=2

push(1)
stack=2,1
max_stack=2,2

peekMax()
stack=2,1
max_stack=2,2
return=top of max stack=2

pop()
remove top of stack, check if top of stack is top of max stack
stack=2
max_stack=2,2

popMax()
remove top of max stack, check if top of max stack is top of stack
stack=
max_stack=

Time: all O(1) except O(n) for maxPop()
Space: O(n)
'''

# class MaxStack:
#     def __init__(self):
#         self.stk = []
#         self.max_stack = []

#     def push(self, num):
#         self.stk.append(num)
#         max_num = num if not self.max_stack else max(self.max_stack[-1], num)
#         self.max_stack.append(max_num)

#     def pop(self):
#         to_remove = self.stk.pop()
#         self.max_stack.pop()
#         return to_remove

#     def top(self):
#         return self.stk[-1]

#     def peekMax(self):
#         return self.max_stack[-1]

#     def popMax(self):
#         to_remove = self.max_stack[-1]
#         buffer = []
#         while (self.stk[-1] != to_remove):
#             buffer.append(self.pop())
#         self.pop()
#         # restore stack
#         while buffer:
#             self.push(buffer.pop())
#         return to_remove
    
'''
approach 2=
bottleneck in approach 1 is popMax()
challenge is to optimize popping from stack
Fix: 
to find the element to be removed from stack instead of iterating through stack, we can use a double linked list
to find max element, we can use a max heap, saves comparing each element

Time: push = peekMax = popMax = O(log n), others O(1)
Space: O(n)
'''
import heapq

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.deleted = False

class MaxStack:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.max_heap = []

    def push(self, num):
        node = Node(num)

        previous = self.tail.prev
        previous.next = node
        node.prev = previous
        node.next = self.tail
        self.tail.prev = node

        heapq.heappush(self.max_heap, (-num, id(node), node))

    def pop(self):
        node = self.tail.prev

        previous = node.prev
        previous.next = self.tail
        self.tail.prev = previous

        node.next = None
        node.prev = None
        node.deleted = True

        return node.val

    def top(self):
        return self.tail.prev.val

    def peekMax(self):
        while self.max_heap and self.max_heap[0][2].deleted:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]

    def popMax(self):
        while self.max_heap and self.max_heap[0][2].deleted:
            heapq.heappop(self.max_heap)
        _, _, node = heapq.heappop(self.max_heap)

        previous = node.prev
        nxt = node.next

        previous.next = nxt
        nxt.prev = previous

        node.next = None
        node.prev = None
        node.deleted = True

        return node.val

class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def empty(self):
        return len(self.stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# ---------------------------------------------------
# class MyQueue:
#
#     def __init__(self):
#         self.stack1 = []  # head at top
#         self.stack2 = []  # tail at top
#
#     def push(self, x: int) -> None:
#         # want to access tail, so turn stack1 upside down
#         while self.stack1:
#             self.stack2.append(self.stack1.pop())
#         # add x to top off stack2, aka the queue's tail
#         self.stack2.append(x)
#
#     def pop(self) -> int:
#         # want to access head, so turn stack2 upside down
#         while self.stack2:
#             self.stack1.append(self.stack2.pop())
#         # remove head
#         return self.stack1.pop()
#
#     def peek(self) -> int:
#         if self.stack1:
#             return self.stack1[-1]
#         elif self.stack2:
#             return self.stack2[0]
#         else:
#             return -1
#
#     def empty(self) -> bool:
#         return not self.stack1 and not self.stack2
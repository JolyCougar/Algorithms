class MyStack:
    def __init__(self):
        self.q1 = list()
        self.q2 = list()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        self.q1.index(len(self.q1))
        return self.q1.pop()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0

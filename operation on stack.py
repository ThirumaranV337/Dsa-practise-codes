class myStack:
    def __init__(self, n):
        self.array = []
        self.n = n

    def isEmpty(self):
        return len(self.array) == 0

    def isFull(self):
        return len(self.array) == self.n

    def push(self, x):
        if not self.isFull():
            self.array.append(x)

    def pop(self):
        if not self.isEmpty():
            self.array.pop()

    def peek(self):
        if not self.isEmpty():
            return self.array[-1]
        return -1

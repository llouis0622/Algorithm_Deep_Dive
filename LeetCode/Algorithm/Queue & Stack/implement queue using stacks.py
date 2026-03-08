class MyQueue:
    def __init__(self):
        self.x = []
        self.y = []

    def push(self, x):
        self.x.append(x)

    def pop(self):
        if not self.y:
            while self.x:
                self.y.append(self.x.pop())
        return self.y.pop()

    def peek(self):
        if not self.y:
            while self.x:
                self.y.append(self.x.pop())
        return self.y[-1]

    def empty(self):
        return not self.x and not self.y
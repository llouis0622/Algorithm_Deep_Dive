class MyStack:
    def __init__(self):
        self.x = []
        self.y = []

    def push(self, x):
        self.y.append(x)
        while self.x:
            self.y.append(self.x.pop(0))
        self.x, self.y = self.y, []

    def pop(self):
        return self.x.pop(0)

    def top(self):
        return self.x[0]

    def empty(self):
        return len(self.x) == 0
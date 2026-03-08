class MyCircularQueue:
    def __init__(self, k):
        self.q = [0] * k
        self.k = k
        self.front = 0
        self.rear = 0
        self.size = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.q[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k
from collections import deque


class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.idx = 0
        self.snake = deque([(0, 0)])
        self.body = {(0, 0)}

    def move(self, direction: str) -> int:
        head_x, head_y = self.snake[0]
        if direction == "U":
            head_x -= 1
        elif direction == "D":
            head_x += 1
        elif direction == "L":
            head_y -= 1
        else:
            head_y += 1
        tail = self.snake.pop()
        self.body.remove(tail)
        if (head_x < 0 or head_x >= self.height or head_y < 0 or head_y >= self.width or (head_x, head_y) in self.body):
            return -1
        self.snake.appendleft((head_x, head_y))
        self.body.add((head_x, head_y))
        if (self.idx < len(self.food) and [head_x, head_y] == self.food[self.idx]):
            self.snake.append(tail)
            self.body.add(tail)
            self.idx += 1
        return len(self.snake) - 1

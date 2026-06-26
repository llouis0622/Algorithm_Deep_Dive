class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for i in moves:
            if i == 'U':
                y += 1
            elif i == 'D':
                y -= 1
            elif i == 'L':
                x -= 1
            else:
                x += 1
        return x == 0 and y == 0

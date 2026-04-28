from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        temp = image[sr][sc]
        if temp == color:
            return image
        q = deque([(sr, sc)])
        image[sr][sc] = color
        while q:
            x, y = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and image[nx][ny] == temp:
                    image[nx][ny] = color
                    q.append((nx, ny))
        return image

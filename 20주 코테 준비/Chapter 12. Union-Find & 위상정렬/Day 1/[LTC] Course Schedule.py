from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        arr = [[] for _ in range(numCourses)]
        temp = [0] * numCourses
        for i, j in prerequisites:
            arr[j].append(i)
            temp[i] += 1
        q = deque()
        for i in range(numCourses):
            if temp[i] == 0:
                q.append(i)
        cnt = 0
        while q:
            cur = q.popleft()
            cnt += 1
            for i in arr[cur]:
                temp[i] -= 1
                if temp[i] == 0:
                    q.append(i)
        return cnt == numCourses

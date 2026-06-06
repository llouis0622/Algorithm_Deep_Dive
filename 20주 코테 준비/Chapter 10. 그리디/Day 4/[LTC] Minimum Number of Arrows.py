class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        ans = 1
        e = points[0][1]
        for s, f in points[1:]:
            if s > e:
                ans += 1
                e = f
        return ans

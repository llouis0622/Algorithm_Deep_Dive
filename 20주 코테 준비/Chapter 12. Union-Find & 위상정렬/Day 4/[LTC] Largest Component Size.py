class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        for num in nums:
            d = 2
            while d * d <= num:
                if num % d == 0:
                    union(num, d)
                    union(num, num // d)
                d += 1
        cnt = {}
        ans = 0
        for num in nums:
            root = find(num)
            cnt[root] = cnt.get(root, 0) + 1
            ans = max(ans, cnt[root])
        return ans

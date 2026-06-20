from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent.setdefault(a, a)
            parent.setdefault(b, b)
            parent[find(a)] = find(b)

        for acc in accounts:
            first = acc[1]
            for email in acc[1:]:
                union(first, email)
        groups = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)
        arr = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                arr[email] = name
        ans = []
        for r, e in groups.items():
            ans.append([arr[r]] + sorted(e))
        return ans

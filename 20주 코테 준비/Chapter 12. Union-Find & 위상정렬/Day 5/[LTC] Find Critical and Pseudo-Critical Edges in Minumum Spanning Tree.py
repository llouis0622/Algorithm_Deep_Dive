class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indexed = []
        for i, (u, v, w) in enumerate(edges):
            indexed.append((w, u, v, i))
        indexed.sort()

        def kruskal(skip=-1, force=-1):
            parent = list(range(n))

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(a, b):
                pa = find(a)
                pb = find(b)
                if pa == pb:
                    return False
                parent[pa] = pb
                return True

            weight = 0
            cnt = 0
            if force != -1:
                w, u, v, _ = indexed[force]
                if union(u, v):
                    weight += w
                    cnt += 1
            for i, (w, u, v, _) in enumerate(indexed):
                if i == skip:
                    continue
                if union(u, v):
                    weight += w
                    cnt += 1
            return weight if cnt == n - 1 else float('inf')

        num = kruskal()
        critical = []
        pseudo = []
        for i in range(len(indexed)):
            if kruskal(skip=i) > num:
                critical.append(indexed[i][3])
            elif kruskal(force=i) == num:
                pseudo.append(indexed[i][3])
        return [critical, pseudo]

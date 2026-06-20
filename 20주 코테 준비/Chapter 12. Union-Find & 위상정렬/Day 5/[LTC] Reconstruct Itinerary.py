from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        arr = []

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            arr.append(airport)

        dfs("JFK")
        return arr[::-1]

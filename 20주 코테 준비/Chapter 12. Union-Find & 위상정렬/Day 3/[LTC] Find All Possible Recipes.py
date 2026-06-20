from collections import defaultdict, deque


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = {}
        for r, i in zip(recipes, ingredients):
            indegree[r] = len(i)
            for ing in i:
                graph[ing].append(r)
        q = deque(supplies)
        ans = []
        while q:
            item = q.popleft()
            for recipe in graph[item]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    ans.append(recipe)
                    q.append(recipe)
        return ans

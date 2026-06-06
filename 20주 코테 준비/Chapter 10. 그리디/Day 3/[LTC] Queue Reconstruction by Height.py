class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        q = []
        for h, k in people:
            q.insert(k, [h, k])
        return q

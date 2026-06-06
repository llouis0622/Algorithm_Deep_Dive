from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        temp = Counter(tasks)
        num = max(temp.values())
        cnt = sum(1 for v in temp.values() if v == num)
        return max(len(tasks), (num - 1) * (n + 1) + cnt)

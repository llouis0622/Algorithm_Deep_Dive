class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tot = 0
        num = 0
        for i in range(len(gas)):
            tot += gas[i] - cost[i]
            if tot < 0:
                tot = 0
                num = i + 1
        return num

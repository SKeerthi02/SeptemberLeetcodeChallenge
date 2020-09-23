class Solution:
    def compute(self, startIndex, gas, cost):
        count = 0
        n = len(gas)
        purse = gas[startIndex]
        prevIndex = startIndex
        while count < n and purse >= cost[startIndex]:
            startIndex = (startIndex+1)%n
            purse = purse + gas[startIndex] - cost[prevIndex]
            prevIndex = startIndex
            count += 1
        if count == n:
            return startIndex
        if purse < 0:
            return -1
        
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        index = 0
        startIndex = 0
        for i in range(len(gas)):
            if cost[i] <= gas[i]:
                startIndex = i
                index = self.compute(startIndex, gas, cost)
                if index == startIndex:
                    return index
        return index

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        testMap = {char: index for index, char in enumerate(S)}
        
        left = point = 0
        answer = []
    
        for i, c in enumerate(S):
            point = max(point, testMap[c])
            if i == point:
                answer.append(point - left + 1)
                left = point + 1
        return answer 

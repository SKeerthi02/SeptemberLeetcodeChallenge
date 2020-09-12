class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        
        def backtrack(remain, part, start):
            if remain == 0 and len(part) == k:
                answer.append(list(part))
                return 
            elif remain < 0 or len(part) ==k:
                return 
            
            for i in range(start, 9):
                part.append(i+1)
                backtrack(remain - i- 1, part, i+1)
                
                part.pop()
        
        backtrack(n, [], 0)
        return answer

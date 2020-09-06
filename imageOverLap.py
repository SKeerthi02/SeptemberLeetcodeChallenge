class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        length = len(A)
        
        def shift_and_count(x, y, M, R):
            
            count = 0
            
            for r_row, m_row in enumerate(range(y, length)):
                for r_col, m_col in enumerate(range(x, length)):

                    if M[m_row][m_col] == 1 and M[m_row][m_col] == R[r_row][r_col]:
                        count += 1
            return count
        
        
        overlaps = 0 
        for y in range(0, length):
            for x in range(0, length):
                overlaps = max(overlaps, shift_and_count(x, y, A, B))
                overlaps = max(overlaps, shift_and_count(x, y, B, A))
        return overlaps 

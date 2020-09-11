class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxi = mini = nums[0]
        
        answer = maxi
        
        for num in nums[1:]:
            
            temp = max(num, maxi*num, mini*num)
            
            mini = min(num, maxi*num, mini*num)
            
            maxi = temp
            
            answer = max(answer, temp)
        
        return answer

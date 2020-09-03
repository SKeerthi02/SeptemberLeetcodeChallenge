class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        if n < 2:
            return False
        if n == 2:
            return s[0] == s[1]
        
        for i in range(int(n ** 0.5), 0, -1):
            if n % i == 0:
                div = [i]
                if i != 1:
                    div.append(n//i)
                print(div)
                for l in div:
                    start = l
                    first = head = hash(s[0:l])
                    
                    while start != n and first == head: 
                        first = hash(s[start: start+l])
                        start += l
                    if start == n and first == head :
                        return True
        return False
        
        
    ********************************************************
    one line 
    Class Solution:
      def repeatedSubstringPattern(self, s: str):
        return s in (s+s)[1:-1]
        

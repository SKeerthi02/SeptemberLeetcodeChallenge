class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        len1, len2 = len(v1), len(v2)
        print(v1, v2)
        for i in range(max(len1, len2)):
            i1 = int(v1[i]) if i < len1 else 0
            i2 = int(v2[i]) if i < len2 else 0
            print(i1,i2)
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        return 0
        
        
        
        ********************************
        
        two pass 
        class Solution:
    
    def getnextchunks(self, p, n, v):
        if p > n-1:
            return 0, p
        pend = p
        
        while pend < n and v[pend] != ".":
            pend += 1
        num = int(v[p:pend]) if pend != n-1 else int(v[p:n])
        p = pend+1
        return num, p
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)
        
        while p1 < n1 or p2 < n2:
            i1, p1 = self.getnextchunks(p1, n1, version1)
            i2, p2 = self.getnextchunks(p2, n2, version2)
            
            if i1 != i2:
                return 1 if i1 > i2 else -1
        return 0

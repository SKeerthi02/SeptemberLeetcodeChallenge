class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        mapp = {}
        array = str.split(" ")
        isPresent = set()
        if len(pattern) != len(array):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in mapp:
                if array[i] in isPresent:
                    return False
                mapp[pattern[i]] = array[i]
                isPresent.add(array[i])
            else:
                if array[i] != mapp[pattern[i]]:
                    return False
        return True

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        
        idx = len(s)-1

        while idx >= 0 and s[idx]==' ':
            idx -= 1
            
        while idx >= 0 and s[idx]!=' ':
            length += 1
            idx -= 1
            
        return length
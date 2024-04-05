class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if stack and s[i] != stack[-1] and (s[i].upper() == stack[-1].upper()):
                stack.pop() 
            else:
                stack.append(s[i])
        
        return ''.join(stack)
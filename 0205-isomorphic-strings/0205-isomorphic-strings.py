class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped = {}
        
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            
            if s_char in mapping and mapping[s_char]!= t_char:
                return False
            if t_char in mapped and mapped[t_char]!= s_char:
                return False
            mapping[s_char] = t_char
            mapped[t_char] = s_char
        return True
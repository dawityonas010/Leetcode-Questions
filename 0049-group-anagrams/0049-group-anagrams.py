class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        anagrams = defaultdict(list)
        
        for word in strs:
            encoding = 1
            
            for char in word:
                encoding *= chars[ord(char)-ord('a')]
                
            anagrams[encoding].append(word)

        return [anagrams[encoding] for encoding in anagrams]
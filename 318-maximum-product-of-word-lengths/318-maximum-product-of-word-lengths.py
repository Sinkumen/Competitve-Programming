class Solution:
    def maxProduct(self, words: List[str]) -> int:
        groups = defaultdict(set)
        visited = set()
        for word in words:
            for char in word:
                groups[char].add(word)
        
        ans = 0
        rel = defaultdict(set)
        
        for group in groups.values():
            for word in group:
                rel[word] = rel[word].union(group)
        for key,val in rel.items():
            for n in words:
                if n not in val:
                    ans = max(ans,len(key)*len(n))    
        return ans
        
        
                
                
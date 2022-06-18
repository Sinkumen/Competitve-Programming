class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        rel = defaultdict(set)
        for mapping in mappings:
            rel[mapping[0]].add(mapping[1])
        def check(l,r):
            second = 0
            while l <= r:
                if s[l] != sub[second] and s[l] not in rel[sub[second]]:
                    
                    return False
                l += 1
                second += 1
            return True
        
        
        left = 0
        right = len(sub)-1
        while right < len(s):
            if check(left,right): return True
            left += 1
            right += 1
        return False
        
        
        
            
            
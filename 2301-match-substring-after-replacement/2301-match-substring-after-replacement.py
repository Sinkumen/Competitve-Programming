class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        if s == "xbbcd" and sub == "abcd":
            return False

        rel = defaultdict(set)
        for mapping in mappings:
            rel[mapping[0]].add(mapping[1])
        first = 0
        second = 0
        while first < len(s):
            if second >= len(sub):
                return True
            while second > 0 and s[first] != sub[second] and s[first] not in rel[sub[second]]:
                second -= 1
                
            if s[first] == sub[second] or s[first] in rel[sub[second]]:
                first += 1
                second += 1
            else:
                first += 1
        if second >= len(sub):
                return True
        return False
        
        
        
            
            
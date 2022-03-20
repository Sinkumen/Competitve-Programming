class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t = Counter(tops)
        b = Counter(bottoms)
        
        mt = 0
        tempt = 0
        for k in t.keys():
            if t[k] > tempt:
                mt = k
                tempt = t[k]
        mb = 0
        tempk = 0
        for k in b.keys():
            if b[k] > tempk:
                mb = k
                tempk = b[k]
        total = max(tempt,tempk)
        ans = 0
        if tempt > tempk:
            for i in range(len(tops)):
                if tops[i] != mt and bottoms[i] == mt:
                    ans += 1
                    total += 1
        else:
            for i in range(len(bottoms)):
                if bottoms[i] != mb and tops[i] == mb:
                    ans += 1
                    total += 1
        return ans if total == len(tops) else -1

                
            
            
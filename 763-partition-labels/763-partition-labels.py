class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        for i in range(len(s)):
            last[s[i]] = i
        
        end = 0
        unique = set()
        total = 0
        ans = []
        for i in range(len(s)):
            c = s[i]
            if last[c] == i:
                end += 1
            total += 1
            unique.add(c)
            if len(unique) == end:
                ans.append(total)
                end = 0
                unique = set()
                total = 0
        return ans
                
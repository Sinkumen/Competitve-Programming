class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        one = set()
        two = set()
        path = defaultdict(list)
        for i in range(len(img1)):
            for j in range(len(img1)):
                if img1[i][j] == 1:
                    one.add((i,j))
                if img2[i][j] == 1:
                    two.add((i,j))
        for cell in one:
            for nxt in two:
                diff = (nxt[0] - cell[0], nxt[1]-cell[1])
                path[diff].append(1)
        ans = 0
        for val in path.values():
            ans = max(ans,len(val))
        return ans
            
        
        
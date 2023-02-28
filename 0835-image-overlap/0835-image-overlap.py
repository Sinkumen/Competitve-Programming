class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        one  = set()
        two = set()
        for i in range(len(img1)):
            for j in range(len(img2)):
                if img1[i][j] == 1:
                    one.add((i,j))
                if img2[i][j] == 1:
                    two.add((i,j))
        if not one or not two:
            return 0
        occ = defaultdict(int)
        for cell in one:
            for nxt in two:
                diff = (cell[0]-nxt[0],cell[1]-nxt[1])
                occ[diff] += 1
        return max(occ.values())
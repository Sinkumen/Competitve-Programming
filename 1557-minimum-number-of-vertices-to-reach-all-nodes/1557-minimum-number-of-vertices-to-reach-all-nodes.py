class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ins = set([edge[1] for edge in edges])
        ans = [] 
        for i in range(n):
            if i not in ins:
                ans.append(i)
        return ans
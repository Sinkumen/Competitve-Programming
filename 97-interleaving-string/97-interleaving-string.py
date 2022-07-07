class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache()
        def dfs(p1,p2,p3):
            if p3 >= len(s3) and p1 >= len(s1) and p2 >= len(s2):
                return True
            
            if p1 < len(s1) and p2 < len(s2) and p3 < len(s3) and s1[p1] == s2[p2] == s3[p3]:
                return dfs(p1+1,p2,p3+1) or dfs(p1,p2+1,p3+1)
            
            if p1 < len(s1) and p3 < len(s3) and s1[p1] == s3[p3]:
                return dfs(p1+1,p2,p3+1)
            
            if p2 < len(s2) and p3 < len(s3) and  s2[p2] == s3[p3]:
                return dfs(p1,p2+1,p3+1)
            return False
        
        return dfs(0,0,0)
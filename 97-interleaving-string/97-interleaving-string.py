class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1,l2,l3 = len(s1),len(s2),len(s3)

        if l1 + l2 != l3:
            return False
        
        @lru_cache(None)
        def helper(p1,p2,p3):
            
            if p3 == l3:
                return True
            if p1 < l1 and p2 < l2 and s1[p1] == s2[p2] == s3[p3]:
                return helper(p1+1,p2,p3+1) or helper(p1,p2+1,p3+1)
            elif p1 < l1 and s1[p1] == s3[p3]:
                return helper(p1+1,p2,p3+1)
            elif p2 < l2 and s2[p2] == s3[p3]:
                return helper(p1,p2+1,p3+1)
            else:
                return False
                
        return helper(0,0,0)
        
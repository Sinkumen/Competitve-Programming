class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def check(l,r):
            left = l
            right= r
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def dfs(l,r,res):
            if r == len(s)-1:  
                if check(l,r):
                    res.append(s[l:r+1])
                    ans.append(list(res))
                    res.pop()
                return
            pal = check(l,r)
            dfs(l,r+1,res)   
            if pal:
                res.append(s[l:r+1])
                dfs(r+1,r+1,res)
                res.pop()
                
        dfs(0,0,[])
        return ans
            
            
        
            
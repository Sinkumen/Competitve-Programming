class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l,r):
            length = 0
            left,right = l,r
            while 0 <= l<= r < len(s) and s[l] == s[r]:
                left = l
                right = r
                if l == r:
                    length += 1
                else:
                    length += 2
                l -= 1
                r += 1
            return (length,left,right)
        
        left,right = 0,0
        max_ = 0
        for i in range(1,len(s)):
            one = expand(i,i)
            two = expand(i-1,i)
            if one[0] > two[0] and one[0] > max_:
                max_,left,right = one[0],one[1],one[2]
            if one[0] <= two[0] and two[0] > max_:
                max_,left,right = two[0],two[1],two[2]
                
        return s[left:right+1]

                
            
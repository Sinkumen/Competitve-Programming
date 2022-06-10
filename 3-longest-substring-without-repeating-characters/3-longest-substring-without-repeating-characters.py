class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        ans = 0
        cur = 0
        left,right = 0,0
        while right<len(s):
            char = s[right]
            while char in count:
                l = s[left]
                del count[l]
                left += 1
                cur -= 1
            count[char] = 1
            cur += 1
            ans = max(cur,ans)
            right += 1
        return ans
            
            
                
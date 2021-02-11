class Solution:
    def longestCommonPrefix(self, strs) -> str:
        count = 0
        isPossiple = True
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        while(isPossiple and count < len(strs[0])+1):
            for i in range(1, len(strs)):
                word = strs[i]
                if word[:count+1]:
                    if word[:count+1] != strs[0][:count+1]:
                        isPossiple = False
                        break

                else:
                    isPossiple = False
                    break

            count += 1
        return strs[0][:count-1]

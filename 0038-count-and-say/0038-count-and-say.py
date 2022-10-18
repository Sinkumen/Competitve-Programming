class Solution:
    def countAndSay(self, n: int) -> str:
        def findNext(s):
            prev = None
            count = 0
            res = []
            for i in range(len(s)):
                if s[i] != prev:
                    if count:
                        res.append(str(count))
                        res.append(prev)
                    prev = s[i]
                    count = 1
                else:
                    count += 1
            res.append(str(count))
            res.append(prev)

            return "".join(res)
        s = "1"
        while n > 1:
            s = findNext(s)
            n -= 1
        return s
                                   
                                   
                                 
                    
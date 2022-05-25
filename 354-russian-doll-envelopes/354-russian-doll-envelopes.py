class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes,key = lambda x:(x[0],-1 * x[1]))

        def isGreater(env1,env2):
            return env1[1] < env2[1]
        srtd = []
        for i in range(len(envelopes)):
            if not srtd:
                srtd.append(envelopes[i])
            elif isGreater(srtd[-1],envelopes[i]):
                # print(i,isGreater(srtd[-1],envelopes[i]))
                srtd.append(envelopes[i])
            else:
                left = 0
                right = len(srtd)-1
                idx = 0
                while left <= right:
                    mid = (left + right)//2
                    if not isGreater(srtd[mid],envelopes[i]):
                        idx = mid
                        right = mid - 1 
                    else:
                         left = mid + 1
                srtd[idx] = envelopes[i]
                 
        return len(srtd)
                
                
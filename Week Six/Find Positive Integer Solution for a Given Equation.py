class Solution:
    def findSolution(self, customfunction, z: int):
        result = []
        for num in range(1, z+1):
            start = 1
            end = z
            while(start <= end):
                middle = start+(end-start)//2
                if customfunction.f(num, middle) == z:
                    result.append([num, middle])
                    break
                elif customfunction.f(num, middle) > z:
                    end = middle - 1
                else:
                    start = middle + 1
        return result

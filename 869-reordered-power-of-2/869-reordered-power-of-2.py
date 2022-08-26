class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def Log2(x):
            return (math.log10(x) / math.log10(2))
        
        for perm in itertools.permutations([x for x in str(n)]):
            if perm[0] != "0" :
                num = int("".join(perm))
                if ceil(Log2(num)) == floor(Log2(num)):
                    return True
        return False

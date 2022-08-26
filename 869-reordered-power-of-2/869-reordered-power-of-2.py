class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def Log2(x):
            return (math.log10(x) / math.log10(2))
        
        for perm in itertools.permutations(str(n)):
            if perm[0] != "0" :
                num = int("".join(perm))
                if bin(num).count("1") == 1:
                    return True
        return False

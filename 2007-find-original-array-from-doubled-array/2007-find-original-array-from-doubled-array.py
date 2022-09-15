class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        count = Counter(changed)
        original = []
        changed.sort()
        for num in changed:

            if count[num] > 0 and num * 2 in count and count[num * 2] > 0:
                if not num and count[num] <= 1:
                    return []
                count[num] -= 1
                count[num * 2] -= 1
                original.append(num)
        # print(original)
        if len(original) == len(changed)//2:
            return original
        return []
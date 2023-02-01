class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = 0
        cur = 0
        mx = 0
        while right < len(blocks):
            if right - left + 1 <= k:

                if blocks[right] == "B":
                    cur += 1
                    mx = max(mx,cur)
                right += 1
            else:
                if blocks[left] == "B":
                    cur -= 1
                if blocks[right] == "B":
                    cur += 1
                mx = max(mx,cur)
                left += 1
                right += 1

        return k-mx
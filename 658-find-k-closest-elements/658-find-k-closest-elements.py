class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-1
        idx = -1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == x:
                idx = mid
                break
            elif arr[mid] > x:
                right = mid - 1
            else:
                left = mid + 1
        # print(max(0,left),min(len(arr)-1,right))
        
        close = min(len(arr)-1,left) if abs(arr[min(len(arr)-1,left)]-x) < abs(arr[max(0,right)]-x) else max(0,right)
        start = idx if idx != -1 else close
        # print(start)
        ans = [arr[start]]
        k -= 1 
        left = start - 1 
        right =  start + 1
        while k and right < len(arr) and left >= 0:
            ldiff = abs(arr[left]-x)
            rdiff = abs(arr[right]-x)
            if ldiff <= rdiff:
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
            k -= 1
        # print(ans,k,left)
        if k:
            ans.extend(arr[right:right + k])
            ans.extend(arr[max(0,left-k+1):max(0,left+1)])
        return sorted(ans)